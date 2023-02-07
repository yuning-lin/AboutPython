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
* [Doc：xlsxwriter](https://xlsxwriter.readthedocs.io/)
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
* 隱藏欄位
    ```python
    worksheet.set_column("A:D", None, None, {'hidden': True})

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
* [Example: DATA VALIDATION IN EXCEL](https://cxn03651.github.io/write_xlsx/data_validation.html)
    ```python
    import xlsxwriter
    # validate 選項：any, integer, decimal, list, date, time, length, custom
    col_content_dict = {
        "Name": {"validate": "list", "source": ["Alex", "Amy", "Alen"]},
        "City": {"validate": "list", "source": ["Taipei", "Tainan", "Taichung"]},
        "Height": {"validate": "integer", "source": None}
    }

    for col_idx, col_name in enumerate(df.columns.values):
        worksheet.write(0, col_idx, col_name, None)
        col_letter = xlsxwriter.utility.xl_col_to_name(col_idx) # idx 轉字母
        worksheet.data_validation(f'{col_letter}2:{col_letter}200', col_content_dict[col_name])
        worksheet.set_column(col_idx, col_idx, 10)
    ```
    錯誤訊息
    ```python
    UserWarning: Length of list items exceeds Excel's limit of 255, use a formula range instead
    ```
    解方
    ```python
    n = 100 # 值會寫入的欄
    city_lst = ["Taipei", "Tainan", "Taichung"]
    for row_count in range(0, len(city_lst)):
        worksheet.write(row_count, n, city_lst[row_count]) # 將所有值寫入該欄
    
    worksheet.data_validation(f'B2:B200', {"validate": "list", "source": '=$CW$1:$CW$3'}) # 利用引用該欄所有值的方式創造下拉選單
    ```
* 顯示篩選符號
    ```python
    writer = pd.ExcelWriter('testtest.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    worksheet = writer.sheets['Sheet1']
    worksheet.autofilter('A1:BX1')
    ```
* 列顏色交錯
    * 若僅橫列需要控制格式，則可使用 set_row
    ```python
    import xlsxwriter
    from itertools import cycle
    
    writer = pd.ExcelWriter('testtest.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    worksheet = writer.sheets['Sheet1']
    # 法一：cycle
    data_format1 = workbook.add_format({'bg_color': '#EEEEEE'})
    data_format2 = workbook.add_format({'bg_color': '#DDDDDD'})
    data_format3 = workbook.add_format({'bg_color': '#CCCCCC'})
    formats = cycle([data_format1, data_format2, data_format3])
    for row, value in enumerate(data):
        data_format = next(formats)
        worksheet.set_row(row, cell_format=data_format)
    
    # 法二：邏輯判斷
    bg_format1 = workbook.add_format({'bg_color': '#78B0DE'}) # blue cell background color
    bg_format2 = workbook.add_format({'bg_color': '#FFFFFF'}) # white cell background color
    for i in range(10): # integer odd-even alternation 
        worksheet.set_row(i, cell_format=(bg_format1 if i%2==0 else bg_format2))
    ```
    * 若直行橫列皆有格式設定，會先後彼此覆蓋格式，則建議用：add_table（可將滑鼠移置 excel 模板 > 設計 > 表格樣式 > 停留幾秒，小白框會顯示 style）
    ```python
    from xlsxwriter.utility import xl_range
    df.T.reset_index().T.to_excel(
        writer, sheet_name='Sheet1', index=False, header=None)
    worksheet = writer.sheets['Sheet1']

    end_row = len(df.index)
    end_column = len(df.columns) - 1
    cell_range = xl_range(0, 0, end_row, end_column) # 指定表格位置
    worksheet.add_table(cell_range, {'data': df.values.tolist(),
                                     'columns': [{'header': c} for c in df.columns.tolist()],
                                     'style': 'Table Style Medium 2'})
    ```
