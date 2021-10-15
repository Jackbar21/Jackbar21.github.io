import ast
from datetime import date

########################### BONDS (10%) ########################################

VBTLX_MONEY = 990
VBTLX_PERCENT = 0.10
# Vanguard Total Bond Market Index Fund Admiral Shares
# Expense Ratio: 0.050%

# ETF Equivalent: BND

########################### STOCKS (90%) #######################################

VTWAX_MONEY = 10050
VTWAX_PERCENT = 0.90
# Vanguard Total World Stock Index Fund Admiral Shares
# Expense Ratio: 0.100%

# ETF Equivalent: VT

################################################################################

MONEY = 0
PERCENT = 1

DISCREPANCY_CONSTANT = 0.01

dict_of_stocks = {'VBTLX': [VBTLX_MONEY, VBTLX_PERCENT],
                  'VTWAX': [VTWAX_MONEY, VTWAX_PERCENT]}

final_dict = {}
for key in dict_of_stocks:
    final_dict[key] = 0

# This function was copied from a website in order to calculate age
    def calculateAge(birthDate):
        today = date.today()
        age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
        return age

def define_current_total_price(dictionary: dict):
    current_total_price = 0
    for key in dict_of_stocks:
        current_total_price += dict_of_stocks[key][MONEY]
    return current_total_price


current_total_price = define_current_total_price(dict_of_stocks)

dict_current_percentages = {}

def list_current_percentages(dict_of_stocks):
    current_total_price = define_current_total_price(dict_of_stocks)
    for key in dict_of_stocks:
        dict_current_percentages[key] = dict_of_stocks[key][MONEY] / current_total_price
    #
    # If current_total_price was $0 (no investments yet), then the correct
    # coding format for this function would be as follows:
    #
    # current_total_price = define_current_total_price(dict_of_stocks)
    # for key in dict_of_stocks:
    #     if current_total_price != 0:
    #         dict_current_percentages[key] = dict_of_stocks[key][MONEY] / current_total_price
    #     else:
    #         dict_current_percentages[key] = 0

list_current_percentages(dict_of_stocks)

def round_nearest_cent(num: int):
    round(num, 2)
    '{:.2f}'.format(num)


def dict_of_discrepancy(dict_of_stocks: dict):
    dict_of_discrepancies = {}
    for key in dict_of_stocks:
        dict_of_discrepancies[key] = dict_of_stocks[key][PERCENT] - dict_current_percentages[key]
    return dict_of_discrepancies
    # ONLY FOCUS ON POSITIVE VALUES IN DICT.

def find_highest_value(dictionary: dict):
    dirty_list = str(dictionary.values())
    clean_list = ast.literal_eval(dirty_list[12:-1])
    highest_value = max(clean_list)
    return highest_value

def corresponding_key_to_value(dictionary: dict, num: float):
    for key in dictionary:
        if dictionary[key] == num:
            return key

def find_best_investment():
    current_total_price = define_current_total_price(dict_of_stocks)
    invest_money = float(input('How much money would you like to invest today? : $'))
    initial_invest_money = invest_money
    # DISCREPANCY_CONSTANT = float(input('What would you like to use as your Discrepancy Constant today? : '))
    # I commented this out and made DISCREPANCY_CONSTANT a global variable as a float with an assigned value of 0.01
    while invest_money > 0:
        dict_of_discrepancies = dict_of_discrepancy(dict_of_stocks)
        highest_discrepancy = find_highest_value(dict_of_discrepancies)
        highest_discrepancy_stock = corresponding_key_to_value(dict_of_discrepancies, highest_discrepancy)
        invest_money = invest_money - DISCREPANCY_CONSTANT
        dict_of_stocks[highest_discrepancy_stock][MONEY] += DISCREPANCY_CONSTANT
        current_total_price = define_current_total_price(dict_of_stocks)
        list_current_percentages(dict_of_stocks)
        final_dict[highest_discrepancy_stock] += DISCREPANCY_CONSTANT
    print("")
    print("Here's how much you should invest in each Index Fund:")
    PENNY_UNCERTAINTY = 0.00
    for index_fund in final_dict:
        print(str(index_fund) + ": $" + '{:.2f}'.format(final_dict[index_fund]))
        PENNY_UNCERTAINTY += float('{:.2f}'.format((final_dict[index_fund])))
    print("")
    print("Total Final Price: $" + '{:.2f}'.format(current_total_price) + " (this final price is off by: $" + '{:.2f}'.format(abs(PENNY_UNCERTAINTY - initial_invest_money)) + ")")

find_best_investment()