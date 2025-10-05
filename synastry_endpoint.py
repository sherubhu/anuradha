
import base64
from flask import Blueprint, request, jsonify
from synastry import generate_synastry_svg, generate_synastry_aspects

synastry_bp = Blueprint('synastry', __name__)

@synastry_bp.route('/synastry/svg', methods=['POST'])
def create_synastry_chart():
    data = request.get_json()
    try:
        person1_data = data['person1']
        person2_data = data['person2']
    except (KeyError, ValueError) as e:
        return jsonify({'error': f'Missing or invalid parameter: {e}'}), 400

    try:
        svg_content = generate_synastry_svg(person1_data, person2_data)
        svg_base64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
        return jsonify({"svg": svg_base64}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@synastry_bp.route('/synastry/aspects', methods=['POST'])
def get_synastry_aspects():
    data = request.get_json()
    try:
        person1_data = data['person1']
        person2_data = data['person2']
    except (KeyError, ValueError) as e:
        return jsonify({'error': f'Missing or invalid parameter: {e}'}), 400

    try:
        aspects = generate_synastry_aspects(person1_data, person2_data)
        return jsonify({"aspects": aspects}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
