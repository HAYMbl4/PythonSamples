import json

NAME = "name"
TRANSFER = "transfer"
EVENTS = "events"
DRINKS = "drinks"
MAIN_MEAL = "mainMeal"

TRANSFER_STATISTIC = "transferStatistic"
EVENTS_STATISTIC = "eventsStatistic"
DRINKS_STATISTIC = "drinksStatistic"
MAIN_MEAL_STATISTIC = "mainMealStatistic"

# with open("D:\Work\PythonSamples\\visitor\\visitors.json", "r") as visitors_file:
with open("visitor/visitors.json", "r") as visitors_file:
    visitors = json.load(visitors_file)

transfer_statistic = {}
events_statistic = {}
drinks_statistic = {}
main_meal_statistic = {}


def put_or_add(dict_of_statistic, key, value):
    if key in dict_of_statistic:
        dict_of_statistic.get(key).append(value)
    else:
        dict_of_statistic[key] = [value]


def process_one_select_item(dict_of_statistic, visitor_info, list_name):
    put_or_add(dict_of_statistic, visitor_info[list_name], visitor_info[NAME])


def process_multi_select_items(dict_of_statistic, visitor_info, list_name):
    for e in visitor_info[list_name]:
        put_or_add(dict_of_statistic, e, visitor_info[NAME])


def add_statistic(dict_of_visitors, key, dict_of_statistic):
    list_for_json = []
    for ks in dict_of_statistic.keys():
        list_for_json.append({"position": ks, "persons": dict_of_statistic.get(ks)})
    dict_of_visitors[key] = list_for_json


for vi in visitors["visitors"]:
    process_one_select_item(transfer_statistic, vi, TRANSFER)
    process_multi_select_items(events_statistic, vi, EVENTS)
    process_multi_select_items(drinks_statistic, vi, DRINKS)
    process_one_select_item(main_meal_statistic, vi, MAIN_MEAL)

# print("transfer  : %s" % transfer_statistic)
# print("events    : %s" % events_statistic)
# print("drinks    : %s" % drinks_statistic)
# print("main meal : %s" % main_meal_statistic)

add_statistic(visitors, TRANSFER_STATISTIC, transfer_statistic)
add_statistic(visitors, EVENTS_STATISTIC, events_statistic)
add_statistic(visitors, DRINKS_STATISTIC, drinks_statistic)
add_statistic(visitors, MAIN_MEAL_STATISTIC, main_meal_statistic)

# print(visitors)

print('Content-Type: application/json\n\n')
print(json.dumps(visitors))
