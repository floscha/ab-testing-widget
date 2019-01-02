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
        'ipython==7.2.0',
        'matplotlib==3.0.2',
        'numpy==1.15.4',
        'seaborn==0.9.0'
    ],
    zip_safe=False
)
