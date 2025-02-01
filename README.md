# FAQ Project

This is a simple Django-based FAQ system that supports multiple languages for questions and answers. It uses Django REST framework to expose an API to fetch FAQ data. Additionally, the FAQ model automatically translates the questions and answers into multiple languages (Hindi, Bengali) if not already provided.

## Features

- **Multi-language Support**: Fetch FAQs in English, Hindi, and Bengali.
- **API Endpoint**: `GET /api/faqs/` to retrieve the list of FAQs.
- **Database Caching**: Frequently fetched data is cached to improve performance.

## Installation

Follow these steps to get the project up and running locally.

### Prerequisites

- Python 3.x
- Django 5.1+
- Django REST framework
- Google Translate API or `googletrans` library (you may need to install this manually)

### Steps to Run Locally

1. **Clone the repository**:
    ```bash
    git clone <repo_url>
    cd faq_project
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      .\env\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source env/bin/activate
      ```

4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser for admin access**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

8. **Visit the API at**:
    ```bash
    http://127.0.0.1:8000/api/faqs/
    ```

9. **Access the Django admin panel at**:
    ```bash
    http://127.0.0.1:8000/admin/
    ```

## API Endpoints

- **GET /api/faqs/**: Fetches all the FAQs in the requested language (`lang` query parameter, defaults to `en`).

### Example Request:
```bash
GET http://127.0.0.1:8000/api/faqs/?lang=hi
