### 簡介
陣列的計算效率會比 dataframe 來得快  
在需要大量計算下建議使用陣列的形式  
下列將曾經用到的計算技巧記錄
### 引入套件
```python
import numpy as np
```
### 建立單維、多維陣列
```python
x = np.arange(6)
print('arange:', x, '',sep='\n')
x = x.reshape((2, 3))
print('reshape:', x, '',sep='\n')
y = np.ones_like(x)
print('ones_like:', y, '',sep='\n')
y = np.ones_like(x)*np.nan
print('ones_like in nan:', y, '',sep='\n')
```
```
arange:
[0 1 2 3 4 5]

reshape:
[[0 1 2]
 [3 4 5]]

ones_like:
[[1 1 1]
 [1 1 1]]

ones_like in nan:
[[nan nan nan]
 [nan nan nan]]
```
### 排序、反轉陣列
```python
x = np.arange(6)

sorted_x = np.sort(x)
print('sort in ascending order:', sorted_x, '',sep='\n')

reverse_x = sorted_x[::-1]
print('reverse:', reverse_x, '',sep='\n')
```
```
sort in ascending order:
[0 1 2 3 4 5]

reverse:
[5 4 3 2 1 0]
```
### 陣列指定值的位置
```python
ary = np.array([[10, 11, 12, 13, 14],[20, 0, 23, np.inf, 25],[31, -np.inf, np.inf, 100, 36]])

print('get minimum location in row and column:', np.where(ary == ary.min()), '', sep='\n')
print('get maximum location in row and column:', np.where(ary == ary.max()), '', sep='\n')
print('get minimum location in index:', ary.argmin(), '', sep='\n')
print('get maximum location in index:', ary.argmax(), '', sep='\n')
```
```
get minimum location in row and column:
(array([2]), array([1]))

get maximum location in row and column:
(array([1, 2]), array([3, 2]))

get minimum location in index:
11

get maximum location in index:
8
```
### 陣列是否含有 nan, inf
```python
ary = np.array([[10, 11, 12, 13, 14],[20, np.nan, 23, np.inf, 25],[31, -np.inf, np.inf, np.nan, 36]])

print('array:', 
      ary, '',sep='\n')
print('check array if contains any nan:',
      np.any(np.isnan(ary)), '',sep='\n')
print('check array if contains any inf:', 
      np.any(np.isinf(ary)), '',sep='\n')
```
```
array:
[[ 10.  11.  12.  13.  14.]
 [ 20.  nan  23.  inf  25.]
 [ 31. -inf  inf  nan  36.]]

check array if contains any nan:
True

check array if contains any inf:
True
```
### 存取陣列
```python
data = x.reshape((2, 3))
print('array:', data, '',sep='\n')
np.savez("Myfile", data) # save array 

ary = np.load("Myfile.npz") #make sure you use the .npz!
print('get array:', ary['arr_0'], '',sep='\n')
```
```
array:
[[0 1 2]
 [3 4 5]]

get array:
[[0 1 2]
 [3 4 5]]
```
