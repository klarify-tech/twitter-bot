import tweepy as tp
import time
import os

consumer_key = '6PgknYt9iOWCKv52tjisdBUYQ'
consumer_secret = 'PGGhzJ2oNiR97NBSveN3sVdig2iSSmNeNSlecxGraf2MV140Xb'
access_token = '1361727452712607744-9mLoWCl12e1VfdyPvzAOIiQ5dayyVt'
access_secret = ''

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tp.API(auth)

os.chdir('models')
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    api.update_status("Fire !!")
    time.sleep(30)

