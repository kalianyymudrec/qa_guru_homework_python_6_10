import os

from selene import browser, be, have
from selene.core import command
from selene.support.shared.jquery_style import s, ss

from test.conftest import RES_DIR


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        s('#adplus-anchor').perform(command.js.remove)
        s('#fixedban').perform(command.js.remove)
        s('footer').perform(command.js.remove)

    def register(self, user):
        self._fill_first_name(user.first_name)
        self._fill_last_name(user.last_name)
        self._fill_email(user.email)
        self._fill_gender(user.gender)
        self._fill_mobile_number(user.mobile_number)
        self._fill_date_of_birth(user.date_of_birth)
        self._fill_subjects(user.subjects)
        self._fill_hobbies(user.hobbies)
        self._upload_picture(user.picture)
        self._fill_current_address(user.current_address)
        self._fill_state_and_city(user.state, user.city)
        self._submit()

    def should_have_registered(self, user):
        s('.modal-content').should(be.visible)
        ss('.modal-content td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.mobile_number}',
            '{0} {1},{2}'.format(user.date_of_birth.strftime("%d"),
                                 user.date_of_birth.strftime("%B"),
                                 user.date_of_birth.year),
            f'{", ".join(user.subjects)}',
            f'{", ".join(user.hobbies)}',
            f'{user.picture}',
            f'{user.current_address}',
            f'{user.state} {user.city}'
        ))

    def _fill_first_name(self, value):
        s('#firstName').should(be.blank).type(value)

    def _fill_last_name(self, value):
        s('#lastName').should(be.blank).type(value)

    def _fill_email(self, value):
        s('#userEmail').should(be.blank).type(value)

    def _fill_gender(self, value):
        s(f'input[value={value}] + label').perform(command.js.scroll_into_view).click()

    def _fill_mobile_number(self, value):
        s('#userNumber').should(be.blank).type(value)

    def _fill_date_of_birth(self, date):
        year = date.year
        month = date.month - 1
        day = date.strftime('%d')
        s('#dateOfBirthInput').click()
        s('.react-datepicker__year-select').click()
        s(f'.react-datepicker__year-select option[value="{year}"]').click()
        s('.react-datepicker__month-select').click()
        s(f'.react-datepicker__month-select option[value="{month}"]').click()
        s(f'.react-datepicker__day--0{day}').click()

    def _fill_subjects(self, values):
        for value in values:
            s('#subjectsInput').type(value)
            ss('#subjectsWrapper div').element_by(have.exact_text(value)).click()

    def _fill_hobbies(self, values):
        for value in values:
            ss('#hobbiesWrapper label').element_by(have.exact_text(value)).click()

    def _upload_picture(self, value):
        path_to_image = os.path.join(RES_DIR, value)
        s('#uploadPicture').locate().send_keys(path_to_image)

    def _fill_current_address(self, value):
        s('#currentAddress').type(value)

    def _fill_state_and_city(self, state, city):
        s('#state').perform(command.js.scroll_into_view).click()
        ss('#state div').element_by(have.exact_text(state)).click()
        s('#city').click()
        ss('#city div').element_by(have.exact_text(city)).click()

    def _submit(self):
        s('#submit').click()
