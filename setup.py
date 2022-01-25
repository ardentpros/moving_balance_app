from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in moving_balance/__init__.py
from moving_balance import __version__ as version

setup(
	name="moving_balance",
	version=version,
	description="Simple Document uncleared final balance on transist",
	author="Jide and Co (clone from ghorz)",
	author_email="appmail@mail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
