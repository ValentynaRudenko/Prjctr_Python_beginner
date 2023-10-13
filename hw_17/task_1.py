from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import Date, ForeignKey, Double

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
import os
from dotenv import load_dotenv
load_dotenv()

password = os.getenv('password')


Base = declarative_base()


class Users(Base):
    __tablename__ = 'abn_user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    user_type = Column(String(10), nullable=False)

    def __repr__(self):
        return (f'User {self.username} email: {self.email},'
                f'phone: {self.phone}, type: {self.user_type}')


class Rooms(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)
    abn_user_id = Column(Integer, ForeignKey('abn_user.id'))
    price_night = Column(Double, nullable=False)
    amount_of_residents = Column(Integer, nullable=False)
    n_of_rooms = Column(Integer, nullable=False)
    n_of_beds = Column(Integer, nullable=False)
    air_conditioning = Column(Boolean, nullable=False)

    abn_user = relationship('Users')


class Reservations(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True)
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    abn_user_id = Column(Integer, ForeignKey('abn_user.id'), nullable=False)

    room = relationship('Rooms')
    abn_user = relationship('Users')


DATABASE_URL = 'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(
    DATABASE_URL.format(
        host='localhost',
        database='postgres',
        user='valentyna',
        password='password',
        port=5432
    )
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()


#  get the users who reserved the room with id == 1
results = session.query(Users)\
                  .join(Reservations, Users.id == Reservations.abn_user_id)\
                  .join(Rooms, Reservations.room_id == Rooms.id)\
                  .filter(Rooms.id == 1)\
                  .all()


for user in results:
    print(f"user_id {user.id}, name {user.username}")
