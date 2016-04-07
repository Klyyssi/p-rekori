import flask
from flask import Blueprint, render_template

def get_main_page_routes(get_connection):
    main_page = Blueprint("main_page", __name__, template_folder="templates")

    @main_page.route("/")
    def index():
        with get_connection() as conn:
            args = {}
            args['tags'] = conn.execute("""\
                SELECT id_ AS "%s", name_ AS "%s" FROM tags_ ORDER BY id_""",
                ('id', 'name')).fetchall()
            args['notes'] = conn.execute("""\
                SELECT id_ AS "%s", subject_ AS "%s", body_ AS "%s"
                    FROM notes_ ORDER BY id_""", ('id', 'subject', 'body')
            ).fetchall()
        return render_template("index.html", **args)

    @main_page.route('/tags/', methods=['GET', 'POST'], defaults={'id': None})
    @main_page.route('/tags/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def tags(id):
        # FIXME: implement error handling for database queries
        if flask.request.method == 'GET':
            with get_connection() as conn:
                args = {}
                args['tags'] = conn.execute("""\
                    SELECT id_ AS "%s", name_ AS "%s" FROM tags_
                        WHERE id_ = coalesce(%s, id_) ORDER BY id_""",
                    ('id', 'name', id)).fetchall()

            return render_template("tags.html", **args)
        elif flask.request.method == 'POST':
            # TODO: Implement adding of new tags
            pass
        elif flask.request.method == 'PUT':
            # TODO: Implement renaming of tag
            pass
        elif flask.request.method == 'DELETE':
            # FIXME: assert that id is nonnegative integer
            with get_connection() as conn:
                conn.execute('DELETE FROM tags_ WHERE id_ = %s', (id,))
                conn.execute('DELETE FROM note_tags WHERE tag_ = %s', (id,))
            # FIXME: look up appropriate return code for DELETE
            return "OK"
        else:
            # FIXME: should never occur, assert or raise something
            pass

    return main_page


