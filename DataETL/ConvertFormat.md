# 不同數據結構轉換
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
### array to Dataframe
```python
data_array = [[0,1], [7,9], [2,6]]
row_indices = [3, 4, 5]
column_names = ['col1, 'col2']
pd.DataFrame(data_array, index=row_indices, columns=column_names)
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
