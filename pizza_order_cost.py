print("Small Pizza : $8")
print("Large Pizza : $12")
print("Extra toppings : $1 each")
print("Delivery fee : $2 for fist 5km,additional $1 per mile")

small_pizza = 1
large_pizza = 2

pizza_size = int(input("Enter pizza size :"))

if pizza_size == 1:
    toppings = int(input("Enter amount of toppings :"))    
    if toppings < 1:
        total_cost = 8 
    elif toppings > 1:
        total_cost = 8 + toppings 
        
    distance = int(input("Enter delivery distance :"))
    if distance < 1:
        distance_cost = 0
        final_cost = total_cost + distance_cost
        print(f"Your total order is {final_cost}")
    elif distance <= 5:
        distance_cost = 2 
        final_cost = total_cost + distance_cost
        print(f"Your total order is {final_cost}")
    else :
        distance_cost = 2 + (distance - 5 )
        final_cost = total_cost + distance_cost
        print(f"Your total order is {final_cost}")
elif pizza_size == 2:
    toppings = int(input("Enter amount of toppings :"))    
    if toppings < 1:
        total_cost = 12
    elif toppings > 1:
        total_cost = 12 + toppings 
        
    distance = int(input("Enter delivery distance :"))
    if distance < 1:
        distance_cost = 0
        final_cost = total_cost + distance_cost
        print(f"Your total order is {final_cost}")
    elif distance <= 5:
        distance_cost = 2 
        final_cost = total_cost + distance_cost
        print(f"Your total order is {final_cost}")
    else :
        distance_cost = 2 + (distance - 5 )
        final_cost = total_cost + distance_cost
        print(f"Your total order is {final_cost}")
    
    