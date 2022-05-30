```python
import numpy as np
import pandas as pd
import math
```

## 空值們
### nan
```python
pd.isna(np.nan)
np.isnan(np.nan)
math.isnan(np.nan)

## 同直行全為空值則刪除該行
df.dropna(axis=1, how='all')
## 列出欄位名稱為 col 中元素為 nan 的資料
df[df['col'].isna()]
```

### None
```python
is None
is not None
isinstance(None, type(None))
```

### NAT
```python
np.isnat(np.datetime64("NaT"))
np.isnat(np.datetime64('nat'))
np.isnat(np.datetime64('nAt'))

## nat 藉由轉換成 object，可用 isna() 辨別
df = df.astype(object).mask(df.isna(), np.nan) 
```

## 資料格式
```python
## 確認是否為日期格式
isinstance(x, datetime)
```
