# coding: utf-8

from setuptools import setup, find_packages
from os import path

NAME = "aspose-omr-cloud"
VERSION = "20.10"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "pyopenssl", "idna", "urllib3[secure]", "python-dateutil",
            "requests[security]"]

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description='Aspose.OMR Cloud SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Aspose Pty Ltd',
    author_email='aspose.cloud@asposeptyltd.com',
    url="https://github.com/aspose-omr-cloud/aspose-omr-cloud-python",
    license='MIT',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 3.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

        'Topic :: Software Development :: Libraries :: Python Modules',
        "Operating System :: OS Independent"
    ],
    keywords=["Aspose.OMR Cloud API Reference", "Aspose", "OMR", "OMR Cloud"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True
    # long_description="""
    # Aspose.OMR Cloud API Reference
    # This package contains Aspose.OMR Cloud SDK for Python.
    # This SDK allows you to work with Aspose.OMR Cloud REST APIs in your Python applications, and integrate OMR functionality in few steps.
    #
    # Aspose.OMR for Cloud is a REST API that helps you to perform optical mark recognition in the cloud. We provide a series of SDKs. Along with that, you can get binaries to start working immediately and recognize various OMR forms.
    #
    # Developers can embed optical recognition in any type of application to extract data from images of tests, exams, questionnaires, surveys, etc. In the repository you can find examples on how to start using Aspose.OMR API in your project.
    # """
)
