from datetime import datetime
from app import app
from models import db, User, Event

with app.app_context():
    # Create sample admin and student users
    admin = User(name="Admin User", email="admin@example.com", role="admin")
    student = User(name="Student One", email="student@example.com", role="student")
    db.session.add(admin)
    db.session.add(student)
    db.session.commit()

    # Create a sample event
    event = Event(
        title="Tech Talk",
        event_type="Workshop",
        start_time=datetime.now(),
        end_time=datetime.now(),
        created_by=admin.user_id
    )
    db.session.add(event)
    db.session.commit()

    print("Test event added!")
