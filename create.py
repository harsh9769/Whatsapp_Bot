from webapp import app, db

# Push the application context
with app.app_context():
    db.create_all()