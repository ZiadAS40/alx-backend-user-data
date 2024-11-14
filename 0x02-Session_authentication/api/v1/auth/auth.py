#!/usr/bin/env python3
""" making the class for the authentication
"""
from typing import List, TypeVar
from flask import request
import os


class Auth:
    """
    the class used for the authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        just return Fals for now
        """
        if path is None:
            return True

        if not path.endswith('/'):
            path += '/'

        if excluded_paths is None or not excluded_paths:
            return True

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        just return None for now
        """
        if request is None:
            return None
        auth_header = request.headers.get("Authorization", None)
        if auth_header is None:
            return None
        else:
            return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """"
        just return None for now
        """
        return None

    def session_cookie(self, request=None):
        """
        return the cookie value
        from a request
        """
        if not request:
            return None

        cookie_name = os.getenv("SESSION_NAME")

        return request.cookies.get(cookie_name)
