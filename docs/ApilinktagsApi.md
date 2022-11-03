# infodbclient.ApilinktagsApi

All URIs are relative to *http://localhost:8002*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apilinktags_create**](ApilinktagsApi.md#apilinktags_create) | **POST** /apilinktags/ | 
[**apilinktags_delete**](ApilinktagsApi.md#apilinktags_delete) | **DELETE** /apilinktags/{id}/ | 
[**apilinktags_list**](ApilinktagsApi.md#apilinktags_list) | **GET** /apilinktags/ | 
[**apilinktags_partial_update**](ApilinktagsApi.md#apilinktags_partial_update) | **PATCH** /apilinktags/{id}/ | 
[**apilinktags_read**](ApilinktagsApi.md#apilinktags_read) | **GET** /apilinktags/{id}/ | 
[**apilinktags_update**](ApilinktagsApi.md#apilinktags_update) | **PUT** /apilinktags/{id}/ | 


# **apilinktags_create**
> LinkTag apilinktags_create(data)



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
api_instance = infodbclient.ApilinktagsApi(infodbclient.ApiClient(configuration))
data = infodbclient.LinkTag() # LinkTag | 

try:
    api_response = api_instance.apilinktags_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApilinktagsApi->apilinktags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**LinkTag**](LinkTag.md)|  | 

### Return type

[**LinkTag**](LinkTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apilinktags_delete**
> apilinktags_delete(id)



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
api_instance = infodbclient.ApilinktagsApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this link tag.

try:
    api_instance.apilinktags_delete(id)
except ApiException as e:
    print("Exception when calling ApilinktagsApi->apilinktags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this link tag. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apilinktags_list**
> list[LinkTag] apilinktags_list(name=name, search=search, ordering=ordering)



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
api_instance = infodbclient.ApilinktagsApi(infodbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apilinktags_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApilinktagsApi->apilinktags_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[LinkTag]**](LinkTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apilinktags_partial_update**
> LinkTag apilinktags_partial_update(id, data)



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
api_instance = infodbclient.ApilinktagsApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this link tag.
data = infodbclient.LinkTag() # LinkTag | 

try:
    api_response = api_instance.apilinktags_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApilinktagsApi->apilinktags_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this link tag. | 
 **data** | [**LinkTag**](LinkTag.md)|  | 

### Return type

[**LinkTag**](LinkTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apilinktags_read**
> LinkTag apilinktags_read(id)



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
api_instance = infodbclient.ApilinktagsApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this link tag.

try:
    api_response = api_instance.apilinktags_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApilinktagsApi->apilinktags_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this link tag. | 

### Return type

[**LinkTag**](LinkTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apilinktags_update**
> LinkTag apilinktags_update(id, data)



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
api_instance = infodbclient.ApilinktagsApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this link tag.
data = infodbclient.LinkTag() # LinkTag | 

try:
    api_response = api_instance.apilinktags_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApilinktagsApi->apilinktags_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this link tag. | 
 **data** | [**LinkTag**](LinkTag.md)|  | 

### Return type

[**LinkTag**](LinkTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

