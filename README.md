# Cloud-Native Hyperlocal Delivery Platform

Solo-built backend-focused project to demonstrate real-world system development using
Flask, SQLite, Git, and Linux.

This project is being developed step-by-step with proper documentation and version control.

---

## 🎯 Project Goal

Build a production-style hyperlocal delivery backend with:

- Users
- Orders
- Vendors (coming)
- REST APIs
- Database integration
- Cloud deployment (later)
- DevOps practices (later)

---

## 🛠 Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite (MVP)
- Git + GitHub (SSH)
- Linux (Ubuntu)
- curl (API testing)

Future:
- Docker
- PostgreSQL
- CI/CD
- Cloud VM

---

## 📁 Project Structure

cloud-hyperlocal/
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ ├── venv/
│ ├── models/
│ └── routes/
├── frontend/ (later)
└── docs/


---

## ✅ Progress Log

### Day 1 – Git + GitHub Setup
- Initialized repository
- Created README
- Configured Git user
- Generated SSH keys
- Connected GitHub via SSH
- First commit pushed

---

### Day 2 – Backend Skeleton (Flask)
- Created backend folder structure
- Setup Python virtual environment
- Installed Flask
- Created `app.py`
- Ran first backend server
- Generated `requirements.txt`

---

### Day 3 – Database + APIs
- Integrated SQLite with Flask-SQLAlchemy
- Created User and Order models
- Built REST APIs:
  - POST /user
  - POST /order
  - GET /orders
- Tested APIs using curl
- Database file `app.db` created
- Changes committed to GitHub

---

## 🚀 How to Run Backend Locally

```bash
cd backend
source venv/bin/activate
python app.py

