# coding: utf-8

"""
    MagicBell REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from magicbell.api_client import ApiClient
from magicbell.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class UsersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_user(self, **kwargs):  # noqa: E501
        """Create a user  # noqa: E501

        Create a user. Please note that you must provide the user's email or the external id so MagicBell can uniquely identify the user.  The external id, if provided, must be unique to the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_user(async_req=True)
        >>> result = thread.get()

        :param wrapped_user:
        :type wrapped_user: WrappedUser
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WrappedUser
        """
        kwargs["_return_http_data_only"] = True
        return self.create_user_with_http_info(**kwargs)  # noqa: E501

    def create_user_with_http_info(self, **kwargs):  # noqa: E501
        """Create a user  # noqa: E501

        Create a user. Please note that you must provide the user's email or the external id so MagicBell can uniquely identify the user.  The external id, if provided, must be unique to the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param wrapped_user:
        :type wrapped_user: WrappedUser
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WrappedUser, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["wrapped_user"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "wrapped_user" in local_var_params:
            body_params = local_var_params["wrapped_user"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get(
            "_content_type",
            self.api_client.select_header_content_type(
                ["application/json"], "POST", body_params
            ),
        )  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["AuthAPIKeyAuth", "AuthAPISecretAuth"]  # noqa: E501

        response_types_map = {
            201: "WrappedUser",
            422: None,
        }

        return self.api_client.call_api(
            "/users",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def delete_user(self, user_id, **kwargs):  # noqa: E501
        """Delete a user  # noqa: E501

        Delete a user by id, email or external_id.  We will delete the user completely 7 days after. If the user makes a request to the API, the deletion will be canceled. This will happen when the notification inbox for this user is loaded in your app, for example.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_user(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: The user id is the MagicBell user id. Alternatively, provide an id like `email:theusersemail@example.com` or `external_id:theusersexternalid` as the user id. (required)
        :type user_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        return self.delete_user_with_http_info(user_id, **kwargs)  # noqa: E501

    def delete_user_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Delete a user  # noqa: E501

        Delete a user by id, email or external_id.  We will delete the user completely 7 days after. If the user makes a request to the API, the deletion will be canceled. This will happen when the notification inbox for this user is loaded in your app, for example.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_user_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: The user id is the MagicBell user id. Alternatively, provide an id like `email:theusersemail@example.com` or `external_id:theusersexternalid` as the user id. (required)
        :type user_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = ["user_id"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'user_id' is set
        if (
            self.api_client.client_side_validation
            and local_var_params.get("user_id") is None
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `user_id` when calling `delete_user`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "user_id" in local_var_params:
            path_params["user_id"] = local_var_params["user_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["AuthAPIKeyAuth", "AuthAPISecretAuth"]  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            "/users/{user_id}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def update_user(self, user_id, **kwargs):  # noqa: E501
        """Update a user  # noqa: E501

        Update a user's data. If you identify users by their email addresses, you need to update the MagicBell data, so this user can still access their notifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_user(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: The user id is the MagicBell user id. Alternatively, provide an id like `email:theusersemail@example.com` or `external_id:theusersexternalid` as the user id. (required)
        :type user_id: str
        :param wrapped_user:
        :type wrapped_user: WrappedUser
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WrappedUser
        """
        kwargs["_return_http_data_only"] = True
        return self.update_user_with_http_info(user_id, **kwargs)  # noqa: E501

    def update_user_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Update a user  # noqa: E501

        Update a user's data. If you identify users by their email addresses, you need to update the MagicBell data, so this user can still access their notifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_user_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: The user id is the MagicBell user id. Alternatively, provide an id like `email:theusersemail@example.com` or `external_id:theusersexternalid` as the user id. (required)
        :type user_id: str
        :param wrapped_user:
        :type wrapped_user: WrappedUser
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WrappedUser, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["user_id", "wrapped_user"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'user_id' is set
        if (
            self.api_client.client_side_validation
            and local_var_params.get("user_id") is None
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `user_id` when calling `update_user`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "user_id" in local_var_params:
            path_params["user_id"] = local_var_params["user_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "wrapped_user" in local_var_params:
            body_params = local_var_params["wrapped_user"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get(
            "_content_type",
            self.api_client.select_header_content_type(
                ["application/json"], "PUT", body_params
            ),
        )  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["AuthAPIKeyAuth", "AuthAPISecretAuth"]  # noqa: E501

        response_types_map = {
            200: "WrappedUser",
            422: None,
            404: None,
        }

        return self.api_client.call_api(
            "/users/{user_id}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )
