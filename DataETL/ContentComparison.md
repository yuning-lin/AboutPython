## 比較 dataframe 內容是否一致  
合併兩個 dataframe 再 drop_duplicates()  
若僅留下空的 dataframe 則為一致

```python
import pandas as pd

old_df = pd.read_csv('old.csv')
new_df = pd.read_csv('new.csv')
com_df = pd.concat([old_df, new_df], axis=0).reset_index(drop=True)

print(com_df.drop_duplicates(keep=False))
```

## 比較檔案內容是否一致
利用套件 filecmp 直接比較檔案內容是否相同  
True 為相同、False 為不同  

```python
import os
import filecmp

path = 'your_path'
old_file = os.path.join(path, 'oldfile')
new_file = os.path.join(path, 'newfile')
res = filecmp.cmp(old_file, new_file)

print(res)
```
