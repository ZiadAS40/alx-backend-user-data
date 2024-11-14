#!/usr/bin/env python3
""" making the class for session authentication
"""
from .auth import Auth
import uuid
import os
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        return user id based on
        a session
        """
        if session_id is None or type(session_id) != str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        get the user based of
        session ID
        """
        session_id = self.session_cookie(request)

        user_id = self.user_id_for_session_id(session_id)

        user = User().get(user_id)

        return user
