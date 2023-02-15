## Create Empty
* dataframe
```python
import pandas as pd
df = pd.DataFrame()
```
  
* dictionary
```python
from collections import defaultdict
d = dict()
d = {}
d = defaultdict() # 可以直接新增 d['key'] = value
d = defaultdict(list) # 格式為：{'key':[]}
```
  
* list
```python
l = list()
l = []
```
## Check Empty
* dataframe
```python
df.empty
```
  
* dictionary
```python
if not d:
  print(True)


if len(d)==0:
  print(True)
```
  
* list
```python
if not l:
  print(True)


if len(l)==0:
  print(True)
```
