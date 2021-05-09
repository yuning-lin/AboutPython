## 主題：爬取 0050 成分股
### 引入套件
```python
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
```
### Requests.get
get：直接擷取網站 html 
text：以文字的形式印出  
```python
etf_url = 'https://www.moneydj.com/ETF/X/Basic/Basic0007A.xdjhtm?etfid={}.TW'
r = requests.get(etf_url.format('0050'))
r.encoding = 'utf-8'
print(r.text)
```
### BeautifulSoup
bs：將 html 內容包裝成較好讀取的形式  
select：. 代表 class、# 代表 id、＞ 代表階層上下   
```python
soup = bs(r.content, "html.parser") #soup = bs(r.text, "lxml")
col_name_lst = [col.text for col in soup.select('#Repeater1 > tr th')]
stock_name_lst = [col.text for col in soup.select('.datalist > tr > .col05')] 
shareholding_amount_lst = [col.text for col in soup.select('.datalist > tr > .col06')]
shareholding_ratio_lst = [col.text for col in soup.select('.datalist > tr > .col07')]
shareholding_change_ratio_lst = [col.text for col in soup.select('.datalist > tr > .col08')]
```
最後將分別讀取的欄位包裝成 dataframe  
```python
col_lsts = list(zip(stock_name_lst, shareholding_amount_lst, shareholding_ratio_lst, shareholding_change_ratio_lst))
etfcomponent_df = pd.DataFrame(col_lsts, columns = col_name_lst) 
```
