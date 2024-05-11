from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///innofund.db'

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# Bind the SQLAlchemy instance to the Flask application
db.init_app(app)

# Define your SQLAlchemy models
class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(100), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    purpose = db.Column(db.String(200), nullable=False)
    # Add more fields as needed

# Now you can use the `current_app` object within the application context
with app.app_context():
    # Example usage of current_app
    current_app.logger.info('This is within the application context')

# Define your routes and other application logic here

if __name__ == '__main__':
    app.run(debug=True)
