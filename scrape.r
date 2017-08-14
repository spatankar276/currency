

json_file <- "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD"

coinabv <- c("BTC","ETH","XRP","BCH","MIOTA","LTC","NEO","XEM","DASH","ETC","XMR","BCC","STRAT","WAVES","ZEC","BTS","STEEM","LSK")

i = 1
while(TRUE){
  if (i > 29){

  break          

  }
   
  coinabv[2]        
  data <- RJSONIO::fromJSON(json_file)

  currency <- c('Time', 'BTC', 'USD', 'Current')
  df = data.frame(data)

  btc <- df[1,1]
  usd <- df[2,1]
  price <- df[2,1]/df[1,1]

  x <- c(btc, usd, price)

  names(x) <- c('BTC', 'USD', 'Price')

  dog<- Sys.time()



  x[["Time"]] <- c(Sys.time())
    

  print(x)
  Sys.sleep(time = 5) #Time in seconds

  i = i + 1
}


