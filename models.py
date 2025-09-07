from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    role = db.Column(db.String(20))

class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    event_type = db.Column(db.String(50))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    created_by = db.Column(db.Integer, db.ForeignKey('user.user_id'))

class Registration(db.Model):
    reg_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    registered_at = db.Column(db.DateTime)

class CheckIn(db.Model):
    checkin_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    checkin_time = db.Column(db.DateTime)

class Feedback(db.Model):
    feedback_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(300))
