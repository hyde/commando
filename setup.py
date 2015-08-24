from setuptools import setup

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''


setup(
    name='commando',
    description='A declarative interface to argparse and extras.',
    long_description=long_description,

    version='1.0.0',

    author='Lakshmi Vyas',
    author_email='lakshmi.vyas@gmail.com',
    url='http://github.com/hyde/commando',

    packages=['commando'],
    requires=['python (>= 2.7)'],
    provides=['commando'],
    test_requires=['nose', 'mock', 'fswrap', 'markdown', 'yaml'],

    license='MIT',

    keywords=('argparse commandline utility'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    test_suite='nose.collector',
)
