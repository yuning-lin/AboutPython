## lambda function
* 一般用法
```python
add = lambda x: x + 1
print(add(5)) # 6
```
* 進階用法－搭配 global 變數
```python
x = 10

def my_func():
    global x
    x = 20
    my_lambda = lambda y: x + y
    return my_lambda

print(my_lambda(5))  # 25
```
* 進階用法－搭配 ABC
```python
from abc import ABC, abstractmethod

class FilterFunc(ABC):
    @abstractmethod
    def match(self, supply: Supply) -> bool:
        pass

class LambdaMatch(FilterFunc):
    def __init__(self, lambdaFunc):
        self.lambdaFunc = lambdaFunc

    def match(self, args) -> bool:
        return self.lambdaFunc(args)


def Filtering(FilterA: FilterFunc, FilterB: FilterFunc, keywords):
    if keywords.startswith('A'):
        return FilterA.match(keywords)
    elif keywords.startswith('B'):
        return FilterB.match(keywords)

Filtering(FilterA = LambdaMatch(lambda keywords: len(keywords.split('_')[0]) > 1),
          FilterB = LambdaMatch(lambda keywords: keywords+'_END'),
          'America')
```


### 參考資料
* [Blog：Python進階技巧 (4) — Lambda Function 與 Closure 之謎！](https://medium.com/citycoddee/python%E9%80%B2%E9%9A%8E%E6%8A%80%E5%B7%A7-4-lambda-function-%E8%88%87-closure-%E4%B9%8B%E8%AC%8E-7a385a35e1d8)
* [Blog：認識 Lambda/Closure（3）Python 對 Lambda/Closure 的支援](https://openhome.cc/Gossip/CodeData/JavaLambdaTutorial/Python.html)
