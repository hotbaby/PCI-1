# encoding: utf8

import os
import math
import random
import pandas as pd


# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs, person1, person2):
    # Get the list of shared_items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # if they have no ratings in common, return 0
    if len(si) == 0:
        return 0

    # Add up the squares of all the differences
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])

    return 1/(1+sum_of_squares)

# Returns the Pearson correlation coefficient for p1 and p2


def sim_pearson(prefs, p1, p2):
    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    # if they are no ratings in common, return 0
    if len(si) == 0:
        return 0

    # Sum calculations
    n = len(si)

    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # Sum of the products
    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])

    # Calculate r (Pearson score)
    num = pSum-(sum1*sum2/n)
    den = math.sqrt((sum1Sq-pow(sum1, 2)/n)*(sum2Sq-pow(sum2, 2)/n))
    if den == 0:
        return 0

    r = num/den

    return r


def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            # Flip item and person
            result[item][person] = prefs[person][item]
    return result


def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]


# 基于用户的协同过滤推荐
# 根据用户对相同电影评分求的用户的相似度，再根据用户相似度和电影评分乘机倒序，获取电影的推荐列表
def getRecommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        # don't compare me to myself
        if other == person:
            continue

        # 根据用户对相同电影的评分，求两个用户的相似度
        sim = similarity(prefs, person, other)
        # ignore scores of zero or lower
        if sim <= 0:
            continue

        for item in prefs[other]:
            # only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item]*sim  # 其他用户对电影的评分 * 用户相似度
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim    # 相似度

    # Create the normalized（标准化） list
    rankings = [(total/simSums[item], item) for item, total in totals.items()]

    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings


def load_data(datapath, **kwargs):
    """
    加载数据
    :param datapath 目录
    :return rating_data, movie_data
    """
    # 电影数据
    movie_data = {}
    movie_filepath = os.path.join(datapath, 'movies.csv')
    df = pd.read_csv(movie_filepath)
    for row in df.values:
        movie_id = int(row[0])
        movie_data[movie_id] = {
            'title': row[1],
            'genres': row[2],
        }

    # 电影评分数据
    rating_data = {}
    rating_filepath = os.path.join(datapath, 'ratings.csv')
    df = pd.read_csv(rating_filepath)
    for row in df.values:
        user_id = int(row[0])
        movie_id = int(row[1])
        rating = float(row[2])
        rating_data.setdefault(user_id, dict())
        rating_data[user_id][movie_id] = rating

    return rating_data, movie_data


def recommend(datapath, user=None, n=20):
    """
    推荐
    """
    rating_data, movie_data = load_data(datapath)

    random_user = random.randint(0, len(rating_data))
    user = rating_data.keys()[random_user] if user is None else user
    if user not in rating_data:
        print 'user %s not found' % user
        os._exit(-1)

    recomm_movies = []
    rankings = getRecommendations(rating_data, user)
    for sim_movie in rankings[:n]:
        sim, movie_id = sim_movie
        sim = int(sim * 10) / 10
        movie_title = movie_data[movie_id]['title'] if movie_id in movie_data else None
        recomm_movies.append([sim, movie_id, movie_title])

    return user, recomm_movies


def similar_movies(datapath, movie_id=None):
    rating_data, movie_data = load_data(datapath)
    transPrefs = transformPrefs(rating_data)

    random_movie_index = random.randint(0, len(transPrefs))
    movie_id = transPrefs.keys()[random_movie_index] if movie_id is None else movie_id

    if movie_id not in transPrefs:
        print 'Invalid movie id'
        os._exit(-1)

    sim_movies = []
    for sim_movie in topMatches(transPrefs, movie_id, 10):
        sim, sim_movie_id = sim_movie
        title = movie_data[sim_movie_id]['title'] if sim_movie_id in movie_data else None
        sim_movies.append([sim, sim_movie_id, title])

    return movie_data[movie_id]['title'], sim_movies
