## dataframe to dictionary
dataframe 兩欄位合成 key, value 的 dictionary
```python
ex_dict = ex_df.set_index(selected_key)[selected_value].to_dict()
```
dataframe 三欄位合成巢狀的 dictionary
```python
ex_dict = ex_df.groupby(selected_outer_key).apply(lambda x:x.set_index(selected_inner_key)[selected_value].to_dict()).reset_index()
```
