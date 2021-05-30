## 多線程
當執行的運算不會有先後順序影響才可以使用此法讓運算更有效率  
### 引入套件
```python
import concurrent.futures # 平行運算
import tqdm # 呈現運算進度條
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
