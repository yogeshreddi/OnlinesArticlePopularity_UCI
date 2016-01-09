# OnlinesArticlePopularity_UCI                                                                      
# Data set has been taken form UCI repository please refer to the link                               #(https://archive.ics.uci.edu/ml/datasets/Online+News+Popularity) for more information on the       
#problem and date set                                                                               

  This project is about predicting the content popularity of the articles that are published online. 
Recent research trends showed that predicting such popularity has direct implications to ad revenue 
models and content distribution markets.
  We have used a large set of inputs including the information about the article’s digital content, 
general popularity of the news. As predicting an article’s popularity is based on the regularity with 
which a user focuses on content, few natural language features are also considered. These features were 
considered possibly relevant to influence the number of shares. 
  Heterogeneous properties about the articles are summarized in a dataset and we compared them with other 
characteristics for a better prediction accuracy. Using the popular SEMMA approach, we have explored, 
cleansed the data and prepared a ready-to-model dataset. Five classification methods were used to predict 
two popularity classes (“POPULAR”, “UNPOPULAR”) and ensemble models are tried to improve the accuracy of 
the predictive classifications.


⦁	Conventional data models like Latent Dirichlet Allocation (LDA) implicitly capture the document-level 
word co-occurrence patterns to reveal topics. Through this project, we observed that LDA had great 
influence in the learning process of model parameters and deviated the purpose of prediction towards a 
low classification accuracy. This shortcomings suggests that a non-supervised learning model like LDA 
cannot be directly used in classification. Data distribution can be considered a remedy for reliable 
source of information.

⦁	Metadata columns were important to model large volumes of information; but we had to drop 9 variables as 
they couldn’t clearly communicate their relation with other features. We feel that a robust data dictionary 
is necessary to understand the variables of a dataset.

⦁	Another dimension of predicting the popularity could be analyzing the social features of an author. 
Additional readings suggested that there is a relationship between author’s social quant and their article’s 
popularity.

We are trying to implement the same project on Python by scraping the web URL of article to extract author 
related information like his popularity in mashable.com, no of followers he has, how long and how many articles 
he has been writing etc.
