import os
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.user import User
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business import adobjects


class FacebookAccess(object):
    """ Instantiate environment variables """
    def __init__(self):
         self.app_id = os.environ['FACEBOOK_APP_ID']
         self.app_secret = os.environ['FACEBOOK_APP_SECRET']
         self.access_token = os.environ['FACEBOOK_ACCESS_TOKEN']

    def __call__(self):
         return self.app_id
         return self.app_secret
         return self.access_token


# Access Facebook Business API
access = FacebookAccess()

# Debugging message 1
print('FacebookAccess done')

class FacebookInit(object):
    """ Send secrets """
    def login(self, x, y, z):
        self.contents = FacebookAdsApi.init(x, y, z)
        return self.contents

login = FacebookInit()
login.login(access.app_id, access.app_secret, access.access_token)

# Debugging message 2
print('FacebookInit done')

# List accounts
class GetAccounts(object):
    """ Get account id list """
    def __init__(self):
        me = User(fbid = 'me')
        self.getaccountlist = list(me.get_ad_accounts())

    def __call__(self):
        return self.getaccountlist

# Call the object
account_list = GetAccounts()

# Debugging message 3
print('GetAccounts done')

# Get total amount of accounts
def account_list_length():
    """ Counts the accounts """
    if account_list.getaccountlist:
        return len(account_list.getaccountlist)
    else:
        return print('empty list')

account_list_length = account_list_length()

# account_list_range resembles seq_along
account_list_range = list(range(account_list_length))

# Debugging message 4
print('account_list_length done')

# Listing account names
def account_names(x):
    if not account_list.getaccountlist:
        return print('no accounts here.')
    else:
        names = account_list.getaccountlist[x].api_get(fields=[adobjects.adaccount.AdAccount.Field.name])
        #act = account_list.getaccountlist[x]
        #names = act[adobjects.adaccount.AdAccount.Field.name]

        return names

act_names = map(account_names, account_list_range)

print(list(act_names))
