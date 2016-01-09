
# coding: utf-8

# In[1]:

import urllib as ul
import pandas as pd
import re


# In[66]:

df = pd.read_csv('E:\Study\uconn\PRED MOD\Team project\OnlineNewsPopularity\OnlineNewsPopularity.csv')
urls = list(df.url)

regexp = '<span class="author_name">By+\s+(.+?)</span>'
regexbad = '<h1>(.+?)</h1>'

pattern = re.compile(regexp)
patternbad = re.compile(regexbad)


# In[70]:

i = 0
url = []
authors = []
auth_urls = []
a_comments = []
a_topics = []
a_followings = []
a_followers = []
url_shares = []


while i<len(urls):   
    print i
    url = url + [urls[i]]
    hf = ul.urlopen(urls[i])
    ht = hf.read()
    
    ### Fetching URL Shares
    
    url_shares = url_shares + [re.findall('<em.*?>([0-9.kK]+?)</em>',ht,re.S)[0]]
    
    ### Finding the author name of the uathor 
      
    name = re.findall(pattern,ht)
    
    ### else If loop to hanlde if the article has not author mentioned. 
    
    if name == []:
		
    ### Asigning Na's for urls without any data available
		
	auth_urls = auth_urls + ["NA"]
        a_comments = a_comments + ["NA"]
        a_topics = a_topics+ ["NA"]
        a_followings = a_followings + ["NA"]
        a_followers =  a_followers + ["NA"]


	
	name = re.findall('<div class="article-info">\\n<span class="byline basic">(.+?)</span>',ht,re.S)+[' Other']
	if name == []: authors = authors +["NA"]
	else: authors = authors + name
        

        
    else: 
        
        #### Forming a list of Author names
        
        authors = authors + name
        
        
        ###Forming author url which will be used for fetching comments, topics, followers and following details of author
        
        auth_url = "http://mashable.com/people/"+authors[i].replace('  ','-').replace(' ', '-').lower()
        hfauth = ul.urlopen(auth_url)
        htauth = hfauth.read()
        if re.findall(patternbad,htauth)[0] =="The Bad News":
            auth_url = "http://mashable.com/author/"+authors[i].replace('  ','-').replace(' ', '-').lower()
        

        auth_urls = auth_urls + [auth_url]
        
        
        ###Reading the Author information HTML Page
        
        hfc = ul.urlopen(auth_url)
        htc = hfc.read()
        
        ###Scraping for Comments on Authors Articles till date
        
        a_comment = re.findall('<em>([0-9]+?)</em>\\nComments' , htc , re.S)
        if a_comment ==[]:
            a_comments = a_comments + ["NA"]
        else:
            a_comments = a_comments + a_comment
            
        ###Scraping for No of topics on whihc Author has written Articles till date
        
        a_topic = re.findall('<li>\\n<em>([0-9]+?)</em>\\nTopics' , htc , re.S)
        
        if a_topic ==[]:
            a_topics = a_topics + ["NA"]
        else:
            a_topics = a_topics + a_topic
            
        ###Scraping for No of people author is foll0wing
            
        a_followg = re.findall('<li>\\n<em>([0-9]+?)</em>\\nFollowing' , htc , re.S)
       
        if a_followg ==[]:
            a_followings = a_followings + ["NA"]
        else:
            a_followings = a_followings + a_followg
        
        ###Scraping for No of followers author has
            
        a_followr = re.findall('<li>\\n<em>([0-9]+?)</em>\\nFollowers' , htc , re.S)
       
        if a_followr ==[]:
            a_followers = a_followers + ["NA"]
        else:
            a_followers = a_followers + a_followr

    
    i+=1

NewsPopularityData = pd.DataFrame ({'url': url, 'author_url':auth_urls ,'authors':authors,'NoOfComments':a_comments,'NoOfTopics':a_topics,'NoOfFollowing':a_followings,'NoOfFollowers' : a_followers, 'url_shares': url_shares })
pd.DataFrame(NewsPopularityData).to_csv("NewsPopularityData.csv")
