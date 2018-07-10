import unittest
import unittest.mock
import pyramid.testing


class AccountControllerTests(unittest.TestCase):

    def test_register_validation_valid(self):
        # 3 A's of test: Arrange, Act, then Assert

        # Arrange
        from pypi.viewmodels.account.register_viewmodel import RegisterViewModel
        request = pyramid.testing.DummyRequest()
        request.POST = {
            'name': 'Michael',
            'email': 'michael@talkpython.fm',
            'password': 'a'
        }
        # noinspection PyTypeChecker
        vm = RegisterViewModel(request)

        # Act
        target = 'pypi.services.user_service.find_user_by_email'
        with unittest.mock.patch(target, return_value=None):
            vm.validate()

        # Assert:
        self.assertIsNone(vm.error)

    def test_register_validation_existing_user(self):
        # Arrange
        from pypi.viewmodels.account.register_viewmodel import RegisterViewModel
        from pypi.data.users import User
        request = pyramid.testing.DummyRequest()
        request.POST = {
            'name': 'Michael',
            'email': 'michael@talkpython.fm',
            'password': 'a'
        }
        # noinspection PyTypeChecker
        vm = RegisterViewModel(request)

        # Act
        target = 'pypi.services.user_service.find_user_by_email'
        with unittest.mock.patch(target, return_value=User()):
            vm.validate()

        # Assert:
        self.assertIsNotNone(vm.error)
        self.assertTrue('exist' in vm.error)

    def test_register_validation_no_email(self):
        # Arrange
        from pypi.viewmodels.account.register_viewmodel import RegisterViewModel
        request = pyramid.testing.DummyRequest()
        request.POST = {
            'email': '',
            'password': 'a'
        }
        # noinspection PyTypeChecker
        vm = RegisterViewModel(request)

        # Act
        vm.validate()

        # Assert:
        self.assertIsNotNone(vm.error)
        self.assertTrue('email' in vm.error)
