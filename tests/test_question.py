from flask import Flask, jsonify, request
from app.models import Question
from app import db

def test_create_question(client):
    response = client.post('/api/questions', json={
        'content': 'What is the capital of France?',
        'difficulty': 'easy',
        'subject_id': 1
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Question created successfully'

def test_get_questions(client):
    response = client.get('/api/questions')
    assert response.status_code == 200
    assert isinstance(response.json['questions'], list)

def test_update_question(client):
    response = client.post('/api/questions', json={
        'content': 'What is the capital of France?',
        'difficulty': 'easy',
        'subject_id': 1
    })
    question_id = response.json['question']['id']
    
    response = client.put(f'/api/questions/{question_id}', json={
        'content': 'What is the capital of Germany?',
        'difficulty': 'medium'
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Question updated successfully'

def test_delete_question(client):
    response = client.post('/api/questions', json={
        'content': 'What is the capital of France?',
        'difficulty': 'easy',
        'subject_id': 1
    })
    question_id = response.json['question']['id']
    
    response = client.delete(f'/api/questions/{question_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Question deleted successfully'