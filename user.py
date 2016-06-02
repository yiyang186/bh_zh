# encoding: utf-8

from zhihu_oauth import ZhihuClient
import sys
import csv

reload(sys)
sys.setdefaultencoding('utf-8')

users = set()
writer = csv.writer(file('user.csv', 'wb'), quotechar='|')
writer.writerow(['uid', 'name', 'gender', 'business', 'school', 'major',
                 'company', 'job', 'location'])

def login(username, password):
    client = ZhihuClient()
    client.login_in_terminal(username, password)
    # if client.is_login():
    #     me = client.me()
    #     print me.name, '成功登陆！'
    # else:
    #     print '登陆失败!'
    return client

def is_in_users(person):
    uid = person.id
    length_1 = len(users)
    users.add(uid)
    length_2 = len(users)
    if length_2 > length_1:
        return False
    else:
        return True

def get_info_from_person(person):
    uid = person.id
    name = person.name
    gender = person.gender
    business = person.business.name if person.business else ''
    school, major, company, job, location = '', '', '', '', ''
    if person.educations:
        for education in person.educations:
            school += education.school.name if 'school' in education else ''
            major += education.major.name if 'major' in education else ''
    if person.employments:
        for employment in person.employments:
            company += employment.company.name if 'company' in employment else ''
            job += employment.job.name if 'job' in employment else ''
    if person.locations:
        for aLocation in person.locations:
            location += aLocation.name
    writer.writerow([uid, name, gender, business, school, major, company,
                     job, location])

def get_info_from_comments(item):
    for comment in item.comments:
        person = comment.author
        if is_in_users(person):
            continue
        get_info_from_person(person)

def get_info_from_answers(item):
    for answer in item.answers:
        person = answer.author
        if is_in_users(person):
            continue
        get_info_from_person(person)
        get_info_from_comments(answer)

def get_user_info(question):
    get_info_from_comments(question)
    get_info_from_answers(question)

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    questionID = int(sys.argv[3])
    client = login(username, password)
    if client:
        question = client.question(questionID)
        get_user_info(question)
