from setuptools import setup, find_packages

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='contextprinter',
   version='1.0.1',
   description='Tool for simple and appealing display of context in which each operation is executer',
   license="",
   long_description=long_description,
   long_description_content_type="text/markdown",
   author='Bonvin Etienne, Rey Valérian',
   author_email='etienne.bonvin@epfl.ch, valerian.rey@epfl.ch',
   url="",
   packages=["contextprinter"]
)
