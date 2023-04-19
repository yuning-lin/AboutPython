## 多線程
當執行的運算不會有先後順序影響，且工作內容是重複性的才可以使用以下方法讓運算更有效率  
### 引入套件
```python
import concurrent.futures # 平行運算
from tqdm import tqdm # 呈現運算進度條
```
### map
EX：將較複雜的欄位計算做平行處理
```python
with concurrent.futures.ProcessPoolExecutor(4) as pool:
    data.loc[mask, 'col_name'] = list(
        tqdm(
            pool.map(
                function_name,
                function_parameters,
                chunksize=10,
            ),
            total=data.loc[mask].shape[0],
        )
    )
```
### submit
EX：將 dataframe 用 groupby 做切分，不同 group 個別丟入做平行運算，且 function 回傳<ins>單值</ins>
```python
data_lst = []
with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(function_name, group) for _, group in data.groupby(['col_name'])]
    for fut in tqdm(concurrent.futures.as_completed(futures)):
        data_lst.append(fut.result()) # result() 若 function 僅回傳一種值則不需要索引
result = pd.concat(data_lst, axis=0)
```
EX：將 dataframe 用 groupby 做切分，不同 group 個別丟入做平行運算，且 function 回傳<ins>多值</ins>
```python
data1_lst = []
data2_lst = []
with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(function_name, group) for _, group in data.groupby(['col_name'])]
    for fut in tqdm(concurrent.futures.as_completed(futures)):
        data1_lst.append(fut.result()[0]) # result() 根據函式回傳順序做存儲
        data2_lst.append(fut.result()[1])
result1 = pd.concat(data1_lst, axis=0)
result2 = pd.concat(data2_lst, axis=0)
```
### 問題與解決
* Q：多線程程式碼和執行 function 在同一檔案下，執行多線程遇到以下問題
    ```
    concurrent.futures.process.BrokenProcessPool: A process in the process pool was terminated abruptly while the future was running or pending.
    ```
  A：多線程程式碼和執行 function 中間用 `if __name__ == '__main__':` 隔開
    ```python
    def function(para):
        return
        
    if __name__ == '__main__':
        data_lst = []
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(function, group) for _, group in data.groupby(['col_name'])]
            for fut in tqdm(concurrent.futures.as_completed(futures)):
                data_lst.append(fut.result()) # result() 若 function 僅回傳一種值則不需要索引
        result = pd.concat(data_lst, axis=0)
    ```
* Q：執行多線程遇到以下問題
    ```
    RecursionError: maximum recursion depth exceeded while pickling an object
    ```
  A：除了簡化程式運算外，可以利用 sys 改變設置，並設置於整包程式起始程式內
    ```python
    import sys
    sys.getrecursionlimit() # get default value
    sys.setrecursionlimit(4000) # there is no rules for setting new value. keep try and error.
    ```
* Q：`Synchronized objects should only be shared between processes through inheritance`  
  A：[Parent process 分享資料(shared memory) Child process](https://myapollo.com.tw/blog/python-multiprocessing/#parent-process-%e5%88%86%e4%ba%ab%e8%b3%87%e6%96%99shared-memory-child-process)
    
## 佇列（Queue）
欲將不同工作同時作業除了利用 [airflow](https://github.com/yuning-lin/EnvironmentSetup/tree/main/AirFlow) 作控管外  
也可以讓多個 CPU 去佇列中處理尚未運算的工作  
運算結果仍須是不受先後順序影響，且工作內容可以是非重複性的  

### 無須回到 main process 執行其他動作
```python
import multiprocessing as mp

def job(q):
    result = 0
    for i in range(100):
        result += i*i
    q.put(result) 

q = mp.Queue()   # 使用 queue 接收 function 的回傳值
p1 = mp.Process(target=job, args=(q,)) # 注意：若傳入參數只有一個的話，後面要有逗號
p2 = mp.Process(target=job, args=(q,))
p1.start()
p2.start()

p1.join()
p2.join()
res1 = q.get()
res2 = q.get()
```

### 須回到 main process 執行其他動作
```python
import multiprocessing as mp

def job(q):
    result = 0
    for i in range(100):
        result += i*i
    q.put(result) 

q = mp.Queue()   # 使用 queue 接收 function 的回傳值
p1 = mp.Process(target=job, args=(q,)) # 注意：若傳入參數只有一個的話，後面要有逗號
p2 = mp.Process(target=job, args=(q,))
p1.start()
p2.start()

res1 = q.get()
res2 = q.get()
final = res1 + res2
p1.join()
p2.join()
```

### 函數意義
* put 類似 return 的概念
* join 是在等待 child process 執行完畢
    1. 若 child process 執行完畢後無須回到 main process 執行其他動作 ＞ 先 join 再 get  
    2. 若 child process 執行完畢後須回到 main process 執行其他動作 ＞ 先 get 再 join；或是直接不用 join

### multiprocessing.Pool method 比較表
```
                  | Multi-args   Concurrence    Blocking     Ordered-results
---------------------------------------------------------------------
Pool.map          | no           yes            yes          yes
Pool.map_async    | no           yes            no           yes
Pool.apply        | yes          no             yes          no
Pool.apply_async  | yes          yes            no           no
Pool.starmap      | yes          yes            yes          yes
Pool.starmap_async| yes          yes            no           no
```
### 參考資料
* [python multiprocessing guidelines](https://docs.python.org/3.9/library/multiprocessing.html#programming-guidelines)
* [multiprocessing.Pool: When to use apply, apply_async or map?](https://stackoverflow.com/questions/8533318/multiprocessing-pool-when-to-use-apply-apply-async-or-map)
* [python多进程踩过的坑](https://www.jianshu.com/p/2e6d72ae1770)


