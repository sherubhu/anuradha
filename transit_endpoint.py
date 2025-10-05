
import base64
from flask import Blueprint, request, jsonify
from transit import generate_transit_svg

transit_bp = Blueprint('transit', __name__)

@transit_bp.route('/transit/svg', methods=['POST'])
def create_transit_chart():
    data = request.get_json()
    try:
        subject_data = data['subject']
        transit_data = data['transit']
    except (KeyError, ValueError) as e:
        return jsonify({'error': f'Missing or invalid parameter: {e}'}), 400

    try:
        svg_content = generate_transit_svg(subject_data, transit_data)
        svg_base64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
        return jsonify({"svg": svg_base64}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
