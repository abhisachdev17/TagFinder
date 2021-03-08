from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    from main import main 
    from stub import stub
    app.register_blueprint(stub)
    
    return app