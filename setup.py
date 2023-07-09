from setuptools import setup, find_packages

setup(
    name='Package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='<JC Els>',
    author_email='<jels@wesbank.co.za>'

)