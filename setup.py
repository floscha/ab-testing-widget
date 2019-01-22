from setuptools import setup


setup(
    name='abtesting',
    version='0.0.1',
    description='A Jupyter widget for analyzing A/B tests',
    url='https://github.com/floscha/ab-testing-widget/',
    author='Florian Schäfer',
    author_email='florian.joh.schaefer@gmail.com',
    license='MIT',
    packages=['abtesting'],
    install_requires=[
        'future-fstrings==0.4.5',
        'ipython==6.5.0',
        'matplotlib==2.2.3',
        'numpy==1.16.0',
        'pandas==0.22.0',
        'seaborn==0.9.0'
    ],
    zip_safe=False
)
