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
* 客製化欄位設置：[add_format](https://xlsxwriter.readthedocs.io/format.html)
    1. 凍結欄位
    2. 數值欄位帶千分位逗號
    3. 調整欄寬
    ```python
    col_lst = df.columns.tolist()
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sheet_name, freeze_panes=(1, 9), index=False) # freeze_panes=(1, 9)：凍結欄位名稱及左邊九欄
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]

    num_format = workbook.add_format({'num_format': '#,##0.00'}) # 將數值欄位轉成千分位帶逗號，並取到小數點第二位
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
* 鎖住欄位（有 cell > row > col 這樣可以 overwrite 的關係）
    1. 鎖欄
    2. 鎖列
    3. [overwrite 的關係](https://stackoverflow.com/questions/56240667/not-able-to-unlock-cell-with-custom-value-using-pd-xlsxwriter)
    ```python
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    unlocked = workbook.add_format({'locked': False})
    worksheet.protect()
    worksheet.set_column('A:E', None, unlocked) # 鎖欄
    for row in range(1, 150):
        worksheet.set_row(row, None, unlocked) # 鎖列

    writer.save()
    ```
* 隱藏 sheet（建議要隱藏的 sheet 放後頭做）
    ```python
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    worksheet = writer.sheets['Sheet1']

    df.to_excel(writer, sheet_name='Sheet2', index=False)
    worksheet = writer.sheets['Sheet2']
    worksheet.hide()

    writer.save()
    ```
* [Example: Data Validation and Drop Down Lists](https://xlsxwriter.readthedocs.io/example_data_validate.html)
