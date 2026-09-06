# 👨‍💼 Employee Management System

A desktop-based **Employee Management System** developed using **Python (Tkinter)** and **PostgreSQL**. The system provides a user-friendly graphical interface (GUI) for managing employee records, with additional **CSV import/export and search functionality**.

---

## 🚀 Key Features

### 1. 👤 Employee Information Management (CRUD)

The system allows users to manage employee records containing:

* 🆔 **Employee ID**
* 👤 **Name**
* 📧 **Email**
* 📱 **Phone Number**

Available functions:

| Function       | Description                           |
| -------------- | ------------------------------------- |
| ➕ **Register** | Add a new employee record             |
| 👁️ **View**   | Display existing employee information |
| ✏️ **Update**  | Modify registered employee details    |
| 🗑️ **Delete** | Remove an employee record             |
| 🧹 **Clear**   | Clear all input fields                |
| 🚪 **Exit**    | Safely close the application          |

---

### 2. 📊 Smart Data Management & Notifications

The system includes several features to improve data management:

* **Dynamic Employee Counter**
  Automatically updates the total number of employees after a successful registration or deletion.

* **Automated Registration Alert**
  Displays a pop-up notification containing the employee details after successful registration.

---

### 3. 📁 CSV Integration & Search

The system supports CSV-based data management:

* 📥 **Import CSV** — Import employee records from a CSV file.
* 📤 **Export CSV** — Export employee records into a CSV file.
* 🔢 **CSV Counter** — Displays the number of employee records processed through CSV operations.
* 🔍 **Quick Search** — Search for specific employees within the imported or exported CSV records.

---

### 4. 🐘 PostgreSQL Database Integration

The system was enhanced with **PostgreSQL database integration** to provide centralized employee data storage.

#### Database capabilities:

* 💾 Store registered employee information directly in PostgreSQL.
* 🔄 Retrieve and manage employee records through the application.
* 🗃️ Centralize employee data in a structured relational database.
* 🔎 Allow administrators to verify and manage records using database management tools such as **pgAdmin** or **DBeaver**.

> **Phase 2 Update:** PostgreSQL integration was added to improve data persistence, organization, and centralized data management.

---

## 🛠️ Technologies Used

| Technology        | Purpose                        |
| ----------------- | ------------------------------ |
| 🐍 **Python**     | Main programming language      |
| 🖥️ **Tkinter**   | Graphical User Interface (GUI) |
| 🐘 **PostgreSQL** | Relational database            |
| 🔗 **psycopg2**   | PostgreSQL-Python connection   |
| 📄 **CSV**        | Data import/export             |
| 💻 **VS Code**    | Development environment        |

---

## 📋 Prerequisites

Before running the application, make sure the following are installed:

* [Python 3.x](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/download/)
* `tkinter` — Usually included with Python
* `psycopg2` — Python PostgreSQL database adapter

Install `psycopg2` using:

```bash
pip install psycopg2
```

---

## ⚙️ System Architecture

```text
                 Employee Management System
                           │
                           ▼
                  ┌─────────────────┐
                  │   Tkinter GUI   │
                  └────────┬────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       ┌──────────────┐         ┌────────────────┐
       │  CSV Files   │         │   PostgreSQL   │
       │ Import/Export│         │    Database    │
       └──────────────┘         └────────────────┘
```

---

## 📌 Project Status

### Phase 1 — Employee Management & CSV

* ✅ Employee registration
* ✅ Employee viewing
* ✅ Employee updating
* ✅ Employee deletion
* ✅ Employee counter
* ✅ CSV import
* ✅ CSV export
* ✅ CSV search
* ✅ Registration notifications

### Phase 2 — PostgreSQL Integration

* ✅ PostgreSQL database connection
* ✅ Employee data insertion
* ✅ Centralized employee data storage
* ✅ Database-based employee management

---

## 🎯 Project Objective

The main objective of this project is to develop a simple yet functional employee management system while gaining practical experience in:

* Python programming
* GUI development with Tkinter
* CRUD operations
* CSV file handling
* PostgreSQL database integration
* Database connectivity using Python
* Basic software development workflow

---

## 👩‍💻 Author

Developed as a **Python & PostgreSQL Employee Management System project**.
