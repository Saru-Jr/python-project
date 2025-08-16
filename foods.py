class food:
    def __init__(food, name, calories, vitamineA, vitamineC, cost):
        food.name = name
        food.calories = calories
        food.vitamineA = vitamineA
        food.vitamineC = vitamineC
        food.cost = cost

    def get_nutrition_info(food):
        return f"name: {food.name}, Calories: {food.calories}, Vitamine A: {food.vitamineA}%, Vitamine C: {food.vitamineC}%"

    def get_cost_info(food):
        return f"Cost: ${food.cost}"
    
name = input("Enter food name: ")
calories = int(input("Enter calories: "))
vitamineA = int(input("Enter Vitamine A (%): "))
vitamineC = int(input("Enter Vitamine C (%): "))
cost = float(input("Enter cost: $"))

food_item = food(name, calories, vitamineA, vitamineC, cost)

print(food_item.get_nutrition_info())
print(food_item.get_cost_info())