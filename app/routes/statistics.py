from flask import Blueprint, jsonify
from app.services.statistics_service import StatisticsService

statistics_bp = Blueprint('statistics', __name__)

@statistics_bp.route('/statistics/exam', methods=['GET'])
def get_exam_statistics():
    stats = StatisticsService.get_exam_statistics()
    return jsonify(stats), 200

@statistics_bp.route('/statistics/question', methods=['GET'])
def get_question_statistics():
    stats = StatisticsService.get_question_statistics()
    return jsonify(stats), 200

@statistics_bp.route('/statistics/completion', methods=['GET'])
def get_completion_statistics():
    stats = StatisticsService.get_completion_statistics()
    return jsonify(stats), 200

@statistics_bp.route('/statistics/assignment', methods=['GET'])
def get_assignment_statistics():
    stats = StatisticsService.get_assignment_statistics()
    return jsonify(stats), 200