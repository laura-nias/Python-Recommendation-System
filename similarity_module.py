#!/usr/bin/env python
# coding: utf-8

import math
   
#List of all possible features user can select
all_features = ['acousticness','danceability', 'energy', 'liveness', 'loudness', 'popularity', 'speechiness', 'tempo', 'valence']
    
#Function for Manhattan Similarity - Adapted from: https://dataaspirant.com/five-most-popular-similarity-measures-implementation-in-python/

def manhattan_similarity(data, id_1, id_2):
    
    #Two empty lists
    vec_a = []
    vec_b = []
        
    #Asks user which feature they want to compute similarty for, converts to lower case and strips leading and tailing whitespace
    feature = input("\nLIST OF FEATURES\n\nAll Features\nAcousticness\nDanceability\nEnergy\nLiveness\nLoudness\nPopularity\nSpeechiness\nTempo\nValence\n\nWhich feature would you like to use? ").strip().lower()
    
    #If the user chooses 'all features', the for loop will loop through the value for that row and add them to the empty lists
    if(feature == "all features"):
        for i in all_features:
            vec_a.append(float(data[id_1][i]))
            vec_b.append(float(data[id_2][i]))
        
    #Else it takes the values for the one feature and adds it to the empty lists
    elif(feature in all_features):
        vec_a.append(float(data[id_1][feature]))
        vec_b.append(float(data[id_2][feature]))
        
    else:
        #Validation of feature error
        print("ERROR: The input doesn't match any feature")
        manhattan_similarity(data, id_1, id_2)

    #Returns the result from Manhattan Similarity - abs() means absolute values
    return sum(abs(a-b) for a,b in zip(vec_a,vec_b))

#Function for Jaccard Similarity - Adapted from: https://dataaspirant.com/five-most-popular-similarity-measures-implementation-in-python/
def jaccard_similarity(data, id_1, id_2):
    
     #Two empty lists
    vec_a = []
    vec_b = []
    
    #Asks user which feature they want to compute similarty for, converts to lower case and strips leading and tailing whitespace
    feature = input("\nLIST OF FEATURES\n\nAll Features\nAcousticness\nDanceability\nEnergy\nLiveness\nLoudness\nPopularity\nSpeechiness\nTempo\nValence\n\nWhich feature would you like to use? ").strip().lower()
    
    #If the user chooses 'all features', the for loop will loop through the value for that row and add them to the empty lists
    if(feature == "all features"):
        for i in all_features:
            vec_a.append(float(data[id_1][i]))
            vec_b.append(float(data[id_2][i]))
            
        intersection = len(list(set(vec_a).intersection(vec_b)))
        union = (len(vec_a) + len(vec_b)) - intersection
        return float(intersection) / union
    
    #Else it checks validity of feature and use values    
    elif(feature in all_features):
        a = data[id_1][feature]
        b = data[id_2][feature]

        #Turns a and b into a set
        a = set(a)
        b = set(b)

        #Length of a intersection b
        intersection = len(a.intersection(b))
        #Length of a union b
        union = len(a.union(b))
        
        #Returns the result from Jaccard Similarity
        return intersection/float(union)
    else:
        #Validation of feature error
        print("ERROR: The input doesn't match any feature")
        jaccard_similarity(data, id_1, id_2)

#Function for Euclidean Similarity - Adapted from: https://dataaspirant.com/five-most-popular-similarity-measures-implementation-in-python/
def euclidean_similarity(data, id_1, id_2):
    
     #Two empty lists
    vec_a = []
    vec_b = []
    
    #Asks user which feature they want to compute similarty for, converts to lower case and strips leading and tailing whitespace
    feature = input("\nLIST OF FEATURES\n\nAll Features\nAcousticness\nDanceability\nEnergy\nLiveness\nLoudness\nPopularity\nSpeechiness\nTempo\nValence\n\nWhich feature would you like to use? ").strip().lower()
    
    #If the user chooses 'all features', the for loop will loop through the value for that row and add them to the empty lists
    if(feature == "all features"):
        for i in all_features:
            vec_a.append(float(data[id_1][i]))
            vec_b.append(float(data[id_2][i]))
    #Else it checks validity of feature and use values to append to empty lists   
    elif(feature in all_features):
        vec_a.append(float(data[id_1][feature]))
        vec_b.append(float(data[id_2][feature]))
    else:
        #Validation of feature error
        print("ERROR: The input doesn't match any feature")
        euclidean_similarity(data, id_1, id_2)

    #Returns the result from Euclidean Similarity - **2 means to the power of 2
    return math.sqrt(sum((a - b)**2 for a, b in zip(vec_a, vec_b)))
    
