#!/usr/bin/env python3
""" making the class for basic authentication
"""
from .auth import Auth


class BasicAuth(Auth):
    """a class for the basic authentication
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """decoding the base64 header
        """
        if authorization_header is None:
            return None

        if type(authorization_header) is not str:
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(" ", 1)[1]
