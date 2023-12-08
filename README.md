

# Across The Globe

Across The Globe is a web application developed using Python, Django, and MySQL, aiming to facilitate the storage and retrieval of data for doctors and patients. The project features a signup form for both doctors and patients, storing their respective data in MySQL tables. Once logged in, users can access their personalized information provided during the signup process.


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Managing data for doctors and patients is simplified with Across The Globe. The project offers a signup form for both user types, storing their information in MySQL tables. After logging in as a doctor or patient, users can seamlessly access and manage their respective signup form data.

## Features

- **Signup Form:** A user-friendly signup form for doctors and patients, capturing essential information.

- **User Authentication:** Secure user authentication process, ensuring privacy and data integrity.

- **Personalized Dashboards:** Upon logging in, doctors and patients are presented with personalized dashboards displaying the information submitted during the signup process.

## Tech Stack

Across The Globe is built using the following technologies:

- **Python:** The primary programming language for the project.

- **Django:** A high-level web framework for rapid development, providing a clean and pragmatic design.

- **MySQL:** The relational database management system used to store user data securely.

## Installation

To set up Across The Globe locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Across-The-Globe.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Across-The-Globe
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://localhost:8000`.

## Usage

Describe how users can utilize Across The Globe for managing doctor and patient data:

- How to sign up as a doctor or patient.
- How to log in and access personalized dashboards.
- Any additional features or functionalities available.



---

Feel free to customize this README template to match your project's specific details and structure. Update the links, descriptions, and any additional information that is relevant to your project.