#Function for Cosine Similarity - Adapted from: https://clay-atlas.com/us/blog/2020/03/27/cosine-similarity-text-calculate-python/
def cosine_similarity(data, id_1, id_2):
    
     #Two empty lists
    vec_a = []
    vec_b = []
    
    #Asks user which feature they want to compute similarty for, converts to lower case and strips leading and tailing whitespace
    feature = input("\nLIST OF FEATURES\n\nAll Features\nAcousticness\nDanceability\nEnergy\nLiveness\nLoudness\nPopularity\nSpeechiness\nTempo\nValence\n\nWhich feature would you like to use? ").strip().lower()
    
    #If the user chooses 'all features', the for loop will loop through the value for that row and add them to the empty lists
    if(feature == "all features"):
        for i in all_features:
            vec_a.append(float(data[id_1][i]))
            vec_b.append(float(data[id_2][i]))
    #Else it checks validity of feature and use values to append to empty lists   
    elif(feature in all_features):
        vec_a.append(float(data[id_1][feature]))
        vec_b.append(float(data[id_2][feature]))
        
    else:
        #Validation of feature error
        print("ERROR: The input doesn't match any feature")
        cosine_similarity(data, id_1, id_2)
        
    #Absolute values, summed up
    norm_a = sum(abs(x) for x in vec_a)
    norm_b = sum(abs(x) for x in vec_b)

    dot = sum(a * b for a, b in zip(vec_a, vec_b))

    #Returns the result from Cosine Similarity
    return dot / (norm_a * norm_b)

#Function for Pearson Similarity - Adapted from: https://stackoverflow.com/questions/3949226/calculating-pearson-correlation-and-significance-in-python
def pearson_similarity(data, id_1, id_2):
    
     #Two empty lists
    vec_a = []
    vec_b = []
    
    #Asks user which feature they want to compute similarty for, converts to lower case and strips leading and tailing whitespace
    feature = input("\nLIST OF FEATURES\n\nAll Features\nAcousticness\nDanceability\nEnergy\nLiveness\nLoudness\nPopularity\nSpeechiness\nTempo\nValence\n\nWhich feature would you like to use? ").strip().lower()
    
    #If the user chooses 'all features', the for loop will loop through the value for that row and add them to the empty lists
    if(feature == "all features"):
        for i in all_features:
            vec_a.append(float(data[id_1][i]))
            vec_b.append(float(data[id_2][i]))
    #Else it checks validity of feature and use values to append to empty lists   
    elif(feature in all_features):
        vec_a.append((float(data[id_1][feature])))
        vec_b.append((float(data[id_2][feature])))
        
    else:
        #Validation of feature error
        print("ERROR: The input doesn't match any feature")
        pearson_similarity(data, id_1, id_2)

    #n = length of vec_a
    n=len(vec_a)
    #vals = range of numbers up to n
    vals=range(n)
    #Sum of values
    sumx=sum([float(vec_a[i]) for i in vals])
    sumy=sum([float(vec_b[i]) for i in vals])
    
    #Values to the power of 2, summed up
    sumxSq=sum([vec_a[i]**2.0 for i in vals])
    sumySq=sum([vec_b[i]**2.0 for i in vals])

    #vec_a values * vec_b values, summed up
    pSum=sum([vec_a[i]*vec_b[i] for i in vals])

    num=pSum-(sumx*sumy/n)
    #pow(, 2) means squared, **.5 means to the power of 0.5 
    den=((sumxSq-pow(sumx,2)/n)*(sumySq-pow(sumy,2)/n))**.5
    
    #Returns the result from Pearson Similarity
    try:
        return num/den
    except ZeroDivisionError:
        #Tried to divide by zero so throws error
        return "Similarity cannot be computed for this feature"
   
