
from kerykeion import AstrologicalSubject, KerykeionChartSVG, Report

def generate_birth_report(name, year, month, day, hour, minute, lng, lat, tz_str, city, zodiac_type="Tropic", sidereal_mode=None):
    """
    Generates a birth chart report.
    """
    subject_args = {
        'name': name,
        'year': year,
        'month': month,
        'day': day,
        'hour': hour,
        'minute': minute,
        'lng': lng,
        'lat': lat,
        'tz_str': tz_str,
        'city': city,
        'zodiac_type': zodiac_type
    }
    if zodiac_type == "Sidereal" and sidereal_mode:
        subject_args['sidereal_mode'] = sidereal_mode

    subject = AstrologicalSubject(**subject_args)
    report = Report(subject)
    return report.get_full_report()

def generate_birth_svg(name, year, month, day, hour, minute, lng, lat, tz_str, city, zodiac_type="Tropic", sidereal_mode=None):
    """
    Generates a birth chart SVG and returns the SVG content.
    """
    subject_args = {
        'name': name,
        'year': year,
        'month': month,
        'day': day,
        'hour': hour,
        'minute': minute,
        'lng': lng,
        'lat': lat,
        'tz_str': tz_str,
        'city': city,
        'zodiac_type': zodiac_type
    }
    if zodiac_type == "Sidereal" and sidereal_mode:
        subject_args['sidereal_mode'] = sidereal_mode
        
    subject = AstrologicalSubject(**subject_args)
    chart = KerykeionChartSVG(subject)
    chart.makeSVG()

    return chart.template
