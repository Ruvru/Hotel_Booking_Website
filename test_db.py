from app import create_app
from extension import db
from models.user import User
from models.hotel import Hotel, Room

app = create_app()

with app.app_context():
    # Check if user already exists
    existing_user = User.query.filter_by(email='test@example.com').first()
    if not existing_user:
        # Create a test user
        user = User(username='testuser', email='test@example.com', phone='1234567890')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        print("✅ User created!")
    else:
        print("ℹ️ User already exists, skipping...")

    # Check if Grand Hotel already exists
    existing_hotel = Hotel.query.filter_by(name='Grand Hotel').first()
    if not existing_hotel:
        # Create Grand Hotel with full details
        hotel = Hotel(
            name='Grand Hotel',
            description='Experience ultimate luxury in the heart of New York. Our 5-star hotel offers world-class amenities, stunning city views, and exceptional service that exceeds expectations.',
            address='123 Main St',
            city='New York',
            country='USA',
            star_rating=5,
            image_url='https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=800',
            amenities='Free WiFi, Swimming Pool, Spa, Gym, Restaurant, Bar, Room Service, Concierge'
        )
        db.session.add(hotel)
        db.session.commit()

        # Create rooms with full details
        room1 = Room(
            hotel_id=hotel.id,
            room_name='Deluxe',
            price_per_night=150.0,
            capacity=2,
            available_rooms=10,
            description='Spacious deluxe room with king bed, city views, and modern amenities',
            image_url='https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=800'
        )
        room2 = Room(
            hotel_id=hotel.id,
            room_name='Suite',
            price_per_night=300.0,
            capacity=4,
            available_rooms=5,
            description='Luxurious suite with separate living area, premium furnishings, and panoramic views',
            image_url='https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800'
        )
        db.session.add(room1)
        db.session.add(room2)
        db.session.commit()

        print("✅ Grand Hotel created with all details!")
        print(f"Hotel: {hotel.name}")
        print(f"Rooms: {room1.room_name} (${room1.price_per_night}), {room2.room_name} (${room2.price_per_night})")
    else:
        print("ℹ️ Grand Hotel already exists, skipping...")