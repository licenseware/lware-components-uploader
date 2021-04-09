from setuptools import setup, find_packages

#Distribute py wheels
#python3 setup.py bdist_wheel sdist
#twine check dist/*
#cd dist 
#twine upload *

with open("README.md", "r") as fh:
    long_description = fh.read()


setup (
	name="uploader",
	version="0.0.1",
	description="Files uploader registration.",
	url="https://github.com/licenseware/lware-components-uploader",
	author="licenseware",
	author_email="contact@licenseware.io",
	license='',
	py_modules=["uploader"],
	install_requires=[],
	packages=find_packages(exclude=("tests",)),
	long_description=long_description,
    long_description_content_type="text/markdown",
	package_dir={"":"src"}
)