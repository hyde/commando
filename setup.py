from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(
    name='commando',
    version='0.1.2a',
    author='Lakshmi Vyas',
    author_email='lakshmi.vyas@gmail.com',
    url='http://github.com/lakshmivyas/commando',
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
    install_requires = open('requirements.txt').read(),
)
