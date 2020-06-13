# shopping_cart.py

import datetime as dt
tax_rate = 0.0875 #NY Tax Rate = 8.75%

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

checkout_time = dt.datetime.now()
subtotal_price = 0
purchase_ids = []

# User Inputs
while True:
    pick_item = input("Please input a product indentifier, or DONE if there are no more items: ") # output: string
    if pick_item == "DONE":
        break
    else:
        try:
            match_items = [i for i in products if str(i["id"]) == str(pick_item)] #make sure we are comparing 2 strings
            match_item = match_items[0] #Line above outputs a list, but we only want the first item of the list
            #total_price = total_price + match_item["price"]
            #print("PICKED ITEM: " + match_item["name"] + " " + str(match_item["price"]))
            purchase_ids.append(pick_item)
        except IndexError as e: #to address the IndexError for an out of range input
            print("INVALID PRODUCT IDENTIFIER. PLEASE TRY AGAIN...OR IF THERE ARE NO MORE ITEM, PLEASE ENTER 'DONE'")
            
   
   
    

# Outputs

#print(purchase_ids)
print("---------------------------------")
print("YUMMY IN MY TUMMY MARKET")
print("WWW.YUM-IN-TUM.COM")
print("---------------------------------")
print("CHECKOUT AT: " + checkout_time.strftime("%Y-%m-%d %I:%M %p")) # datetime formatting, see: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print("---------------------------------")



print("SELECTED PRODUCTS:")
for pick_item in purchase_ids:
    match_items = [i for i in products if str(i["id"]) == str(pick_item)] #make sure we are comparing 2 strings
    match_item = match_items[0] #Line above outputs a list, but we only want the first item of the list
    subtotal_price = subtotal_price + match_item["price"]
    print("PICKED ITEM: " + match_item["name"] + " (" + to_usd(match_item["price"]) + ")")

tax = subtotal_price * tax_rate
total_price = subtotal_price + tax

print("---------------------------------")
print("SUBTOTAL: " + to_usd(subtotal_price))
print("TAX: " + to_usd(tax))
print("TOTAL: " + to_usd(total_price))
print("---------------------------------")
print("THANKS FOR SHOPPING WITH US, SEE YOU AGAIN SOON!")
print("---------------------------------")


