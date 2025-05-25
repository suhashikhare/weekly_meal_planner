import json
import os

FILENAME = "meal_plan.json"

def load_meal_plan():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    else:
        return {"Monday": {}, "Tuesday": {}, "Wednesday": {}, "Thursday": {}, "Friday": {}, "Saturday": {}, "Sunday": {}}

def save_meal_plan(plan):
    with open(FILENAME, "w") as f:
        json.dump(plan, f, indent=2)

def display_plan(plan):
    print("\nWeekly Meal Plan:")
    for day, info in plan.items():  
        if info:
            print(f"{day}: {info['meal']} (Ingredients: {', '.join(info['ingredients'])})")
        else:
            print(f"{day}: [No meal planned]")

def add_meal(plan):
    day = input("Enter day (e.g., Monday): ").capitalize()
    if day not in plan:
        print("Invalid day!")
        return
    meal = input(f"Enter the meal for {day}: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(",")
    ingredients = [i.strip() for i in ingredients]
    plan[day] = {"meal": meal, "ingredients": ingredients}
    print(f"Meal added for {day}!")

def remove_meal(plan):
    day = input("Enter day to remove meal from: ").capitalize()
    if day in plan and plan[day]:
        plan[day] = {}
        print(f"Meal removed from {day}.")
    else:
        print("No meal found for that day.")

def generate_shopping_list(plan):
    ingredients_set = set()
    for day in plan:
        if plan[day]:
            ingredients_set.update(plan[day]["ingredients"])
    print("\nShopping List:")
    if ingredients_set:
        for item in sorted(ingredients_set):
            print(f"- {item}")
    else:
        print("No meals planned yet.")

def main():
    meal_plan = load_meal_plan()
    while True:
        print("\n--- Plateful Planner ---")
        print("1. View meal plan")
        print("2. Add/Update meal")
        print("3. Remove meal")
        print("4. Generate shopping list")
        print("5. Save and exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            display_plan(meal_plan)
        elif choice == "2":
            add_meal(meal_plan)
        elif choice == "3":
            remove_meal(meal_plan)
        elif choice == "4":
            generate_shopping_list(meal_plan)
        elif choice == "5":
            save_meal_plan(meal_plan)
            print("Meal plan saved. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
