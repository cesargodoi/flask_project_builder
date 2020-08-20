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
        flash(f"Project name: {project['proj']}")
        new_project.directories()
        flash(f" - Creating the directories ...")
        new_project.files()
        flash(f" - Writing the files ...")

        if request.form.get("zip"):
            new_project.make_zipfile()
            flash(f" - Creating the .zip file ...")
            file_name = f"../{project['proj']}.zip"
        else:
            new_project.make_tarfile()
            flash(f" - Creating the .tar.gz file ...")
            file_name = f"../{project['proj']}.tar.gz"

        return redirect(url_for("site.download_file", ziped_file=file_name))

    return render_template("index.html")


@bp.route("/download/<string:ziped_file>")
def download_file(ziped_file):
    return send_file(ziped_file)