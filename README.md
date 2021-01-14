![](https://img.shields.io/badge/api-v3.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/aspose-omr-cloud) ![PyPI - Format](https://img.shields.io/pypi/format/aspose-omr-cloud) ![PyPI - Downloads](https://img.shields.io/pypi/dm/aspose-omr-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aspose-omr-cloud) [![GitHub license](https://img.shields.io/github/license/aspose-omr-cloud/aspose-omr-cloud-python)](https://github.com/aspose-omr-cloud/aspose-omr-cloud-php/blob/master/LICENSE) ![GitHub last commit](https://img.shields.io/github/last-commit/Aspose-omr-Cloud/aspose-omr-cloud-python)

# Python REST API for OMR Processing
[Aspose.OMR for Cloud](https://products.aspose.cloud/omr/) is a REST API that helps you to perform optical mark recognition in the cloud. We provide a series of [SDKs](https://github.com/aspose-omr-cloud). Along with that, you can get [binaries](https://github.com/aspose-omr-cloud/aspose-omr-cloud-dotnet/releases) to start working immediately and recognize various OMR forms.

Developers can embed [optical recognition](https://en.wikipedia.org/wiki/Optical_mark_recognition) in any type of application to extract data from images of tests, exams, questionnaires, surveys, etc. In the repository you can find examples on how to start using [Aspose.OMR API](https://docs.aspose.cloud/omr/omr-api-specification/) in your project.

## OMR Processing Features

- Perform recognition of scanned photos and images for OMR operations.
- Ability to perform OMR on rotated & perspective (within 25 deg) photos.
- Extract & recognize human-marked data from scanned tests, exams, surveys, etc.
- Supports the export of OMR results to CSV file format.
- Use textual markup to generate OMR templates, generate surveys, and test sheets.
- Availability of GUI application for managing OMR templates.
- Specify the number of OMR based questions & answers in the template.
- Availability of GUI OMR editor as a cloud client.
- Provide JSON rules to perform OMR answer grading.
- Clip an area of interest from an image, save it as JPEG & perform OMR on it.
- Perform highly accurate optical mark recognition (OMR).

## Save OMR As
CSV

## Read OMR Formats
JPEG, PNG, BMP, TIFF, PDF
## How to use the SDK?

Our API is completely independent of your operating system, database system, or development language. You can use any language and platform that supports HTTP to interact with our API. However, manually writing client code can be difficult, error-prone, and time-consuming. Therefore, we have provided and support [SDKs](https://github.com/aspose-omr-cloud) in many development languages to make it easier to integrate with us.

## Examples

```python
import asposeomrcloud.apis.storage_api as storage_api
from asposeomrcloud.configuration import Configuration
from asposeomrcloud.apis.omr_api import OmrApi
from asposeomrcloud.models import OmrFunctionParam

def run_demo():

    configuration = Configuration(apiKey=config.get('app_key'), appSid=config.get('app_sid'))

    api = OmrApi(configuration)
    storage = storage_api.StorageApi(configuration)

    # Step 1: Upload demo files on cloud and Generate template
    print("\t\tUploading demo files...")
    upload_demo_files(storage, data_dir)
    print("\t\tGenerate template...")
    res_gen = generate_template(api, storage, os.path.join(data_dir, TEMPLATE_DST_NAME), LOGOS_FOLDER_NAME)
    if res_gen.error_code == 0:
        deserialize_files(res_gen.payload.result.response_files, PATH_TO_OUTPUT)

    # Step 2: Validate template
    print("\t\tValidate template...")
    template_id = validate_template(api, storage, os.path.join(PATH_TO_OUTPUT, TEMPLATE_IMAGE_NAME), PATH_TO_OUTPUT)

    # Step 3: Recognize photos and scans
    print("\t\tRecognize image...")
    for user_image in TEMPLATE_USER_IMAGES_NAMES:
        res_rec = recognize_image(api, storage, template_id, os.path.join(data_dir, user_image))
        if res_rec.error_code == 0:
            result_file = deserialize_files(res_rec.payload.result.response_files, PATH_TO_OUTPUT)[0]
            print('Result file %s' % result_file)
```
_________________________


## Quickstart
Make your solution using [SDK](https://github.com/aspose-omr-cloud), follow these steps:

#### 1. Clone from Github

Clone the solution using the command:
```sh
git clone git@github.com:aspose-omr-cloud/aspose-omr-cloud-python.git --recurse-submodules
```

#### 2. Get API keys if you haven't

Make a personal account on [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/) and click _Get Keys_. These keys are useful for all OMR Cloud products. If you have any trouble, look at this [detailed manual](https://docs.aspose.cloud/omr/quickstart/).

#### 3. Install SDK

Install `aspose-omr-cloud` with [PIP](https://pypi.org/project/pip/) from [PyPI](https://pypi.org/) by:

```sh
pip install aspose-omr-cloud
```

Or clone repository and install it via [Setuptools](http://pypi.python.org/pypi/setuptools):

```sh
python setup.py install
```

#### 4. Run Demo

  * Checkout the SDK or get from PyPi
  * Set Your AppSid & AppKey
  * Run `run_demo.py`

---------------------------

### Structure

This project includes:

- Module "asposeomrcloud", this is SDK. You can integrate it in your application. It contains both `Omr` and `Storage` `API`
- Module "demo". Sample API requests.
- Module "test", unittests. You can take a look at them to see various code examples.

### Dependencies
- See requirements.txt

## Versions support:
- Python :: 3.6
- Python :: 3.7
- Python :: 3.8
- Python :: 3.9

_________________________

## OMR Cloud SDKs

||||||||
|--------------|----------|-------|-------|-------|---------|---------|
|[.NET](https://github.com/aspose-omr-cloud/aspose-omr-cloud-dotnet)|[Java](https://github.com/aspose-omr-cloud/aspose-omr-cloud-java)|[PHP](https://github.com/aspose-omr-cloud/aspose-omr-cloud-php)|[Ruby](https://github.com/aspose-omr-cloud/aspose-omr-cloud-ruby)|[Python](https://github.com/aspose-omr-cloud/aspose-omr-cloud-python)|[Node.js](https://github.com/aspose-omr-cloud/aspose-omr-cloud-nodejs)|[Perl](https://github.com/aspose-omr-cloud/aspose-omr-cloud-perl)

## Documentation for API Endpoints

All URIs are relative to *https://api.aspose.cloud/v3.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OmrApi* | **post_run_omr_task** | **POST** /omr/{name}/runOmrTask | Run specific OMR task


## Authentication

Library uses OAUTH2 internally

## Aspose.OMR Cloud SDKs in Popular Languages

| .NET | Java | PHP | Python | Ruby | Node.js |
|---|---|---|---|---|---|
| [GitHub](https://github.com/aspose-omr-cloud/aspose-omr-cloud-dotnet) | [GitHub](https://github.com/aspose-omr-cloud/aspose-omr-cloud-java) | [GitHub](https://github.com/aspose-omr-cloud/aspose-omr-cloud-php) | [GitHub](https://github.com/aspose-omr-cloud/aspose-omr-cloud-python) | [GitHub](https://github.com/aspose-omr-cloud/aspose-omr-cloud-ruby)  | [GitHub](https://github.com/aspose-omr-cloud/aspose-omr-cloud-node) |
| [NuGet](https://www.nuget.org/packages/Aspose.omr-Cloud/) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-omr-cloud) | [Composer](https://packagist.org/packages/aspose/aspose-omr-cloud) | [PIP](https://pypi.org/project/aspose.omr-cloud/) | [GEM](https://rubygems.org/gems/aspose_omr_cloud)  | [NPM](https://www.npmjs.com/package/aspose-omr-cloud) |

[Product Page](https://products.aspose.cloud/omr/python) | [Documentation](https://docs.aspose.cloud/display/omrcloud/Home) | [API Reference](https://apireference.aspose.cloud/omr/) | [Code Samples](https://github.com/aspose-omr-cloud/aspose-omr-cloud-python) | [Blog](https://blog.aspose.cloud/category/omr/) | [Free Support](https://forum.aspose.cloud/c/omr) | [Free Trial](https://dashboard.aspose.cloud/#/apps)|
