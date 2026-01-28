from dotenv import dotenv_values

config_dict = dotenv_values(".env")

BOT_TOKEN = config_dict["BOT_TOKEN"]
USER_ID = config_dict["USER_ID"]
USER_NAME = config_dict["USER_NAME"]
IMAP_PASS = config_dict["IMAP_PASS"]
