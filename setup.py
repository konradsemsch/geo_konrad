from setuptools import setup, find_packages
 
setup(name = 'geo_konrad',
      version = '0.1',
      url = 'https://github.com/konradsemsch/geo_konrad',
      license = 'MIT',
      author = 'Konrad Semsch',
      author_email = 'konrad.semsch@gmail.com',
      description = 'An example of how to prepare raw Python code as a package ready for distribution',
      packages = ['geo_konrad'],
      install_requires=[
          'geopy'
      ],
      long_description = open('README.md').read(),
      zip_safe = False)