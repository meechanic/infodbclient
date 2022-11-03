# infodbclient.ApilinksApi

All URIs are relative to *http://localhost:8002*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apilinks_create**](ApilinksApi.md#apilinks_create) | **POST** /apilinks/ | 
[**apilinks_delete**](ApilinksApi.md#apilinks_delete) | **DELETE** /apilinks/{id}/ | 
[**apilinks_list**](ApilinksApi.md#apilinks_list) | **GET** /apilinks/ | 
[**apilinks_partial_update**](ApilinksApi.md#apilinks_partial_update) | **PATCH** /apilinks/{id}/ | 
[**apilinks_read**](ApilinksApi.md#apilinks_read) | **GET** /apilinks/{id}/ | 
[**apilinks_update**](ApilinksApi.md#apilinks_update) | **PUT** /apilinks/{id}/ | 


# **apilinks_create**
> Link apilinks_create(data)



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
api_instance = infodbclient.ApilinksApi(infodbclient.ApiClient(configuration))
data = infodbclient.Link() # Link | 

try:
    api_response = api_instance.apilinks_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApilinksApi->apilinks_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Link**](Link.md)|  | 

### Return type

[**Link**](Link.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apilinks_delete**
> apilinks_delete(id)



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
api_instance = infodbclient.ApilinksApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this link.

try:
    api_instance.apilinks_delete(id)
except ApiException as e:
    print("Exception when calling ApilinksApi->apilinks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this link. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apilinks_list**
> list[Link] apilinks_list(text=text, search=search, ordering=ordering)



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
api_instance = infodbclient.ApilinksApi(infodbclient.ApiClient(configuration))
text = 'text_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apilinks_list(text=text, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApilinksApi->apilinks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Link]**](Link.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apilinks_partial_update**
> Link apilinks_partial_update(id, data)



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
api_instance = infodbclient.ApilinksApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this link.
data = infodbclient.Link() # Link | 

try:
    api_response = api_instance.apilinks_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApilinksApi->apilinks_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this link. | 
 **data** | [**Link**](Link.md)|  | 

### Return type

[**Link**](Link.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apilinks_read**
> Link apilinks_read(id)



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
api_instance = infodbclient.ApilinksApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this link.

try:
    api_response = api_instance.apilinks_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApilinksApi->apilinks_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this link. | 

### Return type

[**Link**](Link.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apilinks_update**
> Link apilinks_update(id, data)



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
api_instance = infodbclient.ApilinksApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this link.
data = infodbclient.Link() # Link | 

try:
    api_response = api_instance.apilinks_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApilinksApi->apilinks_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this link. | 
 **data** | [**Link**](Link.md)|  | 

### Return type

[**Link**](Link.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

