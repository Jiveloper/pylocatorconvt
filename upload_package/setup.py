from setuptools import setup, find_packages

setup(
    name             = 'pylocatorconvt',
    version          = '1.0.1',
    description      = 'Appium Inspector Locator Creation Helper',
    author           = 'jiwon.lee',
    author_email     = 'easyone.jio@gmail.com',
	include_package_data=True,
	packages=find_packages(),
    keywords         = ['LOCATORCONVERTER', 'locatorconverter'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 