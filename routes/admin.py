from flask import Blueprint, render_template, request, redirect, url_for, flash
from extension import db
from models.hotel import Hotel, Room
from models.user import User
from models.booking import Booking

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# Dashboard
@admin_bp.route('/')
def dashboard():
    hotels = Hotel.query.all()
    rooms = Room.query.all()
    users = User.query.all()
    bookings = Booking.query.all()

    stats = {
        'total_hotels': len(hotels),
        'total_rooms': len(rooms),
        'total_users': len(users),
        'total_bookings': len(bookings)
    }

    return render_template('admin/dashboard.html',
                           hotels=hotels,
                           rooms=rooms,
                           users=users,
                           bookings=bookings,
                           stats=stats)


# View all hotels
@admin_bp.route('/hotels')
def hotels():
    hotels = Hotel.query.all()
    return render_template('admin/hotels.html', hotels=hotels)


# Add new hotel
@admin_bp.route('/hotels/add', methods=['GET', 'POST'])
def add_hotel():
    if request.method == 'POST':
        hotel = Hotel(
            name=request.form['name'],
            description=request.form['description'],
            address=request.form['address'],
            city=request.form['city'],
            country=request.form['country'],
            star_rating=int(request.form['star_rating']),
            image_url=request.form['image_url'],
            amenities=request.form['amenities']
        )
        db.session.add(hotel)
        db.session.commit()
        return redirect(url_for('admin.hotels'))

    return render_template('admin/add_hotel.html')


# Edit hotel
@admin_bp.route('/hotels/edit/<int:id>', methods=['GET', 'POST'])
def edit_hotel(id):
    hotel = Hotel.query.get_or_404(id)

    if request.method == 'POST':
        hotel.name = request.form['name']
        hotel.description = request.form['description']
        hotel.address = request.form['address']
        hotel.city = request.form['city']
        hotel.country = request.form['country']
        hotel.star_rating = int(request.form['star_rating'])
        hotel.image_url = request.form['image_url']
        hotel.amenities = request.form['amenities']

        db.session.commit()
        return redirect(url_for('admin.hotels'))

    return render_template('admin/edit_hotel.html', hotel=hotel)


# Delete hotel
@admin_bp.route('/hotels/delete/<int:id>')
def delete_hotel(id):
    hotel = Hotel.query.get_or_404(id)
    db.session.delete(hotel)
    db.session.commit()
    return redirect(url_for('admin.hotels'))


# View all rooms
@admin_bp.route('/rooms')
def rooms():
    rooms = Room.query.all()
    return render_template('admin/rooms.html', rooms=rooms)


# Add new room
@admin_bp.route('/rooms/add', methods=['GET', 'POST'])
def add_room():
    if request.method == 'POST':
        room = Room(
            hotel_id=int(request.form['hotel_id']),
            room_name=request.form['room_type'],
            price_per_night=float(request.form['price_per_night']),
            capacity=int(request.form['capacity']),
            available_rooms=int(request.form['available_rooms']),
            description=request.form['description'],
            image_url=request.form['image_url']
        )
        db.session.add(room)
        db.session.commit()
        return redirect(url_for('admin.rooms'))

    hotels = Hotel.query.all()
    return render_template('admin/add_room.html', hotels=hotels)


# Edit room
@admin_bp.route('/rooms/edit/<int:id>', methods=['GET', 'POST'])
def edit_room(id):
    room = Room.query.get_or_404(id)

    if request.method == 'POST':
        room.hotel_id = int(request.form['hotel_id'])
        room.room_name = request.form['room_type']
        room.price_per_night = float(request.form['price_per_night'])
        room.capacity = int(request.form['capacity'])
        room.available_rooms = int(request.form['available_rooms'])
        room.description = request.form['description']
        room.image_url = request.form['image_url']

        db.session.commit()
        return redirect(url_for('admin.rooms'))

    hotels = Hotel.query.all()
    return render_template('admin/edit_room.html', room=room, hotels=hotels)


# Delete room
@admin_bp.route('/rooms/delete/<int:id>')
def delete_room(id):
    room = Room.query.get_or_404(id)
    db.session.delete(room)
    db.session.commit()
    return redirect(url_for('admin.rooms'))