from kerykeion import AstrologicalSubject, KerykeionChartSVG, Report
import datetime

def get_birth_info():
    """Gets birth information from the user."""

    name = input("Enter name: ")

    while True:
        try:
            year = int(input("Enter year of birth (YYYY): "))
            month = int(input("Enter month of birth (1-12): "))
            day = int(input("Enter day of birth (1-31): "))
            birth_date = datetime.datetime(year, month, day)
            break
        except ValueError:
            print("Invalid date. Please enter valid numbers for year, month, and day.")

    while True:
        birth_time_str = input("Enter time of birth (HH:MM, 24-hour format): ")
        try:
            birth_time = datetime.datetime.strptime(birth_time_str, "%H:%M").time()
            hour = birth_time.hour
            minute = birth_time.minute
            break
        except ValueError:
            print("Invalid time format. Please use HH:MM (24-hour format).")

    while True:
        try:
            lat = float(input("Enter latitude: "))
            lng = float(input("Enter longitude: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers for latitude and longitude.")

    tz_str = input("Enter timezone (e.g., Europe/Rome): ")
    city = input("Enter city: ")

    return name, year, month, day, hour, minute, lat, lng, tz_str, city

if __name__ == "__main__":
    name, year, month, day, hour, minute, lat, lng, tz_str, city = get_birth_info()

    # Create AstrologicalSubject instance for the birth chart
    birth_subject = AstrologicalSubject(
        name, year, month, day, hour, minute,
        lng=lng,
        lat=lat,
        tz_str=tz_str,
        city=city
    )

    # Get transit information from the user
    print("\nEnter Transit Information:")

    while True:
        try:
            transit_year = int(input("Enter transit year (YYYY): "))
            transit_month = int(input("Enter transit month (1-12): "))
            transit_day = int(input("Enter transit day (1-31): "))
            transit_date = datetime.datetime(transit_year, transit_month, transit_day)
            break
        except ValueError:
            print("Invalid date. Please enter valid numbers for year, month, and day.")

    while True:
        try:
            transit_lat = float(input("Enter current latitude: "))
            transit_lng = float(input("Enter current longitude: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers for latitude and longitude.")

    transit_tz_str = input("Enter current timezone (e.g., Europe/Rome): ")
    transit_city = input("Enter current city: ")

    # Get current system time for transit
    now = datetime.datetime.now()
    transit_hour = now.hour
    transit_minute = now.minute

    # Create AstrologicalSubject instance for the transit location and time
    transit_subject = AstrologicalSubject(
        "Transit", transit_year, transit_month, transit_day, transit_hour, transit_minute,
        lng=transit_lng,
        lat=transit_lat,
        tz_str=transit_tz_str,
        city=transit_city
    )

    print("\nBirth Chart Information:")
    print(f"Name: {birth_subject.name}")
    print(f"Date of Birth: {birth_subject.year}-{birth_subject.month}-{birth_subject.day}") # Corrected attribute
    print(f"Time of Birth: {birth_subject.hour}:{birth_subject.minute}") # Corrected attribute
    print(f"Location: {birth_subject.city}, Lat: {birth_subject.lat}, Lng: {birth_subject.lng}, Timezone: {birth_subject.tz_str}")

    # --- Transit Calculation Logic will be added here ---
    print("\nTransit Information:")
    print(f"Date of Transit: {transit_subject.year}-{transit_subject.month}-{transit_subject.day}")
    print(f"Time of Transit: {transit_subject.hour}:{transit_subject.minute}")
    print(f"Location: {transit_subject.city}, Lat: {transit_subject.lat}, Lng: {transit_subject.lng}, Timezone: {transit_subject.tz_str}")

    print("\nTransits:")
    # Kerykeion provides methods to calculate transits between two AstrologicalSubject objects.
    # You can access transit aspects, positions, etc.
    # Here's a basic example of printing transit aspects.
    # The exact methods and attributes available may depend on the kerykeion version.
    try:
        transits = birth_subject.get_transits(transit_subject)
        if transits:
            for transit in transits:
                print(f"- {transit.house1.name} {transit.aspect.name} {transit.house2.name} (orb: {transit.orb})")
        else:
            print("No significant transits found.")
    except AttributeError:
        print("Kerykeion version might not support get_transits method directly or requires a different approach for transit calculations.")