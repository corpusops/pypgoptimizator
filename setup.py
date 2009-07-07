from setuptools import setup, find_packages


readme = open('README.txt').read()

setup(
    name='pypgoptimizator',
    version="1.0",
    description='Postgresql configuration optimizator',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    license='BSD',
    include_package_data=True,
    long_description=reame,
    install_requires=[
    'steuptools'
    ],
    entry_points = {
    'console_scripts': [
    'pypgoptimizator = pypgoptimizator:main',
    ],

)
