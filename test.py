import os

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.user import User
from facebook_business import adobjects


app_id = os.environ['FACEBOOK_APP_ID']
app_secret = os.environ['FACEBOOK_APP_SECRET']
access_token = os.environ['FACEBOOK_ACCESS_TOKEN']

FacebookAdsApi.init(app_id, app_secret, access_token)


me = User(fbid = 'me')
my_accounts = list(me.get_ad_accounts())
print(my_accounts[1])
my_account = my_accounts[1]

campaigns = my_accounts[1].get_campaigns()
#print(campaigns)


spend = my_accounts[1].api_get(fields=[adobjects.adaccount.AdAccount.Field.amount_spent])
# spend = my_accounts[0].api_get(fields=[adobjects.AdAccount.Field.amount_spent])
# documentation is wrong: https://github.com/facebook/facebook-python-business-sdk

print('printing spend object')
print(spend)

print("         ")

print('printing spend value')
print(my_account[adobjects.adaccount.AdAccount.Field.amount_spent])

name = my_account.api_get(fields=[adobjects.adaccount.AdAccount.Field.name])
print("         ")
print("printing name")
print(name)