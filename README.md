# 🗨️ Real-Time Django Chat Application

<p align="center">
  <img src="chat_images/Screenshot 2025-11-17 054004.png" width="750">
</p>

A real-time chat application built with Django, AJAX, user authentication, and image sharing.


## **📖 Overview**

This is a real-time Django Chat Application built with Python, Django, AJAX, and session-based authentication.
It allows users to register, log in, send text messages, and upload images inside the chat room.

The project includes:

* User Registration
* User Login
* Global Chat Room
* Sending Text Messages
* Sending Image Files
* Displaying All Active Users
* Real-time message updating using AJAX
* Image preview in chat
* Django Models for Rooms, Users, and Messages

---

## **📁 Features**

### ✔ **User Authentication**

* Register new users with validation
* Prevent duplicate usernames and emails
* Login system using Django sessions

### ✔ **Chat Room System**

* Global chat room (`main`)
* Displays all users
* Shows all previous messages (text + image)

### ✔ **Messaging System**

* Send text messages
* Upload & send image files
* AJAX request handles message posting
* No page refresh required
* Messages displayed with timestamps

### ✔ **Backend**

* Django ORM
* CSRF-exempt API endpoint for AJAX
* Room & Message Models
* Logging for debugging errors

---

## **📂 Important Files**

| File          | Description                                             |
| ------------- | ------------------------------------------------------- |
| `views.py`    | All backend logic (login, register, chat, send message) |
| `models.py`   | Database models (User, Room, Message)                   |
| `room.html`   | Chat UI + AJAX                                          |
| `urls.py`     | Routing                                                 |
| `settings.py` | Media file support enabled                              |

---

## **🛠 Technologies Used**

* Python
* Django
* HTML/CSS
* JavaScript
* AJAX
* SQLite3
* Bootstrap (optional)

---

## 📸 **Image Upload Feature**

* Users can upload images inside chat
* Files are stored in `MEDIA/` folder
* Image URLs are returned through JSON
* Displayed immediately in chat UI

---

## **🚀 How to Run the Project**

### **1️⃣ Install Dependencies**

```
pip install django
```

### **2️⃣ Apply Migrations**

```
python manage.py makemigrations
python manage.py migrate
```

### **3️⃣ Run Server**

```
python manage.py runserver
```

### **4️⃣ Open in Browser**

```
http://127.0.0.1:8000/
```

---

## **🎥 Demo Video Explanation (Script)**

Use this script to record your GitHub demo video.

---

# 🎬 **VIDEO SCRIPT — "How the Django Chat App Works"**

### **1. Introduction**

"Hello everyone, in this video I will show my Django Chat Application.
This app allows users to register, log in, and chat in real time with text and image messages."

---

### **2. Registration Page**

"Here is the registration page.
I will enter a username, email, and password.
The backend checks if the email or username already exists.
If everything is correct, the user is registered successfully."

---

### **3. Login Page**

"Now I will log in with the registered account.
On login, Django stores the username in session."

---

### **4. Main Chat Room**

"This is the chat room.
Here on the left you see all registered users.
In the middle we have the message area."

---

### **5. Sending Text Messages**

"I will type a message and click send.
The message immediately appears without refreshing the page.
This works using AJAX that sends data to the Django view."

---

### **6. Sending Image**

"Now I will upload an image.
Once I select the image, it also appears inside the chat.
The backend saves it in the MEDIA folder and returns the URL."

---

### **7. Backend Logic**

"In Django views.py, the `post_message()` function receives the username, text, and image.
It saves the message and returns JSON response to update the chat instantly."

---

### **8. Conclusion**

"This was a quick demo of my Django Chat Application.
Thank you for watching!"

---

# ✅ **If you want, I can also create:**

✔ README.md for GitHub
✔ Upload instructions
✔ Video subtitles
✔ Project diagram
✔ Architecture diagram
✔ UI screenshots

Just tell me!
