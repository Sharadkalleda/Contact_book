📇 Contact Book
A comprehensive, web-based application designed to simplify contact management for freelancers, small business owners, and professionals. This project provides a centralized, secure environment to ensure that important relationship data is always organized and accessible.


🚀 Project Overview
In an era of digital fragmentation, managing client information across multiple platforms can be difficult and prone to errors. This system offers a streamlined solution with a focus on:
> Centralization: A single source of truth for all contact-related data.
> Security: Unique registration and authentication gates for every user.
> Ease of Use: A clean, intuitive interface for seamless CRUD operations.


🛠️ Tech Stack
> Frontend: HTML5, CSS3, JavaScript.
> Backend: Python & Django Framework.
> Database: MySQL.
> Development Environment: Visual Studio Code (VS Code).


🏗️ System Architecture
The application follows the Model-View-Template (MVT) architecture:
> Model: Manages the database schema in MySQL.
> View: Handles business logic and fetches data from the Model.
> Template: The frontend layer that renders information for the user.


✨ Key Features
> Secure Authentication: User registration, login, and session management to ensure data privacy.
> Full CRUD Functionality: Effortlessly Create, View, Update, and Delete contact entries.
> Admin Dashboard: Specialized server-view for superusers to monitor active users and oversee total data entries.
> Personalized Experience: The system links each user to their specific contacts so they only see their own data.

📊 Database Design
The database is structured around two primary entities:
> User (Admin): Stores unique credentials (Username, Email, Hashed Password).
> Contact: Stores specific details including Name, Phone Number, Email, Address, and a Foreign Key linking it to the registered user.



🛠️ Installation & Setup
1. Clone the Repository:
> git clone https://github.com/Sharadkalleda/Contact_book.git
> cd Contact_book

2. Set up Virtual Environment:
> python -m venv venv
> .\venv\Scripts\activate  # Windows

3. Install Requirements:
> pip install -r requirements.txt

4. Database Configuration:
> Create a MySQL database.
> Update your credentials in: core/settings.py.

5. Run Migrations & Start Server:
> python manage.py migrate
> python manage.py runserver



> > > Author: Sharadchandra Kalleda < < < 