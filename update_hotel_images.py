from app import create_app
from extension import db
from models.hotel import Hotel, Room

app = create_app()

with app.app_context():
    # Update existing hotel with image
    hotel = Hotel.query.first()
    if hotel:
        hotel.image_url = 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=800'
        hotel.description = 'Experience ultimate luxury in the heart of New York. Our 5-star hotel offers world-class amenities, stunning city views, and exceptional service that exceeds expectations.'
        hotel.amenities = 'Free WiFi, Swimming Pool, Spa, Gym, Restaurant, Bar, Room Service, Concierge'

        # Update rooms with images
        rooms = Room.query.filter_by(hotel_id=hotel.id).all()
        for room in rooms:
            if room.room_type == 'Deluxe':
                room.image_url = 'https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=800'
                room.description = 'Spacious deluxe room with king bed, city views, and modern amenities'
            elif room.room_type == 'Suite':
                room.image_url = 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800'
                room.description = 'Luxurious suite with separate living area, premium furnishings, and panoramic views'

        db.session.commit()
        print("✅ Hotel images updated successfully!")
        print(f"Hotel: {hotel.name}")
        print(f"Image URL: {hotel.image_url}")
    else:
        print("❌ No hotel found. Run test_db.py first!")