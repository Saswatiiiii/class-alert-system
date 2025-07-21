from twilio.rest import Client
import datetime

# Your Twilio Account SID and Auth Token
account_sid = 'AC693df6b69b4df12e77915baa1fc7f844'
auth_token = '646d14be89f440a77bd2ccb3ec5b5567'
client = Client(account_sid, auth_token)

# Array of class routines with their respective timings and students' phone numbers
class_routine = [
    {"day": "Sunday", "classes": [
        {"name": "Yoga", "time": ":10:00","teacher": "S.K.H", "students": ["+919382298424", "+918777685356"]},
    ]},
    
    {"day": "Monday", "classes": [
        {"name": "Database Management System", "time": "10:30","teacher": "S.S", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
        {"name": "Computer Network", "time": "13:50","teacher": "S.D", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
        {"name": "Java", "time": "14:50","teacher": "A.T", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
    ]},
    {"day": "Tuesday", "classes": [
        {"name": "Operating System", "time": "11:30","teacher": "P.G.R", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
        {"name": "Java", "time": "13:50","teacher": "A.T", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","++91 98316 79648","+91 84363 03370","+91 93828 72368"]},
        {"name": "Database Lab", "time": "14:50","teacher": "S.S", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
    ]},
    {"day": "Wednesday", "classes": [
        {"name": "Java", "time": "11:30","teacher": "A.T", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
        {"name": "Operating System", "time": "13:50","teacher": "P.G.R", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
        {"name": "Computer Network Lab", "time": "14:50","teacher": "S.D", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
    ]},
    {"day": "Thursday", "classes": [
        {"name": "Computer Network", "time": "11:30","teacher": "S.D", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
        {"name": "Software Engineering", "time": "13:30","teacher": "S.S", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
        {"name": "Minor Project", "time": "14:50","teacher": "S.S", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
    ]},
    {"day": "Friday", "classes": [
        {"name": "Minor Project", "time": "10:30","teacher": "S.S", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
        {"name": "Software Engineering", "time": "12:30","teacher": "S.S", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
        {"name": "Operating System Lab", "time": "14:50","teacher": "P.G.R", "students": ["+919382298424", "+918777685356","+917908225650","+918391851186","+916294275658","+91 75848 26317","+91 79082 40579","+91 62961 24057","+91 98316 79648","+91 84363 03370","+91 93828 72368"]},
    ]}
    # Add more days and classes as needed
]

# Function to send reminder for each class to all students
def send_reminder_to_all(class_name, class_time, teacher, students):
    message = f"Don't forget today your {class_name} class by {teacher} at {class_time}!"  

    # Send message to each student using Twilio
    for student in students:
        client.messages.create(
            to=student,
            from_="+19497102252",
            body=message
        )
    print(f"Reminder sent for {class_name} to all students")

# Main function to iterate through class routines and send reminders to all students
def main():
    # Get current day
    current_day = datetime.datetime.now().strftime('%A')
    
    # Find routine for the current day
    for day_info in class_routine:
        if day_info["day"] == current_day:
            classes_today = day_info["classes"]
            # Send reminders for each class today
            for class_info in classes_today:
                class_name = class_info["name"]
                class_time = class_info["time"]
                teacher = class_info["teacher"]
                students = class_info["students"]
                send_reminder_to_all(class_name, class_time, teacher, students)
                
            break

if __name__ == "__main__":
    main()