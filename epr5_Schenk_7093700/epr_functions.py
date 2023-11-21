""" This script contains 3 different functions for the new exercise in epr """

__author__ = "7093700, Schenk"

import requests


def call_api():
    url = 'https://lrs.studiumdigitale.uni-frankfurt.de/data/xAPI/activities/state?activityId=https://moodle.studiumdigitale.uni-frankfurt.de/course.d06f71786ac6450bbd60e752b665a84f&agent={"objectType":"Agent","name":"Schenk, Philipp","account":{"name":"s5477353","homePage":"https://moodle.studiumdigitale.uni-frankfurt.de/"}}&stateId=state_20221101.175850'
    data = {"question|-_-|c8a4e37703e846b68481c5365303d03c":{"answers":[False,True,True,True],"points":0,"response":"0_1_0_0","triesMade":2,"solutionShown":False,"history":[{"answers":[True,False,False,False],"points":100,"response":"1_0_0_0","triesMade":0,"solutionShown":False,"timestamp":1698951588496}],"timestamp":1700583717461}}
    headers = {'Authorization': 'Basic ',
               'X-Experience-API-Version': '1.0.1'}
    response = requests.post(url, headers=headers, json=data)
    print(response)
    print(response.text)

    url2 = 'https://lrs.studiumdigitale.uni-frankfurt.de/data/xAPI/statements'
    data = {"actor":{"name":"Schenk, Philipp","account":{"name":"s5477353","homePage":"https://moodle.studiumdigitale.uni-frankfurt.de/"}},"verb":{"id":"http://adlnet.gov/expapi/verbs/answered","display":{"de-DE":"beantwortete","en-US":"answered","fr-FR":"a répondu","es-ES":"contestó"}},"object":{"objectType":"Activity","id":"https://moodle.studiumdigitale.uni-frankfurt.de/course.d06f71786ac6450bbd60e752b665a84f/question.c8a4e37703e846b68481c5365303d03c"},"result":{"score":{"scaled":0,"raw":0,"min":0,"max":100},"success":True,"response":"0_1_0_0"},"context":{"contextActivities":{"grouping":[{"objectType":"Activity","id":"https://moodle.studiumdigitale.uni-frankfurt.de/course.d06f71786ac6450bbd60e752b665a84f"}],"parent":[{"objectType":"Activity","id":"https://moodle.studiumdigitale.uni-frankfurt.de/course.d06f71786ac6450bbd60e752b665a84f/page.10228a5a63e549e0896fb6fe15439134"}]},"revision":"20221101.175850","language":"de","instructor":{"objectType":"Agent","name":"anonymous","account":{"name":"anonymous","homePage":"http://lernbar.uni-frankfurt.de"}},"extensions":{"http://id.tincanapi.com/extension/irl":"https://moodle.studiumdigitale.uni-frankfurt.de/moodle/mod/scorm/loadSCO.php?a=1906&scoid=4119&currentorg=ORG-d06f71786ac6450bbd60e752b665a84f&mode=review&attempt=1","http://lernbar.uni-frankfurt.de/extensions/lms/scormid":"1906","http://lernbar.uni-frankfurt.de/xAPI/activities/question":"question.c8a4e37703e846b68481c5365303d03c","http://lernbar.uni-frankfurt.de/xAPI/activities/question/type":"singleChoice","http://lernbar.uni-frankfurt.de/xAPI/activities/page":"page.10228a5a63e549e0896fb6fe15439134","http://lernbar.uni-frankfurt.de/xAPI/activities/page/type":"H","http://lernbar.uni-frankfurt.de/xAPI/activities/lesson":"lesson.5df7d3cab5dd4edf90a6e186851a37ab","http://lernbar.uni-frankfurt.de/xAPI/activities/course":"course.d06f71786ac6450bbd60e752b665a84f","https://w3id.org/xapi/video/extensions/user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0"}}}
    response = requests.post(url, headers=headers, json=data)
    print(response)
    print(response.text)


if __name__ == '__main__':
    call_api()