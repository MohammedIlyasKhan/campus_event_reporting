from flask import Flask, jsonify, request
from models import db, User, Event, Registration, CheckIn, Feedback
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# 1. Event Report (Attendance % etc.)
@app.route('/report/event/<int:event_id>', methods=['GET'])
def event_report(event_id):
    total_regs = Registration.query.filter_by(event_id=event_id).count()
    total_checkins = CheckIn.query.filter_by(event_id=event_id).count()
    attendance_rate = round((total_checkins / total_regs) * 100, 2) if total_regs > 0 else 0
    return jsonify({
        "event_id": event_id,
        "registrations": total_regs,
        "checkins": total_checkins,
        "attendance_rate": attendance_rate
    })


# 2. Add Feedback
@app.route('/feedback', methods=['POST'])
def add_feedback():
    data = request.get_json()
    fb = Feedback(
        event_id=data['event_id'],
        user_id=data['user_id'],
        rating=data['rating'],
        comment=data.get('comment', "")
    )
    db.session.add(fb)
    db.session.commit()
    return jsonify({"message": "Feedback added"})


# 3. Event Popularity Report
@app.route('/report/popularity', methods=['GET'])
def event_popularity():
    results = db.session.query(
        Registration.event_id,
        func.count(Registration.reg_id).label('registrations')
    ).group_by(Registration.event_id).order_by(func.count(Registration.reg_id).desc()).all()
    return jsonify([{"event_id": r.event_id, "registrations": r.registrations} for r in results])


# 4. Student Participation Report
@app.route('/report/student/<int:user_id>', methods=['GET'])
def student_participation(user_id):
    events_attended = db.session.query(CheckIn).filter_by(user_id=user_id).count()
    return jsonify({"user_id": user_id, "events_attended": events_attended})


# 5. Top 3 Most Active Students
@app.route('/report/top-students', methods=['GET'])
def top_students():
    results = db.session.query(
        CheckIn.user_id,
        func.count(CheckIn.checkin_id).label('attended')
    ).group_by(CheckIn.user_id).order_by(func.count(CheckIn.checkin_id).desc()).limit(3).all()
    return jsonify([{"user_id": r.user_id, "events_attended": r.attended} for r in results])


# 6. Average Feedback Score per Event
@app.route('/report/feedback/<int:event_id>', methods=['GET'])
def feedback_report(event_id):
    avg_rating = db.session.query(func.avg(Feedback.rating)).filter_by(event_id=event_id).scalar()
    return jsonify({"event_id": event_id, "average_feedback": round(avg_rating or 0, 2)})


if __name__ == "__main__":
    app.run(debug=True)
