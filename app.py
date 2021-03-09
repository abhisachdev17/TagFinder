from flask import Flask, render_template
from datetime import datetime

def create_app():
    app = Flask(__name__)
    
    from main import main 
    app.register_blueprint(main)
    
    # from stub import stub
    # app.register_blueprint(stub)
    

    @app.template_filter('strftime')
    def filter_datetime(s, fmt=None):
        dt = datetime.fromtimestamp(int(s)).strftime('%Y-%m-%d %H:%M:%S')
        return str(dt)

    return app