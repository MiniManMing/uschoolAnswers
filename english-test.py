import urllib.request
import json
import jsonpath

header_selfdefine={
    'Connection':'keep-alive',
    'x-annotator-auth-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcGVuX2lkIjoiZWI1ODgxZDI5NmQ0NDcyOGIyM2E5YWM3NmFhNzA3MGEiLCJuYW1lIjoiIiwiZW1haWwiOiIiLCJhZG1pbmlzdHJhdG9yIjpmYWxzZSwiZXhwIjoxNTc2Njc2NjUyMjQyLCJpc3MiOiJjNGY3NzIwNjNkY2ZhOThlOWM1MCIsImF1ZCI6ImVkeC51bmlwdXMuY24ifQ.sdbsQoHgSuiYjgdvJaagfIoqxotF4jpPiu-xk_m7g_Y',
    'x-csrftoken':'undefined',
    'Accept':'*/*',
    'Referer':'http://127.0.0.1:8090/uex/course-v1:Unipus+CELS_3+2017_09/u4g346/_exerciseType_3/_sed_1/_ntc_1/_nad_1/_css_1/_sms_1/_lcs_1/_required_1/_startTime_0/_endTime_0/_for_default/preview.html',
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
    'Host':'uexeapi.unipus.cn',
    'If-Modified-Since':'Tue, 18 Dec 2018 14:22:35 GMT'
}
question_list=["297","298"]
for item in question_list:
 url_request="http://uexeapi.unipus.cn/api/mobile/stu/homework/content/"+item+"/u0g1-173"
 print(url_request)
 request_obj=urllib.request.Request(url=url_request,headers=header_selfdefine)
 response_obj=urllib.request.urlopen(request_obj)
 html_code=response_obj.read().decode("utf8")
 format1= json.loads(html_code)
 answer_list= jsonpath.jsonpath(format1,"$..answers")
 print(answer_list)

