from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup

setup(
    name='commando',
    description='A declarative interface to argparse with additional utilities',
    long_description='Adds decorators that allow subcommands to be defined as simple functions',

    version='0.3a',

    author='Lakshmi Vyas',
    author_email='lakshmi.vyas@gmail.com',
    url='http://github.com/lakshmivyas/commando',

    packages=['commando'],
    requires=['python (>= 2.7)'],
    provides=['commando'],
    test_requires=['nose', 'mock'],

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
