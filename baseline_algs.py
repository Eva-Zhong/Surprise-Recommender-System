from surprise import Dataset
from surprise.model_selection import cross_validate
from surprise import BaselineOnly
from surprise.model_selection import train_test_split
from surprise import accuracy

def predict(data, userId, itemId):
    bsl_options = {'method': 'als',
                   'n_epochs': 5,
                   'reg_u': 12,
                   'reg_i': 5
                   }
    trainset, testset = train_test_split(data, test_size=.25)
    algo = BaselineOnly(bsl_options=bsl_options)
    algo.fit(trainset)
    pred = algo.predict(userId, itemId, r_ui=actualRating, verbose=True)

# Make a prediction using movieLens dataset
def predict_ml(userId, itemId, actualRating):
    # Load the movielens-100k dataset (download it if needed).
    data = Dataset.load_builtin('ml-100k')
    trainset, testset = train_test_split(data, test_size=.25)
    # bsl_options = {'method': 'sgd',
    #                'learning_rate': .00005,
    #                }

    ###### Some similarity algs may use baseline
    # bsl_options = {'method': 'als',
    #                'n_epochs': 20,
    #                }
    # sim_options = {'name': 'pearson_baseline'}
    # algo = KNNBasic(bsl_options=bsl_options, sim_options=sim_options)
    # Customize baseline options
    bsl_options = {'method': 'als',
                       'n_epochs': 5,
                       'reg_u': 12,
                       'reg_i': 5
                       }
    algo = BaselineOnly(bsl_options=bsl_options)
    algo.fit(trainset)
    # predictions = algo.test(testset)
    # accuracy.rmse(predictions)

    # Make a specific prediction
    uid = str(userId)  # raw user id (as in the ratings file). They are **strings**!
    iid = str(itemId)  # raw item id (as in the ratings file). They are **strings**!
    pred = algo.predict(uid, iid, r_ui=actualRating, verbose=True)

def main():
    predict_ml(196,302,4)

if __name__ == '__main__':
    main()
