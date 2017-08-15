import urllib.request, urllib.parse, urllib.error
import json
import requests
import time
import pandas as pd 
import numpy as np


coinlist = ["BTC", "ETH", "XRP","BCH","MIOTA"]	#"LTC",	"XEM",	"NEO",	"DASH",	"ETC",	"QTUM",	"XMR",	"BCC",	"OMG",	"STRAT",	"WAVES",	"EOS",	"PAY",	"ZEC",	"BTS",	"USDT",	"STEEM",	"BCN",	"LSK",	"ICN",	"VERI",	"REP",	"GNT",	"SC",	"SNT",	"CVC",	"PPT",	"XLM",	"GNO",	"DOGE",	"ARK",	"BAT",	"BTM",	"GBYTE",	"MAID",	"FCT",	"DCR",	"DGD",	"MCAP",	"ARDR",	"GAME",	"MTL",	"DGB",	"KMD",	"ICO",	"BNB",	"NXT",	"PIVX",	"BNT",	"STORJ",	"LKK",	"FUN",	"GAS",	"MGO",	"SNGLS",	"NXS",	"DNT",	"ETP",	"ANT",	"PART",	"BTCD",	"EDG",	"XAS",	"DCT",	"PLR",	"1ST",	"SYS",	"CFI",	"SAFEX",	"XEL",	"RLC",	"BLOCK",	"WINGS",	"UBQ",	"BQX",	"STX",	"MLN",	"LEO",	"ROUND",	"NMR",	"PPC",	"XRL",	"EMC",	"PPY",	"XVG",	"RDD",	"DICE",	"NLC2",	"LUN",	"IOC",	"BDL",	"MYST",	"ADT",	"XCP",	"MCO",	"ION",	"XZC",	"VSL",	"FRST",	"POT",	"NLG",	"HMQ",	"TAAS",	"VIA",	"EB3",	"LBC",	"FAIR",	"NMC","TKN"]
urla = 'https://min-api.cryptocompare.com/data/histominute?fsym='
urlb = '&tsym=USD&limit=60&aggregate=3&e=CCCAGG'

n = 0
#time
t = []
#close
close = []
#high
high = []
#low
low = []
#open
opener = []
#volumefrom
volumefrom = []
#volumeto
volumeto = []
d = {'Time': pd.Series(t),
'Close': pd.Series(close),
'High': pd.Series(high),
'Low': pd.Series(low),
'Open': pd.Series(opener),
'Volume From': pd.Series(volumefrom),
'Volume To': pd.Series(volumeto),
'Name': coinlist[n]}

df = pd.DataFrame(d)


while (n < len(coinlist)):

	url = urla + coinlist[n] + urlb

	uh = urllib.request.urlopen(url)

	data = uh.read().decode('utf8', 'ignore')
	js = json.loads(data)



	for a in js['Data']:
		t.append(a['time'])

	for b in js['Data']:
		close.append(b['close'])

	for c in js['Data']:
		high.append(c['high'])

	for d in js['Data']:
		low.append(d['low'])

	for e in js['Data']:
		opener.append(e['open'])

	for f in js['Data']:
		volumefrom.append(f['volumefrom'])

	for g in js['Data']:
		volumeto.append(g['volumeto'])

	apple = {'Time': pd.Series(t),
	'Close': pd.Series(close),
	'High': pd.Series(high),
	'Low': pd.Series(low),
	'Open': pd.Series(opener),
	'Volume From': pd.Series(volumefrom),
	'Volume To': pd.Series(volumeto),
	'Name': coinlist[n]}

	dfb = pd.DataFrame(apple)
	df.append(dfb)


	n = n + 1
	time.sleep(1)


	

print(df)


#{"time":1502810640,"close":3972.01,"high":3977.26,"low":3967.3,"open":3967.3,"volumefrom":276.13,"volumeto":1098290.25},

