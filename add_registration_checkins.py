from datetime import datetime
from app import app
from models import db, Registration, CheckIn

with app.app_context():
    # Add a registration for student
    reg = Registration(event_id=1, user_id=2, registered_at=datetime.now())
    db.session.add(reg)

    # Add a check-in for student
    checkin = CheckIn(event_id=1, user_id=2, checkin_time=datetime.now())
    db.session.add(checkin)

    db.session.commit()
    print("Sample registration and check-in added!")
