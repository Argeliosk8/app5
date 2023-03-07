from app import db
from models import *
'''
all_vehicles = Vehicle.query.all()

for vehicle in all_vehicles:
    print(vehicle.brand)

    u1 = User(username = 'Argelio', email = 'argelio@gmail.com', password_hash = 'Python2023$')

db.session.add(u1)
db.session.commit()

all_users = User.query.all()

for user in all_users:
    print(user.username)
    print(user.email)

'''
all_users = User.query.all()

for user in all_users:
    print(user.username)
    print(user.email)
    print(user.password_hash)
