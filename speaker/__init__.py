"""
    Speaker
    -------

    Speaker is a library for Python that wraps the Expand Speaker API.

    It aims to abstract away all the API endpoints, so that additions to the library
    and/or the Expand Speaker API won't cause any overall problems.

    Questions, comments? marcelor@gmail.com
"""

__author__ = 'Marcelo Ramos <marcelor@gmail.com>'
__version__ = '0.0.1'

from speaker.api import Speaker
from speaker.exceptions import SpeakerError
