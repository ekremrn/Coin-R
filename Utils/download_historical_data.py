import os
import pandas as pd
from dotenv import load_dotenv
from binance.client import Client
from argparse import ArgumentParser


#
load_dotenv()

apiKey = str(os.getenv("BINANCE_APIKEY"))
apiSecurity = str(os.getenv("BINANCE_APISECURITY"))


#
parser = ArgumentParser()

parser.add_argument('--pair', type = str, default = "BTCUSDT")
parser.add_argument('--interval', type = str, default = "1h")
parser.add_argument('--date', type = str, default = "1 April 2017")
parser.add_argument('--datapath', type = str, default = "data/")

args = parser.parse_args()


#
client = Client(apiKey, apiSecurity)


#
data = client.get_historical_klines(args.pair, args.interval, args.date)

data = pd.DataFrame(data = data, index = range(len(data)), columns = [
    'OpenTime', 'Open', 'High', 
    'Low', 'Close', 'Volume', 
    'CloseTime', 'QuoteAssetVolume', 'NumberOfTrades', 
    'TakerBuyBaseAssetVolume', 'TakerBuyQuoteAssetVolume', 'CanBeIgnored'])


#
if not os.path.isdir(args.datapath): os.mkdir(args.datapath)
csvpath = "{}/{}_{}.csv".format(args.datapath, args.pair, args.interval)
data.to_csv(csvpath, index = False)
print("File has been downloaded on \"{}\"".format(csvpath))
