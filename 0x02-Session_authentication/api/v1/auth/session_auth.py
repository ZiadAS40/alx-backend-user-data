#!/usr/bin/env python3
""" making the class for session authentication
"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """
    a Class for the new mechanism
    for the authenticatio
    which is 'Session authenticatio
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creating a sesseion and store it
        """
        if not user_id or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id
