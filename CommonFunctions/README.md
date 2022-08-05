## 常用 functions
  
* 若路徑不存在則建立該路徑
```python
import os

def check_path_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)
```
