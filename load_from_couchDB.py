from surprise import BaselineOnly
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
import couchdb
import pandas as pd
# from surprise import SVD


user = "admin"
password = "atth1132"
couchserver = couchdb.Server("http://%s:%s@couch.harp3r.com" % (user, password))

userIds = []
movieIds = []
ratings = []
tstamps = []

rating_db = couchserver['test_ratings']

for item in rating_db.view('_all_docs'):
    i = item['id']
    if "_design" in i:
        continue
    # print(i)
    doc = rating_db[i]
    userIds.append(doc['userId'])
    movieIds.append(doc['movieId'])
    ratings.append(doc['rating'])
    tstamps.append(doc['tstamp'])

ratings_dict = {'UserIds':userIds,
                    'MovieIds':movieIds,
                    'Ratings':ratings,
                    'tstamps':tstamps}

# The processing step can take a few minutes
df = pd.DataFrame(ratings_dict)
# print(df)

# Converting panda dataframe to a Dataset object
reader = Reader(rating_scale=(1, 5))

# columns names follow this specific order!
data = Dataset.load_from_df(df[['UserIds','MovieIds','Ratings']], reader)


# Using the baseline algorithm
# cross_validate(BaselineOnly(), data, verbose=True)
algo = SVD()
algo.fit(trainset)
# predictions = algo.test(testset)
# accuracy.rmse(predictions)

# Make prediction for a specific user
pred = algo.predict(1, 110, r_ui=5, verbose=True)

# Run 5-fold cross-validation and print results.
# cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
