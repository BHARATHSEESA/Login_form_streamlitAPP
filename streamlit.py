import streamlit as st

#Header of the application
st.header("Students Record Management")

#Title of teh application
st.title("Student Management System")

#Subheader of the application
st.subheader("Manage student records with Create, Read, Update, and Delete operations")

#horizontal line
st.markdown("--------------------------------------------------------")

#text method to display information 
st.text("This application allows you to perform CRUD operations on student records using a MySQL database.")


#write method to provide additional details
st.write("hello Bharath")

#Markdown for formatted text
st.markdown("### Features of application:")
st.markdown("** Bold Text**")
st.markdown("*Italic Text*")
st.markdown("-Item 1\n- Item 2")

st.markdown("<h3 style='color:red'>Done Student</h3>",unsafe_allow_html=True)

#caption method to add captions
st.caption("This is a caption for the student management system.")

#code method to display code snippets
st.code("""
def add(a,b):
return a+b 
""",language="python")


#latex
st.latex(r'''
a^2 + b^2 = c^2
''')

#dividermethod to display
st.divider()


#button method to create a button
if st.button("Click Me"):
    st.write("Button clicked")
    
    st.balloons()
else:
    st.write("Button not clicked yet.")
    st.error("Connection error!")

#text input method to get user input
name = st.text_input("Enter your name:")
if name =="":
    st.warning("Name cannot  be empty!")
elif not name.isalpha():
    st.error("Invalid input! Please enter only alphabets (no nubers or symbols).")
else:
    st.success(f"Hello,{name}!")

#text area for multiline input
feedback = st.text_area("Enter your feedback")
st.write(feedback)

#checkbox
if st.checkbox("I agree to the terms and conditions"):
    st.write("Thankyou!")

#radio button
gender = st.radio("Select your gender:", ("Male","Female","Other"))
st.write(f"You selected:{gender}")

#selectbox
country = st.selectbox("Select your country:", ("India","America","Russia","Dubai"))
st.write(f"select country:{country}")

#multiseleect
skills= st.multiselect(
    "Select skills",
    ["python","SQL","ML","Streamlit"]
)
st.write(skills)

#slider
age = st.slider("Select your age:",0, 100, 25)
st.write(f"You are {age}  years old")

#file uploadder method
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write(f"Filename: {uploaded_file.name}")

#form method to create a form
with st.form("my_form"):
    name=st.text_input("name")
    age=st.number_input("age",0,100)
    submit=st.form_submit_button("submit")
if submit:
    st.write(name,age)


#form_submit_button method to create a submit
with st.form("login"):
    user_name = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    login = st.form_submit_button("login")

if login:
    st.success("Login Successful")

#columns method to create columns
col1,col2,col3,col4 = st.columns(4)
with col1:
    st.header("Column 1")
    st.write("This is column1")
with col2:
    st.header("Column 2")
    st.write("This is column2")
with col3:
    st.header("Column 3")
    st.write("This is column3")
with col4:
    st.header("Column 4")
    st.write("This is column4")

st.divider()

#container
container = st.container()
container.write("This is inside the container")
container.button("Click here")

#table
data = {
    'Name': ['Anurag','bharath','rambo','tom'],
    'Age':[35,21,29,20],
    'course':['M.tech','Law','MBBS','b.tech']
}
st.table(data)

st.divider()

#sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")

st.divider()
