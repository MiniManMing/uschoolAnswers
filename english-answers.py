import urllib.request
import json
import jsonpath

header_selfdefine={
     'Connection':'keep-alive',
     'x-annotator-auth-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcGVuX2lkIjoiZWI1ODgxZDI5NmQ0NDcyOGIyM2E5YWM3NmFhNzA3MGEiLCJuYW1lIjoiIiwiZW1haWwiOiIiLCJhZG1pbmlzdHJhdG9yIjpmYWxzZSwiZXhwIjoxNTc2Njc2NjUyMjQyLCJpc3MiOiJjNGY3NzIwNjNkY2ZhOThlOWM1MCIsImF1ZCI6ImVkeC51bmlwdXMuY24ifQ.sdbsQoHgSuiYjgdvJaagfIoqxotF4jpPiu-xk_m7g_Y',
     'x-csrftoken':'undefined',
     'uni-ucontent-ver':'7a5cdde',
     'content-type':'application/json',
     'Accept':'*/*',
     'Referer':'http://127.0.0.1:8090/_mobile_default/',
     'Accept-Language':'zh-CN,en-GB;q=0.9,en-US;q=0.8',
     'X-Requested-With':'cn.unipus.ucampus.student',
     'User-Agent':'android8.0.0 ONEPLUS A3010',
     'uni-ticket':'ST-3882822-E7KaXWfIUkySTxrp4z7z-unipus41',
     'uni-openid-hash':'87HmGEPMK3HHV1Y1bn94z8ON0paNyrtiXnk43+FIsFs=',
     'uni-device-token':'1104a89792fd8fa4807',
     'uni-device-id':'862561037439534',
     'uni-udid':'',
     'uni-os':'android',
     'uni-os-ver':'android8.0.0',
     'uni-model':'ONEPLUS A3010',
     'uni-app-ver':'1.0',
     'uni-app-prod':'ucampus-student',
     'uni-js-ver-models':'ucontent uex',
     'uni-js-ver':'209001 209005',
     'uni-client-ver':'19000',
     'Host':'ucontentapi.unipus.cn',
     'If-Modified-Since':'Tue, 18 Dec 2018 13:26:09 GMT'
}
question_list=["u0g20","u0g21","u0g22","u1g180","u1g187","u1g194","u2g181","u2g188","u2g195","u3g182","u3g189","u3g196","u5g300","u5g304","u5g308","u6g301","u6g305","u6g309","u7g302","u7g306","u7g310","u8g303","u8g307","u8g311"]
for item in question_list:
 url_request="http://ucontentapi.unipus.cn/course/api/content/course-v1:Unipus+CELS_3+2017_09/"+item+"/default/"
 request_obj=urllib.request.Request(url=url_request,headers=header_selfdefine)
 response_obj=urllib.request.urlopen(request_obj)
 html_code=response_obj.read().decode("utf8")
 format = json.loads(html_code)
 format2 =json.loads(format['content'])
 format3 = format2['questions:questions']
 print(item)
 answer_list= jsonpath.jsonpath(format3['questions'],"$..answers")
 print(answer_list)

