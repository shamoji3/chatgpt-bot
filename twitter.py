import json
from   common import config
from   requests_oauthlib import OAuth1Session

class Twitter:
  def __init__(self, consumer:str, consumer_secret:str, token:str, token_secret:str):
    self.tw = OAuth1Session(
      consumer, consumer_secret, token, token_secret
    )
  def post(self, tweet:str): 
    url    = "https://api.twitter.com/1.1/statuses/update.json"
    params = {"status" : tweet}
    self.tw.post(url=url, params=params)

  def timeline(self, name:str, num:int): 
    url    = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {
        "count": num,
        "screen_name" : name,
      }
    r = self.tw.get(url=url, params=params)
    if r.status_code == 200:
      return json.loads(r.text)
    else:
      return [{"code": r.status_code}]

### Unit Test
if __name__ == '__main__':
  tw = Twitter(
    config.env['TWITTER_API_CUSTOMER'],
    config.env['TWITTER_API_CUSTOMER_SECURE'],
    config.env['TWITTER_API_TOKEN'],
    config.env['TWITTER_API_TOKEN_SECURE'],
    )
  print(config.env['TWITTER_SCREEN_NAME'])
  print(tw.timeline(config.env['TWITTER_SCREEN_NAME'], 1))