# encoding: utf-8

from zhihu_oauth import ZhihuClient
import sys
import csv

reload(sys)
sys.setdefaultencoding('utf-8')

writer = csv.writer(file('says.csv', 'wb'), quotechar='|')
writer.writerow(['sayid', 'ans', 'uid', 'content'])

def login(username, password):
    client = ZhihuClient()
    client.login_in_terminal(username, password)
    return client

def get_says(item, ans):
    sayid = item.id
    uid = item.author.id
    content = item.content
    writer.writerow([sayid, ans, uid, content])

def get_says_from_comments(item):
    for comment in item.comments:
        get_says(comment, item.id)

def get_says_from_answers(item):
    for answer in item.answers:
        get_says(answer, 0)
        get_says_from_comments(answer)

def get_says_from_question(question):
    sayid = question.id
    uid = 0
    ans = 0
    content = question.title + question.detail
    writer.writerow([sayid, ans, uid, content])
    get_says_from_comments(question)
    get_says_from_answers(question)

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    questionID = int(sys.argv[3])
    client = login(username, password)
    if client:
        question = client.question(questionID)
        get_says_from_question(question)