from flask import Blueprint, render_template, request

stub = Blueprint('main', __name__, template_folder='templates')

@stub.route('/')
def index():
    return render_template('index.html')

@stub.route('/results', methods=['POST'])
def results():
    stub_list = [
        {
            'creation_date': '12:12:12', 
            'score': '1', 
            'title': 'XYZTESTING', 
            'comments': [{'body':'c1'}, {'body':'c2'}],
            'answers': [
                {
                    'body' : 'Answer1',
                    'comments':[{'body':'ac1'}, {'body':'ac2'}],
                }
            ]
        }, 
        {
            'creation_date': '11:11:11', 
            'score': '2', 
            'title': 'XYZTESTING123',
            'comments': [{'body':'c3'}, {'body':'c4'}],
            'answers': [
                {
                    'body' : 'Answer2',
                    'comments':[{'body':'ac3'}, {'body':'ac4'}],
                }
            ]
        }
    ]

    return render_template('results.html', all_questions= [{'title':'Top Voted', 'list': stub_list}, {'title':'Newest', 'list': stub_list}, {'title':'Merged', 'list': stub_list}])
