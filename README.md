# twitterUpdates
Print Twitter updates to the console from a list of users

## Dependencies
* Python 3
* Twitter API (for making requests to Twitter to grab recent Tweet data)

## What It Does
twitterUpdates prints a console notification of the latest tweets from specified users. Meant to be extended and used with a notification system. I personally attached mine to my Discord bot for a centralized medium of notifications.

## Necessary Input
In order to make the code work, you must modify the following in the code:
* Twitter Verification (you can acquire these by registering an application with Twitter [here](https://apps.twitter.com/))
  * Consumer Key
  * Consumer Secret
  * Access Token Key
  * Access Token Secret
* User List (users to check for updates from)

## Important Notes
* If a user makes more than one tweet before the next request is made, it will only show the most recent tweet

## Special Thanks
Thanks to the following articles as they helped in various functionality with this script:
* Twitter API Example - Search and Get User Tweets in Python, November 19, 2016
  * Used as a significant reference for learning how to utilize the Twitter API and acquire the consumer and access credentials
