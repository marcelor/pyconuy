# -*- coding: utf-8 -*-

"""
    Speaker.api
    ~~~~~~~~~~~

    This module contains functionality for access to core Expand Speaker API calls.
"""

import json
import requests

from . import __version__
from .endpoints import EndpointsMixin
from .exceptions import SpeakerError
from .helpers import _transparent_params


class Speaker(EndpointsMixin, object):
    def __init__(self, client_args=None):
        """
            Creates an instance of Speaker.
        """

        self.api_url = 'http://voiceapi.expand.com.uy'

        self.client = requests.Session()

        self.client_args = client_args or {}
        default_headers = {'User-Agent': 'Speaker v' + __version__}
        if not 'headers' in self.client_args:
            # If they didn't set any headers, set our defaults for them
            self.client_args['headers'] = default_headers
        elif 'User-Agent' not in self.client_args['headers']:
            # If they set headers, but didn't include User-Agent.. set it for them
            self.client_args['headers'].update(default_headers)

    def __repr__(self):
        return '<Speaker: %s>' % (self.app_key)

    def _request(self, url, method='GET', params=None):
        """
            Internal request method
        """

        method = method.lower()
        params = params or {}

        func = getattr(self.client, method)
        params, files = _transparent_params(params)

        if 'frames' in params:
            frames = params.pop('frames')
            files = {'file': ('audiodata', frames)}

        requests_args = {}
        for k, v in self.client_args.items():
            # Maybe this should be set as a class variable and only done once?
            if k in ('timeout', 'allow_redirects', 'stream', 'verify'):
                requests_args[k] = v

        if method == 'get':
            requests_args['params'] = params
        else:
            requests_args.update({
                'data': params,
                'files': files,
            })

        try:
            response = func(url, **requests_args)
        except requests.RequestException as e:
            raise SpeakerError(str(e))

        content = response.content.decode('utf-8')

        json_error = False
        try:
            try:
                # try to get json
                content = content.json()
            except AttributeError:
                # if unicode detected
                content = json.loads(content)
        except ValueError:
            json_error = True
            content = {}

        if response.status_code >= 400:
            # If there is no error message, use a default.
            errors = content.get('errors',
                                 [{'message': 'An error occurred processing your request.'}])
            if errors and isinstance(errors, list):
                error_message = errors[0]['message']
            else:
                error_message = errors

            raise SpeakerError(error_message, error_code=response.status_code)

        if json_error and response.status_code != 200:
            raise SpeakerError('Response was not valid JSON, unable to decode.')

        content['status_code'] = response.status_code

        return content

    def request(self, endpoint, method='GET', params=None):
        """
            Return dict of response received from Expand Speaker's API

            :param endpoint: (required) Expand Speaker API endpoint (e.g. recognize/gender/result)
            :type endpoint: string

            :param method: (optional) Method of accessing data, either GET or POST. (default GET)
            :type method: string

            :param params: (optional) Dict of parameters (if any) accepted the by Expand Speaker API
                endpoint you are trying to access (default None)
            :type params: dict or None

            :rtype: dict
        """

        url = '%s/%s' % (self.api_url, endpoint)
        content = self._request(url, method=method, params=params)

        return content

    def get(self, endpoint, params=None):
        """
            Shortcut for GET requests via :class:`request`
        """
        return self.request(endpoint, params=params)

    def post(self, endpoint, params=None):
        """
            Shortcut for POST requests via :class:`request`
        """
        return self.request(endpoint, 'POST', params=params)


