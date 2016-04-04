from flask import Blueprint, render_template

def get_main_page_routes(db_execute):
    main_page = Blueprint("main_page", __name__, template_folder="templates")

    @main_page.route("/")
    def index():
        notes = db_execute('select * from snippets_ where type_=2')
        return render_template("index.html", notes=notes)

    return main_page


