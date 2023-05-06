import requests
import json
import html


class Data:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        if not difficulty in ('easy', 'medium'):
            self.difficulty = 'medium'
        print(f'select difficulty : {self.difficulty}')
        self.url = 'https://opentdb.com/api.php?amount=10&category=18&difficulty=' + str(
            self.difficulty) + '&type=boolean'

    def get(self):
        print('Generating questions ...')
        response = requests.get(self.url)
        content = json.loads(response.text)['results']
        for data in content:
            data['question'] = html.unescape(data['question'])
        return content
