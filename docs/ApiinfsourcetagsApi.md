# infodbclient.ApiinfsourcetagsApi

All URIs are relative to *http://localhost:8002*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiinfsourcetags_create**](ApiinfsourcetagsApi.md#apiinfsourcetags_create) | **POST** /apiinfsourcetags/ | 
[**apiinfsourcetags_delete**](ApiinfsourcetagsApi.md#apiinfsourcetags_delete) | **DELETE** /apiinfsourcetags/{id}/ | 
[**apiinfsourcetags_list**](ApiinfsourcetagsApi.md#apiinfsourcetags_list) | **GET** /apiinfsourcetags/ | 
[**apiinfsourcetags_partial_update**](ApiinfsourcetagsApi.md#apiinfsourcetags_partial_update) | **PATCH** /apiinfsourcetags/{id}/ | 
[**apiinfsourcetags_read**](ApiinfsourcetagsApi.md#apiinfsourcetags_read) | **GET** /apiinfsourcetags/{id}/ | 
[**apiinfsourcetags_update**](ApiinfsourcetagsApi.md#apiinfsourcetags_update) | **PUT** /apiinfsourcetags/{id}/ | 


# **apiinfsourcetags_create**
> InfsourceTag apiinfsourcetags_create(data)



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
api_instance = infodbclient.ApiinfsourcetagsApi(infodbclient.ApiClient(configuration))
data = infodbclient.InfsourceTag() # InfsourceTag | 

try:
    api_response = api_instance.apiinfsourcetags_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiinfsourcetagsApi->apiinfsourcetags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InfsourceTag**](InfsourceTag.md)|  | 

### Return type

[**InfsourceTag**](InfsourceTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiinfsourcetags_delete**
> apiinfsourcetags_delete(id)



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
api_instance = infodbclient.ApiinfsourcetagsApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this infsource tag.

try:
    api_instance.apiinfsourcetags_delete(id)
except ApiException as e:
    print("Exception when calling ApiinfsourcetagsApi->apiinfsourcetags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this infsource tag. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiinfsourcetags_list**
> list[InfsourceTag] apiinfsourcetags_list(key=key, value=value, search=search, ordering=ordering)



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
api_instance = infodbclient.ApiinfsourcetagsApi(infodbclient.ApiClient(configuration))
key = 'key_example' # str |  (optional)
value = 'value_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apiinfsourcetags_list(key=key, value=value, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiinfsourcetagsApi->apiinfsourcetags_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 
 **value** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[InfsourceTag]**](InfsourceTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiinfsourcetags_partial_update**
> InfsourceTag apiinfsourcetags_partial_update(id, data)



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
api_instance = infodbclient.ApiinfsourcetagsApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this infsource tag.
data = infodbclient.InfsourceTag() # InfsourceTag | 

try:
    api_response = api_instance.apiinfsourcetags_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiinfsourcetagsApi->apiinfsourcetags_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this infsource tag. | 
 **data** | [**InfsourceTag**](InfsourceTag.md)|  | 

### Return type

[**InfsourceTag**](InfsourceTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiinfsourcetags_read**
> InfsourceTag apiinfsourcetags_read(id)



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
api_instance = infodbclient.ApiinfsourcetagsApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this infsource tag.

try:
    api_response = api_instance.apiinfsourcetags_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiinfsourcetagsApi->apiinfsourcetags_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this infsource tag. | 

### Return type

[**InfsourceTag**](InfsourceTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiinfsourcetags_update**
> InfsourceTag apiinfsourcetags_update(id, data)



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
api_instance = infodbclient.ApiinfsourcetagsApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this infsource tag.
data = infodbclient.InfsourceTag() # InfsourceTag | 

try:
    api_response = api_instance.apiinfsourcetags_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiinfsourcetagsApi->apiinfsourcetags_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this infsource tag. | 
 **data** | [**InfsourceTag**](InfsourceTag.md)|  | 

### Return type

[**InfsourceTag**](InfsourceTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

