#!/usr/bin/env python3
""" Module for session based auth
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'])
def post_on_login():
    """
    make the login end point
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    if not users[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(users[0].id)

    res = jsonify(users[0].to_json())

    name = os.getenv("SESSION_NAME", "_my_session_id")

    res.set_cookie(name, session_id)

    return res
