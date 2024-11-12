#!usr/bin/env python3
""" making the class for the authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    the class used for the authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        just return Fals for now
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        just return None for now
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """"
        just return None for now
        """
        return None
