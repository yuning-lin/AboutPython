## 所需套件
|名稱|用途|
|----|----|
|pptx|利用 python 製作 ppt|
|pandas|製作表格使用|
|itertools|用迴圈放置 dataframe 於表格|


## 程式結構
* based on python 3.6.8
  
### [範例一](https://github.com/yuning-lin/PythonTips/blob/main/ReportingTool/DeliverPresentations/main.ipynb)：一般自動化新增簡報內容
|檔名|功能|
|-----|-----|
|main.ipynb|將常用功能：封面、文字、表格、圖片的功能分 cell 紀錄|
|config.py|路徑參數紀錄於此|
|requirements.txt|使用套件及對應版本|
|ppt_module.pptx|ppt 模板檔|
|test.pptx|程式製作的 ppt 內容|

### [範例二](https://github.com/yuning-lin/PythonTips/blob/main/ReportingTool/DeliverPresentations/update_ppt_content.ipynb)：更新既有簡報框架下的內容
|檔名|功能|
|-----|-----|
|update_ppt_content.ipynb|示範如何更新既有簡報框架下的內容|
|customized_template.pptx|既有簡報框架 ppt 模板檔|
|customized_template_v2.pptx|更新後的 ppt 內容|


## 參考來源
* [官方文件：python-pptx](https://python-pptx.readthedocs.io/en/latest/user/quickstart.html#)
* [部落格：用 Python 自動化操作 PPT](https://www.readfog.com/a/1632006902852456448)
