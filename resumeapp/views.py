from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Resumelist

def resume_index(request):
    return render(request, 'resume_index.html')


def resume_list(request):
    resumelist = Resumelist.objects
    return render(request, 'resume_list.html', { 'resumelist' : resumelist })


def resume_input(request):

    company_list = ['대기업', '중소기업', '스타트업', '공공/공기업', '해외근무', '외국계기업']
    position = ['경영지원', 'IT개발','연구개발(R&D)/생산/제조','영업/마케팅','전문직/특수직무']
    position2 = ['사원/주임', '대리', '과장', '차장', '부장', '임원']
    position_detail1 = ['기획/전략/경영관리', '총무/법무/사무관리', '언론홍보/PR','회계/재무/세무/IR','인사/교육/노무','경영지원/기타']
    position_detail2 = ['웹개발','프론트엔드/백엔드/안드로이드/iSO','게임','서버/네트워크/보안','웹기획/PM','모바일개발','ERP/시스템분석/시스템설계','웹디자인','퍼블리싱/UIUX개발','하드웨어개발', '동영상편집/코덱', '데이터베이스/DBA', '인공지능/AI/빅데이터']
    position_detail3 = ['금속/금형', '기계/기계설비', '화학/에너지', '섬유/의류/패션', '전기/전자/제어', '생산관리/품질관리', '반도체/디스플레이', '바이오/제약/식품', '생산/제조','물류/유통/운송','납품/배송/택배','구매/자재/재고관리','선박/기사/중장비']
    position_detail4 = ['오프라인영업', '온라인영업', '마케팅/광고/홍보', '디지털마케팅', 'IT/솔루션영업', '금융/보험영업', 'B2B영업/광고영업/AE', '해외영업/해외무역', '국내영업/영업관리', '상품기획/MD', 'TM/고객서비스', '매장관리/점장']                   
    position_detail5 = ['방송/연예/엔터테인먼트', '카피/기자/에디터', '방송연출/PD/포토그래퍼', '경영분석/컨설턴트', '증권/투자/펀드/외환', '금융전문인력/은행/보험/증권', '연구소/R&D', '보건/간호/의료', '디자인/설계/건축/시공/인테리어']                  
    sex = ['남','여']
    edu = ['고졸','전졸','대졸(학사)','대학원졸(석사)','대학원졸(박사)']
    outcome = ['합','불']


    return render(request, 'resume_input.html', { 'sex' : sex, 'company_list' : company_list, 'edu':edu, 'position' : position , 'position2' : position2, 'outcome' : outcome, 'position_detail1' : position_detail1, 'position_detail2' : position_detail2, 'position_detail3' : position_detail3, 'position_detail4' : position_detail4, 'position_detail5' : position_detail5  })



def resume_create(request): # 입력받은 내용 데이터베이스에 넣어주기
    resumelist = Resumelist()  
    resumelist.company = request.POST['company'] #폼에 입력했던 name이 title 정보를 끌어온다.
    resumelist.position = request.POST['position']
    resumelist.position2 = request.POST['position2']
    resumelist.position_detail = request.POST['position_detail']
    resumelist.resume_name = request.POST['resume_name']
    resumelist.born_year = request.POST['born_year']
    resumelist.sex = request.POST['sex']
    resumelist.final_edu = request.POST['final_edu']
    resumelist.work_year = request.POST['work_year']
    resumelist.salary = request.POST['salary']
    resumelist.resume_detail = request.POST['resume_detail']
    resumelist.outcome = request.POST['outcome']  #폼에 입력했던 name이 body 정보를 끌어온다.
    resumelist.pub_date = timezone.datetime.now() # 작성 시간 출력해주는 함수, 상단에 임포트 해와야 함.
    resumelist.save()
    return redirect('resume_index')

