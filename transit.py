
from kerykeion import AstrologicalSubject, KerykeionChartSVG

def generate_transit_svg(subject_data, transit_data, request_id, user_id):
    """
    Generates a transit chart SVG and saves it to the charts directory.
    """
    subject_zodiac_type = subject_data.get('zodiac_type', 'Tropic')
    subject_sidereal_mode = subject_data.get('sidereal_mode')
    subject_args = {
        'name': subject_data['name'],
        'year': subject_data['year'],
        'month': subject_data['month'],
        'day': subject_data['day'],
        'hour': subject_data['hour'],
        'minute': subject_data['minute'],
        'lng': subject_data['lng'],
        'lat': subject_data['lat'],
        'tz_str': subject_data['tz_str'],
        'city': subject_data['city'],
        'zodiac_type': subject_zodiac_type
    }
    if subject_zodiac_type == "Sidereal" and subject_sidereal_mode:
        subject_args['sidereal_mode'] = subject_sidereal_mode

    subject = AstrologicalSubject(**subject_args)

    transit_zodiac_type = transit_data.get('zodiac_type', 'Tropic')
    transit_sidereal_mode = transit_data.get('sidereal_mode')
    transit_args = {
        'name': "Transit",
        'year': transit_data['year'],
        'month': transit_data['month'],
        'day': transit_data['day'],
        'hour': transit_data['hour'],
        'minute': transit_data['minute'],
        'lng': transit_data['lng'],
        'lat': transit_data['lat'],
        'tz_str': transit_data['tz_str'],
        'city': transit_data['city'],
        'zodiac_type': transit_zodiac_type
    }
    if transit_zodiac_type == "Sidereal" and transit_sidereal_mode:
        transit_args['sidereal_mode'] = transit_sidereal_mode

    transit = AstrologicalSubject(**transit_args)

    transit_chart = KerykeionChartSVG(subject, "Transit", transit)
    transit_chart.makeSVG()

    # Save the SVG to a file
    file_name = f"transit_{request_id}_{user_id}.svg"
    file_path = f"charts/{file_name}"
    with open(file_path, "w") as f:
        f.write(transit_chart.template)
