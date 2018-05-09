from surprise import Dataset
from surprise import Reader
import couchdb
import pandas as pd
from top_n_recommendations import get_top_n,KNN_top_n
# user = "admin"
# password = "atth1132"
# couchserver = couchdb.Server("http://%s:%s@couch.harp3r.com" % (user, password))


def load_from_couchDB(couchserver):
    userIds = []
    movieIds = []
    ratings = []
    tstamps = []

    rating_db = couchserver['test_ratings']
    for item in rating_db.view('rating_design1/view1'):
        i = item['id']
        if "_design" in i:
            continue
        doc = rating_db[i]
        userIds.append(doc['userId'])
        movieIds.append(doc['movieId'])
        ratings.append(doc['rating'])
        tstamps.append(doc['tstamp'])

    ratings_dict = {'UserIds':userIds,
                        'MovieIds':movieIds,
                        'Ratings':ratings,
                        'tstamps':tstamps}

    df = pd.DataFrame(ratings_dict)
    print(df)
    # print(type(df['UserIds']))
    # print(df)
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['UserIds','MovieIds','Ratings']], reader)
    return data


# Define a method that takes in an algorithm and make predictions
# def train():

def main():
    ##### Make predictions by calling functions in top_n_recommendations
    # users_top_n()
    #####TODO: connect to CouchDB and make predictions
    user = "admin"
    password = "atth1132"
    couchserver = couchdb.Server("http://%s:%s@couch.harp3r.com" % (user, password))
    print("load from couchDB...")
    data = load_from_couchDB(couchserver)
    print("Finished loading data")
    print("making predictions...")
    KNN_top_n(data)

if __name__=="__main__":
    main()
