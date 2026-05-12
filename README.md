# projects-portal
Personal VPS Lab Portal built with Flask.

Projects Portal is a web application developed with Flask that serves as the central access point to all applications, dashboards, APIs and experiments deployed on my personal VPS.

The portal functions both as a technical portfolio and as a project directory, providing a professional and centralized way to present deployed applications and the infrastructure that supports them.

---

## Overview

The application is available at:

https://projects.fernandorioseco.es

Projects Portal provides:

- A presentation of the personal VPS laboratory.
- A summary of the server infrastructure.
- A showcase of the technology stack.
- Direct access to deployed applications.
- Links to technical documentation.
- Links to source code repositories.
- Optional API documentation links.

---

## Features

- Modern landing page design.
- Hero section with project overview.
- VPS infrastructure summary.
- Technology stack section.
- Dynamic project cards loaded from a JSON file.
- Direct links to:
  - Live application.
  - Documentation article.
  - GitHub repository.
  - API documentation (optional).
- Responsive design for desktop and mobile devices.

---

## Technology Stack

### Backend

- Python 3.13
- Flask
- Gunicorn
- Jinja2
- python-dotenv

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Infrastructure

- Ubuntu Server
- Nginx
- Let's Encrypt
- GitHub

---

## Project Structure

projects-portal/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── data/
│   │   └── projects.json
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── components/
│   └── static/
│       ├── css/
│       ├── js/
│       └── img/
├── config.py
├── requirements.txt
├── run.py
└── wsgi.py

## Installation

### Clone the repository:

git clone https://github.com/fernandorioseco/projects-portal.git
cd projects-portal

### Create a virtual environment:

python -m venv venv

### Activate the virtual environment.

Windows
venv\Scripts\activate
Linux/macOS
source venv/bin/activate

### Install dependencies:

pip install -r requirements.txt
Usage

### Run the development server:

python run.py

Open your browser at:

http://127.0.0.1:5000

### Deployment

The application is designed to be deployed on a VPS using the following stack:

Gunicorn as WSGI application server.
Nginx as reverse proxy.
HTTPS certificates generated with Let's Encrypt.
DNS configuration pointing projects.fernandorioseco.es to the VPS.

### Deployment flow:

User Browser
     ↓
Nginx
     ↓
Gunicorn
     ↓
Flask Application
     ↓
Jinja2 Templates
Data Source

### Project information is stored in:

app/data/projects.json

Each project entry includes:

Name
Description
Technologies
Application URL
Documentation URL
GitHub URL
API documentation URL (optional)
License

### This project is licensed under the MIT License.

### Author

Fernando Rioseco

Website: https://fernandorioseco.es
