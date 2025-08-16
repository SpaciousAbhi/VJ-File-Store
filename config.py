# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default=False):
    if value is None:
        return default
    v = str(value).strip().lower()
    if v in ("true", "yes", "1", "enable", "enabled", "y", "on"):
        return True
    if v in ("false", "no", "0", "disable", "disabled", "n", "off"):
        return False
    return default

# ---------- Bot Information ----------
API_ID = int(environ.get("API_ID", "4770590"))
API_HASH = environ.get("API_HASH", "e33bf9032335b874acb9c6406f044836")
BOT_TOKEN = environ.get("BOT_TOKEN", "7184578061:AAEDa_nHSiEzRXFFPIM3UnLkLDOgRhkiXig")

# Pictures for /start (space-separated list). Safe if empty.
_default_pics = (
    "https://telegra.ph/file/eb119179b4d2a13e71163.jpg "
    "https://telegra.ph/file/dc5a1a49c2786685ff97a.jpg "
    "https://telegra.ph/file/1a9519a68c4d45ac9455a.jpg "
    "https://telegra.ph/file/e5a3d6969f2082eecc3c1.jpg "
    "https://telegra.ph/file/57d6d774cf4baf2de5968.jpg"
)
PICS = [p for p in environ.get("PICS", _default_pics).split() if p] or _default_pics.split()

ADMINS = [
    int(a) if id_pattern.search(a) else a
    for a in environ.get("ADMINS", "1654334233").split()
]

BOT_USERNAME = environ.get("BOT_USERNAME", "VenomStoneFileStoreBot")  # without @
PORT = int(environ.get("PORT", "8080"))

# ---------- Clone Info ----------
CLONE_MODE = is_enabled(environ.get("CLONE_MODE"), False)

# If Clone Mode is True, fill these:
CLONE_DB_URI = environ.get(
    "CLONE_DB_URI",
    "mongodb+srv://kajaki7757:kGDRiPGNX691vlCL@cluster0.ylww9nv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
CDB_NAME = environ.get("CDB_NAME", "cluster0")

# ---------- Database Information ----------
DB_URI = environ.get(
    "DB_URI",
    "mongodb+srv://kajaki7757:kGDRiPGNX691vlCL@cluster0.ylww9nv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
DB_NAME = environ.get("DB_NAME", "cluster0")

# ---------- Auto Delete ----------
AUTO_DELETE_MODE = is_enabled(environ.get("AUTO_DELETE_MODE"), True)
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30"))          # minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800"))  # seconds

# ---------- Channel / Logs ----------
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002113810572"))

# ---------- File Caption ----------
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# ---------- Public File Store ----------
PUBLIC_FILE_STORE = is_enabled(environ.get("PUBLIC_FILE_STORE", "True"), True)

# ---------- Verification ----------
VERIFY_MODE = is_enabled(environ.get("VERIFY_MODE", "True"), True)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "get2short.com")  # without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "9ae188a4e5609c6f089d21d01816974230a64218")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/VenomStoneNetwork/85")

# ---------- Website Mode (for genlink.py) ----------
WEBSITE_URL_MODE = is_enabled(environ.get("WEBSITE_URL_MODE"), False)
WEBSITE_URL = environ.get("WEBSITE_URL", "")  # If enabled, set full base URL

# ---------- File Stream Config ----------
STREAM_MODE = is_enabled(environ.get("STREAM_MODE"), False)
MULTI_CLIENT = is_enabled(environ.get("MULTI_CLIENT"), False)

SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes

ON_HEROKU = "DYNO" in environ
URL = environ.get("URL", "https://testofvjfilter-1fa60b1b8498.herokuapp.com/")-------------------------------------------------------------
