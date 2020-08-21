from os.path import dirname, abspath, join

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    send_file,
)
from flask.helpers import url_for

from .project_builder import ProjectBuilder

bp = Blueprint("site", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        if not request.form.get("project_name"):
            flash("Please, enter the application name.")
            return redirect(url_for("site.index"))

        project = dict(proj=request.form["project_name"])
        project["afp"] = True if request.form.get("afp") else False
        project["sqlal"] = True if request.form.get("sqlal") else False
        project["dyna"] = True if request.form.get("dyna") else False

        new_project = ProjectBuilder(**project)
        new_project.directories()
        new_project.files()
        if request.form.get("zip"):
            new_project.make_zipfile()
            zip_file = f"{project['proj']}.zip"
        else:
            new_project.make_tarfile()
            zip_file = f"{project['proj']}.tar.gz"

        return redirect(url_for("site.download_file", zip_file=zip_file))

    return render_template("index.html")


@bp.route("/download/<string:zip_file>")
def download_file(zip_file):
    to_send = join(dirname(dirname(abspath(__file__))), f"temp/{zip_file}",)
    return send_file(to_send, as_attachment=True)
