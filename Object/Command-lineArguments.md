## 簡介
希望可以呼叫 python 程式，又可以有彈性地引入不同參數時  
就可以使用 command-line arguments 來達到效果  
常用的兩個套件有：`sys`、`argparse`

## 套件：`sys`
* cmd or bash
```linux
python3 test.py 20220820 ascending
```
* test.py
```python
import sys

print(f'arguments number:{len(sys.argv)}')
print(f'1st arguments:{sys.argv[0]} and type is {type(sys.argv[0])}')
print(f'2nd arguments:{sys.argv[1]} and type is {type(sys.argv[1])}')
print(f'3rd arguments:{sys.argv[2]} and type is {type(sys.argv[2])}')
```

## 套件：`argparse`
* cmd or bash
```linux
python3 test.py 20220820 ascending
```
* test.py
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("date", type=int,
                    help="current yyyymmdd")
parser.add_argument("order", type=str,
                    choices=['ascending', 'descending'],
                    help="display order")
args = parser.parse_args()

print(f'1st arguments:{args[0]} and type is {type(args[0])}')
print(f'2nd arguments:{args[1]} and type is {type(args[1])}')
```

## 參考資源
* [Blog：Python argparse 教學：比 sys.argv 更好用，讓命令列引數整潔又有序](https://haosquare.com/python-argparse/)
