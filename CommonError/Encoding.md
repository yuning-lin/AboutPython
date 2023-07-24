* `UnicodeDecodeError: 'cp950' codec can't decode byte 0xe5 in position 83: illegal multibyte sequence`
* 通常根據讀取方式加 encoding 的設定即可
  
  ```python
  # EX：

  f = open(file_name, "r", encoding="utf-8").read()
  ```
