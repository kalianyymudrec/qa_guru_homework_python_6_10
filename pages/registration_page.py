from selene import browser, be, have
from selene.core import command
from selene.support.shared.jquery_style import s, ss


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        s('#adplus-anchor').perform(command.js.remove)
        s('#fixedban').perform(command.js.remove)
        s('footer').perform(command.js.remove)

    def fill_first_name(self, value):
        s('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        s('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        s('#userEmail').should(be.blank).type(value)
        return self

    def fill_gender(self, value):
        s(f'input[value={value}] + label').perform(command.js.scroll_into_view).click()
        return self

    def fill_mobile_number(self, value):
        s('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__year-select').click()
        s(f'.react-datepicker__year-select option[value="{year}"]').click()
        s('.react-datepicker__month-select').click()
        s(f'.react-datepicker__month-select option[value="{month}"]').click()
        s(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subjects(self, *values):
        for value in values:
            s('#subjectsInput').type(value)
            ss('#subjectsWrapper div').element_by(have.exact_text(value)).click()
        return self

    def fill_hobbies(self, *values):
        for value in values:
            ss('#hobbiesWrapper label').element_by(have.exact_text(value)).click()
        return self

    def upload_picture(self, path_to_image):
        s('#uploadPicture').locate().send_keys(path_to_image)
        return self

    def fill_current_address(self, value):
        s('#currentAddress').type(value)
        return self

    def fill_state_and_city(self, state, city):
        s('#state').perform(command.js.scroll_into_view).click()
        ss('#state div').element_by(have.exact_text(state)).click()
        s('#city').click()
        ss('#city div').element_by(have.exact_text(city)).click()
        return self

    def submit(self):
        s('#submit').click()

    def should_have_registered(self, *table_rows):
        s('.modal-content').should(be.visible)
        ss('.modal-content td').should(have.exact_texts(*table_rows))