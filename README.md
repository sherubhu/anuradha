
This is a minimal Flask API service starter based on [Google Cloud Run Quickstart](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service).

## Getting Started

Server should run automatically when starting a workspace. To run manually, run:

./devserver.sh
```
### Here is the complete JSON structure that the /birth/svg endpoint can accept:

{
  "name": "string",
  "year": "integer",
  "month": "integer",
  "day": "integer",
  "hour": "integer",
  "minute": "integer",
  "lng": "float",
  "lat": "float",
  "tz_str": "string",
  "city": "string",
  "zodiac_type": "string (optional, defaults to 'Tropic')",
  "sidereal_mode": "string (optional, used if zodiac_type is 'Sidereal')"
}

Outputs 

{
  "svg": "PD94bWwgdmVyc2lvbj0nMS4wJyBlbmNvZGluZz0nVVRGLTgnPz4K..."
}
### Here is the complete JSON structure that the /birthchart/report endpoint,
{
  "name": "string",
  "year": "integer",
  "month": "integer",
  "day": "integer",
  "hour": "integer",
  "minute": "integer",
  "lng": "float",
  "lat": "float",
  "tz_str": "string",
  "city": "string",
  "zodiac_type": "string (optional, defaults to 'Tropic')",
  "sidereal_mode": "string (optional, used if zodiac_type is 'Sidereal')"
}

 The endpoint returns a JSON object with a single key, report.
 
 {
  "report": "string"
}

### for the /synastry/report endpoint.
### The endpoint accepts a JSON object with the following structure. It requires a request_id, a user_id, and two nested objects, person1 and person2, each containing the birth data for an individual.

{
  "request_id": "string",
  "user_id": "string",
  "person1": {
    "name": "string",
    "year": "integer",
    "month": "integer",
    "day": "integer",
    "hour": "integer",
    "minute": "integer",
    "lng": "float",
    "lat": "float",
    "tz_str": "string",
    "city": "string",
    "zodiac_type": "string (optional, defaults to 'Tropic')",
    "sidereal_mode": "string (optional, used if zodiac_type is 'Sidereal')"
  },
  "person2": {
    "name": "string",
    "year": "integer",
    "month": "integer",
    "day": "integer",
    "hour": "integer",
    "minute": "integer",
    "lng": "float",
    "lat": "float",
    "tz_str": "string",
    "city": "string",
    "zodiac_type": "string (optional, defaults to 'Tropic')",
    "sidereal_mode": "string (optional, used if zodiac_type is 'Sidereal')"
  }
}

The output is 

{
  "report": "string"
}

For /synastry/svg the output is 

{
  "svg": "PD94bWwgdmVyc2lvbj0nMS4wJyBlbmNvZGluZz0nVVRGLTgnPz4K..."
}

### the input and output for /transit/svg is 

 The endpoint accepts a JSON object with two primary keys: subject (the birth data of the person) and transit (the data for the transit moment).

 {
  "subject": {
    "name": "string",
    "year": "integer",
    "month": "integer",
    "day": "integer",
    "hour": "integer",
    "minute": "integer",
    "lng": "float",
    "lat": "float",
    "tz_str": "string",
    "city": "string",
    "zodiac_type": "string (optional, defaults to 'Tropic')",
    "sidereal_mode": "string (optional, used if zodiac_type is 'Sidereal')"
  },
  "transit": {
    "name": "string",
    "year": "integer",
    "month": "integer",
    "day": "integer",
    "hour": "integer",
    "minute": "integer",
    "lng": "float",
    "lat": "float",
    "tz_str": "string",
    "city": "string",
    "zodiac_type": "string (optional, defaults to 'Tropic')",
    "sidereal_mode": "string (optional, used if zodiac_type is 'Sidereal')"
  }
}

#### The endpoint returns a JSON object containing the base64-encoded SVG chart.

{
  "svg": "PD94bWwgdmVyc2lvbj0nMS4wJyBlbmNvZGluZz0nVVRGLTgnPz4K..."
}
