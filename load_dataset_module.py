#!/usr/bin/env python
# coding: utf-8

import csv

#Artist funtion which obtains certain values from the csv file and put them into a dictionary
def artist():
    #Two empty dictionaries
    artist_dict = {}
    artist_features = {}
    #Reads the csv file and separates values by comma
    try:
        with open('data.csv','r')as f:
            data=csv.DictReader(f,delimiter=",")
            #For each row in the data, put values into dictionary
            for rows in data:
                x=artist_dict.get(rows['row_id'],dict())
                x[rows['row_id']]={k:rows[k] for k in ('acousticness','artists','danceability', 'energy', 'liveness', 'loudness', 'name', 'popularity', 'speechiness', 'tempo', 'valence')}
                artist_features.update(x)
            #Returns the artist features
            return artist_features
    #Triggers an error if something goes wrong
    except IOError as e:
        errno, strerror = e.args
        print("I/O error({0}): {1}".format(errno,strerror))

#Music funtion which obtains certain values from the csv file and put them into a dictionary
def music():
    music_dict={}
    music_features = {}
    
    try:
        with open('data.csv','r')as csv_file:
            data=csv.DictReader(csv_file,delimiter=",")
            for row in data:
                y=music_dict.get(row['row_id'],dict())
                y[row['row_id']]={k:row[k] for k in ('acousticness','danceability', 'energy', 'liveness', 'loudness', 'name', 'popularity', 'speechiness', 'tempo', 'valence')}
                music_features.update(y)
            #Returns the music features
            return music_features
    except IOError as e:
        errno, strerror = e.args
        print("I/O error({0}): {1}".format(errno,strerror))