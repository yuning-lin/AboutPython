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

## 佇列（Queue）
欲將不同工作同時作業除了利用 [airflow](https://github.com/yuning-lin/EnvironmentSetup/tree/main/AirFlow) 作控管外  
也可以讓多個 CPU 去佇列中處理尚未運算的工作  
運算結果仍須是不受先後順序影響，且工作內容可以是非重複性的  

```python
import multiprocessing as mp

def job(q):
    result = 0
    for i in range(100):
        result += i*i
    q.put(result) 
# put 類似 return 的概念，若 result 資訊太大，對 join 運作效果不佳
# 故建議若 result 為 dataframe 可以先存成 csv，並用 put 回傳 EX：路徑訊息即可

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
