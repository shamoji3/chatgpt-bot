import logging
import openai
import twitter
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

#import config
from common import config

logging.basicConfig(level=logging.WARN)

app = App(token = config.SLACK_BOT_TOKEN)
openai.api_key  = config.OPENAI_API_TOKEN

### stick environment variables to global
APP_ENV                     = config.env['APP_ENV']
SLACK_BOT_TOKEN             = config.env['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN             = config.env['SLACK_APP_TOKEN']
OPENAI_ENGINE               = config.env['OPENAI_ENGINE']
OPENAI_API_TOKEN            = config.env['OPENAI_API_TOKEN']
TWITTER_SCREEN_NAME         = config.env['TWITTER_SCREEN_NAME'] 
TWITTER_API_CUSTOMER        = config.env['TWITTER_API_CUSTOMER']
TWITTER_API_CUSTOMER_SECURE = config.env['TWITTER_API_CUSTOMER_SECURE']
TWITTER_API_TOKEN           = config.env['TWITTER_API_TOKEN']
TWITTER_API_TOKEN_SECURE    = config.env['TWITTER_API_TOKEN_SECURE']

### Basic work
@app.message("hello")
def message_hello(message, say):
  say("Hello, <@{}>!".format(message['user']))

### Learn work
@app.message("learn")
def message_learn(message, say):
  character = str()
  tweets    = get_timeline(30)
  if tweets:
    for tweet in tweets:
      # ・ Tweet1
      # ・ Tweet2
      # ・ Tweet3
      character += "・ "+tweet['text']+"\n"
    name = tweet['user']['name']
    data = ("登場人物「{}」の設定を教えます。以下に続くセリフ\n{}これらは全て「{}」のものです。「{}」になりきってお話してください。".format(name,character,name,name))
    say("learned from {} on twitter! {}".format(config.TWITTER_SCREEN_NAME,data))
  else:
    say("nothing to learn.")

def get_timeline(num:int):
  tw = twitter.Twitter(
    config.TWITTER_API_CUSTOMER,
    config.TWITTER_API_CUSTOMER_SECURE,
    config.TWITTER_API_TOKEN,
    config.TWITTER_API_TOKEN_SECURE
  )
  return tw.timeline(config.TWITTER_SCREEN_NAME, num)

### Message
@app.event('message')
def handle_message(event, say):
  text = event['text']
  response = generate_response(text)
  say(response)

### Generrate from OpenAI
@decorators.exception
def generate_response(message):
  content  = message
  response = openai.Completion.create(
    engine      = config.OPENAI_ENGINE,
    prompt      = content,
    max_tokens  = 1024,
    temperature = 0.5
  )
  response_text = response['choices'][0]['text']
  return response_text

if __name__ == "__main__":
  handler = SocketModeHandler(app=app, app_token=config.SLACK_APP_TOKEN)
  handler.start()