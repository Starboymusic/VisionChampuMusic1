import json
import os

YOUTUBE = {
    "access_token": "ya29.a0AeDClZDYZhBNMm7qR8hu6PB76WoaSYH-2iymTWaXalM8O9OJLEWrPP7SrPsd6a76YKxnGbEKZPHy7bHKB7_hvK-YF8UGmLCo__OMVzw5dpNDHlZzZabxW00Da6p6J1dRO0AIpt9YaBjiaZXStOX79bbaA-ylo-gTovY360wEdl512um8aMVhaCgYKAZESARESFQHGX2MifYwqzm2kGW3L2FU92yI4PA0187",
    "expires": 1730226399.79375,
    "refresh_token": "1//05iOunvYEkVXCCgYIARAAGAUSNwF-L9IryHGrPr4UQtSvss8gxw1Vjyvo5CwdY3aYaNL1HQU3nVBzRwXWeW2xZhzU_mPpApz0bOA",
    "token_type": "Bearer"
}


def vipboy():
    TOKEN_DATA = os.getenv("TOKEN_DATA")
    if not TOKEN_DATA:
        os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
