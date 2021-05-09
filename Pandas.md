### 開放資料來源
[xlsx](https://www.stats.govt.nz/assets/Reports/Global-New-Zealand/Global-New-Zealand-year-ended-June-2017/global-nz-jun-2017-tables-0.xlsx)  
[csv](https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2019-financial-year-provisional/Download-data/annual-enterprise-survey-2019-financial-year-provisional-csv.csv)
### 引入套件
```python
import pandas as pd
import xlrd 
import openpyxl
```
### 指定 pandas dataframe 在 console 秀出的大小
```python
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 100)
```
### 讀檔
read_csv：根據檔案下載處記錄下路徑，讀取 csv 檔  
印出前五列以及所有欄位名稱；將欄位名稱改成全大寫  
```python
csv_file_path = './annual-enterprise-survey-2019-financial-year-provisional-csv.csv'
csv_data = pd.read_csv(csv_file_path)
print(csv_data.head())
print(csv_data.columns)
rename_dict = dict(zip(csv_data.columns,csv_data.columns.str.upper()))
csv_data = csv_data.rename(columns=rename_dict)
```
read_excel：讀 xlsx, xls 檔皆可以用  read_excel  
當 sheet_name=None 時，用字典存取各個 sheet  
呼叫指定 sheet 需用 sheet 名作為 key  
```python
xlsx_file_path = './global-nz-jun-2017-tables-0.xlsx'
xlsx_data = pd.read_excel(xlsx_file_path, sheet_name=None)
xlsx_data.keys()
table01 = xlsx_data['0.1']
```
read_excel：讀取單一 sheet，並指定 3,4,5 列作為欄位名稱  
且合併多列成單一欄位  
```python
xlsx_data = pd.read_excel(xlsx_file_path, sheet_name='0.1', header=[3,4,5])
xlsx_data.columns = xlsx_data.columns.map('_'.join)
```
### 建立 dataframe
建立空的 dataframe  
append：插入新列，印出新列的值域型態  
```python
df = pd.DataFrame()
data_dict = {'A':[2,4,6,8], 'B':'even', 'C':4, 'D':3.14}
df = df.append(data_dict, ignore_index=True)
print(df.dtypes)
```
建立有欄位名稱的空 dataframe，並指定索引  
loc, at：根據索引存入新資料  
append：接上新的 dataframe  
reset_index：重新編列索引  
```python
col_names =  ['A', 'B', 'C']
df  = pd.DataFrame(columns = col_names, index=range(6,10))
df.loc[len(df)] = [2, 4, 5]
df.loc[10] = [1,3,7]
df.at[11,'A'] = 9
df2 = pd.DataFrame([[20,20,20], [200,200,200]], columns=list('ABC'))
df = df.append(df2)
df = df.reset_index(drop=True)
```
### 合併 dataframe
concat：組合 series 成  dataframe  
merge：根據同樣欄位合成更大的 dataframe  
drop：丟棄某欄位  
```python
s1 = pd.Series(["X0", "X1", "X2", "X3"], name="ID")
s2 = pd.Series(range(4))
data_lst = list(zip(list(range(10,14)),
                    ["X0", "X1", "X2", "X3"],
                    ['one', 'two', 'three', 'four']))
df = pd.DataFrame(data_lst, columns=['order','id','number'])
concat_by_row = pd.concat([s1, s2], axis=0)
concat_by_col = pd.concat([s1, s2], axis=1)
merged = pd.merge(df, concat_by_col, left_on='id', right_on='ID', how='left')
merged = merged.drop(columns=['ID'])

concat_by_col = concat_by_col.rename(columns={'ID':'id'})
concat_by_col = concat_by_col.append({'id':'X4',0:4}, ignore_index=True)
merged2 = df.merge(concat_by_col, on='id', how='right', indicator=True)
```
### 篩選 dataframe
isna：過濾出 dataframe 某欄位為空值的列  
isin：過濾出 dataframe 某欄位存在指定值的列  
邏輯運算子：過濾出某欄位特定值的列  
```pyhon
print(merged2[merged2.order.isna()])
print(merged2[~merged2.order.isna()])
print(merged2[merged2._merge=='right_only'])
print(merged2[(merged2._merge=='both')&(merged2.order>11)])
print(merged2[(merged2._merge=='both')&(merged2.number.isin(['one','two']))])
```
### 進階功能
map：指定欄位引用 function  
apply：多欄位引用 function  
```python
merged2.id = merged2.id.map(lambda x: x.replace('X','Y'))
merged2['id2'] = merged2.id.map(lambda x: x.replace('Y','X'))
merged2['selected'] = merged2.apply(lambda x:
                                    (x._merge=='both')&
                                    (x.order>11), axis=1)
```
groupby：針對不同群引用 function  
EX：計算不同群的平均值、百分比  
```python
grouped1 = merged2.groupby(['selected']).order.mean().reset_index()
grouped2 = merged2.groupby(['selected','_merge']).order.mean().reset_index()
grouped3 = merged2.groupby(['selected','_merge']).order.sum().groupby(level=[1]).apply(lambda x:x/x.sum()).reset_index()
```
