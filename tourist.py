from peewee import *
from random import randint as rdt

db = SqliteDatabase('tourist.db')

class inner_flights(Model):
    id = PrimaryKeyField(column_name="id")
    from_region = CharField(max_length=255, column_name="from_region", default="No name")
    to_destination = CharField(max_length=255, column_name="to_destionation", default="No name")
    company = CharField(max_length=255, column_name="company", default="No name")
    quantity = IntegerField(null=True, column_name="quantity")

    class Meta:
        database = db

flight = {1:"Грузовой",
          2:"Пассажирский"
          }

class outter_flights(Model):
    id = PrimaryKeyField(column_name="id")
    from_country = CharField(max_length=255, column_name="from_country", default="No name")
    flight_type = CharField(max_length=255, column_name="flight_type", default="No name")
    company = CharField(max_length=255, column_name="company", default="No name")
    neighbors = IntegerField(null=True, column_name="neighbors")

    class Meta:
        database = db


countries = (
    'Brazil',
    'China',
    'Argentina',
    'Korea',
    'Germany',
    'USA',
    'UK',
    'Russia',
    'Japan'
)

company = ('Air Turkish',
           'China air',
           'British air',
           'Aeroflot',
           'Air Japan')


flights = ("Грузовой",
          "Пассажирский")

for i in range(1,16):
    n = rdt(0,1)
    quanrnd = rdt(10,200)
    rowN = inner_flights.create(id = i, from_region = f'\'{countries[rdt(0, len(countries)-1)]}\'', to_destination= f'\'{countries[rdt(0, len(countries)-1)]}\'',
                                company = f'\'{company[rdt(0, len(company)-1)]}\'',
                                quantity=f'{quanrnd}')

#
# for i in range(1,16):
#     n = rdt(0,1)
#     quanrnd = rdt(1,10)
#     rowN = outter_flights.create(
#                                 # id = i,
#                                 from_country = f'\'{countries[rdt(0, len(countries)-1)]}\'',
#                                 flight_type= f'\'{flights[rdt(0, len(flights)-1)]}\'',
#                                 company = f'\'{company[rdt(0, len(company)-1)]}\'',
#                                 neighbors=f'{quanrnd}'
#                                  )


db.connect()
db.commit()
db.close()