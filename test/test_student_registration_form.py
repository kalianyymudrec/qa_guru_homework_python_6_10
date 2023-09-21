import os

from pages.registration_page import RegistrationPage
from test.conftest import RES_DIR


def test_fill_out_and_submit_form():
    registration_page = RegistrationPage()

    registration_page.open()

    (
        registration_page
        .fill_first_name('Danila')
        .fill_last_name('Panov')
        .fill_email('danila.panov.02@mail.ru')
        .fill_gender('Male')
        .fill_mobile_number('0123456789')
        .fill_date_of_birth('2002', '08', '18')
        .fill_subjects('Maths', 'English')
        .fill_hobbies('Reading', 'Music')
        .upload_picture(os.path.join(RES_DIR, 'image.jpg'))
        .fill_current_address('Omsk')
        .fill_state_and_city(state='Haryana', city='Panipat')
    )

    registration_page.submit()

    registration_page.should_have_registered(
        ('Student Name', 'Danila Panov'),
        ('Student Email', 'danila.panov.02@mail.ru'),
        ('Gender', 'Male'),
        ('Mobile', '0123456789'),
        ('Date of Birth', '18 August,2002'),
        ('Subjects', 'Maths, English'),
        ('Hobbies', 'Reading, Music'),
        ('Picture', 'image.jpg'),
        ('Address', 'Omsk'),
        ('State and City', 'Haryana Panipat')
    )

