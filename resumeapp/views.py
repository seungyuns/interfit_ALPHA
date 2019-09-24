from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import time
from .models import Resumelist

from django.contrib import messages

from django.core.paginator import Paginator

def resume_search(request):
    qs = Resumelist.objects.all()
    resume_count = qs.count()
    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    
    if q: # q가 있으면
        qs = qs.filter(position_detail__icontains=q) | qs.filter(resume_name__icontains=q) | qs.filter(phone_number__icontains=q)
        resume_count = qs.count()
    return render(request, 'resume_list.html', {
        'posts' : qs,
        'q' : q,
        'resume_count' : resume_count
    })




def resume_index(request):
    return render(request, 'resume_index.html' )


def resume_list(request):
    resumelist = Resumelist.objects
    resume_list_all = Resumelist.objects.all().order_by('-pub_date')
    resume_count = resume_list_all.count()

    paginator = Paginator(resume_list_all, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'resume_list.html', { 'resumelist' : resumelist, 'resume_count' : resume_count, 'posts' : posts })

def resume_detail(request, resumelist_id):
    resumedetail = get_object_or_404(Resumelist, pk=resumelist_id)
    year = int(resumedetail.work_year)//10
    month = int(resumedetail.work_year)%10
    return render(request, 'resume_detail.html', {'resumedetail':resumedetail, 'year':year, 'month':month })


def resume_input(request):

    company_list = ['대기업', '중소기업', '스타트업', '공공/공기업', '해외근무', '외국계기업']
    position = ['경영지원', 'IT개발','연구개발(R&D)/생산/제조','영업/마케팅','전문직/특수직무']
    position2 = ['사원/주임', '대리', '과장', '차장', '부장', '임원']
    position_detail1 = ['기획/전략/경영관리', '총무/법무/사무관리', '언론홍보/PR','회계/재무/세무/IR','인사/교육/노무', '사업개발','경영지원/기타']
    position_detail2 = ['웹개발', 'Backend', 'Frontend', 'APP/앱','게임개발','서버/네트워크/보안','웹기획/PM', '서비스기획','모바일개발','ERP/시스템분석/시스템설계', '3D디자인/2D디자인', '제품디자인','퍼블리싱/UIUX개발','하드웨어개발', '동영상편집/코덱', '데이터베이스/DBA', '인공지능/AI/빅데이터']
    position_detail3 = ['금속/금형', '자동차', '기계/기계설비', '화학/에너지', '섬유/의류/패션', '전기/전자/제어', '생산관리/품질관리', '반도체/디스플레이', '바이오/제약/식품', '서비스디자인','제품디자인', '생산/제조','물류/유통/운송','납품/배송/택배','구매/자재/재고관리','선박/기사/중장비']
    position_detail4 = ['오프라인영업', '온라인영업', '마케팅/광고/홍보', '디지털마케팅', 'IT/솔루션영업', '금융/보험영업', 'B2B영업/광고영업/AE', '해외영업/해외무역', '국내영업/영업관리', '상품기획/MD', 'TM/고객서비스', '매장관리/점장', 'VMD', 'CRM', '브랜드마케팅', 'Data/퍼포먼스마케팅']                   
    position_detail5 = ['방송/연예/엔터테인먼트', '카피/기자/에디터', '방송연출/PD/포토그래퍼','동영상제작/동영상편집', '경영분석/컨설턴트', '증권/투자/펀드/외환', '금융전문인력/은행/보험/증권', '연구소/R&D', '보건/간호/의료', '디자인/설계/건축/시공/인테리어','변호사', 'CPA/AICPA']                  
    sex = ['남','여']
    edu = ['고졸','전졸','대졸(학사)','대학원졸(석사)','대학원졸(박사)']
    outcome = ['합','불']

    resume_count = Resumelist.objects.all().count()

    return render(request, 'resume_input.html', { 'sex' : sex, 'company_list' : company_list, 'edu':edu, 'position' : position , 'position2' : position2, 'outcome' : outcome, 'position_detail1' : position_detail1, 'position_detail2' : position_detail2, 'position_detail3' : position_detail3, 'position_detail4' : position_detail4, 'position_detail5' : position_detail5, 'resume_count' : resume_count  })



def resume_create(request): 
    resumelist = Resumelist()  
    resumelist.company = request.POST['company'] 
    resumelist.position = request.POST['position']
    resumelist.position2 = request.POST['position2']
    resumelist.position_detail = request.POST['position_detail']
    resumelist.resume_name = request.POST['resume_name']
    resumelist.born_year = request.POST['born_year']
    resumelist.sex = request.POST['sex']
    resumelist.final_edu = request.POST['final_edu']
    resumelist.work_year = request.POST['work_year']
    resumelist.work_year_avg = request.POST['work_year_avg']
    resumelist.salary = request.POST['salary']
    resumelist.salary_fit = request.POST['salary_fit']
    resumelist.job_fit = request.POST['job_fit']
    resumelist.phone_number = request.POST['phone_number']
    resumelist.email_address = request.POST['email_address']
    resumelist.resume_detail = request.POST['resume_detail']
    resumelist.outcome = request.POST['outcome']  
    resumelist.pub_date = timezone.datetime.now() 
    resumelist.save()

    return redirect('/resume_list/' + str(resumelist.id))

