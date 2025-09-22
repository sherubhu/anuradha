
from flask import Blueprint, request, jsonify
from synastry import generate_synastry_svg, generate_synastry_report

synastry_bp = Blueprint('synastry', __name__)

@synastry_bp.route('/synastry/svg', methods=['POST'])
def create_synastry_chart():
    data = request.get_json()
    try:
        request_id = data['request_id']
        user_id = data['user_id']
        person1_data = data['person1']
        person2_data = data['person2']
    except (KeyError, ValueError) as e:
        return jsonify({'error': f'Missing or invalid parameter: {e}'}), 400

    try:
        generate_synastry_svg(person1_data, person2_data, request_id, user_id)
        return jsonify({"message": "Synastry chart created successfully."}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@synastry_bp.route('/synastry/report', methods=['POST'])
def create_synastry_report():
    data = request.get_json()
    try:
        request_id = data['request_id']
        user_id = data['user_id']
        person1_data = data['person1']
        person2_data = data['person2']
    except (KeyError, ValueError) as e:
        return jsonify({'error': f'Missing or invalid parameter: {e}'}), 400

    try:
        report = generate_synastry_report(person1_data, person2_data, request_id, user_id)
        return jsonify({"report": report}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
