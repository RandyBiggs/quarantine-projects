# Lol skipped a day woops
buy_price = int(input("What was the price when you purchased turnips\n"))
sell_price = int(input("What was the price when you sold turnips?\n"))
quantity = int(input("How many turnips did you buy?\n"))
profit = (sell_price - buy_price) * quantity
print("Profit: {} Bells".format(profit))