## 前言
首要通則避開程式保留字  
能短就不要長，但也不能短到看不懂意義  
也可以運用底線來達到對變數的功能控制  
通常團隊間有常用的規則，follow 即可  
此文件介紹常為眾人使用的 coding style：PEP8  
以 79 字元為程式排版斷點原則  
也有其建議的命名規則，大致整理如下

## 命名規則
```python
## 可印出所有保留字
print(vars(__builtin__).keys())
```
### 底線運用
* foo_：避免與保留字撞名
* \_foo：不想被訪問、不想被直接引入
* \_\_foo：子類別繼承父類別時，同樣命名無法輕易改變父類別內容
* \_\_foo\_\_：通常是 python 內建的 methods 或 variables，通常不用此命名

### 程式內文
類別|規則|範例
----|----|----
constant|全大寫用底線連接單詞|GLOBAL_CONSTANT_NAME = 0
class name|駝峰式命名|class DataPreprocessing(object):
module name|全小寫用底線連接單詞|module_name.py
function name|全小寫用底線連接單詞，首詞以動詞開頭|def read_data():
variable name|全小寫用底線連接單詞。有 DB table，需對齊 column name、尾詞可帶入變數型態|iris_df
file name|全小寫用底線連接單詞，若有更新日期可代入檔名|download_data_20200101.csv

### 資料庫
類別|規則|範例
----|----|----
database name|全小寫用底線連接單詞|flowers
table name|全小寫用底線連接單詞，且第一部分是群組名|flowers_location
column name|全小寫用底線連接單詞，縮寫保留全大寫|iris_DE

## Coding Style 設置
### IDE 設定－eclipse
1. Window > Preferences > 搜尋 Code Formatter
2. 選取 black 或 autopep8
3. 左下角 save to 選擇想要套用的範圍 > Apply and Close
4. 若還是沒有改到，可點選 Source > Format Code 後 Refresh 
  
![](https://github.com/yuning-lin/PythonTips/blob/main/PythonTipsPics/eclipse-code-formatter.png)  

### 下 command
1. 需先安裝套件：`pip install black`
2. 根據個人需求下下列指令（切割字元長度預設為 88）

語法|意義
---|---
`black --check .`|秀出當前資料夾套用此 code style **會被更改的檔案有哪些**，但尚不會真的變更檔案
`black --check --diff file_name.py`|秀出指定檔案套用此 code style **會被更改的程式內文**，但尚不會真的變更檔案
`black -l 80 file_name.py/current folder`|指定切割字元長度為 80 且變更此檔／當前目錄的 code style 

## 參考來源：
* [Harvard](https://datamanagement.hms.harvard.edu/collect/file-naming-conventions)
* [Princeton](https://libguides.princeton.edu/c.php?g=102546&p=930626)
* [PEP8 編碼原文](http://legacy.python.org/dev/peps/pep-0008/)
* [PEP8 編碼中譯](https://www.cnblogs.com/PortosHan/p/14447416.html#naming-conventions-%E5%91%BD%E5%90%8D%E8%A7%84%E8%8C%83)
* [PEP8 Wiki](https://zh.wikipedia.org/wiki/%E5%91%BD%E5%90%8D%E8%A7%84%E5%88%99_(%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1))
* [PEP8 編碼手冊－Blog](https://cflin.com/wordpress/603/pep8-python%E7%B7%A8%E7%A2%BC%E8%A6%8F%E7%AF%84%E6%89%8B%E5%86%8A)
* [PEP8 Code Style - Blog](https://myapollo.com.tw/zh-tw/python-pep8-and-vim-configs/)
* [資料庫命名規範詳解](https://kknews.cc/zh-tw/news/r5b22ar.html)
* [資料庫命名規範](https://www.itread01.com/content/1544270418.html)
* [部落格：Python 底線命名](https://aji.tw/2017/06/python%E4%BD%A0%E5%88%B0%E5%BA%95%E6%98%AF%E5%9C%A8__%E5%BA%95%E7%B7%9A__%E4%BB%80%E9%BA%BC%E5%95%A6/)
