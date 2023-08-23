# Import necessary modules and classes
import config 
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate

# Create a Flask app instance
app = Flask(__name__)

# Determine the environment (development/production)
env = 'development'  
if env == 'development':
    app.config.from_object(config.DevelopmentConfig)
    print("Loaded DevelopmentConfig")
else:
    app.config.from_object(config.ProductionConfig)
    print("Loaded ProductionConfig")

# Initialize Flask-Login's LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Enable debug mode for the app (for development)
app.debug = True

# Configure Flask-Mail extension
mail = Mail(app)
mail2 = Mail(app)  # You have two instances of Mail, ensure you're using them correctly

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Migrate for database migrations
migrate = Migrate(app, db)

# Create the database tables within the app's context
with app.app_context():
    db.create_all()  # This line creates the database tables

# Import routes module 
import routes

# Import and apply your custom filter 'laz' from myfilters.py
from myfilters import laz

# Run the app only if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # Start the development server
