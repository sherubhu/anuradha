
from kerykeion import AstrologicalSubject, KerykeionChartSVG

def generate_synastry_svg(person1_data, person2_data, request_id, user_id):
    """
    Generates a synastry chart SVG and saves it to the charts directory.
    """
    p1_zodiac_type = person1_data.get('zodiac_type', 'Tropic')
    p1_sidereal_mode = person1_data.get('sidereal_mode')
    person1_args = {
        'name': person1_data['name'],
        'year': person1_data['year'],
        'month': person1_data['month'],
        'day': person1_data['day'],
        'hour': person1_data['hour'],
        'minute': person1_data['minute'],
        'lng': person1_data['lng'],
        'lat': person1_data['lat'],
        'tz_str': person1_data['tz_str'],
        'city': person1_data['city'],
        'zodiac_type': p1_zodiac_type
    }
    if p1_zodiac_type == "Sidereal" and p1_sidereal_mode:
        person1_args['sidereal_mode'] = p1_sidereal_mode
    
    person1 = AstrologicalSubject(**person1_args)

    p2_zodiac_type = person2_data.get('zodiac_type', 'Tropic')
    p2_sidereal_mode = person2_data.get('sidereal_mode')
    person2_args = {
        'name': person2_data['name'],
        'year': person2_data['year'],
        'month': person2_data['month'],
        'day': person2_data['day'],
        'hour': person2_data['hour'],
        'minute': person2_data['minute'],
        'lng': person2_data['lng'],
        'lat': person2_data['lat'],
        'tz_str': person2_data['tz_str'],
        'city': person2_data['city'],
        'zodiac_type': p2_zodiac_type
    }
    if p2_zodiac_type == "Sidereal" and p2_sidereal_mode:
        person2_args['sidereal_mode'] = p2_sidereal_mode

    person2 = AstrologicalSubject(**person2_args)

    synastry_chart = KerykeionChartSVG(person1, "Synastry", person2)
    synastry_chart.makeSVG()

    # Save the SVG to a file
    file_name = f"synastry_{request_id}_{user_id}.svg"
    file_path = f"charts/{file_name}"
    with open(file_path, "w") as f:
        f.write(synastry_chart.template)
