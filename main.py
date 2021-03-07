from flask import Blueprint, render_template, request

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/results' , methods=['POST'])
def results_display():
    try:
        tag = request.form.get('tag')
    except KeyError as e:
        tag = ''
    
    return render_template('results.html', results="Did not find any results for " + tag)