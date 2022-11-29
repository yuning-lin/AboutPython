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
