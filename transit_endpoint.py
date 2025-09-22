
from flask import Blueprint, request, jsonify
from transit import generate_transit_svg

transit_bp = Blueprint('transit', __name__)

@transit_bp.route('/transit/svg', methods=['POST'])
def create_transit_chart():
    data = request.get_json()
    try:
        request_id = data['request_id']
        user_id = data['user_id']
        subject_data = data['subject']
        transit_data = data['transit']
    except (KeyError, ValueError) as e:
        return jsonify({'error': f'Missing or invalid parameter: {e}'}), 400

    try:
        generate_transit_svg(subject_data, transit_data, request_id, user_id)
        return jsonify({"message": "Transit chart created successfully."}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
