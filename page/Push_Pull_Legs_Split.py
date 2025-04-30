import streamlit as st

# Sidebar Input
st.sidebar.header("User Input")
activity_level = st.sidebar.selectbox(
    "Select your Activity Level:",
    ["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"]
)

# Push-Pull-Legs Split
st.title("Push-Pull-Legs Split Workout Plan")
st.subheader("Personalized Workout Plan")

# Explanation of Push-Pull-Legs
st.markdown("""
The **Push-Pull-Legs (PPL)** split is one of the most effective workout schedules for building strength and muscle mass. It is based on focusing on different muscle groups:
- **Push**: Exercises that work the chest, shoulders, and triceps.
- **Pull**: Exercises that work the back and biceps.
- **Legs**: Exercises that target the legs and lower body.

This plan is split into a 3-day routine (Push, Pull, Legs), with rest days in between to allow for muscle recovery.
""")

# Define exercises for each workout type, with alternatives, reps, and muscles
ppl_split = {
    "Push": [
        {"exercise": "Bench Press (Barbell or Dumbbell)", "reps": "3-4 sets of 8-12 reps", 
         "how_to": "Lie flat on a bench, grip the barbell slightly wider than shoulder-width, lower it to your chest, then press it back up.", 
         "muscles": "Chest, Shoulders, Triceps"},
        {"exercise": "Overhead Press", "reps": "3-4 sets of 8-10 reps", 
         "how_to": "Stand with a barbell at shoulder height, press it overhead until your arms are fully extended.", 
         "muscles": "Shoulders, Triceps"},
        {"exercise": "Push-ups", "reps": "3 sets of 15-20 reps", 
         "how_to": "Place hands slightly wider than shoulder-width apart on the floor, lower your body until your chest almost touches the ground, then push back up.", 
         "muscles": "Chest, Shoulders, Triceps"},
        {"exercise": "Tricep Dips", "reps": "3-4 sets of 8-12 reps", 
         "how_to": "Use parallel bars, lower your body by bending your elbows, then press back up to the starting position.", 
         "muscles": "Triceps, Shoulders"},
        {"exercise": "Incline Bench Press", "reps": "3-4 sets of 8-12 reps", 
         "how_to": "Set the bench to an inclined angle (30-45 degrees), press the barbell up and down.", 
         "muscles": "Upper Chest, Shoulders, Triceps"},
        {"exercise": "Dumbbell Chest Fly", "reps": "3-4 sets of 10-12 reps", 
         "how_to": "Lie on a flat bench, hold a dumbbell in each hand, lower them outward, then bring them back together.", 
         "muscles": "Chest, Shoulders"},
        {"exercise": "Cable Chest Press", "reps": "3-4 sets of 8-12 reps", 
         "how_to": "Use a cable machine with the handles at chest level, press the handles forward while keeping your elbows bent.", 
         "muscles": "Chest, Triceps"}
    ],
    "Pull": [
        {"exercise": "Pull-ups", "reps": "3-4 sets of 6-10 reps", 
         "how_to": "Grip the pull-up bar with palms facing away, pull your body up until your chin is above the bar, then lower back down.", 
         "muscles": "Back, Biceps"},
        {"exercise": "Lat Pulldowns", "reps": "3-4 sets of 8-12 reps", 
         "how_to": "Sit at the lat pulldown machine, grip the bar wider than shoulder-width, pull the bar down towards your chest, then slowly release.", 
         "muscles": "Back, Biceps"},
        {"exercise": "Bent-over Rows", "reps": "3-4 sets of 8-12 reps", 
         "how_to": "Hold a barbell or dumbbells with a bent-over posture, pull the weight towards your torso, then lower back down.", 
         "muscles": "Back, Biceps"},
        {"exercise": "Bicep Curls", "reps": "3-4 sets of 10-15 reps", 
         "how_to": "Stand with a dumbbell in each hand, curl the weights up towards your shoulders, then lower them back down.", 
         "muscles": "Biceps"},
        {"exercise": "Single-arm Dumbbell Row", "reps": "3-4 sets of 8-12 reps", 
         "how_to": "Place one knee on a bench, hold a dumbbell with one arm, pull it towards your hip, then lower it back down.", 
         "muscles": "Back, Biceps"},
        {"exercise": "T-Bar Row", "reps": "3-4 sets of 8-12 reps", 
         "how_to": "Stand in front of a T-bar row machine, pull the barbell towards your chest, then lower it slowly.", 
         "muscles": "Back, Biceps"},
        {"exercise": "Face Pulls", "reps": "3-4 sets of 12-15 reps", 
         "how_to": "Use a rope attachment on a cable machine at face height, pull the rope towards your face, then return.", 
         "muscles": "Upper Back, Shoulders"}
    ],
    "Legs": [
        {"exercise": "Squats (Barbell or Bodyweight)", "reps": "3-4 sets of 8-12 reps", 
         "how_to": "Stand with feet shoulder-width apart, squat down as if sitting in a chair, keeping your chest up, then stand back up.", 
         "muscles": "Quads, Hamstrings, Glutes"},
        {"exercise": "Lunges", "reps": "3-4 sets of 10-12 reps per leg", 
         "how_to": "Step forward with one leg, lower your hips until both knees are bent at 90 degrees, then return to the starting position.", 
         "muscles": "Quads, Hamstrings, Glutes"},
        {"exercise": "Deadlifts", "reps": "3-4 sets of 6-10 reps", 
         "how_to": "Stand with your feet shoulder-width apart, grip the barbell, keep your back flat as you lift the barbell, then lower it back down.", 
         "muscles": "Hamstrings, Glutes, Lower Back"},
        {"exercise": "Leg Press", "reps": "3-4 sets of 8-12 reps", 
         "how_to": "Sit on the leg press machine, place your feet on the platform, lower the weight by bending your knees, then press it back up.", 
         "muscles": "Quads, Hamstrings, Glutes"},
        {"exercise": "Bulgarian Split Squats", "reps": "3 sets of 8-12 reps per leg", 
         "how_to": "Place one foot on a bench behind you, lower your body down, keeping your front knee at 90 degrees, then push back up.", 
         "muscles": "Quads, Hamstrings, Glutes"},
        {"exercise": "Romanian Deadlifts", "reps": "3-4 sets of 8-12 reps", 
         "how_to": "Stand with a barbell, keep your back straight as you lower the bar down along your legs, then return to standing.", 
         "muscles": "Hamstrings, Glutes"},
        {"exercise": "Leg Curls (Machine)", "reps": "3-4 sets of 10-12 reps", 
         "how_to": "Lie on a leg curl machine, curl your legs towards your glutes, then slowly return to the start position.", 
         "muscles": "Hamstrings"}
    ]
}

