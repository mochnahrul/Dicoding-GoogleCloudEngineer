# third-party imports
from flask import render_template

# local imports
from . import public_app


# render template
@public_app.route("/", methods=["GET", "POST"])
def homepage():
  return render_template("public/index.html", title="Mochamad Nahrul Hayawan")