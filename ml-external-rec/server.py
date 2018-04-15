from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from top_n_recommendations import get_top_n
from collections import defaultdict
import os
from surprise import dump
from surprise import SVD
from surprise import Dataset


app = Flask(__name__)
@app.route('/')
def hello():

    # userId_string = input("Please enter a userId ")
    # userId = int(userId_string)
    # top_n = recommend(userId)
    # recs = [1,2,3,4,5,6,7,8,9,10]
    return render_template('index.html')

@app.route('/manage_link', methods=['POST'])
def manage_link():
    print("manage_link")
    userId = request.form['userId']
    print(userId)
    # recommend(userId)
    return redirect(url_for('recommend', userId=userId))

# This method loads the pre-generated prediction model, recommend 10 movies to this user
@app.route('/<userId>')
def recommend(userId):
    data = Dataset.load_builtin('ml-100k')
    trainset = data.build_full_trainset()
    _, loaded_algo = dump.load(os.path.expanduser('./SVD_model'))
    print("file loaded")

    predictions_loaded_algo = loaded_algo.test(trainset.build_testset())
    recs = get_top_n(predictions_loaded_algo,10)[int(userId)]
    print(recs)
    return render_template('recommendation.html', recs=recs, user=userId)
    
