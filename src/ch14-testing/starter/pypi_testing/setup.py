import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'passlib==1.7.4',
    'plaster_pastedeploy==1.0.1',
    'progressbar2==4.2.0',
    'pyramid==2.0.2',
    'pyramid_chameleon==0.3',
    'pyramid_debugtoolbar==4.10',
    'python-dateutil==2.8.2',
    'sqlalchemy==2.0.20',
    'waitress==2.1.2',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup(
    name='pypi',
    version='0.0',
    description='Python Package Index',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = pypi:main',
        ],
    },
)
