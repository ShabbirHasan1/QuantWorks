import logging, csv
import pandas as pd
from datetime import datetime, date
import numpy as np
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker

def tokenList(kite):
	return kite.instruments()

logging.basicConfig(level=logging.DEBUG)

api_key = "lu3hm9qavt86o9uq"
access_token = "lY2V4L02TzhQHw46wwJbfsao9Lt0on7G"

kite = KiteConnect(api_key=api_key)

# print(kite.generate_session(request_token, api_secret))

kite.set_access_token(access_token)

kws = KiteTicker(api_key,access_token)

def on_ticks(ws, ticks):
    # Callback to receive ticks.
    logging.debug("Strating the data stream")
    logging.debug("Ticks: {}".format(ticks))

def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    logging.debug("Starting the connection")
    tokenDict = tokenList(kite)
    print(tokenDict)
    ws.subscribe([3821313])
    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [3821313])
    logging.debug("successfully subscribed")

def on_close(ws, code, reason):
    # On connection close stop the main loop
    # Reconnection will not happen after executing `ws.stop()`
    print("Closing the connection")
    ws.stop()

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()

