# -*- coding: utf-8 -*-
import commando
from distutils.core import setup

setup(
    name='commando',
    version=commando.__version__,
    author='Lakshmi Vyas',
    author_email='lakshmi.vyas@gmail.com',
    url='http://ringce.com/commando/',
    description='A declarative interface for argparse',
    long_description = 'Adds decorators that allow subcommands to be defined as simple functions',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    py_modules=['commando'],
)
