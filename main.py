
import os

from flask import Flask
from birth_chart_endpoint import birth_chart_bp
from synastry_endpoint import synastry_bp
from transit_endpoint import transit_bp

app = Flask(__name__)

app.register_blueprint(birth_chart_bp)
app.register_blueprint(synastry_bp)
app.register_blueprint(transit_bp)

@app.route("/")
def hello_world():
  """Example Hello World route."""
  name = os.environ.get("NAME", "World")
  return f"Hello {name}!"

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
