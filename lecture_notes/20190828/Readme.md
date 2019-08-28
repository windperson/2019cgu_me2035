# 今日上課提到的東西

## 二分類演算法擴充

先前學的Logistic Regression, Decision Tree, SVM都是一種 **二分法** 的分類演算法，如何做到可以分出多類別的判斷？

- one vs all/rest (ova, ovr)
  - 假如預計要分出n類，採用判斷出 _**屬於某一類**_ or _**不屬於該分類**_ 的二分法，依序訓練出 n 個SVM來做預測。
  - [https://www.youtube.com/watch?v=vMIHdOKdnOc](https://www.youtube.com/watch?v=vMIHdOKdnOc)
  - 較易受到極端資料值而影響判斷結果。
- one vs one (ovo, all-pairs)
  - 根據預計要分出n類，[產生出 n(n-1)/2 個SVM，並餵給隨機 C(n, 2) 的組合資料來訓練](https://www.quora.com/Whats-an-intuitive-explanation-of-one-versus-one-classification-for-support-vector-machines)。
  - [https://www.youtube.com/watch?v=6kzvrq-MIO0](https://www.youtube.com/watch?v=6kzvrq-MIO0)
  - 準確性較one vs all高

## Boosting

藉由提供標註這次辨識錯誤的訓練資料，不斷重複訓練本質上辨識成效差的模型，以便讓該模型的辨識能力提高：  

- [整合學習--bagging、boosting、stacking](https://www.itread01.com/content/1547223330.html)
- [Adaptive Boosting(AdaBoosting)](https://www.youtube.com/watch?v=hL8DjIHAzZY)

## 自動訓練機器模型

[Automated machine learning (AutoML)](https://en.wikipedia.org/wiki/Automated_machine_learning)讓不太曉得怎樣調參數的AI訓練家也能train出堪用的模型！

- [Azure AutoML](https://docs.microsoft.com/en-us/azure/machine-learning/service/concept-automated-ml)
- [Cloud AutoML](https://cloud.google.com/automl/docs/)

## 課後學習資源

學習資訊業知識/技能的幾個撇步：

- [模式法則](https://www.facebook.com/startupgrouphk/photos/a.889982791077653/1491460334263226)
- [抽象滲透法則](http://local.joelonsoftware.com/wiki/The_Joel_on_Software_Translation_Project:%E6%8A%BD%E8%B1%A1%E6%BB%B2%E6%BC%8F%E6%B3%95%E5%89%87)
- [側向思維](https://wiki.mbalib.com/zh-tw/%E5%88%9B%E9%80%A0%E6%80%A7%E6%80%9D%E7%BB%B4)

### 台灣機器學習相關社群

- [Taiwan R User Group / MLDM Monday](https://www.meetup.com/Taiwan-R/)
- [Deep Learning for Sciences, Engineering, and Arts](https://www.meetup.com/Deep-Learning-for-Sciences-Engineering-and-Arts/)
- [台灣「人工智慧」社團](https://www.facebook.com/groups/Taiwan.AI.Group)
- [AI Taiwan](https://www.facebook.com/groups/AI4Taiwan)

### 機器學習相關書籍/線上課程

- [從資料科學橫入人工智慧領域](https://www.tenlong.com.tw/products/9789865003159)
- [練好機器學習的基本功｜用 Python 進行基礎數學理論的實作](https://www.tenlong.com.tw/products/9789864768981)
- [深度學習入門教室](https://www.tenlong.com.tw/products/9789862357156)
- [林軒田-機器學習基石](https://www.youtube.com/watch?v=nQvpFSMPhr0&list=PLXVfgk9fNX2I7tB6oIINGBmW50rrmFTqf)
- [林軒田-機器學習技法](https://www.youtube.com/watch?v=A-GxGCCAIrg&list=PLXVfgk9fNX2IQOYPmqjqWsNUFl2kpk1U2)
- [【尹相志深度學習實戰1】秒懂AI深度學習-基本概念篇](https://www.tibame.com/course/493)
- [Introduction to Machine Learning](https://developers.google.com/machine-learning/crash-course/ml-intro)
- [Principles of Machine Learning: Python Edition](https://www.edx.org/course/principles-of-machine-learning-python-edition-3)
