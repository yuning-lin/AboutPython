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
```python
pd.DataFrame({'col1':[0,1,2,3], 'col2':[2,4,6,8]})
pd.DataFrame.from_dict({'col1':[0,1,2,3], 'col2':[2,4,6,8]})
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
