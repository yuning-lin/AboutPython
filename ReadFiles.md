資料檔案的格式百百款  
pandas 可以處理大部分的種類，但還是會有些例外    
以下羅列使用過的讀檔方式以及曾經遇過的問題做整理：  
### .CSV
一般地端的 csv 檔
```python
import pandas as pd
data = pd.read_csv('file_name.csv')
```
用 url 讀取 csv 檔
```python
import pandas as pd
url = 'https://raw.githubusercontent.com/iopsai/iops/master/phase2_env/large_train.csv'
train = pd.read_csv(url)
```
### .xlsx / .xls
```python
xlsx_file_path = 'file_name.xlsx'
xlsx_data = pd.read_excel(xlsx_file_path, sheet_name=None) # 字典形式包含所有 sheet
xlsx_data = pd.read_excel(xlsx_file_path, sheet_name='SheetName', header=[3,4,5]) # 指定讀的 sheet，以及指定當欄位的列數
```
### .xml
### .txt
### .hdf
