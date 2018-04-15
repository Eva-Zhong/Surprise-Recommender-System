from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate
from surprise.model_selection import train_test_split
from surprise import accuracy
from surprise import KNNBasic

# Load the movielens-100k dataset (download it if needed).
data = Dataset.load_builtin('ml-100k')
# Customize sim_options
sim_options = {'name': 'pearson_baseline',
               'shrinkage': 0  # no shrinkage
               }
trainset, testset = train_test_split(data, test_size=.25)

###### Some other similarity algs
# sim_options = {'name': 'cosine',
#                'user_based': False  # compute  similarities between items
#                }

# bsl_options = {'method': 'als',
#                'n_epochs': 20,
#                }
# sim_options = {'name': 'pearson_baseline'}
# algo = KNNBasic(bsl_options=bsl_options, sim_options=sim_options)

algo = KNNBasic(sim_options=sim_options)
algo.fit(trainset)
# Make predictions on the testset
predictions = algo.test(testset)
accuracy.rmse(predictions)

# Make a specific prediction
uid = str(196)  # raw user id (as in the ratings file). They are **strings**!
iid = str(302)  # raw item id (as in the ratings file). They are **strings**!
pred = algo.predict(uid, iid, r_ui=4, verbose=True)

# Run 5-fold cross-validation and print results.
# cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
