# 不同型態轉換
## 數值轉文字
* 千分位、小數點後幾位
```python
num = 10000.3456 
print(f'{int(num):,d}')
print(f'{num:,f}')
print(f'{num:,.2f}')
```
# 不同數據結構轉換
## Dataframe vs List
### column of list into multiple columns
```python
df[['col2','col3']] = pd.DataFrame(df.col1.tolist(), index= df.index)
```
```python
df[['col2','col3']] = df.col1.str.split(",", expand=True)
```

### multiple columns into column of list
```python
df['col1'] = t[['col2','col3']].values.tolist()
```
### 將 list 轉置展開在同個欄位，其它欄位補上一樣的值  
```python
df2 = df.explode('col1')   
```

## Dataframe vs Dictionary
### dataframe to dictionary
dataframe 兩欄位合成 key, value 的 dictionary
```python
ex_dict = ex_df.set_index(selected_key)[selected_value].to_dict()
```
dataframe 三欄位合成巢狀的 dictionary
```python
ex_dict = ex_df.groupby(selected_outer_key).apply(lambda x:x.set_index(selected_inner_key)[selected_value].to_dict()).reset_index()
ex_dict = ex_dict.set_index(selected_outer_key)[0].to_dict()
```
### dictionary to dataframe
一般的 dictionary
```python
pd.DataFrame({'col1':[0,1,2,3], 'col2':[2,4,6,8]})
pd.DataFrame.from_dict({'col1':[0,1,2,3], 'col2':[2,4,6,8]})
pd.DataFrame({'col1':0, 'col2':1}.items(), columns=['name', 'order'])
pd.concat(df_dict.values(), keys=df_dict.keys()).reset_index(level=0).rename(columns={"level_0": "name"}) # rename dictionary key as new column: name
```
巢狀的 dictionary
```python
dict_a = {'col1':{'a':[0,1,2,3], 'b':[2,4,6,8]}, 'col2':{'b':[0,1,2,3], 'a':[2,4,6,8]}}

# 法一：轉成 index
df = pd.concat({k: pd.DataFrame.from_dict(v, 'index') for k, v in dict_a.items()}, axis=0)

# 法二：轉成 column
df = pd.DataFrame.from_records(
    [
        (level1, level2, value)
        for level1, level2_dict in dict_a.items()
        for level2, value in level2_dict.items()
    ],
    columns=['level1', 'level2', 'value']
)
```


## Dataframe vs Array
### dataframe to array
```python
data_array = [[0,1], [7,9], [2,6]]
row_indices = [3, 4, 5]
column_names = ['col1, 'col2']
pd.DataFrame(data_array, index=row_indices, columns=column_names).to_numpy()
pd.DataFrame(data_array, index=row_indices, columns=column_names).values
pd.DataFrame(data_array, index=row_indices, columns=column_names).to_records()
```
### array to dataframe
```python
data_array = [[0,1], [7,9], [2,6]]
row_indices = [3, 4, 5]
column_names = ['col1, 'col2']
pd.DataFrame(data_array, index=row_indices, columns=column_names)
```

## Dataframe vs Json
### dataframe to json
```python
df.to_json()
```

### json to dataframe
```python
import json
with open('filename.json', encoding='utf-8') as fh:
    data_dict = json.load(fh)

df = pd.json_normalize(data_dict,
                       record_path=['nested_col'], # 欲展開的 key
                       meta=main_cols) # 同一 main_cols 下有多組 nested_col

df = pd.json_normalize(data_dict,
                       record_path=['nested_col_layer1', 'nested_col_layer2'], # 欲展開的 key 在更下層的 layer
                       meta=main_cols,
                       errors='ignore') # 同一 main_cols 下有多組 nested_col_layer1 & nested_col_layer2
```

## timestamp vs datetime
### timestamp to datetime
```python
from datetime import datetime

timestamp = 1545730073
dt = datetime.fromtimestamp(timestamp)
```

### datetime to timestamp
```python
from datetime import datetime

dt = datetime.now()
timestamp = datetime.timestamp(dt)
```

## pandas.\_tslib.Timestamp vs datetime
### pandas.\_tslib.Timestamp to datetime
```python
import pandas as pd

timestamp = pd._tslib.Timestamp('2016-03-03 00:00:00')
timestamp.to_pydatetime()
```

### datetime to pandas.\_tslib.Timestamp
```python
from datetime import datetime
import pandas as pd

dt = datetime.now()
timestamp = pd._tslib.Timestamp(dt)
```

# 同數據結構變形
## List
* lists of list into one list
```python
lsts = [[1,2], [3], [5,6]]
sum(lsts, []) # [1,2,3,5,6]
```
* reshape list (but the type into array)
```python
np.reshape([0, 0, 1, 1, 2, 2, 3, 3], (4, 2)).T
# array([[0, 1, 2, 3],
#        [0, 1, 2, 3]])

np.reshape([0, 0, 1, 1, 2, 2, 3, 3], (2, 4))
# array([[0, 0, 1, 1],
#        [2, 2, 3, 3]])
```
## Set
* a list of sets into one set
```python
sets_list = [set(), {' ', '"'}, {',', '-'}, {'-', ' '}]
set().union(*sets_list) # {'"', '-', ',', ' '}
```
