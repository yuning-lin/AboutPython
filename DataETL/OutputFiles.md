回顧 pandas 如何[讀檔](https://github.com/yuning-lin/PythonTips/blob/main/DataETL/ReadFiles.md)  
pandas 大部分的檔案格式都可以儲存  
以下羅列使用過的讀檔方式以及曾經遇過的問題做整理：  
```python
import pandas as pd
```



## .csv
是最常使用的格式之一
```python
## 一般存檔方式
final_df.to_csv('output.csv', index=False)

## 有中文在檔案中
final_df.to_csv('output.csv', index=False, encoding="utf-8")
final_df.to_csv('output.csv', index=False, encoding="utf_8_sig")
```


## .xlsx
客製化 dataframe 在 .xlsx 的樣態
```python
col_lst = df.columns.tolist()
writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name, freeze_panes=(1, 9), index=False) # freeze_panes=(1, 9)：凍結欄位名稱及左邊九欄
workbook = writer.book
worksheet = writer.sheets[sheet_name]

num_format = workbook.add_format({'num_format': '#,##0'}) # 將數值欄位轉成千分位帶逗號
for idx in range(len(col_lst)):
    worksheet.set_column(idx, idx, 10, num_format) # 將欄寬設為：10

writer.save()
```
錯誤訊息
```python
AttributeError: ‘Worksheet’ object has no attribute 'set_column'
```
解方
```python
pip install XlsxWriter
```

