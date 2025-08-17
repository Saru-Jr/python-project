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
    
    def get_food_caloriestat(food):
        if food.calories < 100:
            return "Low-calorie food"
        elif food.calories < 200:
            return "Medium-calorie food"
        else:
            return "High-calorie food"

    def get_vitamineA_stat(food):
        if food.vitamineA < 10:
            return "Low Vitamine A"
        elif food.vitamineA < 20:
            return "Medium Vitamine A"
        else:
            return "High Vitamine A"

    def get_vitamineC_stat(food):
        if food.vitamineC < 10:
            return "Low Vitamine C"
        elif food.vitamineC < 20:
            return "Medium Vitamine C"
        else:
            return "High Vitamine C"
        
    def get_cost(food):
        if food.cost < 1:
            return "Low-cost food"
        elif food.cost < 5:
            return "Medium-cost food"
        else:
            return "High-cost food"

name = input("Enter food name: ")
calories = int(input("Enter calories: "))
vitamineA = int(input("Enter Vitamine A (%): "))
vitamineC = int(input("Enter Vitamine C (%): "))
cost = float(input("Enter cost: $"))

food_item = food(name, calories, vitamineA, vitamineC, cost)

print(food_item.get_nutrition_info())
print(food_item.get_cost_info())
print()
print(food_item.get_food_caloriestat())
print(food_item.get_vitamineA_stat())
print(food_item.get_vitamineC_stat())
print()
print(food_item.get_cost())
