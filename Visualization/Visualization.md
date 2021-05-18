## 常用繪圖套件
[matplotlib](https://github.com/yuning-lin/AboutPython/blob/main/Visualization_Matplotlib.ipynb)：功能彈性較大，但佔的記憶體體積比相對較大  
[bokeh](https://github.com/yuning-lin/AboutPython/blob/main/Visualization_Bokeh.ipynb)：繪圖佔的記憶體體積比 matplotlib 小很多，繪製結果是以網頁呈現  
seaborn：和 pandas 資料結構溝通協調性佳，較 matplotlib 具美學呈現  
## 引入套件
```python
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file # 存成 html
from bokeh.io import output_notebook # 直接 show 在 jupyter notebook console
```

## matplotlib 顯示中文
#### 法一：
1. 找到儲存 matplotlibrc 設定檔的位置
2. 開啟 matplotlibrc 設定檔，找到開頭為 #font.serif、#font.sans-serif 的兩行
3. 皆去掉行頭的 #，並加入 SimHei,
4. 再找到 #axes.unicode_minus 這行，移除 #，並設定為 False

#### 法二：
直接透過 rcParams 修改成如法一的設定：
```python
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
```

#### 法三：
若是本身即沒有中文字體，前往下列網址下載字體 SimHei  
https://link.zhihu.com/?target=https%3A//www.fontpalace.com/not-found/  
將下載的字體放入下列路徑：  
.\Lib\site-packages\matplotlib\mpl-data\fonts\ttf  
並重複法一的動作  
