import requests
from requests_oauth2client import *
#from requests_oauthlib import OAuth2Session
from requests_oauth2client import OAuth2Client

client_id = r'simon.guo@environicsanalytics.com'
client_secret = r'Gwj.677895'

oauth2client = OAuth2Client(
    token_endpoint="https://testb2ceag.b2clogin.com/testb2ceag.onmicrosoft.com/B2C_1_SIGNIN/oauth2/v2.0/token",
    authorization_endpoint="https://testb2ceag.b2clogin.com/testb2ceag.onmicrosoft.com/B2C_1_SIGNIN/oauth2/v2.0/authorize",
    client_id="my_client_id",
    client_secret="my_client_secret",
)


print(oauth2client)







