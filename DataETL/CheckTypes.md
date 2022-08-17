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

## 刪除欄位 col 中元素為 nan 的整列資料
df.dropna(subset=['col'])
## 同直行全為空值則刪除該行
df.dropna(axis=1, how='all')
## 列出欄位名稱為 col 中元素為 nan 的資料
df[df['col'].isna()]
df[df['col'].isnull()]
df[pd.isna(df['col'])]
## 列出欄位名稱為 col 中元素不為 nan 的資料
df[df['col'].notna()]
df[~df['col'].isna()]
df[df['col'].notnull()]
df[pd.notna(df['col'])]
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

```python
## 將 dataframe 所有為 float 的欄位轉換成 int
print(df.dtypes)
float_df = df.select_dtypes(include=['float64'])
float_col = list(float_df.columns)
df[float_col] = df[float_col].applymap(np.int64)
```
