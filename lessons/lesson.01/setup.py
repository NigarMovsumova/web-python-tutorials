import os
from setuptools import setup

# python setup.py bdist
#
# pip install wheel
# python setup.py bdist_wheel
# pip install .whl


setup(
    name='good',
    version='1.0',
    packages=['.good'],
    include_package_data=True,
    license='Test License',
    description='Test description',
    long_description='Long Test description',
    url='',
    author='NigarMovsum',
    author_email='movsum.nigar@gmail.com',
)
