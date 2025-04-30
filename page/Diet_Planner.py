import streamlit as st
import pandas as pd

def calculate_calorie_needs(bmi, activity_level, goal):
    if goal == "Weight Loss":
        calorie_modifier = 0.8
    elif goal == "Weight Gain":
        calorie_modifier = 1.2
    else:  # Maintain weight
        calorie_modifier = 1.0

    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725
    }

    base_calories = 22 * bmi * 10  # Simplistic BMR-based approach
    calories = base_calories * activity_multipliers.get(activity_level, 1.2) * calorie_modifier

    return round(calories)

def generate_meal_plan(calories, diet_preference):
    # Define example meal plans
    meal_plans = {
        "Vegetarian": [
            {"Meal": "Breakfast", "Item": "Oats Upma with Vegetables", "Calories": 250},
            {"Meal": "Lunch", "Item": "Roti, Dal, Paneer Curry, Salad", "Calories": 600},
            {"Meal": "Snack", "Item": "Fruit Salad", "Calories": 150},
            {"Meal": "Dinner", "Item": "Khichdi with Curd", "Calories": 500}
        ],
        "Non-Vegetarian": [
            {"Meal": "Breakfast", "Item": "Egg Bhurji with Multigrain Toast", "Calories": 300},
            {"Meal": "Lunch", "Item": "Chicken Curry, Rice, Salad", "Calories": 700},
            {"Meal": "Snack", "Item": "Boiled Eggs", "Calories": 200},
            {"Meal": "Dinner", "Item": "Grilled Fish with Vegetables", "Calories": 500}
        ],
        "Vegan": [
            {"Meal": "Breakfast", "Item": "Quinoa Porridge with Fruits", "Calories": 250},
            {"Meal": "Lunch", "Item": "Veggie Stir-Fry with Brown Rice", "Calories": 600},
            {"Meal": "Snack", "Item": "Roasted Chickpeas", "Calories": 150},
            {"Meal": "Dinner", "Item": "Vegetable Soup with Whole Wheat Bread", "Calories": 500}
        ]
    }

    # Adjust portion sizes to meet calorie needs
    selected_plan = meal_plans[diet_preference]
    total_plan_calories = sum(meal["Calories"] for meal in selected_plan)
    scale_factor = calories / total_plan_calories

    for meal in selected_plan:
        meal["Calories"] = round(meal["Calories"] * scale_factor)

    return selected_plan

def recommend_supplements(goal, diet_preference):
    supplements = []
    if goal == "Weight Loss":
        supplements.append("Green Tea Extract")
        supplements.append("Protein Powder (if protein intake is low)")
    elif goal == "Weight Gain":
        supplements.append("Mass Gainer")
        supplements.append("Creatine")
    
    if diet_preference in ["Vegetarian", "Vegan"]:
        supplements.append("Vitamin B12")
        supplements.append("Omega-3 (Plant-based for Vegans)")

    return supplements

def add_additional_meals(diet_preference):
    additional_meals = {
        "Vegetarian": [
            {"Meal": "Mid-Morning", "Item": "Sprouts Salad", "Calories": 100},
            {"Meal": "Late Evening", "Item": "Buttermilk", "Calories": 50}
        ],
        "Non-Vegetarian": [
            {"Meal": "Mid-Morning", "Item": "Chicken Soup", "Calories": 120},
            {"Meal": "Late Evening", "Item": "Greek Yogurt", "Calories": 80}
        ],
        "Vegan": [
            {"Meal": "Mid-Morning", "Item": "Smoothie with Almond Milk", "Calories": 150},
            {"Meal": "Late Evening", "Item": "Coconut Water", "Calories": 50}
        ]
    }
    return additional_meals[diet_preference]

def main():
    st.title("Indian Diet Planner and Supplement Recommender")

    # User inputs
    st.sidebar.header("User Inputs")
    goal = st.sidebar.selectbox("Your Goal", ["Weight Loss", "Weight Gain", "Maintain Weight"])
    activity_level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])
    diet_preference = st.sidebar.selectbox("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"])
    bmi = st.sidebar.slider("Your BMI", 15, 40, 22)

    # Calculate calorie needs
    calories = calculate_calorie_needs(bmi, activity_level, goal)
    st.write(f"### Your daily calorie requirement: {calories} kcal")

    # Generate meal plan
    meal_plan = generate_meal_plan(calories, diet_preference)
    st.write("### Your Customized Meal Plan")
    meal_plan_df = pd.DataFrame(meal_plan)
    st.table(meal_plan_df)

    # Add additional meals
    additional_meals = add_additional_meals(diet_preference)
    st.write("### Additional Meals")
    additional_meals_df = pd.DataFrame(additional_meals)
    st.table(additional_meals_df)

    # Recommend supplements
    supplements = recommend_supplements(goal, diet_preference)
    if supplements:
        st.write("### Recommended Supplements")
        for supplement in supplements:
            st.write(f"- {supplement}")

if __name__ == "__main__":
    main()
