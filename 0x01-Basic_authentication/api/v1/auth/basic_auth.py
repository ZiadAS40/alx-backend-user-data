#!/usr/bin/env python3
""" making the class for basic authentication
"""
from .auth import Auth
import base64
import binascii


class BasicAuth(Auth):
    """a class for the basic authentication
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract the base64 header
        """
        if authorization_header is None:
            return None

        if type(authorization_header) is not str:
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode the base64
        """
        if base64_authorization_header is None:
            return None

        if type(base64_authorization_header) is not str:
            return None

        try:
            res = base64.b64decode(base64_authorization_header,
                                   validate=True)
            return res.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None
