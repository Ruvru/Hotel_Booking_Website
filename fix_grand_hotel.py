from app import create_app
from extension import db
from models.hotel import Hotel, Room

app = create_app()

with app.app_context():
    # Delete old Grand Hotel
    old_hotel = Hotel.query.get(1)
    if old_hotel:
        db.session.delete(old_hotel)
        db.session.commit()
        print("✅ Deleted old Grand Hotel")

    # Create new Grand Hotel with full details
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

    # Create rooms
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
    db.session.add_all([room1, room2])
    db.session.commit()

    print("✅ Grand Hotel recreated with full description!")
    print(f"Description: {hotel.description}")