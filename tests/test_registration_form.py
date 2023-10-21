from qa_guru_8_10.pages.registration_page import RegistrationPage
from qa_guru_8_10.data.users import User


def test_student_registration_form():
    user = User('Ivan',
                'Petrov',
                'ivanpetrov@example.com',
                'Male',
                '7999333221',
                '1996', 'October', '17',
                'Computer Science',
                'Reading',
                'cat_image.jpg',
                'Sovetskaya street, 15',
                'NCR',
                'Delhi')

    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.register(user=user)
    registration_page.should_have_registered(user=user)
