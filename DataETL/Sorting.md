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
* 按自訂義排序
a 的順序按照 c 的順序排
```python
a = ['b','a','c']
c = ['c','e','b','a']
d = dict(zip(c,range(len(c))))
a.sort(key=lambda x:d[x])
print(a)
```
