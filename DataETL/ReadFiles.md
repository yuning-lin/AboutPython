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
此兩副檔名讀取方式一樣  
需先安裝套件： `xlrd`、`openpyxl`
```python
import pandas as pd
xlsx_file_path = 'file_name.xlsx'
xlsx_data = pd.read_excel(xlsx_file_path, sheet_name=None) # 字典形式包含所有 sheet
xlsx_data = pd.read_excel(xlsx_file_path, sheet_name='SheetName', header=[3,4,5]) # 指定讀的 sheet，以及指定當欄位的列數
```
常見錯誤訊息：  
```
raise XLRDError(FILE_FORMAT_DESCRIPTIONS[file_format]+'; not supported')
xlrd.biffh.XLRDError: Excel xlsx file; not supported
```
* 法一：安裝較舊版本，`pip install xlrd==1.2.0`
* 法二：使用 openpyxl 開啟，`pd.read_excel(path, engine='openpyxl')`
* 安全組合：pandas==1.1.4, xlrd==1.2.0

### .xml
### .txt
```python
import pandas as pd
txt_data = pd.read_table(txt_file_path, header=None, sep=" ", encoding='utf-8') # sep 根據檔案區分欄列間的標號做選填
```
### .hdf
需先安裝套件： `numpy`、`tables`
```python
import pandas as pd
hdf_data = pd.read_hdf('hdf_file_path.hdf')
```
另外也有專屬套件 `pyhdf` 讀取 .hdf
詳見：[參考一](https://blog.csdn.net/lly1122334/article/details/102493134)、[參考二](https://moonbooks.org/Articles/How-to-read-a-MODIS-HDF-file-using-python-/)
