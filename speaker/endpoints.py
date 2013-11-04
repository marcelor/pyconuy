# -*- coding: utf-8 -*-

"""
    speaker.endpoints
    ~~~~~~~~~~~~~~~~~

    This module provides a mixin for a :class:`Speaker <Speaker>` instance.
    Parameters that need to be sent to the API endpoint just need to be passed as keyword arguments.

    e.g. Speaker.get_gender_recognition_result(task_id='bf4f25f6682d4d2990cec25a91a15e75')
"""


class EndpointsMixin(object):

    def issue_gender_recognition_task(self, **params):
        """
            Issues a gender recognition on provided audio data.
        """
        return self.post('recognize/gender', params=params)


    def get_gender_recognition_result(self, **params):
        """
            Retrieves the gender recognition task result.
        """
        return self.post('recognize/gender/result', params=params)


SPEAKER_HTTP_STATUS_CODES = {
    200: ('OK', 'The request has succeeded.'),
    400: ('Bad Request', 'An invalid multipart-form encoded message was sent.'),
    404: ('Not Found', 'Invalid Request-URI.'),
    405: ('Method Not Allowed', 'An invalid method was used.'),
    422: ('Unprocessable Entity', 'Invalid data was sent.'),
}
