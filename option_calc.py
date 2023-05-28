
import numpy as np

# stock value: stock
# annual cost: cost
# average buy in price: buy_pr
# average sell out price: sell_pr

def income(stock=1000000, percent =0.03, buy_pr= 20, sell_pr = 400):
    cost = stock * percent
    income_val = cost/12/buy_pr * sell_pr - cost
    return income_val

sell_pr = np.arange(400,1000,step=50)
buy_pr = np.arange(10,50,step=5)
# for i in buy_pr:
#     income_val = income(buy_pr= i)
#     print(income_val)

# for i in sell_pr:
#     income_val = income(sell_pr=i)
#     print(income_val)

income_val = income(stock=400000, percent=0.02, buy_pr=30, sell_pr= 600)

print(income_val)