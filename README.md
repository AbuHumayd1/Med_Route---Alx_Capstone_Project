---

# 🏥 MedRoute – Smart Emergency Hospital Routing System

MedRoute is a backend application designed to **reduce emergency mortality rates** by intelligently connecting patients to hospitals with available capacity and the right expertise.
The system allows hospitals to register, manage resources, and receive emergency requests while ensuring patients are routed to the most suitable hospital in real-time.

---

## 🚀 Features

* **User Authentication (JWT-based)**

  * Register and login users securely.
  * Different user roles (e.g., admin, hospital staff).

* **Hospital Management**

  * Register hospitals.
  * Update hospital resources (beds, doctors, equipment).
  * Track hospital capacity in real-time.

* **Emergency Request System**

  * Patients send emergency requests.
  * System finds the nearest hospital with the required resources.
  * If unavailable, the system logs transfers to other hospitals.

* **Smart Matching**

  * Routes patients to hospitals based on availability and specialization.

* **API-First Design**

  * Clean RESTful endpoints for all operations.

---

## 📂 Project Structure

```bash
MedRoute/
├── accounts/           # User authentication and roles
├── hospitals/          # Hospital registration & resource management
├── emergencies/        # Emergency request & smart routing
├── MedRoute/           # Project settings and configurations
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
```


## 🛠️ Tech Stack

* **Backend Framework:** Django + Django REST Framework
* **Database:** PostgreSQL (or SQLite for development)
* **Authentication:** JWT (via djangorestframework-simplejwt)
* **Deployment:** ...

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/your-username/MedRoute.git
cd MedRoute
```

### 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```
python manage.py createsuperuser
```

### 6. Run Server

```
python manage.py runserver
```

Server will start at 👉 `http://127.0.0.1:8000/`

---

## 🔑 Authentication

* **Obtain Token:**
  POST → `/api/token/`

  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```

* **Use Token:**
  Add to request headers:

  ```
  Authorization: Bearer <your_token>
  ```

## 📡 API Endpoints

### Authentication

* `POST /api/accounts/register/` → Register a new user
* `POST /api/token/` → Get JWT access token
* `POST /api/token/refresh/` → Refresh token

### Hospitals

* `POST /api/hospitals/` → Register hospital
* `PUT /api/hospitals/{id}/` → Update hospital resources
* `GET /api/hospitals/` → List all hospitals

### Emergencies

* `POST /api/emergencies/` → Create an emergency request
* `GET /api/emergencies/` → View all emergencies (admin/staff only)


## 🖥️ Demo Workflow

1. **Register/Login a User**

   * Create a test account.
   * Get JWT token.

2. **Register a Hospital**

   * Add hospital details (name, location, capacity, specialization).

3. **Update Hospital Resources**

   * Update available doctors, beds, or equipment.

4. **Send Emergency Request**

   * Patient requests emergency help.
   * System finds nearest available hospital.
   * Logs transfer if capacity is full.


## 📽️ Video Demo

👉 *(demo)*


## 🤝 Contribution

Contributions are welcome! Please:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.


⚡ Built with passion to save lives.



