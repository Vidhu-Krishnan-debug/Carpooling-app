from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carpool.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    is_driver = db.Column(db.Boolean, default=False)
    driver_verified = db.Column(db.Boolean, default=False)
    rides_offered = db.relationship('Ride', backref='driver', lazy=True)

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    departure = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    bookings = db.relationship('Booking', backref='ride', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ride_id = db.Column(db.Integer, db.ForeignKey('ride.id'), nullable=False)
    passenger_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    seats_booked = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled

class DriverApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle_make = db.Column(db.String(50), nullable=False)
    vehicle_model = db.Column(db.String(50), nullable=False)
    vehicle_year = db.Column(db.Integer, nullable=False)
    license_plate = db.Column(db.String(20), nullable=False)
    vehicle_photos = db.Column(db.String(500))  # Comma-separated paths
    drivers_license = db.Column(db.String(200))
    insurance = db.Column(db.String(200))
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('register'))
        
        user = User(email=email, name=name)
        user.password_hash = generate_password_hash(password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/offer-ride', methods=['GET', 'POST'])
@login_required
def offer_ride():
    if request.method == 'POST':
        ride = Ride(
            driver_id=current_user.id,
            departure=request.form.get('departure'),
            destination=request.form.get('destination'),
            date=datetime.strptime(request.form.get('date'), '%Y-%m-%d'),
            seats=int(request.form.get('seats')),
            price=float(request.form.get('price'))
        )
        db.session.add(ride)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('offer_ride.html')

@app.route('/search-rides', methods=['GET', 'POST'])
def search_rides():
    if request.method == 'POST':
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        date = datetime.strptime(request.form.get('date'), '%Y-%m-%d')
        
        rides = Ride.query.filter_by(
            departure=departure,
            destination=destination,
            date=date
        ).all()
        return render_template('search_results.html', rides=rides)
    return render_template('search_rides.html')

@app.route('/book-ride/<int:ride_id>', methods=['POST'])
@login_required
def book_ride(ride_id):
    ride = Ride.query.get_or_404(ride_id)
    seats = int(request.form.get('seats'))
    
    if seats <= ride.seats:
        booking = Booking(
            ride_id=ride_id,
            passenger_id=current_user.id,
            seats_booked=seats,
            status='confirmed'
        )
        ride.seats -= seats
        db.session.add(booking)
        db.session.commit()
        flash('Booking confirmed!')
    else:
        flash('Not enough seats available')
    return redirect(url_for('search_rides'))

@app.route('/become-driver', methods=['GET', 'POST'])
@login_required
def become_driver():
    if request.method == 'POST':
        # Handle file uploads
        vehicle_photos = request.files.getlist('vehicle_photos')
        drivers_license = request.files['drivers_license']
        insurance = request.files['insurance']
        
        # Save files and create application
        application = DriverApplication(
            user_id=current_user.id,
            vehicle_make=request.form['vehicle_make'],
            vehicle_model=request.form['vehicle_model'],
            vehicle_year=int(request.form['vehicle_year']),
            license_plate=request.form['license_plate']
        )
        
        # Here you would typically:
        # 1. Save the files to a secure location
        # 2. Store the file paths in the database
        # 3. Send notification to admin for review
        
        db.session.add(application)
        db.session.commit()
        
        flash('Your application has been submitted and is under review!')
        return redirect(url_for('dashboard'))
    
    return render_template('become_driver.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
