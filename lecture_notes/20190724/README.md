# 分類(Classification) 與 分群(Clustering)

## 分類(Classification)

將資料歸類到已知或已定義的分組

### 邏輯迴歸(Logistic regression)

**線性回歸是用來預測可用連續函數敘述所推算出的數值，邏輯迴歸是用來分類一堆已知資料。**  
相關差異可參見[此篇](https://medium.com/@chih.sheng.huang821/%E6%A9%9F%E5%99%A8-%E7%B5%B1%E8%A8%88%E5%AD%B8%E7%BF%92-%E7%BE%85%E5%90%89%E6%96%AF%E5%9B%9E%E6%AD%B8-logistic-regression-aff7a830fb5d)。

Python的sklearn有提供現成的[`LogisticRegression`類別](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression)可用，[使用範例](https://www.kaggle.com/fatmakursun/logistic-regression#Logistic-Regression)。

### 簡單的分類演算法

- 單純貝氏分類(Naive Bayes)
  - sklearn的[`GaussianNB`類別](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html)，使用方法見[這篇](https://ithelp.ithome.com.tw/articles/10205582)的介紹
  - [Azure Notebooks範例](http://notebooks.azure.com/jakevdp/projects/PythonDataScienceHandbook/html/notebooks/05.05-Naive-Bayes.ipynb)

- K-近鄰演算法(K Nearest Neighbor, **KNN**)
  - sklearn的[`KNeighborsClassifier`類別](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)，使用方法見[這篇](https://ithelp.ithome.com.tw/articles/10197110)的介紹，實際演算法的手刻法可以看[這篇](https://www.kdnuggets.com/2016/01/implementing-your-own-knn-using-python.html)

### 進階的分類演算法

- 支援向量機(Support Vector Machine, SVM)

## 分群(Clustering)

將資料依據某些特性數據量值來分群組，所區分的群組數可能固定可能不固定

### 分群演算法

sklearn的`sklearn.cluster`模組提供了現成可用的演算法：  
[http://scikit-learn.org/stable/modules/clustering.html#clustering](http://scikit-learn.org/stable/modules/clustering.html#clustering)

[The 5 Clustering Algorithms Data Scientists Need to Know](http://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68)

- K-Means
  - 需要預先設定總共區分的群組數
  - sklearn的[`KMeans`類別](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)，使用方法見[這篇](https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1)的介紹。
  - 若資料的原始分布特性很極端，分群的效果會很差，甚至無法分群：[http://www.csie.ntnu.edu.tw/~u91029/Classification.html](http://www.csie.ntnu.edu.tw/~u91029/Classification.html)
- GMM(Gaussian Mixture Models 高斯混合模型)
  - sklearn的[`GaussianMixture`類別](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture)
  - Python Data Science Handbook: [In Depth: Gaussian Mixture Models](https://jakevdp.github.io/PythonDataScienceHandbook/05.12-gaussian-mixtures.html)
  - GMM演算法的[數學解釋](https://www.itread01.com/content/1542559636.html)
  - 常搭配另一個[EM演算法使得收斂速度更快](https://medium.com/@chih.sheng.huang821/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-em-%E6%BC%94%E7%AE%97%E6%B3%95-expectation-maximization-algorithm-em-%E9%AB%98%E6%96%AF%E6%B7%B7%E5%90%88%E6%A8%A1%E5%9E%8B-gaussian-mixture-model-gmm-%E5%92%8Cgmm-em%E8%A9%B3%E7%B4%B0%E6%8E%A8%E5%B0%8E-c6f634410483)。
- Mean-Shift
  - sklearn的[`MeanShift`類別](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html)以及使用[範例](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html)
  - [Mean-Shift演算法的數學原理](https://blog.csdn.net/hjimce/article/details/45718593)
- DBSCAN
  - sklearn的[`DBSCAN`類別](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)以及使用[範例](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)
- Agglomerative Hierarchical Clustering
  - sklearn的[`AgglomerativeClustering`類別](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering)
