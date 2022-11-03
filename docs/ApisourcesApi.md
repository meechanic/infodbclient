# infodbclient.ApisourcesApi

All URIs are relative to *http://localhost:8002*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apisources_create**](ApisourcesApi.md#apisources_create) | **POST** /apisources/ | 
[**apisources_delete**](ApisourcesApi.md#apisources_delete) | **DELETE** /apisources/{id}/ | 
[**apisources_list**](ApisourcesApi.md#apisources_list) | **GET** /apisources/ | 
[**apisources_partial_update**](ApisourcesApi.md#apisources_partial_update) | **PATCH** /apisources/{id}/ | 
[**apisources_read**](ApisourcesApi.md#apisources_read) | **GET** /apisources/{id}/ | 
[**apisources_update**](ApisourcesApi.md#apisources_update) | **PUT** /apisources/{id}/ | 


# **apisources_create**
> Source apisources_create(data)



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
api_instance = infodbclient.ApisourcesApi(infodbclient.ApiClient(configuration))
data = infodbclient.Source() # Source | 

try:
    api_response = api_instance.apisources_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcesApi->apisources_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Source**](Source.md)|  | 

### Return type

[**Source**](Source.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisources_delete**
> apisources_delete(id)



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
api_instance = infodbclient.ApisourcesApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this source.

try:
    api_instance.apisources_delete(id)
except ApiException as e:
    print("Exception when calling ApisourcesApi->apisources_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisources_list**
> list[Source] apisources_list(name=name, search=search, ordering=ordering)



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
api_instance = infodbclient.ApisourcesApi(infodbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apisources_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcesApi->apisources_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Source]**](Source.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisources_partial_update**
> Source apisources_partial_update(id, data)



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
api_instance = infodbclient.ApisourcesApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this source.
data = infodbclient.Source() # Source | 

try:
    api_response = api_instance.apisources_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcesApi->apisources_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source. | 
 **data** | [**Source**](Source.md)|  | 

### Return type

[**Source**](Source.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisources_read**
> Source apisources_read(id)



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
api_instance = infodbclient.ApisourcesApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this source.

try:
    api_response = api_instance.apisources_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcesApi->apisources_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source. | 

### Return type

[**Source**](Source.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisources_update**
> Source apisources_update(id, data)



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
api_instance = infodbclient.ApisourcesApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this source.
data = infodbclient.Source() # Source | 

try:
    api_response = api_instance.apisources_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcesApi->apisources_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source. | 
 **data** | [**Source**](Source.md)|  | 

### Return type

[**Source**](Source.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

