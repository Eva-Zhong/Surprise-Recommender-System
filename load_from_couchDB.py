from surprise import BaselineOnly
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
import couchdb
import pandas as pd


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



# ratings_dict = {'userID': [9, 32, 2, 45, 'user_foo'],
#                 'itemID': [1, 1, 1, 2, 2],
#                 'rating': [3, 2, 4, 3, 1]}
ratings_dict = {'UserIds':userIds,
                    'MovieIds':movieIds,
                    'Ratings':ratings,
                    'tstamps':tstamps}

df = pd.DataFrame(ratings_dict)
print(type(df['UserIds']))
print(df)
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['UserIds','MovieIds','Ratings']], reader)
cross_validate(BaselineOnly(), data, verbose=True)





# path to dataset file
# file_path = os.path.expanduser('~/.surprise_data/ml-100k/ml-100k/u.data')

# As we're loading a custom dataset, we need to define a reader. In the
# movielens-100k dataset, each line has the following format:
# 'user item rating timestamp', separated by '\t' characters.

# reader = Reader(line_format='user item rating timestamp', sep='\t')


# data = Dataset.load_from_file(file_path, reader=reader)

# Confusing part: does df have to follow a certain order?



# # We can now use this dataset as we please, e.g. calling cross_validate
