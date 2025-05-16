
# shopping list note
planned_to_buy = {
    "food":{"sugar","eggs","meat","milk"},
    "clothes":{"Skirt","T-shirt","Trousers","Coat"},
    "drink":{"wine","beer","coke"}
}

all_in_one =set( planned_to_buy['food'] | planned_to_buy["clothes"] | planned_to_buy["drink"])
print("")
print("Items you planned to buy:")
for item in all_in_one:
    print(item)
print("")

items_you_already_bought = input("Enter Items you bought and separate by comma:")
items_you_already_bought_lists = set(items_you_already_bought.split(","))
remaining_items= all_in_one - items_you_already_bought_lists
extra_items = items_you_already_bought_lists - all_in_one

if items_you_already_bought_lists:
    print("Items You have already bought:")
    for item in items_you_already_bought_lists:
        print(item)   
    print("")

if remaining_items:
    print("Remaining Items:")
    for value in remaining_items:
        print(value)
    print("")

if extra_items:
    print ("Extra Items You bought:")
    for value in extra_items:
        print(value)
