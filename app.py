import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("bg.jpeg")

st.markdown(f"""
<style>
.stApp {{
    background: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)),
                url("data:image/jpeg;base64,{img}");
    background-size: cover;
    background-position: center;
}}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="91 Care Helpdesk", page_icon="🏥")


# Center container
col1, col2, col3 = st.columns([2,3,2])

with col2:
    colA, colB = st.columns([1,3])

    with colA:
        st.image("loginlogo.jpg", width=70)

    with colB:
        st.markdown(
            "<h2 style='margin-top:15px;'>91 Care</h2>",
            unsafe_allow_html=True
        )
# -----------------------------
# Session State
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = "greeting"

if "role" not in st.session_state:
    st.session_state.role = None

# -----------------------------
# ✅ Reusable Back Button (to Main Menu)
# -----------------------------
def back_to_main():
    if st.button("⬅ Back"):
        st.session_state.step = "main"


# -----------------------------
# Greeting Section
# -----------------------------
def greeting():
    st.subheader("Welcome to 91 Care Helpdesk")
    st.write("**Your Role please:**")

    col1, col2, col3 , col4 = st.columns(4)

    with col1:
        if st.button("👨‍⚕️ Doctor"):
            st.session_state.role = "Doctor"
            st.session_state.step = "main"

    with col2:
        if st.button("👩‍⚕️ Nurse"):
            st.session_state.role = "Nurse"
            st.session_state.step = "main"

    with col3:
        if st.button("🧑‍💼 Receptionist"):
            st.session_state.role = "Receptionist"
            st.session_state.step = "main"

    with col4:
        if st.button("🧑‍💼 Admin"):
            st.session_state.role = "Admin"
            st.session_state.step = "main"
# -----------------------------
# ✅ Role-Based Main Menu
# -----------------------------
def main_menu():
    role = st.session_state.role

    # ✅ Back to Role Selection (2nd screen)
    col1, col2 = st.columns([6,1])
    with col2:
        if st.button("🔙"):
            st.session_state.role = None
            st.session_state.step = "greeting"

    st.subheader(f"Hello {role}, How can I help you?")

    # 👨‍⚕️ Doctor View
    if role == "Doctor":
        if st.button("🧾 Download Report"):
            st.session_state.step = "Report"

        if st.button("📅 Availability"):
            st.session_state.step = "Availability"

        if st.button("📅 prescription"):
            st.session_state.step = "prescription"   

        if st.button( " 🧾 vitals"):
            st.session_state.step = "vitals"         
    # 👩‍⚕️ Nurse View
    elif role == "Nurse":
         if st.button("📅 prescription"):
            st.session_state.step = "prescription" 

         if st.button(" 💳 Payment Status"):
            st.session_state.step = "Payment_Status" 

         if st.button(" 🛠️ Check Service"):
            st.session_state.step = "service"

         if st.button( " 🧾 Invoice"):
            st.session_state.step = "invoice"
         if st.button( " 🧾 vitals"):
            st.session_state.step = "vitals"    

    # 🧑‍💼 Receptionist View
    elif role == "Receptionist":
        if st.button("📅 Book Appointment"):
            st.session_state.step = "appointment"

        if st.button("🔢 Token"):
            st.session_state.step = "Token"

        if st.button(" 💳 Payment Status"):
            st.session_state.step = "Payment_Status"

        if st.button( "👨‍⚕️ Doctors list"):
            st.session_state.step = "Doctors_List"

        if st.button ( "⚙️ Edit details"):
            st.session_state.step = "Editing"   

#Admin

    elif role == "Admin":
        if st.button("📊 Data Analysis"):
            st.session_state.step = "Data"

        if st.button("🧾 Download Report"):
            st.session_state.step = "Report"

        if st.button("📅 Availability"):
            st.session_state.step = "Availability"

        if st.button("📅 prescription"):
            st.session_state.step = "prescription"   

        if st.button("📅 Book Appointment"):
            st.session_state.step = "appointment"

        if st.button("🔢 Token"):
            st.session_state.step = "Token"

        if st.button(" 💳 Payment Status"):
            st.session_state.step = "Payment_Status"

        if st.button( "👨‍⚕️ Doctors list"):
            st.session_state.step = "Doctors_List"

        if st.button ( "⚙️ Edit details"):
            st.session_state.step = "Editing"

        if st.button(" 🛠️ Check Service"):
             st.session_state.step = "service" 
        if st.button( " 🧾 Invoice"):
            st.session_state.step = "invoice"
        if st.button( " 🧾 vitals"):
            st.session_state.step = "vitals"              
        

# -----------------------------
# Doctor Features
# -----------------------------

def Report():

    st.markdown("""
### 📥 Steps to Download

🔹 Go to **Dashboard**  
🔹 Click on **Download Report** (top-right)  
🔹 File will download automatically  

""")
    back_to_main()


def Availbilty():

    st.markdown("""
### 📅 Steps to Manage Availability

🔹 Go to **Appointment Page**  
🔹 Click on **Doctor's Time Off** (top-right)  
🔹 Fill in the required details  
🔹 Click **Submit** to save  

""")
    back_to_main()
def prescription():

    st.markdown("""
### 💊 Steps to View Prescription

🔹 Go to **Appointment Page**  
🔹 Search for the **Patient Name**  
🔹 Locate the patient in the list  
🔹 Click on **Prescription** (at the end of the row)  
🔹 View the prescribed details  

""")
    back_to_main()
# -----------------------------
# Nurse Features
# -----------------------------
def service():
    
    
    st.markdown("""
### 📋 Steps to Check Patient Services

🔹 Go to **Patients Page**  
🔹 View the list of patients  
🔹 Click on the **(⋮)** at the end of the row . Select **Check Services**  
🔹 View services for the selected patient  

""")
    
    back_to_main()


def Token():

    st.markdown("""
### 🎟️ Steps to Manage Token

🔹 Go to **Appointment Page**  
🔹 Click on **Token Entry** (top-right)  
🔹 Enter or update the **Token Number**  
🔹 Save the changes .
                                          


""")
    back_to_main()

def invoice():
    

    st.markdown("""
### 🧾 Steps to Raise an Invoice

🔹 Go to *Appointments Page*  
🔹 View the list of appointments  
🔹 Click on **'Raise Invoice'** at the end of the required row  
🔹 The invoice will be displayed  
""")
    back_to_main()



def vitals():
    

    st.markdown("""
### 🧾 Steps to see Vitals

🔹 Go to **Appointments Page**  
🔹 View the list of appointments  
🔹 Click on the **three vertical dots (⋮)** at the end of the row
🔹 Click on **' Vitals'** from the list
🔹 The Vitals will be displayed  

""")    
    back_to_main()
# -----------------------------
# Receptionist Features
# -----------------------------
def appointment():

    st.markdown("""
### 📅 Steps to Book Appointment

🔹 Go to **Appointment Page**  
🔹 Click on **+ Appointment** (top-right)  
🔹 Fill in the **required details**  
🔹 Click on **Submit**  

""")
    back_to_main()
def Token():

    st.markdown("""
### 🎟️ Steps to Manage Token

🔹 Go to **Appointment Page**  
🔹 Click on **Token Entry** (top-right)  
🔹 Enter or update the **Token Number**  
🔹 Save the changes  

""")
    back_to_main()


def Payment_Status():

    st.markdown("""
### 💳 Steps to Check Payment Status

🔹 Go to **Patients Page**  
🔹 Search for the **Patient Name**  
🔹 Select the patient from the list  
🔹 View the **Payment Status**  

""")
    back_to_main()

def doctors_list():

    st.markdown("""
### 👨‍⚕️ Steps to View Doctors List

🔹 Go to **Appointment Page**  
🔹 Click on **Doctor Section** (right side)  
🔹 View the list of **Available Doctors**  

""")
    back_to_main()
def Data():
    st.subheader("📊 Data Analysis")
    st.write("Go to the **Dashboard** to view complete data in a simple and easy-to-understand format.")
    back_to_main()

def Editing():
    st.markdown("""
### ✏️ Steps to Edit Patient Details

🔹 Go to **Appointment Page**  
🔹 Locate the **Patient** in the list  
🔹 Click on the **⋮ (3 vertical dots)** at the end of the row  
🔹 Select **Edit Option**  
🔹 Update the required details and save  

""")
    back_to_main()
# -----------------------------
def emergency():
    st.subheader("🚑 Emergency")
    st.error("Call 108 immediately!")
    back_to_main()

    

# -----------------------------
# Navigation Controller
# -----------------------------
if st.session_state.step == "greeting":
    greeting()

elif st.session_state.step == "main":
    main_menu()

elif st.session_state.step == "Report":
    Report()

elif st.session_state.step == "Availability":
    Availbilty()

elif st.session_state.step == "vitals":
    vitals()

elif st.session_state.step == "Token":
    Token()

elif st.session_state.step == "appointment":
    appointment()

elif st.session_state.step == "Editing":
    Editing()

elif st.session_state.step == "Payment_Status":
    Payment_Status()

elif st.session_state.step == "emergency":
    emergency()

elif st.session_state.step == "prescription":
    prescription()

elif st.session_state.step == "Data":
    Data()    

elif st.session_state.step == "service":
    service()    

elif st.session_state.step == "invoice":
    invoice()
    
        