import requests
import time
import math

targets = int(input("희망하는 인원을 입력하세요 : "))

entry_dict = {
    1 : {
        "name" : "entry.1258127436",
        "entry" : ["네", "아니요"],
        "percentage" : [93, 7],
        "result" : [0, 0]
    },
    2 : {
        "name" : "entry.1897951779",
        "entry" : ["1년 미만", "1년 이상 2년 미만", "3년 이상 3년 미만", "3년 이상 4년 미만", "4년 이상"],
        "percentage" : [15, 22, 8 , 31, 24],
        "result" : [0,0,0,0,0]
    }, 
    3 : {
        "name" : "entry.1861666083",
        "entry" : ["최경도", "경도", "중증도", "중증", "심각"],
        "percentage" : [5, 19, 44, 32, 4],
        "result" : [0,0,0,0,0]
    },
    4 : {
        "name" : "entry.1609543169",
        "entry" : ["초기 증상 인식 어려움", "초기 증상 간과", "높은 검사 가격", "낮은 검사 병원 접근성 및 시간적 여유 부족", "치매 검사에 대한 신뢰성 부족"],
        "percentage" : [30, 23, 22, 23, 8],
        "result" : [0,0,0,0,0]
    },
    5 : {
        "name" : "entry.1408933450",
        "entry" : ["치매 관련 교육 및 정부 지원 사업", "심리 상담 및 스트레스 관리 지원", "정기적인 인지 기능 검사 및 치매 초기 증상 알림", "경제적 지원 및 보험 정보 제공"],
        "percentage" : [27, 10, 45, 18],
        "result" : [0,0,0,0]
    },
    6 : {
        "name" : "entry.1173495039",
        "entry" : ["사용할 것 같다", "생각해볼 것 같다", "잘 모르겠다", "다른 옵션을 우선적으로 고려할 것 같다"],
        "percentage" : [56, 12, 7, 15],
        "result" : [0,0,0,0]
    }
}
post_body = {}
for i in range(0, targets):
    for j in range(1, len(entry_dict)+1):
        for p in range(0, len(entry_dict[j]["entry"])):
            if math.ceil((entry_dict[j]["result"][p]/targets)*100) < entry_dict[j]["percentage"][p]:
                post_body[entry_dict[j]["name"]] = entry_dict[j]["entry"][p]
                entry_dict[j]["result"][p] += 1
                break

    post_url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfCc3sOFBN6lOkzGb-h8lQ2CTnO07lQUweEBHtE20XMAwtNwA/formResponse"
    response = requests.post(post_url, data=post_body)

    if response.status_code == 200:
        print("설문 완료 - ", str(i + 1))
    else:
        print("오류 발생(" + str(response.status_code) + ") - ", str(i + 1))
    post_body = {}
    time.sleep(3)
