toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print("We sell {} different kinds of pizza!".format(num_pizzas))

pizzas = list(zip(prices,toppings))

print(pizzas)

pizzas.sort()
print(pizzas)

cheapest_pizza = pizzas[0]

priciest_pizza = pizzas[-1]

#print(priciest_pizza)

three_cheapest = pizzas[0:3]

#print(three_cheapest)





