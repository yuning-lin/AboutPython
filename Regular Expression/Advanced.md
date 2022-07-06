## 使用套件：`re`

## 進階用法
* 擷取文章中的句子
    * 斷句包含標點符號，並根據中英文選取不同標點符號
    * 使用 re.compile、findall
    ```python
    ## 英文
    txt = 'i am smart. you are fool! Are you sure?'
    pattern = re.compile('[\w\d\s]+[;,!\?\.]')
    sentence_lst = pattern.findall(txt)
    
    ## 中文
    txt = '我很聰明，你是蠢蛋！你確定嗎？（我不確定）。'
    pattern = re.compile('[\w\d\s\（\）]+[；，！？。]')
    sentence_lst = pattern.findall(txt)
    ```
    * 斷句不包含標點符號
    * 使用 re.split
    ```python
    txt = '我很聰明，你是蠢蛋！你確定嗎？（我不確定）。'
    re.split(r'(;|,|!|\?|\.|；|，|！|？|。)\s*', txt) # 保留標點符號
    re.split(r'[;|,|!|\?|\.|；|，|！|？|。]\s*', txt) # 去除標點符號
    ```
