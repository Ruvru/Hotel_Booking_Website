from app import create_app
from extension import db
from models.user import User
from models.hotel import Hotel, Room
from models.booking import Booking

app = create_app()

with app.app_context():
    # Read all users (READ operation)
    users = User.query.all()
    print("\n📋 USERS:")
    for user in users:
        print(f"  - {user.username} | {user.email}")

    # Read all hotels (READ operation)
    hotels = Hotel.query.all()
    print("\n🏨 HOTELS:")
    for hotel in hotels:
        print(f"  - {hotel.name} | {hotel.city}, {hotel.country} | {hotel.star_rating}⭐")

    # Read all rooms (READ operation)
    rooms = Room.query.all()
    print("\n🛏️ ROOMS:")
    for room in rooms:
        print(f"  - {room.room_type} | ${room.price_per_night}/night | {room.available_rooms} available")

    # Read all bookings (READ operation)
    bookings = Booking.query.all()
    print(f"\n📅 BOOKINGS: {len(bookings)} total")

    print("\n✅ CRUD - READ operation successful!")