
'''
期权卖出的策略研究
计算期权价格的代码

变量：
option 名称 based on strike price：opt_st_pr
option 买入价格: opt_cost
option 买入数量: opt_num
当前option价格: opt_curr_pr
收益：pro_los

收益等于期权当前价格*期权数量 - 期权成本*期权数量

产生一个随机数，来判断涨跌

'''

opt_st_pr = "AAPL 150 Call"
opt_cost = 2.50
opt_num = 10
opt_curr_pr = 3.00

def generate_demo_code():
    # Define some variables
    name = "John"
    age = 30
    city = "New York"

    # Print out a message using the variables
    print("My name is", name, "and I am", age, "years old. I live in", city)

    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Use a for loop to print out each number in the list
    for number in numbers:
        print(number)

    # Define a dictionary of information about a person
    person = {"name": "Jane", "age": 25, "city": "San Francisco"}

    # Print out the person's name and age
    print(person["name"], "is", person["age"], "years old")

    # Define a function that takes two arguments and returns their sum
    def add_numbers(x, y):
        return x + y

    # Call the function and print out the result
    result = add_numbers(3, 5)
    print("The sum of 3 and 5 is", result)

# generate_demo_code()
def cal_profit_loss(opt_st_pr, opt_cost, opt_num, opt_curr_pr):
    pro_los = opt_curr_pr * opt_num - opt_cost * opt_num
    print("The profit or loss is", pro_los)

# cal_profit_loss(opt_st_pr, opt_cost, opt_num, opt_curr_pr)
def cal_profit_loss_random(opt_st_pr, opt_cost, opt_num, opt_curr_pr):
    import random
    pro_los = opt_curr_pr * opt_num - opt_cost * opt_num
    print("The profit or loss is", pro_los)
    if random.random() < 0.5:
        print("The option price is going down")
    else:
        print("The option price is going up")