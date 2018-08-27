import twitter # API for handling Twitter
import time # Delaying subsequent API calls

# Authentication for use of API
api = twitter.Api(consumer_key="CONSUMER_KEY",
                  consumer_secret="CONSUMER_SECRET",
                  access_token_key="ACCESS_TOKEN_KEY",
                  access_token_secret="ACCESS_TOKEN_SECRET")

userList = ["INSERT TWITTER HANDLES AS LIST HERE"] # List of users you want updates from
userDict = {} #Stores Twitter username and latest tweet

# Generate a dictionary based on your specified list of users
for user in userList:
    userDict[user] = "" # Initialize with latest tweet as an empty string

while True: # Loop infinitely until stop
    counter = 0 # For reference of userlist dictionary
    for user in userList:
        t = api.GetUserTimeline(screen_name=userList[counter], count=1) # Get the latest tweet
        tweets = [i.AsDict() for i in t]
        for t in tweets:
            tweet = t['text']
            if tweet != userDict[user]: # If the tweet is different than the one stored in the dictionary
                userDict[user] = tweet
                print(tweet) # Print the tweet
        counter += 1 # Update counter for dictionary reference
    time.sleep(10) # Delay until next call
