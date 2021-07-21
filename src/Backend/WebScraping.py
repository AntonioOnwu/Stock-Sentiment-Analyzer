# type: ignore
import json
import time

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
    return subred,reddit


# create one dict for number times stock has been mentioned and one dict for all of stocks comments 
def get_comments():
    subred,reddit = get_sub()
    url = subred.url
    submission = reddit.submission(url=url)
    post = {}
    mentioned = {}
    for comment in submission.comments:
        if isinstance(comment, MoreComments):
            continue
        split = comment.body.split(" ")
        for word in split:
            if word.upper() in tickers and word not in blacklist: #
                word = word.upper()
                if word in mentioned:
                    mentioned[word] += 1
                    post[word].append(comment.body)
                else:
                    mentioned[word] = 1
                    post[word] = [comment.body]
    return  mentioned, post
# reg avg is 6.98, tickers made to set 25.91, both 6.17

# gets top 10 most mentioned stocks
def get_top():
    mentioned,post = get_comments()
    picks = 10
    symbols = dict(sorted(mentioned.items(), key=lambda item: item[1], reverse = True))
    top_picks = list(symbols.keys())[0:picks]
    top_ment_stocks =[]
    for i in top_picks:
        top_ment_stocks.append({"stock": i, "mentions": symbols[i], "rating": " "})   
    return post, symbols, top_ment_stocks

def mentions():
    name = []
    i = 0
    post,symbols,top_ment_stocks = get_top()
    for elem in symbols:
        name.append({ "key": i, "value": elem, 'text':elem})
        i+=1
    jsonString =json.dumps(name)
    with open('/Users/antonioonwu/stonkstop/src/Backend/AllMentions.json', 'w') as outfile:
        json.dump(name, outfile, indent = 4)
    return str(jsonString) 

# gets setntiment for each stock
def get_sent():
    post, symbols, top_ment_stocks = get_top()
    picks_ayz = 10
    scores = {}
    vader = SentimentIntensityAnalyzer()
    # # adding custom words from Newwords.py 
    vader.lexicon.update(new_words)
    # # adds score analysis to each stock
    picks_sentiment = list(symbols.keys())[0:picks_ayz]
    for symbol in picks_sentiment:
        stock_comments = post[symbol]
        for cmnt in stock_comments:
            score = vader.polarity_scores(cmnt)  
            if symbol in scores:
                for key, _ in score.items():
                    scores[symbol][key] += score[key]
            else:
                scores[symbol] = score           
        # calculating avg.
      
        for key in score:
            scores[symbol][key] = scores[symbol][key] / symbols[symbol]
            scores[symbol][key]  = "{pol:.3f}".format(pol=scores[symbol][key])
        
    return picks_ayz, scores, top_ment_stocks


def get_rating():
    picks_ayz, scores, top_ment_stocks = get_sent()
    df = pd.DataFrame(scores)
    df.index = ['Negative', 'Nuetral', 'Positive', 'Compound']
    df = df.T
    top_stocks = []
    i = 0
    for elem in df['Compound']:
        if float(elem) >= 0.7:
            top_ment_stocks[i]["rating"] = 'Strong buy'

        elif float(elem) >= 0.1:
            top_ment_stocks[i]["rating"] = 'Buy'

        elif float(elem) >= -0.1:
            top_ment_stocks[i]["rating"] = 'Hold'

        elif float(elem) > -0.7:
            top_ment_stocks[i]["rating"] = 'Sell'
        else:
            top_ment_stocks[i]["rating"] = 'Strong sell'
        i += 1
    return top_ment_stocks

# [stronbuy[.6-1],buy[.2-.6],hold[.1-.2],sell[.1-.6],strongsell[.6-1]]
# exports the stockss' names with their mentions and rating
def export_json():
    # while True:
        top_ment_stocks = get_rating()
        jsonString =json.dumps(top_ment_stocks)
        with open('/Users/antonioonwu/stonkstop/src/Backend/Topstocks.json', 'w') as outfile:
            json.dump(top_ment_stocks, outfile, indent = 4)
        return str(jsonString)     

get_sent()