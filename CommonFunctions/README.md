## 常用 functions
  
* 若路徑不存在則建立該路徑
```python
import os

def check_path_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)
```

* 紀錄 function 運算時間
```python
from functools import wraps
from time import time

def timing(func):
    @wraps(func)
    def wrap_func(cls, *args, **kwargs):
        start_time = time()
        result = func(cls, *args, **kwargs)
        end_time = time()
        spent_time = end_time - start_time
        print(f' {func.__name__!r} executed in {spent_time:.4f}s')
        return result
    return wrap_func

@timing
def test():
    print('test')
```

* 多個 If else 轉 dictionary 形式
  * Method 1
  ```python
  def operations(operator, x, y):
      return {
          'add': lambda: x+y,
          'sub': lambda: x-y,
          'mul': lambda: x*y,
          'div': lambda: x/y
      }.get(operator, lambda: 'invalid operation')()

  operations('mul', 7, 8)
  operations('aaa', 7, 8)
  ```
  * Method 2
  ```python
  def operation_add(x, y):
    return x+y
  def operation_sub(x, y):
    return x-y
  def operation_mul(x, y):
    return x*y
  def operation_div(x, y):
    return x/y

  operation = {
    'add': operation_add,
    'sub': operation_sub,
    'mul': operation_mul,
    'div': operation_div
  }

  operation['mul'](7, 8)
  ```
