## 摘要
彙整一些簡單程式碼就可以出探索性分析的套件  

## [pip install sweetviz](https://pypi.org/project/sweetviz/)
* 可以分析單一 df
* 可以比較兩個 df
* 可以比較同一 df 的不同子集 
```
import sweetviz as sv

df = pd.read_csv("your_data_path.csv")
report = sv.analyze(df)
report.show_html() # 會自動生成 .html
```

## [pip install ydata_profiling](https://pypi.org/project/ydata-profiling/)
* 可以分析單一 df
* 可以輸出 html, json
* 類似 df.describe()
* 可以比較兩個 df
* 有基礎時序模型
```
import ydata_profiling

df = pd.read_csv("your_data_path.csv")
report = df.profile_report()
report.to_file("report.html")
```

## [pip install dataprep](https://docs.dataprep.ai/user_guide/eda/introduction.html)
* 可以連 DB
* 有提供 API
* 可以分析單一 df
* 可以比較兩個 df
```
from dataprep.eda import plot

df = pd.read_csv("your_data_path.csv")
plot(df)
```

## [pip install autoviz](https://pypi.org/project/autoviz/)
* 有提供 API
* 可以分析單一 df
```
from autoviz import AutoViz_Class
AV = AutoViz_Class()

df = pd.read_csv("your_data_path.csv")

dft = AV.AutoViz(
    filename,
    sep=",",
    depVar=target_variable,
    dfte=None,
    header=0,
    verbose=2,
    lowess=False,
    chart_format="bokeh",
    max_rows_analyzed=150000,
    max_cols_analyzed=30,
    save_plot_dir=custom_plot_dir
)
```
