
import unittest
import json
from main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_birth_chart_svg(self):
        data = {
            "request_id": "test_request_123",
            "user_id": "test_user_456",
            "name": "test_user_456",
            "year": 1990,
            "month": 1,
            "day": 15,
            "hour": 12,
            "minute": 0,
            "lng": -74.0060,
            "lat": 40.7128,
            "tz_str": "America/New_York",
            "city": "New York"
        }
        response = self.app.post('/birth/svg', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_birth_chart_report(self):
        data = {
            "request_id": "test_request_123",
            "user_id": "test_user_456",
            "name": "test_user_456",
            "year": 1990,
            "month": 1,
            "day": 15,
            "hour": 12,
            "minute": 0,
            "lng": -74.0060,
            "lat": 40.7128,
            "tz_str": "America/New_York",
            "city": "New York"
        }
        response = self.app.post('/birth/report', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_synastry_svg(self):
        data = {
            "request_id": "synastry_test_1",
            "user_id": "user_test_1",
            "person1": {
                "name": "person1",
                "year": 1988,
                "month": 5,
                "day": 10,
                "hour": 10,
                "minute": 10,
                "lat": 40.7128,
                "lng": -74.0060,
                "tz_str": "America/New_York",
                "city": "New York"
            },
            "person2": {
                "name": "person2",
                "year": 1992,
                "month": 8,
                "day": 20,
                "hour": 20,
                "minute": 20,
                "lat": 34.0522,
                "lng": -118.2437,
                "tz_str": "America/Los_Angeles",
                "city": "Los Angeles"
            }
        }
        response = self.app.post('/synastry/svg', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_synastry_report(self):
        data = {
            "request_id": "synastry_test_1",
            "user_id": "user_test_1",
            "person1": {
                "name": "person1",
                "year": 1988,
                "month": 5,
                "day": 10,
                "hour": 10,
                "minute": 10,
                "lat": 40.7128,
                "lng": -74.0060,
                "tz_str": "America/New_York",
                "city": "New York"
            },
            "person2": {
                "name": "person2",
                "year": 1992,
                "month": 8,
                "day": 20,
                "hour": 20,
                "minute": 20,
                "lat": 34.0522,
                "lng": -118.2437,
                "tz_str": "America/Los_Angeles",
                "city": "Los Angeles"
            }
        }
        response = self.app.post('/synastry/report', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_transit_svg(self):
        data = {
            "request_id": "transit_test_1",
            "user_id": "user_test_1",
            "name": "person1",
            "year": 1988,
            "month": 5,
            "day": 10,
            "hour": 10,
            "minute": 10,
            "lat": 40.7128,
            "lng": -74.0060,
            "tz_str": "America/New_York",
            "city": "New York"
        }
        response = self.app.post('/transit/svg', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_transit_report(self):
        data = {
            "request_id": "transit_test_1",
            "user_id": "user_test_1",
            "name": "person1",
            "year": 1988,
            "month": 5,
            "day": 10,
            "hour": 10,
            "minute": 10,
            "lat": 40.7128,
            "lng": -74.0060,
            "tz_str": "America/New_York",
            "city": "New York"
        }
        response = self.app.post('/transit/report', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
