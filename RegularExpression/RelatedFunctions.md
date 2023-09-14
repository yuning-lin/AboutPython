和 re 常結合使用的 function

* 一種 pattern 對上一組 df
```python
def pattern2df(txt, re_pattern, lst_cols):
    """
    @param txt: input text
    @param re_pattern: assigned re pattern
    @param lst_cols: organize pattern into dataframe columns
    """
    matches = re.findall(re_pattern, txt)
    df = pd.DataFrame(matches)
    df.columns = lst_cols
    return df
```

* 一種 pattern 在多個條件下都要進行相同處理
```python
def pattern2dict(file_path, key_pattern, val_pattern, lst_cols):
    """
    @param file_path: input text path
    @param key_pattern: assigned re pattern of conditions
    @param val_pattern: assigned re pattern of dataframe columns
    @param lst_cols: organize pattern into dataframe columns
    @return: Dict[key_pattern_str]=val_pattern_df
    """
    dict_data = {}
    with open(file_path, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        for _, line in enumerate(lines):
            result = re.findall(key_pattern, line)
            matches = re.findall(val_pattern, line)
            if result:
                key_str = result[0]
                dict_data[key_str] = []
            if matches:
                dict_data[key_str] += matches
    for k, v in dict_data.items():
        dict_data[k] = pd.DataFrame(v)
        dict_data[k].columns = lst_cols
    return dict_data
```
