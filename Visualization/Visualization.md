## 常用繪圖套件
[matplotlib](https://github.com/yuning-lin/PythonTips/blob/main/Visualization/Visualization_Matplotlib.ipynb)：功能彈性較大，但佔的記憶體體積比相對較大  
[bokeh](https://github.com/yuning-lin/PythonTips/blob/main/Visualization/Visualization_Bokeh.ipynb)：繪圖佔的記憶體體積比 matplotlib 小很多，繪製結果是以網頁呈現  
[seaborn](https://github.com/yuning-lin/PythonTips/blob/main/Visualization/Visualization_Seaborn.ipynb)：和 pandas 資料結構溝通協調性佳，較 matplotlib 具美學呈現  
## 引入套件
```python
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file # 存成 html
from bokeh.io import output_notebook # 直接 show 在 jupyter notebook console
```

## matplotlib 顯示中文
#### 法一：
1. 找到儲存 matplotlibrc 設定檔的位置，用 Notepad++ 開啟 matplotlibrc 設定檔
2. 找到開頭為 #font.family、#font.sans-serif 的兩行，皆去掉行頭的 #
3. 並在 font.sans-serif：加入 SimHei,
4. 再找到 #axes.unicode_minus 這行，移除 #，並設定為 False

#### 法二：
直接透過 rcParams 修改成如法一的設定：
```python
import matplotlib.pyplot as plt
plt.rcParams['font.family']='sans-serif'
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False
```

#### 法三：
若是本身即沒有中文字體，前往下列網址下載字體 SimHei
https://www.fontpalace.com/
將下載的字體放入下列路徑：
.\Lib\site-packages\matplotlib\mpl-data\fonts\ttf
並重複法一的動作 

#### 法四：
若上述的方法還是失敗可以先試試刪除緩存  
1. `print(matplotlib.get_cachedir())` 找到緩存位置
2. 使用命令提示字元：`rm -rf ~/.cache/matplotlib/` 刪除緩存（印出的路徑跟網上相差甚遠，所以沒試）
3. 並重啟 python 再 run 畫圖程式

#### 法五：
還是遇到錯誤訊息：
```
serWarning: findfont: Font family ['sans-serif'] not found. Falling back to DejaVu Sans
 (prop.get_family(), self.defaultFamily[fontext]))
```
修改 .\lib\site-packages\matplotlib\font_manager.py
1. 將 font_manager.py 用 Notepad++ 開啟
2. `self.defaultFamily = {'ttf': 'DejaVu Sans','afm': 'Helvetica'}` --> `self.defaultFamily = {'ttf': 'SimHei','afm': 'Helvetica'}`
3. `if fname.lower().find('DejaVuSans.ttf')>=0: self.defaultFont['ttf'] = fname` --> `if fname.lower().find('SimHei.ttf')>=0: self.defaultFont['ttf'] = fname`
4. 並重啟 python 再 run 畫圖程式

但悲慘的是，目前試過上面的方法皆失敗...
