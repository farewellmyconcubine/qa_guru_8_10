from selene import browser, be, have
import os

def test_student_registration_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Petrov')
    browser.element('#userEmail').type('ivanpetrov@example.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('79991112233')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="3"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="2000"]').click()
    browser.element('.react-datepicker__day--015').click()
    browser.element('#subjectsInput').type('Engli').press_enter().type('Chem').press_enter()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../../qa_guru_8_5/tests/images/cat_image.jpg'))
    browser.element('#currentAddress').type('Pushkina 44, Moscow, Russia')
    browser.element('#react-select-3-input').type('Raja').press_enter()
    browser.element('#react-select-4-input').type('Jaip').press_enter()
    browser.element('#submit').click()


    browser.element('.table').all('tr td:nth-child(2)').should(have.texts
    (
    'Ivan Petrov',
    'ivanpetrov@example.com',
    'Male',
    '7999111223',
    '15 Apri,2000',
    'English, Chemistry',
    'Reading',
    'cat_image.jpg',
    'Pushkina 44, Moscow, Russia',
    'Rajasthan Jaipur'
    ))



