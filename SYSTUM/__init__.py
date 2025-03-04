from SYSTUM.core.bot import KING
from SYSTUM.core.dir import dirr
from SYSTUM.core.git import git
from SYSTUM.core.userbot import Userbot
from SYSTUM.misc import dbb, heroku
import config
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = KING()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
import logging 
try:
  from Nexgram import Client
  nx = Client("Master", config.BOT_TOKEN)
except Exception as e:
  nx = None
  logging.error(e)
