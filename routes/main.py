from flask import Blueprint, render_template
from models.hotel import Hotel, Room
from models.user import User
from models.booking import Booking

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    hotels = Hotel.query.all()
    users = User.query.all()
    rooms = Room.query.all()
    bookings = Booking.query.all()
    return render_template('index.html',
                         hotels=hotels,
                         users=users,
                         rooms=rooms,
                         bookings=bookings)

@main_bp.route('/hotel/<int:hotel_id>')
def hotel_details(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    rooms = Room.query.filter_by(hotel_id=hotel_id).all()
    return render_template('hotel_details.html', hotel=hotel, rooms=rooms)