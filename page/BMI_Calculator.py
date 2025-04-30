import streamlit as st

# Sidebar Input
st.sidebar.header("User Input")
name = st.sidebar.text_input("Enter your name:", "")
weight = st.sidebar.number_input("Enter your weight (kg):", min_value=20.0, max_value=200.0, value=70.0)
height = st.sidebar.number_input("Enter your height (cm):", min_value=100.0, max_value=250.0, value=170.0)

# BMI Calculation
def calculate_bmi(weight, height):
    if height > 0:
        height_m = height / 100
        return round(weight / (height_m ** 2), 2)
    return None

st.title("BMI Calculator")
st.subheader("Calculate Your Body Mass Index")

if weight and height:
    bmi = calculate_bmi(weight, height)
    if bmi:
        bmi_category = ""
        if bmi < 18.5:
            bmi_category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            bmi_category = "Normal weight"
        elif 25 <= bmi < 29.9:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obesity"

        # Display BMI Result
        st.write(f"Hello {name}, your BMI is **{bmi}**.")
        st.write(f"This is categorized as **{bmi_category}**.")
    else:
        st.error("Invalid height or weight provided. Please check your inputs.")
else:
    st.info("Please enter your weight and height to calculate your BMI.")
    def main():
    # your code...

if __name__ == "__main__":
    main()

