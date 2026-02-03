from playwright.async_api import BrowserType

use = {
    "headless": False,
    "video": "on",
    "screenshot": "only-on-failure",
    "trace": "retain-on-failure",
    "baseURL": "https://cloud.cronberry.com"
}

config = {
    "use": use,
    "timeout": 30000
}