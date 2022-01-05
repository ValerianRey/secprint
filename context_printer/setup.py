from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='context_printer',
   version='2.0.0',
   description='Tool for simple display of context in which each operation is executer.',
   license="",
   long_description=long_description,
   long_description_content_type="text/markdown",
   author="Bonvin Etienne, Rey Valérian, Robin Richard",
   author_email="etienne.bonvin@epfl.ch, valerian.rey@epfl.ch, raisin@ecomail.fr",
   url="",
   package_dir = {"context_printer": "context_printer"},
   packages=["context_printer"],
   include_package_data=True,
)
