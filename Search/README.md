## 簡介
搜尋方式依型態不同有異  

* list of dictionary and find item by key
```python
#### method 1
list_dicts = [
     { "name": "Tom", "age": 10 },
     { "name": "Mark", "age": 5 },
     { "name": "Pam", "age": 7 },
     { "name": "Dick", "age": 12 }
 ]
next(item for item in list_dicts if item["name"] == "Pam")

# find by name --> {'age': 7, 'name': 'Pam'}

#### method 2
[item for item in list_dicts if item["name"] == "Pam"]

# find by name --> [{'age': 7, 'name': 'Pam'}]
```
