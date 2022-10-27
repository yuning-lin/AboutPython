## pandas
* 重設索引
```python
df.reset_index(drop=True)
```
* MultiIndex
```python
# 將欄位名稱依特殊符號切割後展開成多層索引
df.columns = df.columns.str.split('_', expand=True)
# 只取第一層的所有索引
df.index.get_level_values(0)
```
