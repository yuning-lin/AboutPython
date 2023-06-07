## 類別屬性（class attributes） VS 實例屬性（instance attributes）
* 打 API 的形式，無論是否用 `@dataclass`，類別屬性會記住前一次運行完的值
  ```python
  from dataclasses import dataclass, field

  @dataclass
  class APISimulator:
      value = None  # 模擬的類別屬性

      @staticmethod
      def get_value():
          # 模擬 API 回傳類別屬性的值
          return APISimulator.value

      @staticmethod
      def set_value(new_value):
          # 模擬 API 設定類別屬性的值
          APISimulator.value = new_value

  # 模擬 API 的行為
  print(APISimulator.get_value())  # 輸出: None
  APISimulator.set_value(10)
  print(APISimulator.get_value())  # 輸出: 10

  # 修改類別屬性的值
  APISimulator.set_value(20)
  print(APISimulator.get_value())  # 輸出: 20

  # 在另一個程式區塊中，再次存取類別屬性
  print(APISimulator.get_value())  # 輸出: 20（仍保留之前的值）
  ```
* mutable VS immutable，用 dataclass 打包的
    * 類別屬性（class attributes）
      ```python
      class MyClass:
          value = 0
          lst = []

      obj = MyClass()
      print(obj.value)  # 輸出: 0
      print(obj.lst)  # 輸出: []
      obj.value = 10
      obj.lst.append(0)
      print(obj.value)  # 輸出: 10
      print(obj.lst)  # 輸出: [0]

      # 執行另一個程式
      obj = MyClass()
      print(obj.value)  # 輸出: 0 ---> 注意（immutable objects）
      print(obj.lst)  # 輸出: [0] ---> 注意（mutable objects）
      ```
    * 實例屬性（instance attributes）
      ```python
      class MyClass:

          def __init__(self, value=0, lst=[]):
              self.value = value
              self.lst = lst

      obj = MyClass()
      print(obj.value)  # 輸出: 0
      print(obj.lst)  # 輸出: []
      obj.value = 10
      obj.lst.append(0)
      print(obj.value)  # 輸出: 10
      print(obj.lst)  # 輸出: [0]

      # 執行另一個程式
      obj = MyClass()
      print(obj.value)  # 輸出: 0 ---> 注意（immutable objects）
      print(obj.lst)  # 輸出: [0] ---> 注意（mutable objects）


      obj = MyClass(20, [])
      print(obj.value)  # 輸出: 20 ---> 注意（immutable objects）
      print(obj.lst)  # 輸出: []   ---> 注意（mutable objects）
      ```
    * @dataclass（此裝飾器所產生的類別是 mutable）
      ```python
      @dataclass
      class MyClass:
          value: int
          lst: list = field(default_factory=list)

      obj = MyClass(0)  # immutable objects 一定要賦值
      print(obj.value)  # 輸出: 0
      print(obj.lst)  # 輸出: []
      obj.value = 10
      obj.lst.append(0)
      print(obj.value)  # 輸出: 10
      print(obj.lst)  # 輸出: [0]

      # 執行另一個程式
      obj = MyClass(20)  # immutable objects 一定要賦值
      print(obj.value)  # 輸出: 20 ---> 注意（immutable objects）
      print(obj.lst)  # 輸出: []   ---> 注意（mutable objects）
      ```
