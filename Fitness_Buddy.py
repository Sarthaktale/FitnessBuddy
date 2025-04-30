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

# Main app
def main():
    # Set your background image (absolute path)
    set_background("pexels-olly-868704.jpg")  
    
    # Title and Description
    st.title("Fitness Buddy")
    st.subheader("Your Virtual Fitness Assistant")
    st.markdown("""
    Welcome to **Fitness Buddy**, your personal fitness companion.  
    Use the navigation menu to explore features:
    - **BMI Calculator**: Check your Body Mass Index.
    - **Push-Pull-Legs Split**: Get a personalized workout plan.
    """)

    st.markdown("---")
    st.write("Navigate to different pages using the sidebar on the left.")

# Run the app
if __name__ == "__main__":
    main()
