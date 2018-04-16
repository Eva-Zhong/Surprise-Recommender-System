## Usage:
1. Enter the ml-external-rec directory. 
2. Run build.py
3. Run flask by typing: python -m flask run. Open the URL (e.g.http://127.0.0.1:5000/) from the web browser
4. Type in a userID and view recommendations.

## ml-external-rec
### The ml-external-rec folder contains files that make predictions by using a pre-generated model.

build.py will connect to couchDB, load the data, uses this dataset to train a model, and serializes this model.
The last two functionality is under development.

Currently, top_n_recommendations.py loads a dataset that contains 100k userID, movieId and ratings (ml-100k), trains a model using SVD algorithm, and saves this model for later use.

server.py is a flask server that hosts the external rec demo.
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
