from os      import environ
from os.path import join, dirname
from dotenv  import load_dotenv

#### load .env
env_file = join(dirname(__file__), ".env")
load_dotenv(env_file)

env = dict()

#### Reads shell variables (returns None if not defined)
APP_ENV                     = environ.get('APP_ENV')
SLACK_BOT_TOKEN             = environ.get('SLACK_BOT_TOKEN')
SLACK_APP_TOKEN             = environ.get('SLACK_APP_TOKEN')
OPENAI_ENGINE               = environ.get('OPENAI_ENGINE')
OPENAI_API_TOKEN            = environ.get('OPENAI_API_TOKEN')
TWITTER_SCREEN_NAME         = environ.get('TWITTER_SCREEN_NAME') 
TWITTER_API_CUSTOMER        = environ.get('TWITTER_API_CUSTOMER') 
TWITTER_API_CUSTOMER_SECURE = environ.get('TWITTER_API_CUSTOMER_SECURE') 
TWITTER_API_TOKEN           = environ.get('TWITTER_API_TOKEN') 
TWITTER_API_TOKEN_SECURE    = environ.get('TWITTER_API_TOKEN_SECURE') 