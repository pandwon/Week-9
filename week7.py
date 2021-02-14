stocks = {"tsla":883.45,"amd":94.44,"dis":169.56,"pep":141.80,"nflx":561.93,\
    "ko":49.29,"amzn":3326.13,"ebay":59.17,"aal":15.53,"tsn":66.57}

ticker = input("Enter a stock ticker symbol. Type quit to stop: ")
while not ticker == "quit":
    if ticker in stocks:
        print("{}:{}" .format(ticker, stocks[ticker]))
    else:
        print("{} not found" .format(ticker))

    ticker = input("Enter a stock ticker symbol. Type quit to stop: ")        