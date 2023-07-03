### 開放資料來源
* [Taiwan 政府開放資料](https://data.gov.tw/)
* [America 政府開放資料](https://catalog.data.gov/dataset)
* [New Zealand 政府開放資料](https://www.stats.govt.nz/)  

### [讀檔技巧](https://github.com/yuning-lin/PythonTips/blob/main/ReadFiles.md)
### [建立、合併、篩選、map、apply](https://github.com/yuning-lin/PythonTips/blob/main/DataETL/Pandas.ipynb)

### 存檔技巧
* 存成帶樣式的 EXCEL
* [style 參考資料](https://pandas.pydata.org/pandas-docs/version/0.24.1/user_guide/style.html)
* [to_excel 參考資料](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html)
```python
## 針對特定 cell 上色
def highlight_cells(val):
    if 'fitted' in val and 'carry' not in val:
        bg_color = '#A8DADC'
        ft_color = '#1D3557'
    else:
        bg_color = '#1D3557'
        ft_color = '#A8DADC'
    return 'color: {}; background-color: {}'.format(ft_color, bg_color)

## 針對特定 row 上色
def highlight_rows(row):
    value = row.loc['specific_column_name']
    if 'carry' in value:
        bg_color = '#1D3557'
        ft_color = '#A8DADC'
    else:
        bg_color = 'white'
        ft_color = 'black'
    return ['color: {}; background-color: {}'.format(ft_color, bg_color) for r in row]

## 指定 column 寬度
def format_col_width(ws):
    ws.column_dimensions['B'].width = 25
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15
    ws.column_dimensions['G'].width = 15
```
```python
'''
1. set_properties：將檔案做文字置中、粗體
2. 並且套用 highlight_rows、highlight_cells
3. 指定存檔的位置及名稱
4. 套用指定欄寬
'''
writer = pd.ExcelWriter(path+'file_name.xlsx')
report.style.set_properties(**{'text-align': 'center', 'font-weight': 'bold'}).apply(highlight_rows, axis=1)\
            .applymap(highlight_cells, subset=['specific_column_name'])\
            .to_excel(writer, sheet_name='sheet1', header=False, index=False, startrow=10, startcol=1)
format_col_width(writer.sheets['sheet1'])
writer.save()
```
### 指定 pandas dataframe 在 console 秀出的大小
```python
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 100)
```
### 快速檢查 dataframe 是否含有 nan, inf
```python
df = pd.DataFrame({'col1':[10, 11, 12, 13, 14],
                   'col2':[20, np.nan, 23, np.inf, 25],
                   'col3':[31, -np.inf, np.inf, np.nan, 36]})
print('df:')
print(df)
print()
print('check dataframe if contains any nan:')
print(df.isnull().values.any())
print()
print('get dataframe containing inf, -inf:')
print(df[~np.isfinite(df).all(1)])
print()
print('get column containing inf, -inf:')
col_name = df.columns.to_series()[np.isinf(df).any()]
print(col_name)
print()
print('get index containing inf, -inf:')
idx = df.index[np.isinf(df).any(1)]
print(idx)
```
```
df:
   col1  col2  col3
0    10  20.0  31.0
1    11   NaN  -inf
2    12  23.0   inf
3    13   inf   NaN
4    14  25.0  36.0

check dataframe if contains any nan:
True

get dataframe containing inf, -inf:
   col1  col2  col3
1    11   NaN  -inf
2    12  23.0   inf
3    13   inf   NaN

get column containing inf, -inf:
col2    col2
col3    col3
dtype: object

get index containing inf, -inf:
Int64Index([1, 2, 3], dtype='int64')
```
### 欄位空值補值
```python
df.col2 = df.col2.fillna(-99) #補特定值
df.col2 = df.col2.fillna(df.col1) #用其他欄位補值
```
### 隨機排序 dataframe 順序
```python
df = df.sample(frac=1).reset_index(drop=True)
```
  
參數|意義
----|----
n|要抽出的筆數(int)
frac|要抽出的比例（0～1 的小數）
replace|True 為取後放回
random_state|給固定數字，每次隨機抽取的起始點會一樣
axis|根據哪個軸隨機抽，0：橫列、1：直欄

### 去重
* 去除同樣欄位
```python
df = pd.concat([new_df, old_df], axis=1)
df = df.loc[:,~df.columns.duplicated(keep=False)]
```
* 去除指定欄位同樣值列
```python
df = pd.concat([new_df, old_df], axis=0)
df = df.drop_duplicates(subset=['col'], keep=False)
```

### 一欄位內兩值組為 tuple > 拆成兩欄位
```python
df[['b1', 'b2']] = pd.DataFrame(df['b'].tolist(), index=df.index)
```

### 兩個 series 內的文字 > 組成一欄位
```python
df['b3'] = df['b1'] + df['b2']
df['b4'] = pd.Series(['-'] * len(df)) + df['b2']
```

### groupby
groupby：針對不同群引用 function  
EX：計算不同群的平均值、百分比、將不同群的值包成一個 array  
```python
grouped1 = merged2.groupby(['selected']).order.mean().reset_index()
grouped2 = merged2.groupby(['selected','_merge']).order.mean().reset_index()
grouped3 = merged2.groupby(['selected','_merge']).order.sum().groupby(level=[1]).apply(lambda x:x/x.sum()).reset_index()
grouped4 = merged2.groupby('selected').id.apply(np.array).reset_index()
```

groupby：保留欄位 na 值 
```python
df.groupby('b', dropna=False).sum()
```

groupby 做迴圈取值或計算，可以搭配多線程使用
```python
groupby_action = merged2.groupby(['selected','_merge'])
print(groupby_action.groups) # 取得所有 group 的 key & index
for key, group in groupby_action: # groupby 做迴圈
    print(key)
    print(group)
```

groupby 多欄位做計算且帶欄位命名，依序執行效率由快到慢
```python
df.groupby('group').agg(
    a_sum=('a', 'sum'),
    a_mean=('a', 'mean'),
    b_mean=('b', 'mean'),
    c_sum=('c', 'sum'),
    d_range=('d', lambda x: x.max() - x.min())
)

df.groupby('group').agg(
    a_sum=pd.NamedAgg(column="a", aggfunc="sum"),
    a_mean=pd.NamedAgg(column="a", aggfunc="mean"),
    b_mean=pd.NamedAgg(column="b", aggfunc="mean")
)

df.groupby('group') \
  .apply(lambda x: pd.Series({
      'a_sum'       : x['a'].sum(),
      'a_max'       : x['a'].max(),
      'b_mean'      : x['b'].mean(),
      'c_d_prodsum' : (x['c'] * x['d']).sum()
  })
)
```
