from flask import Blueprint, request, jsonify
from app.services.statistics_service import StatisticsService

statistics_bp = Blueprint('statistics', __name__)

@statistics_bp.route('/statistics/exam')
def exam_statistics():
    kyhoc = request.args.get('kyhoc')
    monhoc = request.args.get('monhoc')
    data = StatisticsService.get_exam_count(kyhoc, monhoc)
    return jsonify(data)

@statistics_bp.route('/statistics/completion')
def completion_statistics():
    kyhoc = request.args.get('kyhoc')
    giangvien = request.args.get('giangvien')
    data = StatisticsService.get_completion_statistics(kyhoc, giangvien)
    return jsonify(data)