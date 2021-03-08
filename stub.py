from flask import Blueprint, render_template, request

stub = Blueprint('main', __name__, template_folder='templates')

@stub.route('/')
def index():
    return render_template('index.html')

@stub.route('/results')
def results():
    stub_list = [{'creation_date': '12:12:12', 'score': '1', 'title': 'XYZTESTING'}, {'creation_date': '11:11:11', 'score': '2', 'title': 'XYZTESTING123'}]
    return render_template('results.html', voted=voted, created=created, merged=merged)
