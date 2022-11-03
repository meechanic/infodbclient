# infodbclient.ApisourcetagsApi

All URIs are relative to *http://localhost:8002*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apisourcetags_create**](ApisourcetagsApi.md#apisourcetags_create) | **POST** /apisourcetags/ | 
[**apisourcetags_delete**](ApisourcetagsApi.md#apisourcetags_delete) | **DELETE** /apisourcetags/{id}/ | 
[**apisourcetags_list**](ApisourcetagsApi.md#apisourcetags_list) | **GET** /apisourcetags/ | 
[**apisourcetags_partial_update**](ApisourcetagsApi.md#apisourcetags_partial_update) | **PATCH** /apisourcetags/{id}/ | 
[**apisourcetags_read**](ApisourcetagsApi.md#apisourcetags_read) | **GET** /apisourcetags/{id}/ | 
[**apisourcetags_update**](ApisourcetagsApi.md#apisourcetags_update) | **PUT** /apisourcetags/{id}/ | 


# **apisourcetags_create**
> SourceTag apisourcetags_create(data)



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
api_instance = infodbclient.ApisourcetagsApi(infodbclient.ApiClient(configuration))
data = infodbclient.SourceTag() # SourceTag | 

try:
    api_response = api_instance.apisourcetags_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcetagsApi->apisourcetags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SourceTag**](SourceTag.md)|  | 

### Return type

[**SourceTag**](SourceTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisourcetags_delete**
> apisourcetags_delete(id)



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
api_instance = infodbclient.ApisourcetagsApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this source tag.

try:
    api_instance.apisourcetags_delete(id)
except ApiException as e:
    print("Exception when calling ApisourcetagsApi->apisourcetags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source tag. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisourcetags_list**
> list[SourceTag] apisourcetags_list(name=name, search=search, ordering=ordering)



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
api_instance = infodbclient.ApisourcetagsApi(infodbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apisourcetags_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcetagsApi->apisourcetags_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[SourceTag]**](SourceTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisourcetags_partial_update**
> SourceTag apisourcetags_partial_update(id, data)



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
api_instance = infodbclient.ApisourcetagsApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this source tag.
data = infodbclient.SourceTag() # SourceTag | 

try:
    api_response = api_instance.apisourcetags_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcetagsApi->apisourcetags_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source tag. | 
 **data** | [**SourceTag**](SourceTag.md)|  | 

### Return type

[**SourceTag**](SourceTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisourcetags_read**
> SourceTag apisourcetags_read(id)



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
api_instance = infodbclient.ApisourcetagsApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this source tag.

try:
    api_response = api_instance.apisourcetags_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcetagsApi->apisourcetags_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source tag. | 

### Return type

[**SourceTag**](SourceTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisourcetags_update**
> SourceTag apisourcetags_update(id, data)



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
api_instance = infodbclient.ApisourcetagsApi(infodbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this source tag.
data = infodbclient.SourceTag() # SourceTag | 

try:
    api_response = api_instance.apisourcetags_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcetagsApi->apisourcetags_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source tag. | 
 **data** | [**SourceTag**](SourceTag.md)|  | 

### Return type

[**SourceTag**](SourceTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