def resume_delete(request, resumelist_id):

    destroy =  get_object_or_404(Resumelist, pk=resumelist_id)
    destroy.delete()

    resumelist = Resumelist.objects
    resume_list_all = Resumelist.objects.all() 
    resume_count = resume_list_all.count()

    paginator = Paginator(resume_list_all, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'resume_list.html', { 'resumelist' : resumelist, 'resume_count' : resume_count, 'posts' : posts }) 

def resume_update(request, resumelist_id):

    company_list = ['대기업', '중소기업', '스타트업', '공공/공기업', '해외근무', '외국계기업']
    position = ['경영지원', 'IT개발','연구개발(R&D)/생산/제조','영업/마케팅','전문직/특수직무']
    position2 = ['사원/주임', '대리', '과장', '차장', '부장', '임원']
    position_detail1 = ['기획/전략/경영관리', '총무/법무/사무관리', '언론홍보/PR','회계/재무/세무/IR','인사/교육/노무', '사업개발','경영지원/기타']
    position_detail2 = ['웹개발', 'Backend', 'Frontend', 'APP/앱','게임개발','서버/네트워크/보안','웹기획/PM', '서비스기획','모바일개발','ERP/시스템분석/시스템설계', '3D디자인/2D디자인', '제품디자인','퍼블리싱/UIUX개발','하드웨어개발', '동영상편집/코덱', '데이터베이스/DBA', '인공지능/AI/빅데이터']
    position_detail3 = ['금속/금형', '자동차', '기계/기계설비', '화학/에너지', '섬유/의류/패션', '전기/전자/제어', '생산관리/품질관리', '반도체/디스플레이', '바이오/제약/식품', '서비스디자인','제품디자인', '생산/제조','물류/유통/운송','납품/배송/택배','구매/자재/재고관리','선박/기사/중장비']
    position_detail4 = ['오프라인영업', '온라인영업', '마케팅/광고/홍보', '디지털마케팅', 'IT/솔루션영업', '금융/보험영업', 'B2B영업/광고영업/AE', '해외영업/해외무역', '국내영업/영업관리', '상품기획/MD', 'TM/고객서비스', '매장관리/점장', 'VMD', 'CRM', '브랜드마케팅', 'Data/퍼포먼스마케팅']                   
    position_detail5 = ['방송/연예/엔터테인먼트', '카피/기자/에디터', '방송연출/PD/포토그래퍼','동영상제작/동영상편집', '경영분석/컨설턴트', '증권/투자/펀드/외환', '금융전문인력/은행/보험/증권', '연구소/R&D', '보건/간호/의료', '디자인/설계/건축/시공/인테리어','변호사', 'CPA/AICPA']                  
    sex = ['남','여']
    edu = ['고졸','전졸','대졸(학사)','대학원졸(석사)','대학원졸(박사)']
    outcome = ['합','불']

    updates = get_object_or_404(Resumelist, pk=resumelist_id)

    return render(request, 'resume_update.html', {'updates' : updates , 'sex' : sex, 'company_list' : company_list, 'edu':edu, 'position' : position , 'position2' : position2, 'outcome' : outcome, 'position_detail1' : position_detail1, 'position_detail2' : position_detail2, 'position_detail3' : position_detail3, 'position_detail4' : position_detail4, 'position_detail5' : position_detail5 })

def resume_edit(request, resumelist_id):

    edit = Resumelist.objects.get(pk=resumelist_id)

    edit.company = request.POST['company'] 
    edit.position = request.POST['position']
    edit.position2 = request.POST['position2']
    edit.position_detail = request.POST['position_detail']
    edit.resume_name = request.POST['resume_name']
    edit.born_year = request.POST['born_year']
    edit.sex = request.POST['sex']
    edit.final_edu = request.POST['final_edu']
    edit.work_year = request.POST['work_year']
    edit.work_year_avg = request.POST['work_year_avg']
    edit.salary = request.POST['salary']
    edit.salary_fit = request.POST['salary_fit']
    edit.job_fit = request.POST['job_fit']
    edit.phone_number = request.POST['phone_number']
    edit.email_address = request.POST['email_address']
    edit.resume_detail = request.POST['resume_detail']
    edit.outcome = request.POST['outcome']  
    edit.pub_date = timezone.datetime.now() 
    edit.save()
    
    return redirect('/resume_list/' + str(edit.id))
    
    