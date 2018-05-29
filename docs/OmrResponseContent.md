# OmrResponseContent

```
Represents information about part of the text.
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** | GUID string that is used to identify template on server This value is assigned after Template Correction and used later in Template Finalization and Image Recognition | [optional] 
**execution_time** | **float** | Indicates how long it took to perform task on server. | 
**response_files** | [**list[FileInfo]**](FileInfo.md) | This structure holds array of files returned in response Type and content of files differes depending on action | [optional] 
**info** | [**OmrResponseInfo**](OmrResponseInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


