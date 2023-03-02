from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in trial_balance_by_multi_account/__init__.py
from trial_balance_by_multi_account import __version__ as version

setup(
	name="trial_balance_by_multi_account",
	version=version,
	description="Trial Balance By Multi Account Report",
	author="Smart Solutions",
	author_email="ahmed.younis_6@hotmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
