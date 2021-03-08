from flask import Blueprint, render_template, request
import datetime

stub = Blueprint('main', __name__, template_folder='templates')

@stub.route('/')
def index():
    return render_template('index.html')

@stub.route('/results', methods=['POST'])
def results():
    stub_list = [
        {
            'creation_date': '1615171571', 
            'score': '1', 
            'title': 'XYZTESTING', 
            'comments': [
                {
                    'body':'c0',
                    'creation_date': '123',
                    'owner': {
                        'display_name': 'some_user',
                    },
                    'votes': '0'
                }
                ],
            'answers': [
                {
                    'body' : 'Answer1',
                    'creation_date': '123',
                    'owner': {
                        'display_name': 'some_user'
                    },
                    'votes': '33',
                    'comments': [
                    {
                        'body':'c1',
                        'creation_date': '123',
                        'owner': {
                            'display_name': 'some_user'
                        },
                        'votes': '0'
                    }
                    ]
                }
            ],
            'owner' : { 'display_name': 'someone that asks questions' }
        }, 
        {
            'creation_date': '1615172030', 
            'score': '2', 
            'title': 'XYZTESTING123',
            'comments': [
                {
                    'body':'c2',
                    'creation_date': '123',
                    'owner': {
                        'display_name': 'some_user'
                    },
                    'votes': '12'
                }
                ],
            'answers': [
                {
                    'body' : 'Answer1',
                    'creation_date': '123',
                    'owner': {
                        'display_name': 'some_user'
                    },
                    'votes': '88',
                    'comments': [
                    {
                        'body':'c3',
                        'creation_date': '123',
                        'owner': {
                            'display_name': 'some_user'
                        },
                        'votes': '0'
                    },
                    ],
                }
            ],
            'owner' : { 'display_name': 'someone that asks questions' }
        }
    ]

    return render_template('results.html', all_questions= [{'title':'Top Voted', 'list': stub_list}, {'title':'Newest', 'list': stub_list}, {'title':'Merged', 'list': stub_list}])
