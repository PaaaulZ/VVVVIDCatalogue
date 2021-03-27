import requests
import json
from flask import Flask
from flask import render_template
from flask import request

from requests.sessions import session

URL_SESSION_ID = "https://www.vvvvid.it/vvvvid/settings"
URL_CONNECTION_ID = "https://www.vvvvid.it/user/login"
URL_LIST = "https://www.vvvvid.it/vvvvid/ondemand/anime/channel/10003/last?conn_id=[[[CID]]]&filter=[[[LETTER]]]"

anime_list = []

app = Flask(__name__)

@app.route('/')
def main():

    global anime_list

    if len(anime_list) == 0:
        # First run, we need to download the list
        tokens  = get_tokens()
        connection_id = tokens['conn_id']
        session_id = tokens['session_id']

        for i in range(97,122):
            # For every letter of the alphabet
            json_list = get_list(chr(i), connection_id, session_id)
            if json_list.get('data') is not None:
                # Check if there is an anime with this letter
                for anime in json_list['data']:
                    anime_list.append({'name': anime['title'], 'url': f"https://www.vvvvid.it/show/{anime['show_id']}/", 'thumbnail': anime['thumbnail'], 'id': anime['show_id']})

    return render_template('catalogue.htm', list=anime_list)

@app.route('/search')
def search():
    global anime_list

    if len(anime_list) == 0:
        return 'You must update the catalogue by visiting the homepage'

    filtered_list = []

    search_parameter = request.args.get('parameter')
    for anime in anime_list:
        if search_parameter in anime['name'].lower():
            filtered_list.append(anime)
        
    return render_template('catalogue.htm', list=filtered_list)

def get_tokens():

    # "Login" as visitor and fetch tokens
    login_body = {'action': 'login', 'email': '', 'password': '', 'facebookParams': '', 'isIframe': 'false', 'mobile': 'false', 'hls': 'true', 'dash': 'true', 'flash': 'false', 'webm': 'true', 'wv+mp4': 'true', 'wv+webm': 'true', 'pr+mp4': 'false', 'pr+webm': 'false', 'fp+mp4': 'false', 'device_id_seed': '777'}

    r = requests.post(URL_CONNECTION_ID, json=login_body, headers={'User-Agent': 'Mozilla/5.0'})
    r_json = json.loads(r.content)
    return {'conn_id': r_json['data']['conn_id'], 'session_id': r_json['data']['sessionId']}

def get_list(letter, connection_id, session_id):

    # Anime list (starting with that letter)
    r = requests.get(URL_LIST.replace("[[[CID]]]", connection_id).replace("[[[LETTER]]]", letter), cookies={'vvvvid_cookies_accepted': '1', 'JSESSIONID': session_id}, headers={'User-Agent': 'Mozilla/5.0', 'Referer': 'https://vvvvid.it'})
    return json.loads(r.content)

