### pipeline
sklearn 模型使用 pipeline 可以讓程式簡潔  
避免在預測或做交叉驗證時忘記和訓練集站在同樣基準線（EX：標準化）  
也防止記得了卻在其他步驟上有順序不同的情形
### 引入套件 
```python
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.base import clone
```
### 資料集
```python
cancer_df = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(cancer_df.data, cancer_df.target, random_state=123)
```
### 單用 pipeline 並指定參數
```python
clf = make_pipeline(StandardScaler(), SVC(C=100))
print(clf.steps)
print(clf.named_steps)
model = clone(clf).fit(x_train, y_train)
model.score(x_test, y_test)
```
### Pipeline 搭配 Grid Search
```python
clf = make_pipeline(StandardScaler(), SVC()) # 不能事先設定參數
print(clf.steps)
params = {'svc__C':[0.001,0.01,0.1,1,10,100], 'svc__gamma':[0.001,0.01,0.1,1,10,100]}
gridsearch_cv = GridSearchCV(clone(clf), param_grid=params, cv=5)
gridsearch_cv.fit(x_train, y_train)
print(gridsearch_cv.best_estimator_) # 印出最佳參數組合
print(gridsearch_cv.best_estimator_['svc'].score(x_test, y_test))
print(gridsearch_cv.best_estimator_['svc'].predict(x_test))
print(gridsearch_cv.best_estimator_['svc'].decision_function(x_test))
```
