# DAT640-FinalProject
DAT640 - Final Project - Group 12
Files to run:

Config.py -> define path variables etc. to datasets

Category Prediction:
- Baseline.ipynb

Type Prediction:
- indexer_memory_intensive.ipynb (memory intensiv)
- Evaluation.ipynb
- indexer.ipynb (first try on indexing, not quite working, some weird behavior)

## Dataset
- Category Prediction Dataset
    - [Dataset](https://github.com/smart-task/smart-dataset)
- Answer Type Prediction Dataset (Dbpedia)
    - [instance_types_en.ttl](http://downloads.dbpedia.org/2016-10/core/instance_types_en.ttl.bz2)
    - [short_abstracts_en.ttl](http://downloads.dbpedia.org/2016-10/core/short_abstracts_en.ttl.bz2)
    - [long_abstracts_en.ttl](http://downloads.dbpedia.org/2016-10/core/long_abstracts_en.ttl.bz2)

## Creating Baseline Models

Baseline model: SVC
- [A guide to Text Classification(NLP) using SVM and Naive Bayes with Python](https://medium.com/@bedigunjit/simple-guide-to-text-classification-nlp-using-svm-and-naive-bayes-with-python-421db3a72d34)

### Two steps
- category prediction
- type prediction


## Resources
- Assigments - DAT640
- [IR-SMART](https://github.com/BerntA/IR-SMART)
- https://github.com/duyet/demo-text-classification/blob/master/classification-with-tfidf-svm.ipynb
- [Bert Classification](https://soumilshah1995.blogspot.com/2021/04/using-bert-with-scikit-learn-to-do-text.html)
- [Smarttask-iswc2020](https://github.com/rcelebi/iswc2020-smarttask/blob/master/notebooks/TFIDF_type_pred_dbpedia_frequent_type.ipynb)
