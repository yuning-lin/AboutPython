## 常用 functions
  
* 若路徑不存在則建立該路徑
```python
import os

def check_path_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)
```

* 客製化 log
```python
from loguru import logger

def CustomizedLog(file_log='./log/file_{time}.log'):  # add: log folder
    logger.add(file_log,
               format="{time:YYYY-MM-DD HH:mm:ss}|[{level}]|{file}|{function}()-[{line}]|{message}",
                retention="10 days",
                encoding="utf-8",
                level="INFO")
    return logger
```

```python
def customized_log(file_log='../log/file_{date}.log'):  
    # 獲取當前日期  
    current_date = datetime.now().strftime("%Y-%m-%d")  

    # 替換檔案名稱中的 {date} 佔位符  
    file_log = file_log.replace("{date}", current_date)  

    logger.add(file_log,  
               format="{time:YYYY-MM-DD HH:mm:ss}|[{level}]|{file}|{function}()-[{line}]|{message}",  
               retention="10 days",  
               encoding="utf-8-sig",  
               level="INFO")  
    return logger  
```

* python sqlalchemy insert table by primary key
```python
from sqlalchemy import create_engine
import pandas as pd

q_str = ', '.join(['?'] * len(df.columns))
c_str = ', '.join(list(df.columns))
w_str = ', '.join([f't.{i}=s.{i}' for i in df.columns])
s_str = ', '.join([f's.{i}' for i in df.columns])
sql = f"""
        MERGE db_name..table_name  as t
        USING (Values({q_str})) AS s({c_str})
        ON t.pri_key1 = s.pri_key1 and t.pri_key2 = s.pri_key2
        WHEN MATCHED
            THEN UPDATE SET
                {w_str}
        WHEN NOT MATCHED BY TARGET
            THEN INSERT ({c_str})
                 VALUES ({s_str});
        """

engine = create_engine("mssql+pyodbc://{}:{}@{}/{}?driver={}".format(UID, PWD, SERVER, DATABASE, DRIVER))
con = engine.connect()
trans = con.begin()
try:
  con.execute(sql, df.values.tolist())
  trans.commit()
except Exception as ex:
  trans.rollback()
```

* 取得 SQL table primary key
```python
sql = f"""
SELECT COLUMN_NAME 
FROM db_name.INFORMATION_SCHEMA.KEY_COLUMN_USAGE 
WHERE OBJECTPROPERTY(OBJECT_ID(CONSTRAINT_SCHEMA + '.' + QUOTENAME(CONSTRAINT_NAME)), 'IsPrimaryKey') = 1 
AND TABLE_NAME = '{table_name}'
"""
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
