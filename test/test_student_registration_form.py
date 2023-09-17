import datetime

from pages.registration_page import RegistrationPage
from models.users import User


def test_register_user():

    registration_page = RegistrationPage()

    ivan = User(
        first_name='Danila',
        last_name='Panov',
        email='danila.panov.02@mail.ru',
        gender='Male',
        mobile_number='0123456789',
        date_of_birth=datetime.date(2002, 8, 18),
        subjects=('Maths', 'Physics'),
        hobbies=('Reading', 'Music'),
        picture='image.jpg',
        current_address='Omsk',
        state='Haryana',
        city='Panipat'
    )

    registration_page.open()

    registration_page.register(ivan)

    registration_page.should_have_registered(ivan)
