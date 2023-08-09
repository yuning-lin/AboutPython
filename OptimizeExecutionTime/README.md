## 簡介
程式執行效率比較紀錄

* dataframe 單欄運算：快到慢（由上到下）
```python
df["col2"] = df["col1"]*2 # 盡可能地向量運算

df["col2"] = [x*2 - 1 for x in df["col1"]]

df["col2"] = df["col1"].map(lambda x: x*2)
```

* dataframe 單欄映射：快到慢（由上到下）
```python
map_dict = {'a':'small', 'b':'big'}
df["col2"] = df["col1"].map(map_dict)

df["col2"] = ['small' for x in df["col1"] if x == 'a' else 'big']
```

* dataframe cell 賦值：快到慢（由上到下）
1. df.apply(axis=1)
2. df.itertuples()
3. df.iterrows()

* dataframe 多欄位賦值：快到慢（由上到下）
```python
df['col1'], df['col2'], df['col3'] = zip(*df['size'].apply(func))

df[['col1', 'col2', 'col3']] = df.apply(func, axis=1) # , result_type="expand"
```

* dataframe 單欄篩選：快到慢（由上到下）
```python
mask = (df.col1.isin(['N']))

mask = (df.col1 == 'N')
```

## 篩選值
* list_comprehension 比較快
* NameError: name 'filter_and_list' is not defined -> 記得 setup 參數要填值
```python
import timeit

def filter_and_list():
    results = list(filter(lambda x: x == 1, range(100000)))

def list_comprehension():
    results = [x for x in range(100000) if x == 1]

if __name__ == "__main__":
    print(timeit.timeit("filter_and_list()", number=1000, setup="from __main__ import filter_and_list"))
    print(timeit.timeit("list_comprehension()", number=1000, setup="from __main__ import list_comprehension"))

```

## 排序
* list：.sort() 效率優於 sorted()，因為不用再另外指向一變數
* 若可以 numpy array 為資料結構，運算上有機會比 list 更快
```python
import numpy as np
import pandas as pd
import time

# 創建一個包含屬性的列表
class TestObject:
   def __init__(self, lst):
       self.lst = lst

data = [TestObject([]) for _ in range(1000000)]
data_list = data.copy()

# 使用 sorted() 進行排序
start_time = time.time()
sorted_list = sorted(data_list, key=lambda obj: len(obj.lst) if obj.lst else -1)
print("sorted() elapsed time:", time.time() - start_time)

# 使用 .sort() 進行排序
data_copy = data_list.copy()
start_time = time.time()
data_copy.sort(key=lambda obj: len(obj.availableResource) if obj.lst else -1)
print(".sort() elapsed time:", time.time() - start_time)

# 使用 NumPy 進行排序
data_np = np.array(data)
start_time = time.time()
sorted_np = data_np[np.argsort([len(obj.lst) if obj.lst else -1 for obj in data])]
print("NumPy sort elapsed time:", time.time() - start_time)
```

## 進度條
* dataframe apply function：
```python
from tqdm import tqdm
tqdm.pandas() # tqdm: 4.8+
df.progress_apply(func, axis=1)
df.groupby([cols]).progress_apply(func)
```

* dataframe iterrows：
```python
from tqdm import tqdm

for i, r in tqdm(df.iterrows(), total=df.shape[0]):
  print('your work')
```
