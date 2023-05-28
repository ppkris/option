import numpy as np

# generate some sample data

import random

# Generate a list of 10 random integers between 1 and 100
sample_data = [random.randint(1, 100) for _ in range(10)]

print(sample_data)

# some new code
def cal_profit_loss_random(opt_st_pr, opt_cost, opt_num, opt_curr_pr):
    pro_los = opt_curr_pr * opt_num - opt_cost * opt_num
    print("The profit or loss is", pro_los)

