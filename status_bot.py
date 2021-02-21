import tweepy as tp

consumer_key = '6PgknYt9iOWCKv52tjisdBUYQ'
consumer_secret = 'PGGhzJ2oNiR97NBSveN3sVdig2iSSmNeNSlecxGraf2MV140Xb'
access_token = '1361727452712607744-9mLoWCl12e1VfdyPvzAOIiQ5dayyVt'
access_secret = 'lqjHFOGlnsjbnA8udCaCY47Zoo0arf3O3UeO1M8YOo9m8'

#Authenticate to twitter
auth = tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tp.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

api.update_profile(description="I like Python. I use python for everything")

#print(api.trends_available())
woeid = 2282863
user = api.get_user("elonmusk")
for tweet in tp.Cursor(api.home_timeline).items(100):
    print(f"{tweet.user.name} said: {tweet.text}")

# trends_result = api.trends_place(id=woeid)
# for trend in trends_result[0]["trends"]:
#     print(trend["name"])


#search for string in twitter
# for tweet in api.search(q="Kim Kardashian", lang="en", rpp=10):
#     print(f"{tweet.user.name}:{tweet.text}")

#get users from timeline
# user = api.get_user("MikezGarcia")

# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)

# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)

#get tweets from timeline
# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")

#api.update_status("How smart are you man !!")