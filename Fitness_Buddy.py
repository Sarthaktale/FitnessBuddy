import streamlit as st
import runpy
import base64
import os

# Function to load and encode the local image

def set_background(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        page_bg_img = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .stMarkdown, .stTitle, .stSubheader, .stText, .stHeader {{
            color: black;
        }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)

# Main app with navigation

def main():
    # Set your background image (update the path if needed)
    set_background("pexels-olly-868704.jpg")

    st.sidebar.title("Fitness Buddy")
    st.sidebar.subheader("Navigation")
    pages = {
        "Home": None,
        "BMI Calculator": "BMI_Calculator.py",
        "Push-Pull-Legs Split": "Push_Pull_Legs_Split.py",
        "Diet Planner": "Diet_Planner.py",
        "Anabolics Info": "anabolics.py",
        "Enhanced Guide": "Enhance_pro.py"
    }

    choice = st.sidebar.radio("Go to", list(pages.keys()))

    if choice == "Home":
        st.title("Fitness Buddy")
        st.subheader("Your Virtual Fitness Assistant")
        st.markdown("""
        Welcome to **Fitness Buddy**, your personal fitness companion.  
        Use the navigation menu on the left to explore:
        - **BMI Calculator**: Check your Body Mass Index.
        - **Push-Pull-Legs Split**: Get a personalized workout plan.
        - **Diet Planner**: Create a meal plan based on your BMI and goals.
        - **Anabolics Info**: Learn about different anabolic substances.
        - **Enhanced Guide**: Read a comprehensive bodybuilding guide.
        """)
        st.markdown("---")
        st.write("Select an option from the sidebar to get started.")
    else:
        script_path = pages[choice]
        if script_path and os.path.exists(script_path):
            runpy.run_path(script_path, run_name="__main__")
        else:
            st.error(f"Unable to find page: {choice}")

if __name__ == "__main__":
    main()
