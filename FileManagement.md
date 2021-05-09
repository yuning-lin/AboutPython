## 常用檔案管理套件
os：基礎套件，功能多元但也龐雜  
shutil：主要用來搬遷檔案及目錄  
glob：常用來做檔案搜尋，並可以搭配表達式  
## os
### 引入套件
```python
import os
```
### 常用功能
```python
os.getcwd() # 取得現在所在資料夾路徑
os.path.exists(檔案或目錄路徑) # 指定的檔案或目錄路徑是否存在
os.path.isdir(路徑) # 回傳路徑是否為目錄
os.path.isfile(路徑) # 回傳路徑是否為檔案
os.path.join(路徑) # 將路徑加入資料夾環境
os.path.dirname(路徑) # 取得目錄路徑
os.path.basename(路徑) # 取得路徑檔名的部分
os.path.splitext(檔名) # 拆分檔名及副檔名並回傳成 tuple
```
## shutil
### 引入套件
```python
import shutil
```
### 常用功能  
```python
shutil.copy(來源檔案,目的檔案) # 連權限都複製過去了
shutil.copyfile(來源檔案,目的檔案) # 僅複製檔案，不包含權限
shutil.copytree(來源目錄,目的目錄) # 以遞迴的方式將整個目錄的檔案複製至目的目錄
shutil.rmtree(目錄) # 刪除指定目錄下所有檔案
shutil.move(來源檔案或目錄,目的地) # 移動檔案或目錄
```
## glob
### 引入套件
```python
import glob
```
### 常用功能
搜尋目錄下指定搜尋的副檔名或符合正則表達式的檔名  
```python
files = glob.glob('*.txt')+glob.glob('./[0-9].py')
for i in files:
    print(i)
```
將目錄下所有指定副檔名檔案由新至舊排序  
```python
files_path = os.path.join(path, "*.csv")
sorted_files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
```
