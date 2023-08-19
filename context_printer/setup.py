from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='context_printer',
   version='1.3.0',
   description='Tool for simple display of context in which each operation is executed.',
   license="",
   long_description=long_description,
   long_description_content_type="text/markdown",
   author="Bonvin Etienne, Rey Valérian",
   author_email="etienne.bonvin@epfl.ch, valerian.rey@epfl.ch",
   url="",
   package_dir={"context_printer": "context_printer"},
   packages=["context_printer"],
   include_package_data=True,
)
