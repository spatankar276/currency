

urlone <- "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms="
urltwo <- "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms="
u = c("USD")

coinabv <- c("BTC","ETH","XRP","BCH","MIOTA","LTC","NEO","XEM","DASH","ETC","XMR","BCC","STRAT","WAVES","ZEC","BTS","STEEM","LSK")


n = 1
while(TRUE){

  if (n > 20){

  break

  }

  monkeyone <- paste(urlone,coinabv[n])
  monkeytwo <- paste(urltwo,u)

  dataone <- RJSONIO::fromJSON(monkeyone)
  datatwo <- RJSONIO::fromJSON(monkeytwo)

  do = data.frame(dataone)
  dt = data.frame(datatwo)
  
  
  cur <- do[1,1]
  us <- dt[1,1]
  price <- dt[1,1]/do[1,1]

  x <- c(coinabv[n],cur,us,price, Sys.time())
  names(x) <- ('Currency Name','Currency Price','USD','Price','Time')
  x
  n = n + 1
  Sys.sleep(time = 1)


  }

	

  


