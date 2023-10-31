# Factory Pattern
可中譯為工廠模式，是最常見的設計模式之一   
可以避免一直用 if、elif、else 實現目的  
達到更好閱讀及維護的效果  

## 範例一
假設一個工廠有兩項產品，這兩項產品的組裝、打包方式皆不同
```python
class ProductA:
    """A產品線"""
    def __init__(self):
        self.name = "A"
    def run(self):
        a = "apple"
        b = "banana"
        process = a+b

class ProductB:
    """B產品線"""
    def __init__(self):
        self.name = "B"
    def run(self):
        c = "citrus"
        b = "banana"
        process = c+2*b

def FactoryInterface(classname):
    """工廠模式介面函式"""
    run = {'A':ProductA,'B':ProductB}
    return run[classname]()

FactoryInterface(A)
FactoryInterface(B)
```
