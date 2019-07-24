# 分類(Classification) 與 分群(Clustering)

## 分類

將已知資料歸類到已知或已定義的分組

### 邏輯迴歸(Logistic regression)

**線性回歸是用來預測可用連續函數敘述所推算出的數值，邏輯迴歸是用來分類一堆已知資料。**  
相關差異可參見[此篇](https://medium.com/@chih.sheng.huang821/%E6%A9%9F%E5%99%A8-%E7%B5%B1%E8%A8%88%E5%AD%B8%E7%BF%92-%E7%BE%85%E5%90%89%E6%96%AF%E5%9B%9E%E6%AD%B8-logistic-regression-aff7a830fb5d)。

Python的sklearn有提供現成的[`LogisticRegression`類別](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression)可用，[使用範例](https://www.kaggle.com/fatmakursun/logistic-regression#Logistic-Regression)。

### 簡單的分類演算法

- 單純貝氏分類(Naive Bayes)

- K-近鄰演算法(K Nearest Neighbor ,KNN)
  - sklearn的[`KNeighborsClassifier`類別](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)，可見[這篇](https://ithelp.ithome.com.tw/articles/10197110)的介紹

### 進階的分類演算法

- 支援向量機(Support Vector Machine, SVM)
