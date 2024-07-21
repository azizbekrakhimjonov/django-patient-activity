# Django Patient Activity Tracker

![Django REST framework Logo](https://www.django-rest-framework.org/img/logo.png)

## Overview

The Django Patient Activity Tracker is a RESTful API designed to register patients and track their activity durations. This project uses Django REST framework to create endpoints for managing patients and their activities.

## Features

- **Patient Registration**: Add new patients with their details.
- **Activity Tracking**: Start and end activity durations for patients.
- **Time Zone**: Automatically handles time zone settings (Asia/Tashkent).

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ayubxontursunov/django-patient-activity.git
    cd django-patient-activity
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the server**:
    ```bash
    python manage.py runserver
    ```

## Endpoints

### Patient Endpoints

- **List Patients**: `GET /patients/`
- **Create Patient**: `POST /patients/`
- **Retrieve Patient**: `GET /patients/{id}/`
- **Update Patient**: `PUT /patients/{id}/`
- **Delete Patient**: `DELETE /patients/{id}/`

### Activity Endpoints

- **Start Activity**: `POST /patients/{id}/start/`
- **End Activity**: `POST /patients/{id}/end/`

## Example Request

### Create Patient

```bash
curl -X POST http://127.0.0.1:8000/patients/ \
  -H "Content-Type: application/json" \
  -d '{
        "name": "John Doe",
        "age": 30,
        "mobile_number": "1234567890"
      }'
