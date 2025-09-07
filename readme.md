1. Overview

This project includes basic functionality for creating events in an event management system for a campus management platform. The purpose was to assist admins in event registration and student attendance. The system is developed in Flask and is backed with a SQLite Database.

2. Features

Register students to events.

Track student checkins (attendance).

Collect feedback (rating 1–5).

Generate reports:
  Event report: total registrations, checkins, attendance percentage.
  Event popularity: events sorted by registrations.
  Student participation: number of events attended by each student.
  Top 3 most active students.
  Average feedback score per event.

3. Technologies Used

Python programmed with the Flask framework.

SQLite Database to manage records of users, events, registrations, and check-ins data. 

Python scripts in modules for inserting data into the tables for testing purposes. 

4. How to Run the Project

Download the zipped folder of the project 

Activate the virtual environment:

.venv\Scripts\activate

Get the custom developed modules:

pip install -r requirements.txt

Initialize the Database with the required tables:

python create_db.py

Insert test data into the Database:

python add_test_data.py

python add_registrations_checkins.py

Start the Flask webserver:

python app.py

5. Access the APIs:

http://127.0.0.1:5000/report/event/1 - Event report

http://127.0.0.1:5000/report/popularity - Event popularity

http://127.0.0.1:5000/report/student/1 - Student participation

http://127.0.0.1:5000/report/top-students - Top 3 active students

http://127.0.0.1:5000/report/feedback/1 - Average feedback score

6. How I Implemented This Project

I created four database tables: Users, Events, Registrations and Checkins.

The reporting API counts the total registrations, checkins, and how much attendance is.

I used Python scripts for inserting sample data for testing.

I took into consideration edge cases like division by 0 among others.

