Design Document – Campus Event Reporting System

1. Assumptions

Each event has a unique event_id across the platform.

All data is stored in a single database (SQLite) for simplicity and easy management.

Users are categorized into two roles- admin (college staff) and student.

Duplicate registrations are not allowed by database constraints.

Attendance can be zero if no students checkin.

Reports handle missing or incomplete data gracefully.

2. Decisions

Chose Flask as the backend framework because it is lightweight and fast to develop.

Used SQLite for the database as it requires no external setup and is sufficient for prototyping.

Implemented a RESTful API endpoint for reporting event attendance.

Focused on minimal functionality to demonstrate a working reporting system without unnecessary features.

Used Python scripts to populate test data quickly.


4. Deviations from AI Suggestions

I wrote additional scripts to insert test data, such as adding sample users, events, registrations, and check-ins.

I handled edge cases like division by zero in attendance calculation by adding conditional checks in the API.

I wrote the README in my own words to explain the setup and usage based on my understanding.

Note:

This document summarizes my approach, assumptions, and how I used AI to brainstorm ideas while implementing the solution. The final implementation reflects my own decisions and understanding.