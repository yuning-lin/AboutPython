## 常用繪圖套件
matplotlib：功能彈性較大，但佔的記憶體體積比相對較大  
bokeh：繪圖佔的記憶體體積比 matplotlib 小很多，繪製結果是以網頁呈現  
seaborn：和 pandas 資料結構溝通協調性佳，較 matplotlib 具美學呈現  
## matplotlib
### 引入套件
```python
import matplotlib.pyplot as plt
```
### line plot
```python
x1 = list(range(10))
y1 = list(range(20,0,-2))
x2 = list(range(-3,5))
y2 = list(range(8))
plt.plot(x1, y1, color='red', linewidth=5, linestyle='--', label='red')
plt.plot(x2, y2, color='green', lw=10, ls=':', label='green')
plt.xlabel('time')
plt.ylabel('value')
plt.xlim(-5,10)
plt.ylim(0,25)
plt.title('line plot')
plt.legend(loc='upper right')
plt.show()
```
### bar chart
```python
plt.bar(x1, y1, color='red', label='red')
plt.bar(x2, y2, color='green', label='green')
plt.title('bar chart')
plt.legend(loc='upper left')
```
### pie chart
```python
lst = ['large']*3
lst += ['medium']*5
lst += ['small']*2
print(lst)
size_lst = ['large', 'medium', 'small']
cnt_lst = [lst.count('large'), lst.count('medium'), lst.count('small')]
color_lst = ['red', 'blue', 'green']
explode_ary = (0,0.08,0)
plt.pie(cnt_lst, explode = explode_ary, labels = size_lst, colors = color_lst,\
        labeldistance = 1.1, autopct = "%3.1f%%", shadow = True,\
        startangle = 20, pctdistance = 0.6)
plt.axis("equal")
plt.title('pie chart')
plt.legend()
```

### 顯示中文
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

## bokeh
### 引入套件
```python
from bokeh.plotting import figure, show, output_file
```
### line plot
```python
output_file('line.html')
p = figure(width=800, height=400, title='line plot')
p.line(x1, y1, line_width=5, line_color='red', line_alpha=0.5, line_dash=[12,3], legend='red')
p.line(x2, y2, line_width=8, line_color='green', line_alpha=0.3, line_dash=[18,1], legend='green')
p.title.text_color='blue'
p.title.text_font_size='16pt'
p.xaxis.axis_label='time'
p.yaxis.axis_label='value'
p.xaxis.axis_label_text_color='brown'
p.yaxis.axis_label_text_color='brown'
```
### scatter plot
```python
p = figure(width=800, height=400, title="統計圖")
p.title.text_font_size = "18pt"
p.xaxis.axis_label = "X 軸"
p.yaxis.axis_label = "y 軸"
listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
sizes=[10,20,30,30,20,10]
colors=["red","blue","green","pink","violet","gray"]
#sizes=25  #所有點相同大小
#colors="red"  #所有點相同顏色
p.circle(listx, listy, size=sizes, color=colors, alpha=0.5)
p.square(listx, listy, size=sizes, color=colors, alpha=0.5)
show(p)
```
