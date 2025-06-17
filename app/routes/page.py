from flask import Blueprint, render_template, session, redirect, url_for

page_bp = Blueprint('page', __name__)

@page_bp.route('/')
def home():
    return render_template('index.html')

@page_bp.route('/index')
def index():
    return render_template('index.html')

@page_bp.route('/login')
def login():
    return render_template('login.html')

@page_bp.route('/profile')
def profile():
    return render_template('profile.html')

@page_bp.route('/bomon')
def bomon():
    return render_template('bomon.html')

@page_bp.route('/assignment')
def assignment():
    return render_template('assignment.html')

@page_bp.route('/progress')
def progress():
    return render_template('progress.html')

@page_bp.route('/users')
def users():
    return render_template('users.html')

@page_bp.route('/create_exam')
def create_exam():
    return render_template('create_exam.html')

@page_bp.route('/exam_list')
def exam_list():
    return render_template('exam_list.html')

@page_bp.route('/question_list')
def question_list():
    return render_template('question_list.html')

@page_bp.route('/add_question')
def add_question():
    return render_template('add_question.html')

@page_bp.route('/completion_stats')
def completion_stats():
    return render_template('completion_stats.html')

@page_bp.route('/statistics')
def statistics():
    return render_template('statistics.html')

@page_bp.route('/chitietde')
def chitietde():
    return render_template('chitietde.html')

@page_bp.route('/chitietdethi')
def chitietdethi():
    return render_template('chitietdethi.html')

@page_bp.route('/assigned_tasks')
def assigned_tasks():
    # Nếu muốn kiểm tra quyền, có thể kiểm tra session['role'] == 'Giảng viên'
    return render_template('assigned_tasks.html')