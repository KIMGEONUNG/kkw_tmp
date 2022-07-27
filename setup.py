from setuptools import setup

setup(
   name='pycomar',
   version='0.6.18',
   description='This is comar\'s python libray for personal purpose',
   author='KimGeonUng',
   author_email='saywooong@gmail.com',
   packages=['pycomar', 'pycomar.images', 'pycomar.io',
       'pycomar.utils'],  #same as name
   # install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
)
