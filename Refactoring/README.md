## 簡介
學習寫好程式的路上...


## 測試
### 測試類別
* [單元測試（unit test）](https://github.com/yuning-lin/PythonTips/blob/main/Refactoring/unit_test.ipynb)
  專案越大越難維護，利用把每個最小單元都有測試去維持程式品質  
  如此在對於程式重構也可以避免新舊程式矛盾或改動情形  
  1. 寫好單元測試，對原程式進行測試
  2. 重構後再行測試，確保沒有破壞程式
  3. PLUS：配合版本控制，可以避免錯誤無法回復
* 整合測試（integration test）
* 端對端測試（end-to-end test）

### 測試框架
在大框架下可以分門別類結構化的管理測試內容  
可以搭配 CI 做到自動化測試並分析程式涵蓋率  
若程式有符合物件導向原則，比較容易可以做單元測試，也是檢視程式品質方法之一  
可以根據每個 function 做測試，也可以根據整個 script 結果做測試  

* unittest：標準庫的單元測試
  執行方式：
  1. `if __name__ == "__main__"`: 下：`unittest.main()`
  2. 終端機：`python -m unittest <file_name>`
  核心概念有四：
  1. test case：最小單元的以 test_ 開頭命名的 function
  2. test fixture：setUp、testDown
  3. test suite：test fixture 集合
  4. test runner：執行
* pytest：Python 第三方單元測試
* Flask-Testing：Flask 的 unittest

### Code Coverage
可以搭配單元測試衡量受測代碼的測試情況，並量化之  
python 套件名稱：`pip install coverage`  
通常會根據專案目的，配合使用相應的 coverage 種類  
可以量化檢驗外，也可以製作成報告或存成 html  
亦可以用測試的角度來寫 function（Test-Driven Development）  
除了可以提升涵蓋率外，也可以將 function 內容切的比較細
* function coverage：受到測試的 function 數／總 function 數
* lin coverage：受到測試的行數／總行數
* statement coverage（一行有多個 statement）：受到測試的行數／總行數
* decision coverage：受到測試的布林值數／總布林值數
* condition coverage：受到測試的 condition 數／總行數
* ...

## 重構

## 學習資源
* [Book：Design Patterns Elements of Reusable Object-Oriented Software](http://www.javier8a.com/itc/bd1/articulo.pdf)
* [Book：重構——改善既有代碼的設計（簡中版）](https://590m.com/file/253469-231196358)
* [Org：Gangs of Four (GoF) Design Patterns](https://www.journaldev.com/31902/gangs-of-four-gof-design-patterns)
* [Org：Design Pattern](https://www.tutorialspoint.com/design_pattern/design_pattern_overview.htm)［不僅有設計模式，還有多種程式語言撰寫教學］
* [Org：DESIGN PATTERNS in PYTHON](https://refactoringguru.cn/design-patterns/python)［可以選其他程式語言並有範例圖示］
* [Blog：Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/)
* [Blog：什麼？又是／不只是 Design Patterns!?(Python)](https://ithelp.ithome.com.tw/users/20120812/ironman/2697)［IT邦幫忙系列文章］
* [Blog：设计模式系列](https://www.cnblogs.com/wuqinglong/category/1030108.html)
* [Blog：一文讀懂七大設計原則及GoF 23種設計模式](https://codingnote.cc/zh-tw/p/83149/)
