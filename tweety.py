  from tweety import Twitter
  
  app = Twitter("session")
  
  all_tweets = app.get_tweets("elonmusk")
  for tweet in all_tweets:
      print(tweet)