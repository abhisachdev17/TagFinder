from flask import Blueprint, render_template, request
import requests
from datetime import datetime, date, timedelta
import json

main = Blueprint('main', __name__, template_folder='templates')

CREATED = 'creation'
VOTED = 'votes'
COUNT = 10

def build_url(count, from_time, to_time, sort_on, tag):
    ## The filer that this url is using returns answers for each questions and all of the related comments

    stackoverflow_url = "https://api.stackexchange.com/2.2/search?order=desc&pagesize={:s}&fromdate={:s}&todate={:s}&sort={:s}&tagged={:s}&filter=!)rTkraPYPefwELKox66q&site=stackoverflow"
    url = stackoverflow_url.format(count, from_time, to_time, sort_on, tag)
    return url

def get_dates_for_url():
    today = datetime.now()
    to_time = int(today.timestamp())

    week_ago = today - timedelta(days=7)
    from_time = int(week_ago.timestamp()) 
    return (from_time, to_time)

def sort_created(data):
    sorted_data = sorted(data, key = lambda x: int(x["creation_date"]),reverse=True)
    return sorted_data

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/results' , methods=['POST'])
def results_display():
    try:
        tag = request.form.get('tag')

        from_time, to_time = get_dates_for_url()
        url = build_url(str(COUNT), str(from_time), str(to_time), CREATED, tag)
        response = requests.get(url)

        data = response.json()
        created = data['items'] # [:COUNT]

        url = build_url(str(COUNT), str(from_time), str(to_time), VOTED, tag)
        response = requests.get(url)

        data = response.json()
        voted = data['items'] # [:COUNT]

        merged = created.copy()
        for i in voted:
            exists = False
            for j in merged:
                if i['question_id'] == j['question_id']:
                    exists = True
            if not exists:
                merged.append(i)

        merged = sort_created(merged)

        return render_template('results.html', all_questions= [{'title':'Merged', 'list': merged}, {'title':'Top Voted', 'list': voted}, {'title':'Newest', 'list': created}])

    except Exception as e:
        return render_template('error.html', error= str(e), response=data)