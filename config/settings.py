from config.browsers import Browsers
import os


BASE_URL = "https://www.saucedemo.com"

DEFAULT_TIMEOUT = 10

HEADLESS = False

IMPLICIT_WAIT = 5

WINDOW_MAXIMIZED = True

DISABLE_NOTIFICATIONS = True

BROWSER = os.getenv(
    "BROWSER",
    Browsers.EDGE
)