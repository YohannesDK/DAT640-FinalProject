import os

# data
DATASETS_PATH = os.path.join("/mntnvme", 'datasets')
DBPEDIA_PATH = os.path.join(DATASETS_PATH, 'DBpedia')
QUERY_TRAIN_PATH = os.path.join(DBPEDIA_PATH, "smarttask_dbpedia_train.json")
QUERY_TEST_PATH = os.path.join(DBPEDIA_PATH, "smarttask_dbpedia_test_questions.json")
DBPEDIA_TYPES_PATH = os.path.join(DBPEDIA_PATH, "dbpedia_types.tsv")


SHORT_ABSTRACT_PATH = os.path.join(DBPEDIA_PATH, "short_abstracts_en.ttl")
INSTANCE_TYPES_EN_PATH = os.path.join(DBPEDIA_PATH, "instance_types_en.ttl")



# entity retrieval
INDEX_NAME = "smart_index"
INDEX_SETTINGS = {
    "mappings": {
        "properties": {
            "abstract": {
                "type": "text",
                "analyzer": "english",
                "term_vector": "yes"
            },
            "instance_type": {
                "type": "text",
            }
        }
    }
}