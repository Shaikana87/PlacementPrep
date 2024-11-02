import requests
from bs4 import BeautifulSoup

from Quiz.models import QuizQuestion

dbms_url = 'https://testbook.com/objective-questions/mcq-on-dbms--5eea6a0939140f30f369da74'

java_url = 'https://testbook.com/objective-questions/mcq-on-java--5eea6a1139140f30f369eb7d'

def run():
    page = requests.get(java_url).text

    soup = BeautifulSoup(page, 'html.parser')

    container = soup.find('div', class_='main-container')

    qcontainer = container.find('div', class_='all-questions')

    cards = qcontainer.find_all('div', class_='question-card')
    answers = qcontainer.find_all('div', class_='answer-card')

    ques = []
    for card in cards:
        q = card.find('p', class_='individual_question').text
        options = card.find_all('li', class_='option')
        a = options[0].text
        b = options[1].text
        c = options[2].text
        d = options[3].text
        ques.append({
            'ques':q,
            'optionA':a,
            'optionB':b,
            'optionC':c,
            'optionD':d,
        })

    ans = []
    for answer in answers:
        num = answer.find('div').text[:8][-1]
        if num == '1':
            ans.append('a')
        elif num == '2':
            ans.append('b')
        if num == '3':
            ans.append('c')
        if num == '4':
            ans.append('d')

    if len(ques) == len(ans):
        for i in range(len(ques)):
            ques[i]['correct'] = ans[i]

    for q in ques:
        quiz_question = QuizQuestion(question_statement=q['ques'],
                                 optionA=q['optionA'],
                                 optionB=q['optionB'],
                                 optionC=q['optionC'],
                                 optionD=q['optionD'],
                                 correct_ans=q['correct']
                                 )
    
        quiz_question.save()
