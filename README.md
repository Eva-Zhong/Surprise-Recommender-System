## ml-external-rec
### The ml-external-rec folder contains files that make predictions by using a pre-generated model.

build.py will connect to couchDB, load the data, uses this dataset to train a model, and serializes this model.
The last two functionality is under development.

Currently, top_n_recommendations load the movielens dataset, develop a model using KNN algorithm, and serializes
this model.

server.py is a flask server that hosts external rec.
Users will provide the userId. The server then loads the pre-generated model, make predictions, and display the results.

SVD_Model is the pre-generated SVD model. It is trained on the ml-100k dataset.


## SURPRISE Functionality Demo:
### load_custom_dataset
This is a demo of how to load a custom dataset and then runs cross validation.

### load_from_couchDB
Connects to the couchDB dataset, loads data from the test_rating database, and uses SVD algorithm to make predictions.
This file can take a few minutes to run.

### baseline_algs
This is a demo of making predictions using the baseline algorithms and movielens 100k dataset.

### similarity algs
This is a demo of making predictions using the similarity-based algorithms and movielens 100k dataset.

### predict_ratings
This is a demo of making predictions using the K nearest neighbors algorithms and movielens 100k dataset.
