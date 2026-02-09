from app import create_app
from extension import db
from models.hotel import Hotel, Room

app = create_app()

with app.app_context():
    # First, delete all existing hotels except Grand Hotel (ID 1)
    hotels_to_delete = Hotel.query.filter(Hotel.id > 1).all()
    for hotel in hotels_to_delete:
        db.session.delete(hotel)
    db.session.commit()
    print("✅ Cleared duplicate hotels")

    # Hotel 2: Sunset Resort
    hotel2 = Hotel(
        name='Sunset Beach Resort',
        description='Tropical paradise with pristine beaches and world-class spa facilities. Perfect for romantic getaways and family vacations.',
        address='456 Ocean Drive',
        city='Miami',
        country='USA',
        star_rating=5,
        image_url='https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800',
        amenities='Private Beach, Infinity Pool, Spa, Water Sports, Kids Club, Fine Dining'
    )
    db.session.add(hotel2)
    db.session.commit()

    # Rooms for Hotel 2
    room1 = Room(hotel_id=hotel2.id, room_name='Ocean View', price_per_night=200.0, capacity=2, available_rooms=15,
                 description='Breathtaking ocean views with private balcony',
                 image_url='https://images.unsplash.com/photo-1590490360182-c33d57733427?w=800')
    room2 = Room(hotel_id=hotel2.id, room_name='Beach Villa', price_per_night=450.0, capacity=4, available_rooms=8,
                 description='Private villa steps from the beach with plunge pool',
                 image_url='https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800')
    db.session.add_all([room1, room2])

    # Hotel 3: Mountain Lodge
    hotel3 = Hotel(
        name='Alpine Mountain Lodge',
        description='Cozy mountain retreat with stunning alpine views. Ideal for skiing, hiking, and nature lovers.',
        address='789 Mountain Peak Rd',
        city='Aspen',
        country='USA',
        star_rating=4,
        image_url='https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800',
        amenities='Ski Access, Fireplace Lounge, Mountain Views, Hiking Trails, Hot Tub'
    )
    db.session.add(hotel3)
    db.session.commit()

    # Rooms for Hotel 3
    room3 = Room(hotel_id=hotel3.id, room_name='Mountain View', price_per_night=180.0, capacity=2, available_rooms=12,
                 description='Cozy room with panoramic mountain views',
                 image_url='https://images.unsplash.com/photo-1598928506311-c55ded91a20c?w=800')
    room4 = Room(hotel_id=hotel3.id, room_name='Luxury Cabin', price_per_night=350.0, capacity=6, available_rooms=5,
                 description='Spacious cabin with fireplace and private deck',
                 image_url='https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=800')
    db.session.add_all([room3, room4])

    # Hotel 4: Royal Palace
    hotel4 = Hotel(
        name='Royal Palace Hotel',
        description='Elegant palace-style hotel with royal ambiance and exceptional service. Experience the grandeur of royalty.',
        address='101 Royal Avenue',
        city='London',
        country='UK',
        star_rating=5,
        image_url='https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=800',
        amenities='Butler Service, Fine Dining, Ballroom, Royal Gardens, Limousine Service'
    )
    db.session.add(hotel4)
    db.session.commit()

    # Rooms for Royal Palace
    room5 = Room(hotel_id=hotel4.id, room_name='Royal Suite', price_per_night=500.0, capacity=2, available_rooms=6,
                 description='Lavish suite with royal furnishings and city views',
                 image_url='https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=800')
    room6 = Room(hotel_id=hotel4.id, room_name='Palace Room', price_per_night=280.0, capacity=2, available_rooms=12,
                 description='Elegant room with classic decor and premium amenities',
                 image_url='https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=800')
    db.session.add_all([room5, room6])

    # Hotel 5: Urban Loft
    hotel5 = Hotel(
        name='Urban Loft Suites',
        description='Modern boutique hotel in the heart of downtown. Contemporary design meets urban sophistication.',
        address='250 Downtown Street',
        city='Tokyo',
        country='Japan',
        star_rating=4,
        image_url='https://images.unsplash.com/photo-1455587734955-081b22074882?w=800',
        amenities='Rooftop Bar, Modern Gym, Co-working Space, Smart Rooms, City Views'
    )
    db.session.add(hotel5)
    db.session.commit()

    # Rooms for Urban Loft
    room7 = Room(hotel_id=hotel5.id, room_name='Loft Suite', price_per_night=220.0, capacity=2, available_rooms=10,
                 description='Spacious loft with floor-to-ceiling windows',
                 image_url='https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=800')
    room8 = Room(hotel_id=hotel5.id, room_name='Studio', price_per_night=140.0, capacity=2, available_rooms=18,
                 description='Compact studio with modern minimalist design',
                 image_url='https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=800')
    db.session.add_all([room7, room8])

    # Hotel 6: Desert Oasis
    hotel6 = Hotel(
        name='Desert Oasis Resort',
        description='Luxury resort in the heart of the desert. Experience tranquility under the stars with premium amenities.',
        address='999 Dune Road',
        city='Dubai',
        country='UAE',
        star_rating=5,
        image_url='https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800',
        amenities='Infinity Pool, Desert Safari, Spa, Stargazing Deck, Premium Dining'
    )
    db.session.add(hotel6)
    db.session.commit()

    # Rooms for Desert Oasis
    room9 = Room(hotel_id=hotel6.id, room_name='Desert Villa', price_per_night=380.0, capacity=3, available_rooms=8,
                 description='Private villa with desert views and outdoor terrace',
                 image_url='https://images.unsplash.com/photo-1566195992011-5f6b21e539aa?w=800')
    room10 = Room(hotel_id=hotel6.id, room_name='Luxury Tent', price_per_night=250.0, capacity=2, available_rooms=15,
                  description='Glamping experience with modern luxury amenities',
                  image_url='https://images.unsplash.com/photo-1617859047452-8510bcf207fd?w=800')
    db.session.add_all([room9, room10])

    db.session.commit()

    print("✅ Successfully added all hotels!")
    print("\nHotels in database:")
    all_hotels = Hotel.query.all()
    for hotel in all_hotels:
        rooms_count = Room.query.filter_by(hotel_id=hotel.id).count()
        print(f"  - {hotel.name} in {hotel.city} ({rooms_count} rooms)")

    print(f"\nTotal: {len(all_hotels)} hotels")