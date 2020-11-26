# coding: utf-8

"""
    Asset

    Data Catalog Asset API.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: katacseke@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from data_catalog.client.asset.api_client import ApiClient
from data_catalog.client.asset.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AssetApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_asset(self, **kwargs):  # noqa: E501
        """create_asset  # noqa: E501

        Create a data asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_asset(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AssetRequest asset_request: The data asset to be created.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_asset_with_http_info(**kwargs)  # noqa: E501

    def create_asset_with_http_info(self, **kwargs):  # noqa: E501
        """create_asset  # noqa: E501

        Create a data asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_asset_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AssetRequest asset_request: The data asset to be created.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'asset_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_asset" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'asset_request' in local_var_params:
            body_params = local_var_params['asset_request']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/assets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_asset(self, asset_id, **kwargs):  # noqa: E501
        """delete_asset  # noqa: E501

        Delete asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_asset(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str asset_id: The unique identifier of the asset.  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_asset_with_http_info(asset_id, **kwargs)  # noqa: E501

    def delete_asset_with_http_info(self, asset_id, **kwargs):  # noqa: E501
        """delete_asset  # noqa: E501

        Delete asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_asset_with_http_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str asset_id: The unique identifier of the asset.  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'asset_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_asset" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if self.api_client.client_side_validation and ('asset_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['asset_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `asset_id` when calling `delete_asset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['assetId'] = local_var_params['asset_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/assets/{assetId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_asset(self, asset_id, **kwargs):  # noqa: E501
        """Your GET endpoint  # noqa: E501

        Get asset by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str asset_id: The unique identifier of the asset.  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AssetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_asset_with_http_info(asset_id, **kwargs)  # noqa: E501

    def get_asset_with_http_info(self, asset_id, **kwargs):  # noqa: E501
        """Your GET endpoint  # noqa: E501

        Get asset by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_with_http_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str asset_id: The unique identifier of the asset.  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AssetResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'asset_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_asset" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if self.api_client.client_side_validation and ('asset_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['asset_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `asset_id` when calling `get_asset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['assetId'] = local_var_params['asset_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/assets/{assetId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_assets(self, **kwargs):  # noqa: E501
        """Your GET endpoint  # noqa: E501

        List all the data assets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_assets(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] tags: Filter by tags.
        :param str namespace: Filter by namespace.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[AssetResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_assets_with_http_info(**kwargs)  # noqa: E501

    def get_assets_with_http_info(self, **kwargs):  # noqa: E501
        """Your GET endpoint  # noqa: E501

        List all the data assets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_assets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] tags: Filter by tags.
        :param str namespace: Filter by namespace.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[AssetResponse], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'tags',
            'namespace'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_assets" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tags' in local_var_params and local_var_params['tags'] is not None:  # noqa: E501
            query_params.append(('tags', local_var_params['tags']))  # noqa: E501
            collection_formats['tags'] = 'multi'  # noqa: E501
        if 'namespace' in local_var_params and local_var_params['namespace'] is not None:  # noqa: E501
            query_params.append(('namespace', local_var_params['namespace']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/assets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AssetResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_asset(self, asset_id, **kwargs):  # noqa: E501
        """patch_asset  # noqa: E501

        Update only the given attributes of the asset. The attributes which are not specified in the body will not change.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_asset(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str asset_id: The unique identifier of the asset.  (required)
        :param AssetRequest asset_request: Specify only the attributes which you want to update.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.patch_asset_with_http_info(asset_id, **kwargs)  # noqa: E501

    def patch_asset_with_http_info(self, asset_id, **kwargs):  # noqa: E501
        """patch_asset  # noqa: E501

        Update only the given attributes of the asset. The attributes which are not specified in the body will not change.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_asset_with_http_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str asset_id: The unique identifier of the asset.  (required)
        :param AssetRequest asset_request: Specify only the attributes which you want to update.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'asset_id',
            'asset_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_asset" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if self.api_client.client_side_validation and ('asset_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['asset_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `asset_id` when calling `patch_asset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['assetId'] = local_var_params['asset_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'asset_request' in local_var_params:
            body_params = local_var_params['asset_request']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/assets/{assetId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)