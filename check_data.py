from app import create_app
from extension import db
from models.hotel import Hotel, Room

app = create_app()

with app.app_context():
    hotels = Hotel.query.all()

    print("📋 All Hotels in Database:\n")
    for hotel in hotels:
        print(f"ID: {hotel.id}")
        print(f"Name: {hotel.name}")
        print(f"Description: {hotel.description[:100] if hotel.description else 'NO DESCRIPTION'}...")
        print(f"Price: ", end="")
        rooms = Room.query.filter_by(hotel_id=hotel.id).all()
        if rooms:
            print(f"${rooms[0].price_per_night}")
        else:
            print("NO ROOMS")
        print("-" * 50)