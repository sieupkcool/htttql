from flask import Flask, jsonify
from flask_testing import TestCase
from app import create_app, db
from app.models import User

class AuthTestCase(TestCase):
    def create_app(self):
        app = create_app('testing')
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()
        self.user = User(username='testuser', password='testpassword')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login_success(self):
        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)

    def test_login_failure(self):
        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn('message', response.json)

    def test_register_user(self):
        response = self.client.post('/auth/register', json={
            'username': 'newuser',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.json)

    def test_register_existing_user(self):
        response = self.client.post('/auth/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', response.json)