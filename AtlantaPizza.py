# Atlantapizza.py - a simple pizza cost colculator

# Ask the person how many pizzas they want, get the number with eval()
number_of_pizzas = eval(input("How many pizzas do you want? "))

# Ask for the menu cost of each pizza
cost_per_pizza = eval(input("How much does each pizza cost? "))

# Calculate the total cost of the pizzas as our subtotal
subtotal = number_of_pizzas * cost_per_pizza   #不含税的披萨总价

# Calculate the total cost of the pizzas as our subtotal
tax_rate = 0.08   # Store 8% as the decimal value 0.08
sales_tas = subtotal * tax_rate   #税费

# Add the sales tas to the subtotal for the final total
total = subtotal + sales_tas  #总价是披萨总价+税费

# Show the user the total amount due, including tax
print("The total cost is $",total)
print("This includes $", subtotal, "for the pizza and")
print("$", sales_tas, "in sales tax.")

