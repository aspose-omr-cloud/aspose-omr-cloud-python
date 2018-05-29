# asposeomrcloud.OmrApi

All URIs are relative to *https://localhost/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_run_omr_task**](OmrApi.md#post_run_omr_task) | **POST** /omr/{name}/runOmrTask | Run specific OMR task


# **post_run_omr_task**
> OMRResponse post_run_omr_task(name, action_name, param=param, storage=storage, folder=folder)

Run specific OMR task

### Example 
```python
from __future__ import print_function
import time
import asposeomrcloud
from asposeomrcloud.rest import ApiException
from pprint import pprint

APP_KEY = 'xxxxx'
APP_SID = 'xxxxx'
# create an instance of the API class
api_instance = asposeomrcloud.OmrApi(APP_KEY, APP_SID, 'https://api.aspose.cloud/v1.1')
name = 'name_example' # str | Name of the file to recognize.
action_name = 'action_name_example' # str | Action name ['CorrectTemplate', 'FinalizeTemplate', 'RecognizeImage']
param = asposeomrcloud.OMRFunctionParam() # OMRFunctionParam | Function params, specific for each actionName (optional)
storage = 'storage_example' # str | Image's storage. (optional)
folder = 'folder_example' # str | Image's folder. (optional)

try: 
    # Run specific OMR task
    api_response = api_instance.post_run_omr_task(name, action_name, param=param, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OmrApi->post_run_omr_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the file to recognize. | 
 **action_name** | **str**| Action name [&#39;CorrectTemplate&#39;, &#39;FinalizeTemplate&#39;, &#39;RecognizeImage&#39;] | 
 **param** | [**OMRFunctionParam**](OMRFunctionParam.md)| Function params, specific for each actionName | [optional] 
 **storage** | **str**| Image&#39;s storage. | [optional] 
 **folder** | **str**| Image&#39;s folder. | [optional] 

### Return type

[**OMRResponse**](OMRResponse.md)

### Authorization

Library uses OAUTH2 authorization internally

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

