from setuptools import setup

# python setup.py bdist
# pip install wheel
# pip3 install wheel
# python setup.py bdist_wheel
# pip install .whl


setup(
    name='pets',
    version='1.0',
    packages=['.pets'],
    include_package_data=True,
    license='Test License',
    description='Test description',
    long_description='Long Test description',
    url='',
    author='NigarMovsum',
    author_email='movsum.nigar@gmail.com',
)
