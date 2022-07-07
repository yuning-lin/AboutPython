## 簡介
常將不同格式的資料做轉換  
Python 也有套件可以做到  
但是要注意大部分的套件做 Microsoft Office 檔案的轉換僅能在 Windows 上執行  
以下介紹在 Windows 上好用的套件

## 套件
套件|優點|缺點|實驗結果
---|---|---|---
`pip install pywin32`|可以使用於多種檔案類型|僅能在 Windows 使用|Windows 可以執行
`pip install aspose.slides`|程式碼少|付費才能沒有浮水印|Windows 可以執行
`pip install unoconv`|[據說](https://gist.github.com/vikram-ai/5c811d076f7c4d17d3b497fc5fff8224)可以在 linux 環境使用|少成功案例|Windows 沒有成功轉檔


## 範例
```python
"""
pip install pywin32
remember the file path should be absolute one not relative
"""

from win32com import client

# word to pdf
def word_to_pdf():
    app = client.Dispatch("Word.Application")
    doc = app.Documents.Open('your_path/doc_name.docx')
    doc.ExportAsFixedFormat('your_path/pdf_name.pdf', client.constants.wdExportFormatPDF)
    doc.Close()
    app.Quit()
    
# excel to pdf
def excel_to_pdf():
    app = client.Dispatch("Excel.Application")
    xls = app.Workbooks.Open('your_path/xls_name.xlsx')
    xls.ExportAsFixedFormat(0, 'your_path/pdf_name.pdf')
    xls.Close()
    app.Quit()

# ppt to pdf
def ppt_to_pdf():
    app = client.Dispatch("PowerPoint.Application")
    ppt = app.Presentations.Open('your_path/ppt_name.pptx', False, False, False)
    # ppt.ExportAsFixedFormat('your_path/pdf_name.pdf', 2, PrintRange=None)
    ppt.SaveAs('your_path/pdf_name.pdf', 32) # 17: to pictures, 32: to pdf 
    # ppt.PrintOut(PrintToFile='your_path/pdf_name.pdf')
    ppt.Close()
    app.Quit()
```

## 資料來源
* [github: pywin32](https://github.com/mhammond/pywin32)
* [github: unoconv](https://github.com/unoconv/unoconv)
* [Aspose: Convert PPT to PDF in Python](https://blog.aspose.com/2021/12/28/convert-pptx-ppt-to-pdf-python/)
