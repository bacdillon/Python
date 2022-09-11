
import streamlit as st
import pandas as pd

# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


def main():

	st.title("HRMS")

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password", type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			result = login_user(username,password)
			if result:

				st.success("Logon in as {}".format(username))
				task = st.selectbox("Task",["Profiles","Analytics","Add Post"])
				if task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)

				elif task == "Analytics":
					st.subheader("Analytics")

				elif task== "Add Post":
					st.subheader("Add Post")

			else:
				st.warning("Incorrect Username/Password")

	elif choice == "SignUp":
		st.subheader("Create an Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,new_password)
			st.success("You have successfully create a valid account")
			st.info("Go to Login Menu to login")


if __name__ == '__main__':
	main()