# Define weekly workout schedule based on activity level
split_schedule = []
if activity_level == "Sedentary":
    split_schedule = ["Push", "Pull", "Rest", "Rest", "Rest", "Rest", "Rest"]
elif activity_level == "Lightly active":
    split_schedule = ["Push", "Rest", "Pull", "Rest", "Legs", "Rest", "Rest"]
elif activity_level == "Moderately active":
    split_schedule = ["Push", "Pull", "Legs", "Rest", "Push", "Rest", "Rest"]
elif activity_level == "Very active":
    split_schedule = ["Push", "Pull", "Legs", "Push", "Pull", "Rest", "Rest"]
elif activity_level == "Extra active":
    split_schedule = ["Push", "Pull", "Legs", "Push", "Pull", "Legs", "Rest"]

# Display the workout schedule
st.write("**Your Weekly Workout Schedule:**")
st.write("Based on your activity level, here is your personalized Push-Pull-Legs workout schedule:")

# Display weekly schedule with exercise details
for day, workout in zip(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    split_schedule
):
    st.write(f"- **{day}:** {workout}")
    if workout in ppl_split:
        for exercise in ppl_split[workout]:
            st.write(f"  - **Exercise**: {exercise['exercise']}")
            st.write(f"  - **Reps**: {exercise['reps']}")
            st.write(f"  - **How to perform**: {exercise['how_to']}")
            st.write(f"  - **Muscles worked**: {exercise['muscles']}")
            st.write("---")

st.markdown("""
### Tips for a Successful Workout Week:
- **Rest Days**: Ensure that you get enough rest to help your muscles recover.
- **Progressive Overload**: Increase weights or reps each week for continuous improvement.
- **Warm-up and Cool-down**: Never skip warm-ups and cool-downs to avoid injuries.
""")

st.markdown("---")
st.write("Created with ❤️ using Streamlit. Stay fit and healthy!")

def main():
    # your code...

if __name__ == "__main__":
    main()

