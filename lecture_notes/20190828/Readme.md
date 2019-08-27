# 今日上課提到的東西

## 二分法擴充、Boosting

先前學的Logistic Regression, Decision Tree, SVM都是一種 **二分法** 的分類演算法，如何做到可以分出多類別的判斷？

- one vs all/rest (ova, ovr)
  - 假如預計要分出n類，採用判斷出 _**屬於某一類**_ or _**不屬於該分類**_ 的二分法，依序訓練出 n 個SVM來做預測。
  - [https://www.youtube.com/watch?v=vMIHdOKdnOc](https://www.youtube.com/watch?v=vMIHdOKdnOc)
  - 較易受到極端資料值而影響判斷結果。
- one vs one (ovo, all-pairs)
  - 根據預計要分出n類，[產生出 n(n-1)/2 個SVM，並餵給隨機 C(n, 2) 的組合資料來訓練](https://www.quora.com/Whats-an-intuitive-explanation-of-one-versus-one-classification-for-support-vector-machines)。
  - [https://www.youtube.com/watch?v=6kzvrq-MIO0](https://www.youtube.com/watch?v=6kzvrq-MIO0)
  - 準確性較one vs all高

## 課後學習資源

### 台灣機器學習相關社群

- [Taiwan R User Group / MLDM Monday](https://www.meetup.com/Taiwan-R/)
- [Deep Learning for Sciences, Engineering, and Arts](https://www.meetup.com/Deep-Learning-for-Sciences-Engineering-and-Arts/)
- [台灣「人工智慧」社團](https://www.facebook.com/groups/Taiwan.AI.Group)
- [AI Taiwan](https://www.facebook.com/groups/AI4Taiwan)

### 機器學習相關書籍/線上課程

- [從資料科學橫入人工智慧領域](https://www.tenlong.com.tw/products/9789865003159)
- [練好機器學習的基本功｜用 Python 進行基礎數學理論的實作](https://www.tenlong.com.tw/products/9789864768981)
- [【尹相志深度學習實戰1】秒懂AI深度學習-基本概念篇](https://www.tibame.com/course/493)
- [Introduction to Machine Learning](https://developers.google.com/machine-learning/crash-course/ml-intro)
- [Principles of Machine Learning: Python Edition](https://www.edx.org/course/principles-of-machine-learning-python-edition-3)
