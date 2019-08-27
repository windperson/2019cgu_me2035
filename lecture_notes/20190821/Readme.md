# 今日上課提到的東西

[github Gist使用教學](https://sofree.cc/github-gist/)

Python 一行文的if else敘述類似C/C++/C#/Java/JavaScript等C-like language的三元運算子：

```Cpp
//C-like:
x !=1 ? true : false
// (判斷式) ? {判斷為true時的回傳} : {判斷為false時的回傳}
```

```python
#python:
0 if item == "*" else item
# {判斷為true時的回傳} if (判斷式) else {判斷為false時的回傳}
```

[Decision Tree的範例](https://stackabuse.com/decision-trees-in-python-with-scikit-learn/)

## 判斷機器學習模型的效果指標

- [precision, recall, accuracy的意義](https://www.ycc.idv.tw/confusion-matrix.html)
- [Explaining precision and recall](https://medium.com/@klintcho/explaining-precision-and-recall-c770eb9c69e9)
- [sckit-learn的內建函式](https://scikit-learn.org/stable/modules/model_evaluation.html#common-cases-predefined-values)

## Support Vector Machine

在類神經網路還有運算資源障礙時代的最佳機器學習方案，不過需要了解如何擴展到高維空間、選擇好的Kernel Function之類的數學知識才算懂得操作。

[SVM(Support Vector Machine)的概念介紹](https://www.youtube.com/watch?v=Y6RRHw9uN9o)

[scikit-learn內建的SVM Kernel function](https://www.bogotobogo.com/python/scikit-learn/scikit_machine_learning_Support_Vector_Machines_SVM.php)

[Jupyter Notebook範例](https://github.com/donnemartin/data-science-ipython-notebooks/blob/master/scikit-learn/scikit-learn-svm.ipynb)

台灣開發[libsvm](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)

## AI現況

### 主流使用類神經網路的技術

因為可以用`Transfer learning`來讓原本有已經訓練了不少資料的pre-trained AI model再提供一些較特化用途的訓練資料，就能拿來做辨識特化用途的AI：  
[Transfer learning from pre-trained models](https://towardsdatascience.com/transfer-learning-from-pre-trained-models-f2393f124751)

### 使用CUDA做機器學習運算的GPU加速

- cuDNN: [https://developer.nvidia.com/cudnn](https://developer.nvidia.com/cudnn)
- TensorRT: [https://developer.nvidia.com/tensorrt](https://developer.nvidia.com/tensorrt)

相關新聞：  
[Nvidia 刷新對話式 AI 訓練成果，一小時內完成最大語言模型](https://technews.tw/2019/08/14/nvidia-bert-ai-nlp-processing-makes-good-process/)
