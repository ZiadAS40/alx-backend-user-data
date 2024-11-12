#!/usr/bin/env python3
""" making the class for basic authentication
"""
from .auth import Auth
from models.user import User
import base64
import binascii
from typing import TypeVar


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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ extract the user credentials
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if type(decoded_base64_authorization_header) is not str:
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None
        username = decoded_base64_authorization_header.split(":")[0]
        password = decoded_base64_authorization_header.split(":")[1]
        return username, password

    def user_object_from_credentials(self,
                                     user_email:
                                     str, user_pwd:
                                     str) -> TypeVar('User'):
        """make a user instance with its credentials
        """
        if user_email is None or user_pwd is None:
            return None

        if type(user_pwd) is not str or type(user_email) is not str:
            return None

        users = User.search({'email': user_email})

        if not users:
            return None

        if users[0].is_valid_password(user_pwd):
            return users[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        header = self.authorization_header(request)
        b64_auth_header = self.extract_base64_authorization_header(header)
        auth_header = self.decode_base64_authorization_header(b64_auth_header)
        email, password = self.extract_user_credentials(auth_header)
        return self.user_object_from_credentials(email, password)
