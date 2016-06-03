# encoding: utf-8

from zhihu_oauth import ZhihuClient
from sklearn.feature_extraction.text import CountVectorizer
import jieba
import sys
import csv

reload(sys)
sys.setdefaultencoding('utf-8')
jieba.load_userdict("dict.txt")
writer = csv.writer(file('says.csv', 'wb'), delimiter='|')
writer.writerow(['sayid', 'ans', 'uid', 'content'])
stopwords = None

def load_stopwords():
	stopwordStr = open('stopword.txt', 'r').read()
	global stopwords
	stopwords = stopwordStr.split('\n')

def delete_stopword(tokenizedContent):
	return [word for word in tokenizedContent if word not in stopwords]

def login(username, password):
    client = ZhihuClient()
    client.login_in_terminal(username, password)
    return client

def get_says(item, ans):
    sayid = item.id
    uid = item.author.id
    tokenizedContent = jieba.cut(item.content)
    noStopwordsContent = delete_stopword(tokenizedContent)
    content = ' '.join(noStopwordsContent).encode('utf-8')
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
    title = delete_stopword(jieba.cut(question.title))
    detail = delete_stopword(jieba.cut(question.detail))
    content = ' '.join(title) + ' ' + ' '.join(detail)
    content = content.encode('utf-8')
    writer.writerow([sayid, ans, uid, content])
    get_says_from_comments(question)
    get_says_from_answers(question)

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    questionID = int(sys.argv[3])
    client = login(username, password)
    if client:
    	load_stopwords()
        question = client.question(questionID)
        get_says_from_question(question)
