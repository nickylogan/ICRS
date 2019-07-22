from flask import send_file


def register_routes(app):
    @app.server.route('/static/sample.csv')
    def download_sample():
        return send_file('app/static/sample.csv', mimetype='text/csv', attachment_filename='sample.csv', as_attachment=True)
