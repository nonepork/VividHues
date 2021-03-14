from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='VividHues',
    url='https://github.com/KennyOliver/VividHues',
    author='Kenneth Oliver',
    author_email='kenny_oliver@icloud.com',
    # Needed to actually package something
    packages=['VividHues'],
    # Needed for dependencies
    #install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='2.5.1',
    # The license can be anything you like
    license='AGPL',
    description='VividHues is a lightweight Python module for coloured strings in the Python console!',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)