from yahoo_fin import stock_info as si

# get live price of Apple
print(si.get_live_price("aapl"))
 
# or Amazon
print(si.get_live_price("amzn"))
 
# get quote table back as a data frame
print(si.get_quote_table("aapl", dict_result = False))
 
# or get it back as a dictionary (default)
print(si.get_quote_table("aapl"))
