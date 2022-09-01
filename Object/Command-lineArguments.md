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
                    nargs='?', default='ascending',
                    choices=['ascending', 'descending'],
                    help="display order")
parser.add_argument("foo", nargs='?', const='c', default='d')
args = parser.parse_args()

print(f'1st arguments:{args[0]} and type is {type(args[0])}')
print(f'2nd arguments:{args[1]} and type is {type(args[1])}')
```
* test2.py
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("foo", nargs='?', const='c', default='d')
args = parser.parse_args()
```
### 補充
* nargs & default：設定 nargs 為 ? 或者 * 時，表程式可接受引數為 0 個，當不輸入引數時則會運行 default 設定值。如範例中的 order
  * nargs=5：引數必須剛好是 5 個
  * nargs='?'：引數必須為 0 或 1 個
  * nargs='+'：引數至少為 1 個（可以為 1 個含以上）
  * nargs='\*'：引數可以是任意數量（可以為 0 個含以上）
* const & default：
  * 若在終端機輸入 `python test2.py --foo`：傳入的參數值為 c
  * 若在終端機輸入 `python test2.py`：傳入的參數值為 d
* choices：包含參數允許值的列表
* help：在終端機輸入 `python test.py --help`、`python test.py -h` 時會顯示的參數提示字



## 參考資源
* [Docs：python-pptx Documentation](https://buildmedia.readthedocs.org/media/pdf/python-pptx/latest/python-pptx.pdf)
* [Blog：Python argparse 教學：比 sys.argv 更好用，讓命令列引數整潔又有序](https://haosquare.com/python-argparse/)
