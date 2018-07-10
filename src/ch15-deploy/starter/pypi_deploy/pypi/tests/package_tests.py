import unittest
import unittest.mock
import pyramid.testing
import pyramid.httpexceptions

from pypi.data.releases import Release


class PackageControllerTests(unittest.TestCase):

    def test_package_details_success(self):
        # Arrange
        request = pyramid.testing.DummyRequest()
        request.matchdict = {'package_name': 'sqlalchemy'}
        from pypi.controllers.packages_controller import details
        from pypi.data.packages import Package
        test_package = Package()
        test_package.id = 'sqlalchemy'
        test_package.releases = [
            Release(),
            Release(),
        ]

        # Act
        with unittest.mock.patch('pypi.services.package_service.find_package_by_name',
                                 return_value=test_package):
            # noinspection PyTypeChecker
            model = details(request)

        # Assert
        package = model.get('package')
        self.assertIsNotNone(package)
        self.assertEqual(package.id, 'sqlalchemy')

    def test_package_details_404(self):
        # Arrange
        request = pyramid.testing.DummyRequest()
        request.matchdict = {'package_name': 'sqlalchemy_missing'}
        from pypi.controllers.packages_controller import details

        # Act
        with unittest.mock.patch('pypi.services.package_service.find_package_by_name',
                                 return_value=None):
            with self.assertRaises(pyramid.httpexceptions.HTTPNotFound):
                # noinspection PyTypeChecker
                details(request)
