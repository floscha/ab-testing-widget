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
        'future-fstrings',
        'ipython',
        'matplotlib',
        'numpy',
        'pandas',
        'seaborn'
    ],
    zip_safe=False
)
