import streamlit as st
import base64

# Function to load and encode the local image
def set_background(image_path):
    # Encode the image to base64
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    # Inject CSS with the encoded image
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    /* Change text color to black */
    .stMarkdown, .stTitle, .stSubheader, .stText, .stHeader {{
        color: black;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)




# Data for anabolic substances
def get_anabolic_info():
    return [
        {
            "Name": "Testosterone",
            "Use": "Increases muscle mass and strength",
            "Dose": "100-200 mg per week (medically supervised)",
            "Pros": [
                "Promotes muscle growth",
                "Enhances recovery",
                "Improves energy levels"
            ],
            "Cons": [
                "Can cause acne",
                "Risk of liver damage",
                "Potential heart issues",
                "Hormonal imbalance on misuse"
            ]
        },
        {
            "Name": "Anadrol (Oxymetholone)",
            "Use": "Increases red blood cell production and muscle mass",
            "Dose": "50-100 mg per day (short cycles under supervision)",
            "Pros": [
                "Rapid weight gain",
                "Enhanced strength",
                "Increased endurance"
            ],
            "Cons": [
                "Severe liver toxicity",
                "Water retention",
                "High blood pressure",
                "Hormonal suppression"
            ]
        },
        {
            "Name": "Dianabol (Methandrostenolone)",
            "Use": "Boosts protein synthesis and muscle growth",
            "Dose": "15-30 mg per day (short-term use)",
            "Pros": [
                "Quick muscle gains",
                "Increased strength",
                "Improved performance"
            ],
            "Cons": [
                "Liver stress",
                "Gynecomastia",
                "High blood pressure",
                "Mood swings"
            ]
        },
        {
            "Name": "Deca-Durabolin (Nandrolone)",
            "Use": "Promotes muscle growth and joint healing",
            "Dose": "200-400 mg per week (medically supervised)",
            "Pros": [
                "Improved recovery",
                "Joint support",
                "Sustainable muscle growth"
            ],
            "Cons": [
                "Sexual dysfunction",
                "Long detection time in drug tests",
                "Hormonal suppression",
                "Potential cardiovascular risks"
            ]
        }
    ]

# Main function for Streamlit page
def main():
    set_background(r"C:\Users\Sarthak tale\Desktop\sarthak\healthandfitness\27c4d50b94f6e88d3fce6c6bb01901f4 (1).jpg")  # Absolute path
    st.title("Bodybuilding Enhancer AI Advisor")

    st.write(
        "This tool provides information about anabolic substances, including their suggested use, dose, potential benefits, and risks. Always consult a medical professional before considering such substances."
    )

    # Get anabolic data
    anabolic_data = get_anabolic_info()

    # User input
    st.sidebar.header("Choose an Anabolic Substance")
    substances = [data["Name"] for data in anabolic_data]
    selected_substance = st.sidebar.selectbox("Select a substance", substances)

    # Display selected substance info
    substance_info = next((item for item in anabolic_data if item["Name"] == selected_substance), None)

    if substance_info:
        st.subheader(substance_info["Name"])
        st.write(f"**Use:** {substance_info['Use']}")
        st.write(f"**Dose:** {substance_info['Dose']}")

        st.write("**Pros:**")
        for pro in substance_info["Pros"]:
            st.write(f"- {pro}")

        st.write("**Cons:**")
        for con in substance_info["Cons"]:
            st.write(f"- {con}")

    st.warning("This information is for educational purposes only and not a substitute for professional advice. Misuse of anabolic substances can have serious health consequences.")

if __name__ == "__main__":
    main()
