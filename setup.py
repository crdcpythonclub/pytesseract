import os
from setuptools import setup


longDesc = ""
if os.path.exists("README.md"):
	longDesc = open("README.md").read().strip()

setup(
    name = "pytesseract",
    version = "0.1.6",
    author = "Samuel Hoffstaetter - Forked by Python Club",
    author_email="",
    maintainer = "cartman",
    maintainer_email = "cartman.djw@gmail.com",
    description = ("Python-tesseract is a python wrapper for google's Tesseract-OCR"),
    long_description = longDesc,
    license = "GPLv3",
    keywords = "python-tesseract OCR Python",
    url = "https://github.com/crdcpythonclub/pytesseract",
    packages=['pytesseract'],
    package_dir={'pytesseract': 'src'},
    package_data = {'pytesseract': ['*.png','*.jpg']},
    entry_points = {'console_scripts': ['pytesseract = pytesseract.pytesseract:main']},
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
