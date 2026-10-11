"""
CHALLENGE 1.4 — Receipt Formatter
Topic: float formatting with f-strings (Day 2)

TASK
----
Ask for an item name, a price per item, and a quantity.
Print a receipt line where the total ALWAYS shows exactly
2 decimal places.

RULES
-----
1. 7.5 is wrong, 7.50 is right.
2. The fix is an f-string "format spec": f'{total:.2f}'
   This syntax is new to you — this challenge exists so you
   learn it. Research what the .2f means and leave a one-line
   comment in your code explaining it in your own words.

SAMPLE RUN
----------
Item name: coffee
Price per item: 2.5
Quantity: 3
------------------------------
coffee x3 ............ EUR 7.50
------------------------------

AFTER YOU FINISH
----------------
Look at your day-2 tip calculator: what does it print when the
per-person share works out to exactly 33.1? Would this fix help?
"""

# --- write your code below this line ---

#.2f in an f-string means to format the number as a floating-point number with 2 digits after the decimal point.

# Ask item details from the user
item_name = input("Item name: ")
price_per_item = float(input("Price per item: "))
quantity = int(input("Quantity: "))

# Calculate the total price
total_price = price_per_item * quantity

# Print the receipt with formatted total price
print (f'---------- \nItem name: {item_name}\nPrice per item: {price_per_item:.2f}\nQuantity: {quantity}\nTotal price: {total_price:.2f}')