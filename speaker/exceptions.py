# -*- coding: utf-8 -*-

"""
    speaker.exceptions
    ~~~~~~~~~~~~~~~~~~

    This module contains Speaker specific Exception classes.
"""

from .endpoints import SPEAKER_HTTP_STATUS_CODES


class SpeakerError(Exception):
    """
        Generic error class, catch-all for most Speaker issues.
    """
    def __init__(self, msg, error_code=None):
        self.error_code = error_code

        if error_code is not None and error_code in SPEAKER_HTTP_STATUS_CODES:
            msg = 'Expand Speaker API returned a %s (%s), %s' % \
                  (error_code,
                   SPEAKER_HTTP_STATUS_CODES[error_code][0],
                   msg)

        super(SpeakerError, self).__init__(msg)

    @property
    def msg(self):
        return self.args[0]
