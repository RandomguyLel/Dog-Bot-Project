import discord
import os
import json
import yamom
#file too large
import instagram_private_api
#holy shit it worked

from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError

# Without any authentication
web_api = Client(auto_patch=True, drop_incompat_keys=False)
user_feed_info = web_api.user_feed('329452045', count=10)
for post in user_feed_info:
    print('%s from %s' % (post['link'], post['user']['username']))

# Some endpoints, e.g. user_following are available only after authentication
authed_web_api = Client(
    auto_patch=True, authenticate=True,
    username='YOUR_USERNAME', password='YOUR_PASSWORD')

following = authed_web_api.user_following('123456')
for user in following:
    print(user['username'])

