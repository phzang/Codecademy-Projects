"""Write a program that asks the user for the weight of their package 
and then tells them which method of shipping is cheapest and how much 
it will cost to ship their package using Sal's Shippers."""

def Sal_Shipping(weight):

	#Permium Ground Shipping is $125.00 reguardless of weight
	premium_ground_charge = 125.00
	
	#Determines ground shipping cost
	#Ground shipping has a flat charge added to the weight cost
	def Ground_Shipping(weight):
		cost = 0
		flat_charge = 20
		
		if (weight <= 2):
			cost = weight * 1.5
		
		elif (weight <= 6):
			cost = weight * 3.00
		
		elif (weight <= 10):
			cost = weight * 4.00
			
		else:
			cost = weight * 4.75
		
		cost += flat_charge
		
		return cost
	
	#print(str(Ground_Shipping(8.4)))
	
	#Determines drone shipping cost
	#Drone shipping does not have a flat charge added to the weight cost
	def Drone_Shipping(weight):
		cost = 0
		
		if (weight <= 2):
			cost = weight * 4.50
		
		elif (weight <= 6):
			cost = weight * 9.00
		
		elif (weight <= 10):
			cost = weight * 12.00
			
		else:
			cost = weight * 14.25
			
		return cost
		
	#print(str(Drone_Shipping(1.5)))
	
	ground_total = Ground_Shipping(weight)
	drone_total = Drone_Shipping(weight)
	
	#If Premium Ground Shipping is the least expensive
	if (ground_total and drone_total) >  premium_ground_charge:
		return "Premium Ground Shipping at $" + str(premium_ground_charge)
		
	#If Drone Shipping is the least expensive
	elif (ground_total > drone_total):
		return "Drone Shipping at $" + str(drone_total)
	
	#Otherwise Ground Shipping is the least expensive
	else:
		return "Ground Shipping at $" + str(ground_total)
		

user_input = input("Thank you for choosing Sals Shipping.  What is the weight of your package? ")

print("The best option for you is " + Sal_Shipping(float(user_input)))
	

	
	
	
	