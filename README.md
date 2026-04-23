# 🏥 Hospital Management System API

## 📌 Project Overview

This project is a **Hospital Management System REST API** built using FastAPI. It enables efficient management of hospital operations such as patient records, doctor details, and appointment scheduling. The system is designed with a modular architecture and follows industry best practices for backend development.

---

## 🚀 Features

* 🔐 **JWT Authentication**

  * Secure login system for users (Admin/Doctor)
  * Token-based authentication for API access

* 🧑 **Patient Management**

  * Add new patients
  * View patient details
  * Maintain structured patient records

* 👨‍⚕️ **Doctor Management**

  * Add and manage doctor profiles
  * Store specialization details

* 📅 **Appointment Scheduling**

  * Book appointments between patients and doctors
  * Track appointment history

* 🗄️ **Database Integration**

  * Relational database design using PostgreSQL
  * Managed via SQLAlchemy ORM

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI
* **Language:** Python
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Authentication:** JWT (python-jose)
* **Server:** Uvicorn

---

## 📁 Project Structure

```
hospital_management/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── services/
│   └── utils/
│
├── .env
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Set environment variables in `.env`
5. Run the server:

   ```bash
   uvicorn app.main:app --reload
   ```
6. Open API docs:

   ```
   http://127.0.0.1:8000/docs
   ```

---

## 🧪 API Testing

* Interactive API testing via Swagger UI
* Supports GET and POST endpoints for all modules
* Can also be tested using Postman or cURL

---

## 🔐 Security

* JWT-based authentication
* Environment variable-based secret management
* Sensitive data stored securely using `.env`

---

## 📈 Future Enhancements

* Role-based access control (RBAC)
* Password hashing using bcrypt
* Docker containerization
* Deployment on cloud (Azure/AWS)
* Integration with analytics dashboards

---

## 💡 Conclusion

This project demonstrates strong backend development skills including API design, database integration, authentication, and clean architecture. It is suitable for real-world applications and can be extended further for enterprise-level systems.
