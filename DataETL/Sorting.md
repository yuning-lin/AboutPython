## list
* 按大小排序
```python
a = ['b','a','c']
a.sort()
# a = sorted(a)
print(a)
```
* 反向排序
```python
a = ['b','a','c']
a.sort(reverse = True)
# a = sorted(a, reverse = True)
print(a)
```
* 按自定義排序
a 的順序按照 c 的順序排
```python
a = ['b','a','c']
c = ['c','e','b','a']
d = dict(zip(c,range(len(c))))
# a.sort(key=lambda x:d[x]) # 部分 python 版本不能使用
a = sorted(a, key=lambda x: d[x])
print(a)
```
* 物件排序
物件依括號填入的 attribute 排序，負號為該 attribute 反向排序
```python
class info:
    def __init__(self, number, age, height, weight):
        self.number = number
        self.age = age
        self.height = height
        self.weight = weight
A = info(0, 15, 160, 50)
B = info(2, 16, 150, 55)
C = info(1, 14, 170, 60)

lst = [A, B, C]
sorted(lst, key=lambda x:(x.number, -x.age, x.height, -x.weight))
```
## dataframe
* 按大小、正反向排序
df 的順序按照 col2 由小到大、col3 由大到小排序
```python
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})
df.sort_values(by=['col2', 'col3'], ascending=[True, False])
```

* 按自定義排序
df 的順序按照 col4 的順序排
```python
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})

# 法一
df.sort_values(by='col4', key=lambda col: col.str.lower())

# 法二
col_order = df.col4.drop_duplicates()
dict_col_order = dict(zip(col_order, range(len(col_order))))
df.sort_values(by="col4", key=lambda x: x.map(dict_col_order))
```
## dictionary
根據 value 排序，回傳 key
```python
my_dict = {'b': 2, 'a': 3, 'c': 0}
max(my_dict, key=my_dict.get)
```
