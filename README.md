# 📚 Class Alert System using Twilio

A Python-based SMS notification system that sends automated reminders to students and teachers before their scheduled classes. This tool helps improve punctuality and communication in educational environments by sending daily class alerts.

---

## 🚀 Features

- ✅ Automatically sends SMS reminders before each scheduled class
- ✅ Reads daily routine and sends messages accordingly
- ✅ Notifies both students and teachers
- ✅ Easy to update class routine and contacts
- ✅ Uses Twilio API for reliable SMS delivery

---

## 🧰 Tech Stack

- **Python 3**
- **Twilio REST API**
- **Datetime Module**

---

## 📁 Project Structure

```
class-alert-system/
├── class_alert_system.py   # Main script to send SMS
├── README.md               # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Saswatiiiii/class-alert-system.git
cd class-alert-system
```

### 2. Install Required Library

Install the Twilio Python SDK:

```bash
pip install twilio
```

### 3. Configure Twilio Credentials

Open `class_alert_system.py` and replace with your own:

```python
account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'
```

Also, update the Twilio sender phone number:

```python
from_ = "+1234567890"  # your Twilio phone number
```

---

## 🧠 How It Works

- The program checks the **current day** using Python's `datetime`.
- It matches the day to the predefined `class_routine` list.
- For each class scheduled that day, it sends an SMS to all the students using Twilio's API.
- The script is designed to be run once daily via scheduler (like a **cron job**) or can be extended to run continuously with delays.

---

## 📅 Sample Class Routine Format

```python
class_routine = [
    {
        "day": "Monday",
        "classes": [
            {
                "name": "Database Management System",
                "time": "10:30",
                "teacher": "S.S",
                "students": ["+91xxxxxxxxxx", "+91xxxxxxxxxx"]
            },
            ...
        ]
    },
    ...
]
```

---

## 🔒 Security Tip

To keep your **Twilio credentials safe**, consider using environment variables or a `.env` file with the `python-dotenv` package.

---

## 🧩 Future Enhancements

- Add web dashboard to update routine and contacts
- Include teacher-specific reminder logic
- Add email notifications
- Integrate real-time calendar syncing (Google Calendar, etc.)

