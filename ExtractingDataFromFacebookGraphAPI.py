# -*- coding: utf-8 -*-
"""
@author: Tanya.Nayyar

"""
#description     :Python Script for extracting data from Facebook Graph API
#author          :Tanya Nayyar
#date            :03-25-2020
#version         :1
#python_version  :3.7.4  
#%%Import the required libraries
import requests
import pickle
#%%Define the token variable with the API token key retreived
token = "<<<<<<Token Key>>>>>>"
#%%
def req_facebook(req):
    r=requests.get("https://graph.facebook.com/v2.8/" + req , {'access_token' : token})
    return r
#%%
req = "me?fields=id,name,posts{created_time,likes.limit(0).summary(True),comments.limit(0).summary(True){message},id}"
results =req_facebook(req).json()
#%%
#initialize an empty list data
data = []

results = results['posts']
#%%
while True:
    
    try:
        #put the data we got in results into another list which is data 
        data.extend(results['data'])
        r=requests.get(results['paging']['next'])
        results = r.json()
  
    except:
        print("done")
        break
#%%
pickle.dump(data, open("Facebook_data_modified.pkl","wb"))
#%%
loaded_data = pickle.load(file = open("Facebook_data_modified.pkl","rb"))
#%%  