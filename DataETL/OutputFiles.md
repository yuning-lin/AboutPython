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
