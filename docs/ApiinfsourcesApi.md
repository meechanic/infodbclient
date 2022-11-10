# infodbclient.ApiinfsourcesApi

All URIs are relative to *http://localhost:8002*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiinfsources_create**](ApiinfsourcesApi.md#apiinfsources_create) | **POST** /apiinfsources/ | 
[**apiinfsources_delete**](ApiinfsourcesApi.md#apiinfsources_delete) | **DELETE** /apiinfsources/{id}/ | 
[**apiinfsources_list**](ApiinfsourcesApi.md#apiinfsources_list) | **GET** /apiinfsources/ | 
[**apiinfsources_partial_update**](ApiinfsourcesApi.md#apiinfsources_partial_update) | **PATCH** /apiinfsources/{id}/ | 
[**apiinfsources_read**](ApiinfsourcesApi.md#apiinfsources_read) | **GET** /apiinfsources/{id}/ | 
[**apiinfsources_update**](ApiinfsourcesApi.md#apiinfsources_update) | **PUT** /apiinfsources/{id}/ | 


# **apiinfsources_create**
> Infsource apiinfsources_create(data)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import infodbclient
from infodbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = infodbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = infodbclient.ApiinfsourcesApi(infodbclient.ApiClient(configuration))
data = infodbclient.Infsource() # Infsource | 

try:
    api_response = api_instance.apiinfsources_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiinfsourcesApi->apiinfsources_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Infsource**](Infsource.md)|  | 

### Return type

[**Infsource**](Infsource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiinfsources_delete**
> apiinfsources_delete(id)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import infodbclient
from infodbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = infodbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = infodbclient.ApiinfsourcesApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this infsource.

try:
    api_instance.apiinfsources_delete(id)
except ApiException as e:
    print("Exception when calling ApiinfsourcesApi->apiinfsources_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this infsource. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiinfsources_list**
> list[Infsource] apiinfsources_list(name=name, search=search, ordering=ordering)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import infodbclient
from infodbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = infodbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = infodbclient.ApiinfsourcesApi(infodbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apiinfsources_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiinfsourcesApi->apiinfsources_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Infsource]**](Infsource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiinfsources_partial_update**
> Infsource apiinfsources_partial_update(id, data)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import infodbclient
from infodbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = infodbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = infodbclient.ApiinfsourcesApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this infsource.
data = infodbclient.Infsource() # Infsource | 

try:
    api_response = api_instance.apiinfsources_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiinfsourcesApi->apiinfsources_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this infsource. | 
 **data** | [**Infsource**](Infsource.md)|  | 

### Return type

[**Infsource**](Infsource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiinfsources_read**
> Infsource apiinfsources_read(id)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import infodbclient
from infodbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = infodbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = infodbclient.ApiinfsourcesApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this infsource.

try:
    api_response = api_instance.apiinfsources_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiinfsourcesApi->apiinfsources_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this infsource. | 

### Return type

[**Infsource**](Infsource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiinfsources_update**
> Infsource apiinfsources_update(id, data)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import infodbclient
from infodbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = infodbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = infodbclient.ApiinfsourcesApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this infsource.
data = infodbclient.Infsource() # Infsource | 

try:
    api_response = api_instance.apiinfsources_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiinfsourcesApi->apiinfsources_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this infsource. | 
 **data** | [**Infsource**](Infsource.md)|  | 

### Return type

[**Infsource**](Infsource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

