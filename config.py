# config.py — safe, hardened, includes WEBSITE_URL
import os
import re
from os import environ
from Script import script

# helpers
id_pattern = re.compile(r'^-?\d+$')

def is_enabled(value, default=False):
    if value is None:
        return default
    v = str(value).strip().lower()
    if v in {"true", "yes", "1", "enable", "y", "on"}:
        return True
    if v in {"false", "no", "0", "disable", "n", "off"}:
        return False
    return default

def to_int(value, default=0):
    try:
        return int(value)
    except Exception:
        return default

# -----------------------
# Basic bot info
# -----------------------
API_ID = to_int(environ.get("API_ID", "4770590"))
API_HASH = environ.get("API_HASH", "e33bf9032335b874acb9c6406f044836")
BOT_TOKEN = environ.get("BOT_TOKEN", "7184578061:AAEDa_nHSiEzRXFFPIM3UnLkLDOgRhkiXig")
BOT_USERNAME = environ.get("BOT_USERNAME", "VenomStoneFileStoreBot")
PORT = environ.get("PORT", "8080")

# -----------------------
# Pictures / branding
# -----------------------
_raw_pics = environ.get('PICS', 'https://telegra.ph/file/eb119179b4d2a13e71163.jpg')
PICS = [p for p in re.split(r'\s+', _raw_pics.strip()) if p]
if not PICS:
    PICS = ['https://telegra.ph/file/eb119179b4d2a13e71163.jpg']

# -----------------------
# Admins
# -----------------------
ADMINS_RAW = environ.get('ADMINS', '1654334233').strip()
ADMINS = []
if ADMINS_RAW:
    for admin in ADMINS_RAW.split():
        admin = admin.strip()
        if id_pattern.match(admin):
            ADMINS.append(int(admin))
        else:
            ADMINS.append(admin)

# -----------------------
# Clone / DB
# -----------------------
CLONE_MODE = is_enabled(environ.get('CLONE_MODE', "false"))
CLONE_DB_URI = environ.get("CLONE_DB_URI", "")
CDB_NAME = environ.get("CDB_NAME", "")

DB_URI = environ.get(
    "DB_URI",
    "mongodb+srv://kajaki7757:kGDRiPGNX691vlCL@cluster0.ylww9nv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
DB_NAME = environ.get("DB_NAME", "cluster0")

# -----------------------
# Auto Delete
# -----------------------
AUTO_DELETE_MODE = is_enabled(environ.get('AUTO_DELETE_MODE', "false"))
AUTO_DELETE = to_int(environ.get("AUTO_DELETE", "30"))          # minutes
AUTO_DELETE_TIME = to_int(environ.get("AUTO_DELETE_TIME", "1800"))  # seconds

# -----------------------
# Channels / Logging
# -----------------------
LOG_CHANNEL = to_int(environ.get("LOG_CHANNEL", "-1002113810572"))

# -----------------------
# File captions
# -----------------------
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# -----------------------
# Toggles
# -----------------------
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "true"))
VERIFY_MODE = is_enabled(environ.get('VERIFY_MODE', "false"))
WEBSITE_URL_MODE = is_enabled(environ.get('WEBSITE_URL_MODE', "false"))
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', "false"))
MULTI_CLIENT = is_enabled(environ.get("MULTI_CLIENT", "false"))

# -----------------------
# Verify / Shortlink / misc
# -----------------------
SHORTLINK_URL = environ.get("SHORTLINK_URL", "")
SHORTLINK_API = environ.get("SHORTLINK_API", "")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "")

# -----------------------
# Website config (ADDED): used by plugins/genlink.py
# -----------------------
# WEBSITE_URL is what plugins expect (full site URL or empty string)
WEBSITE_URL = environ.get("WEBSITE_URL", "")          # e.g. https://example.com
# WEBSITE_URL_MODE toggles whether WEBSITE_URL features are active
WEBSITE_URL_MODE = is_enabled(environ.get("WEBSITE_URL_MODE", "false"))

# -----------------------
# Stream & misc ints
# -----------------------
SLEEP_THRESHOLD = to_int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = to_int(environ.get("PING_INTERVAL", "1200"))
URL = environ.get("URL", "")

# -----------------------
# Environment detection
# -----------------------
ON_HEROKU = 'DYNO' in environ

# ---------------------------------------------------------------------
# End of config
# ---------------------------------------------------------------------
BOT_USERNAME = environ.get("BOT_USERNAME", "VenomStoneFileStoreBot")  # without @
PORT = environ.get("PORT", "8080")

# -----------------------
# Pictures / branding
# -----------------------
# PICS env can be space-separated URLs. Ensure non-empty list.
_raw_pics = environ.get('PICS', 'https://telegra.ph/file/eb119179b4d2a13e71163.jpg')
PICS = [p for p in re.split(r'\s+', _raw_pics.strip()) if p]

if not PICS:
    PICS = ['https://telegra.ph/file/eb119179b4d2a13e71163.jpg']

# -----------------------
# Admins
# -----------------------
ADMINS_RAW = environ.get('ADMINS', '1654334233').strip()
ADMINS = []
if ADMINS_RAW:
    for admin in ADMINS_RAW.split():
        admin = admin.strip()
        if id_pattern.match(admin):
            ADMINS.append(int(admin))
        else:
            ADMINS.append(admin)

# -----------------------
# Clone / DB
# -----------------------
CLONE_MODE = is_enabled(environ.get('CLONE_MODE', "false"))
CLONE_DB_URI = environ.get("CLONE_DB_URI", "")
CDB_NAME = environ.get("CDB_NAME", "")

DB_URI = environ.get(
    "DB_URI",
    "mongodb+srv://kajaki7757:kGDRiPGNX691vlCL@cluster0.ylww9nv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
DB_NAME = environ.get("DB_NAME", "cluster0")

# -----------------------
# Auto Delete
# -----------------------
AUTO_DELETE_MODE = is_enabled(environ.get('AUTO_DELETE_MODE', "false"))
AUTO_DELETE = to_int(environ.get("AUTO_DELETE", "30"))          # minutes
AUTO_DELETE_TIME = to_int(environ.get("AUTO_DELETE_TIME", "1800"))  # seconds

# -----------------------
# Channels / Logging
# -----------------------
LOG_CHANNEL = to_int(environ.get("LOG_CHANNEL", "-1002113810572"))

# -----------------------
# File captions
# -----------------------
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# -----------------------
# Feature toggles (boolean safe parsing)
# -----------------------
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "true"))
VERIFY_MODE = is_enabled(environ.get('VERIFY_MODE', "false"))
WEBSITE_URL_MODE = is_enabled(environ.get('WEBSITE_URL_MODE', "false"))
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', "false"))

# -----------------------
# Verify / Shortlink / Misc
# -----------------------
SHORTLINK_URL = environ.get("SHORTLINK_URL", "")
SHORTLINK_API = environ.get("SHORTLINK_API", "")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "")

# -----------------------
# Stream config & other ints
# -----------------------
MULTI_CLIENT = is_enabled(environ.get("MULTI_CLIENT", "false"))
SLEEP_THRESHOLD = to_int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = to_int(environ.get("PING_INTERVAL", "1200"))
URL = environ.get("URL", "")

# -----------------------
# Environment detection
# -----------------------
ON_HEROKU = 'DYNO' in environ

# ---------------------------------------------------------------------
# End of config
# ---------------------------------------------------------------------
