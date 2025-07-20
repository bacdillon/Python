# Core Pkgs
import streamlit as st

# Utils
import logging

# Save to File
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("%(levelname)s %(asctime)s.%(msecs)03d - %(message)s")

# File
file_handler = logging.FileHandler('activity.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def main():
	st.title("BMI Calculator App")
	st.text("Check your Body Mass Index and understand your health category.")

	# Updated Menu Options
	menu = ["BMI Calculator", "Health Tips", "Activity Log", "About"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice == "BMI Calculator":
		st.subheader("BMI Calculator")
		logger.info("Visited BMI Calculator")

		# You could insert BMI input and calculation logic here
		# Example:
		# weight = st.number_input("Enter weight (kg)")
		# height = st.number_input("Enter height (cm)")
		# if st.button("Calculate BMI"):
		#     bmi = weight / ((height / 100) ** 2)
		#     st.write(f"Your BMI is {bmi:.2f}")

	elif choice == "Health Tips":
		st.subheader("General Health Tips")
		logger.info("Visited Health Tips")

	elif choice == "Activity Log":
		st.subheader("App Activity Log")
		logger.info("Visited Activity Log")
		with open("activity.log", "r") as log_file:
			logs = log_file.read()
			st.text_area("Logs", logs, height=300)

	else:
		st.subheader("About This App")
		logger.info("Visited About Section")
		st.markdown("This app helps you calculate your Body Mass Index (BMI) and provides general wellness tips.")

if __name__ == '__main__':
	main()
