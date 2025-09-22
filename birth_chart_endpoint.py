
import os
from flask import Blueprint, request, jsonify
from birth_chart_kerykeion import generate_birth_report, generate_birth_svg

birth_chart_bp = Blueprint('birth_chart', __name__)

@birth_chart_bp.route('/birth/report', methods=['POST'])
def create_birth_report():
    data = request.get_json()
    try:
        request_id = data['request_id']
        user_id = data['user_id']
        name = data['name']
        year = data['year']
        month = data['month']
        day = data['day']
        hour = data['hour']
        minute = data['minute']
        lng = data['lng']
        lat = data['lat']
        tz_str = data['tz_str']
        city = data['city']
    except (KeyError, ValueError) as e:
        return jsonify({'error': f'Missing or invalid parameter: {e}'}), 400

    zodiac_type = data.get('zodiac_type', 'Tropic')
    sidereal_mode = data.get('sidereal_mode')

    report_data = generate_birth_report(
        name, year, month, day, hour, minute, lng, lat, tz_str, city, zodiac_type, sidereal_mode
    )

    # Create reports directory if it doesn't exist
    if not os.path.exists('reports'):
        os.makedirs('reports')

    # Save the report to a file
    file_name = f"report_{request_id}_{user_id}.txt"
    file_path = os.path.join('reports', file_name)
    with open(file_path, 'w') as f:
        f.write(report_data)

    return jsonify({'report': report_data})

@birth_chart_bp.route('/birth/svg', methods=['POST'])
def create_birth_svg():
    data = request.get_json()
    try:
        request_id = data['request_id']
        user_id = data['user_id']
        name = data['name']
        year = data['year']
        month = data['month']
        day = data['day']
        hour = data['hour']
        minute = data['minute']
        lng = data['lng']
        lat = data['lat']
        tz_str = data['tz_str']
        city = data['city']
    except (KeyError, ValueError) as e:
        return jsonify({'error': f'Missing or invalid parameter: {e}'}), 400

    zodiac_type = data.get('zodiac_type', 'Tropic')
    sidereal_mode = data.get('sidereal_mode')

    generate_birth_svg(
        request_id, user_id, name, year, month, day, hour, minute, lng, lat, tz_str, city, zodiac_type, sidereal_mode
    )

    return jsonify({'message': f'Birth chart for {name} created successfully.'})
