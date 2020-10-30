# Aspose.OMR for Cloud

[Aspose.OMR for Cloud](https://products.aspose.cloud/omr/) is a REST API that helps you to perform optical mark recognition in the cloud. We provide a series of [SDKs](https://github.com/aspose-omr-cloud). Along with that, you can get `binaries` to start working immediately and recognize various OMR forms.

Developers can embed [optical recognition](https://en.wikipedia.org/wiki/Optical_mark_recognition) in any type of application to extract data from images of tests, exams, questionnaires, surveys, etc. In the repository you can find examples on how to start using [Aspose.OMR API](https://docs.aspose.cloud/omr/omr-api-specification/) in your project.

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

Clone the solution using the command: `git clone git@github.com:aspose-omr-cloud/aspose-omr-cloud-python.git --recurse-submodules`

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

## Author

Aspose Pty Ltd (https://www.aspose.com)

## Resources

+ **Website:** [www.aspose.com](https://www.aspose.com/)
+ **Product Home:** [Aspose.OMR for Cloud](https://products.aspose.cloud/omr)
+ **Documentation:** [Aspose.OMR for Cloud Documentation](https://docs.aspose.cloud/omr/)
+ **Cloud Dashboard:** [Aspose Cloud](https://dashboard.aspose.cloud/)
+ **Forum:** [Aspose.OMR for Cloud Forum](https://forum.aspose.cloud/c/omr)
+ **PyPi:** [Aspose.OMR-Cloud](https://pypi.org/project/aspose-omr-cloud/)