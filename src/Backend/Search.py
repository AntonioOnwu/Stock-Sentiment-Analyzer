# type: ignore
import json

import matplotlib.pyplot as plt
import pandas as pd
import praw
from flask import Flask
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from praw.models import MoreComments

from Blacklist import blacklist
from Nasdaq import tickers
from Newwords import new_words


# Pulls daily/weekend plans from WallStreetBets(WSB) 
def get_sub():
    reddit = praw.Reddit(
        client_id="XQm-kylrCmw8AA",
        client_secret="4Q8F7u0E0gaD6AovF3RJUwBeuvYuAA",
        user_agent="StonkStop",)
    subred = reddit.subreddit("wallstreetbets").sticky()
    with open('/Users/antonioonwu/stonkstop/src/Backend/Query.json') as f:
        query = json.load(f)
    query = query['stock']['content'].upper()
    return subred,reddit,query


# # create one dict for number times stock has been mentioned and one dict for all of stocks comments 
def get_comments():
    subred,reddit,query = get_sub()
    url = subred.url
    submission = reddit.submission(url=url)
    post = {}
    mentioned = {}
    for comment in submission.comments:
        if isinstance(comment, MoreComments):
            continue
        split = comment.body.split(" ")
        for word in split:
            if word.upper() == query and word not in blacklist: 
                word = word.upper()
                if word in mentioned:
                    mentioned[word] += 1
                    post[word].append(comment.body)
                else:
                    mentioned[word] = 1
                    post[word] = [comment.body]

    return  mentioned, post,query


# # # gets top 10 most mentioned stocks
def get_top():
    mentioned,post,query = get_comments()
    top_ment_stocks =[]
    top_ment_stocks.append({"stock": query, "mentions": mentioned[query], "rating": " "})
    return mentioned, post, query, top_ment_stocks


# # gets setntiment for each stock
def get_sent():
    mentioned, post, query, top_ment_stocks = get_top()
    scores, s = {}, {}
    vader = SentimentIntensityAnalyzer()
    # # adding custom words from Newwords.py 
    vader.lexicon.update(new_words)
    # # adds score analysis to each stock
    stock_comments = post[query]
    for cmnt in stock_comments:
        score = vader.polarity_scores(cmnt)     
        if query in scores:
            for key, _ in score.items():
                scores[query][key] += score[key]
        else:
            scores[query] = score           
    # calculating avg.
    for key in scores[query]:
        scores[query][key] = scores[query][key] / mentioned[query]
        scores[query][key]  = "{pol:.3f}".format(pol=scores[query][key])
    return scores, top_ment_stocks,query


def get_rating():
    scores, top_ment_stocks, query = get_sent()
    elem = scores[query]['compound']
    if float(elem) >= 0.6:
        top_ment_stocks[0]["rating"] = 'really buy'

    elif float(elem) >= 0.2:
        top_ment_stocks[0]["rating"] = 'buy'

    elif float(elem) >= -0.1:
        top_ment_stocks[0]["rating"] = 'hold'

    elif float(elem) >= -0.6:
        top_ment_stocks[0]["rating"] = 'sell'
    else:
        top_ment_stocks[0]["rating"] = 'really sell'
    return top_ment_stocks


# # exports the stockss' names with their mentions and rating
def export_result():
    top_ment_stocks = get_rating()
    jsonString =json.dumps(top_ment_stocks)
    with open('/Users/antonioonwu/stonkstop/src/Backend/Result.json', 'w') as outfile:
        json.dump(top_ment_stocks, outfile, indent = 4)
    return str(jsonString)

