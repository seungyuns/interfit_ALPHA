from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Recruitlist

from django.core.paginator import Paginator

def position_search(request):
    qs = Recruitlist.objects.all()
    recruitlist_count = qs.count()
    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    
    if q: # q가 있으면
        qs = qs.filter(recruit_position_detail__icontains=q) | qs.filter(recruit_company_name__icontains=q)  # 제목에 q가 포함되어 있는 레코드만 필터링
        recruitlist_count = qs.count()
    return render(request, 'position_list.html', {
        'posts' : qs,
        'q' : q,
        'recruitlist_count' : recruitlist_count
    })



def position_input(request):

    company_list = ['대기업', '중소기업', '스타트업', '공공/공기업', '해외근무', '외국계기업']
    position = ['경영지원', 'IT개발','연구개발(R&D)/생산/제조','영업/마케팅','전문직/특수직무']
    position2 = ['사원/주임', '대리', '과장', '차장', '부장', '임원']
    position_detail1 = ['기획/전략/경영관리', '총무/법무/사무관리', '언론홍보/PR','회계/재무/세무/IR','인사/교육/노무', '사업개발','감사/컴플라이언스', '경영지원/기타']
    position_detail2 = ['웹개발', 'Backend', 'Frontend', 'APP/앱','게임개발','서버/네트워크/보안','웹기획/PM', '서비스기획','모바일개발','ERP/시스템분석/시스템설계', '그래픽디자이너', '제품디자인','퍼블리싱/UIUX개발','하드웨어개발', '동영상편집/코덱', '데이터베이스/DBA', '인공지능/AI/빅데이터', 'IT운영', '지원/QA', 'QC']
    position_detail3 = ['금속/금형', '자동차', '기계/기계설비', '화학/에너지', '섬유/의류/패션', '전기/전자/제어', '반도체/디스플레이', '바이오/제약/식품', '서비스디자인','제품디자인',  '생산관리/품질관리', '생산/제조','물류/유통/운송','납품/배송/택배','구매/자재/재고관리','선박/기사/중장비']
    position_detail4 = ['오프라인영업', '온라인영업', '마케팅/광고/홍보', '디지털마케팅', 'IT/솔루션영업', '금융/보험영업', 'B2B영업/광고영업/AE', '해외영업/해외무역', '국내영업/영업관리', '상품기획/MD', 'TM/고객서비스', '매장관리/점장', 'VMD', 'CRM', '브랜드마케팅', 'Data/퍼포먼스마케팅', '시장/고객Research', '영업지원/admin', 'Customer Success']                   
    position_detail5 = ['방송/연예/엔터테인먼트', '카피/기자/에디터', '방송연출/PD/포토그래퍼','동영상제작/동영상편집', '경영분석/컨설턴트', '증권/투자/펀드/외환', '금융전문인력/은행/보험/증권', '연구소/R&D', '보건/간호/의료', '디자인/설계/건축/시공/인테리어','변호사', 'CPA/AICPA', '요리', '미용', '뷰티']                  
    
    recruitlist_count = Recruitlist.objects.all().count()

    return render(request, 'position_input.html', { 'company_list' : company_list, 'position' : position , 'position2' : position2, 'position_detail1' : position_detail1, 'position_detail2' : position_detail2, 'position_detail3' : position_detail3, 'position_detail4' : position_detail4, 'position_detail5' : position_detail5, 'recruitlist_count' : recruitlist_count  })

def position_detail(request, recruitlist_id):

    recruitdetail = get_object_or_404(Recruitlist, pk=recruitlist_id)

    return render(request, 'position_detail.html', {'recruitdetail':recruitdetail})

def position_list(request):
    recruitlist = Recruitlist.objects
    recruitlist_all = Recruitlist.objects.all().order_by('-pub_date')
    recruitlist_count = recruitlist_all.count()

    paginator = Paginator(recruitlist_all, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'position_list.html', { 'recruitlist' : recruitlist, 'recruitlist_count' : recruitlist_count , 'posts' : posts})

def position_create(request): 

    recruitlist = Recruitlist() 
    recruitlist.recruit_company_name = request.POST['recruit_company_name'] 
    recruitlist.recruit_summary = request.POST['recruit_summary']
    recruitlist.recruit_phone = request.POST['recruit_phone']
    recruitlist.recruit_email = request.POST['recruit_email']
    recruitlist.recruit_company = request.POST['recruit_company']
    recruitlist.recruit_position = request.POST['recruit_position']
    recruitlist.recruit_position2 = request.POST['recruit_position2']
    recruitlist.recruit_position_detail = request.POST['recruit_position_detail']
    recruitlist.recruit_salary = request.POST['recruit_salary']
    recruitlist.recruit_position_detail2 = request.POST['recruit_position_detail2']
    recruitlist.recruit_company_detail = request.POST['recruit_company_detail']
    recruitlist.pub_date = timezone.datetime.now()
    recruitlist.save()
    
    return redirect('/position_list/' + str(recruitlist.id))

def position_delete(request, recruitlist_id):

    destroy_recruit =  get_object_or_404(Recruitlist, pk=recruitlist_id)
    destroy_recruit.delete()

    recruitlist = Recruitlist.objects
    recruitlist_all = Recruitlist.objects.all()
    recruitlist_count = recruitlist_all.count()

    paginator = Paginator(recruitlist_all, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'position_list.html', { 'recruitlist' : recruitlist, 'recruitlist_count' : recruitlist_count, 'posts' : posts }) 

def position_update(request, recruitlist_id):
    
    company_list = ['대기업', '중소기업', '스타트업', '공공/공기업', '해외근무', '외국계기업']
    position = ['경영지원', 'IT개발','연구개발(R&D)/생산/제조','영업/마케팅','전문직/특수직무']
    position2 = ['사원/주임', '대리', '과장', '차장', '부장', '임원']
    position_detail1 = ['기획/전략/경영관리', '총무/법무/사무관리', '언론홍보/PR','회계/재무/세무/IR','인사/교육/노무', '사업개발','감사/컴플라이언스', '경영지원/기타']
    position_detail2 = ['웹개발', 'Backend', 'Frontend', 'APP/앱','게임개발','서버/네트워크/보안','웹기획/PM', '서비스기획','모바일개발','ERP/시스템분석/시스템설계', '그래픽디자이너', '제품디자인','퍼블리싱/UIUX개발','하드웨어개발', '동영상편집/코덱', '데이터베이스/DBA', '인공지능/AI/빅데이터', 'IT운영', '지원/QA', 'QC']
    position_detail3 = ['금속/금형', '자동차', '기계/기계설비', '화학/에너지', '섬유/의류/패션', '전기/전자/제어', '반도체/디스플레이', '바이오/제약/식품', '서비스디자인','제품디자인', '생산관리/품질관리', '생산/제조','물류/유통/운송','납품/배송/택배','구매/자재/재고관리','선박/기사/중장비']
    position_detail4 = ['오프라인영업', '온라인영업', '마케팅/광고/홍보', '디지털마케팅', 'IT/솔루션영업', '금융/보험영업', 'B2B영업/광고영업/AE', '해외영업/해외무역', '국내영업/영업관리', '상품기획/MD', 'TM/고객서비스', '매장관리/점장', 'VMD', 'CRM', '브랜드마케팅', 'Data/퍼포먼스마케팅', '시장/고객Research', '영업지원/admin', 'Customer Success']                   
    position_detail5 = ['방송/연예/엔터테인먼트', '카피/기자/에디터', '방송연출/PD/포토그래퍼','동영상제작/동영상편집', '경영분석/컨설턴트', '증권/투자/펀드/외환', '금융전문인력/은행/보험/증권', '연구소/R&D', '보건/간호/의료', '디자인/설계/건축/시공/인테리어','변호사', 'CPA/AICPA', '요리', '미용', '뷰티']                  
    
    updates_recruit = get_object_or_404(Recruitlist, pk=recruitlist_id)

    return render(request, 'position_update.html', {'updates_recruit' : updates_recruit, 'company_list' : company_list, 'position' : position , 'position2' : position2, 'position_detail1' : position_detail1, 'position_detail2' : position_detail2, 'position_detail3' : position_detail3, 'position_detail4' : position_detail4, 'position_detail5' : position_detail5})

def position_edit(request, recruitlist_id):

    edit_recruit = Recruitlist.objects.get(pk=recruitlist_id)

    edit_recruit.recruit_company_name = request.POST['recruit_company_name'] 
    edit_recruit.recruit_summary = request.POST['recruit_summary']
    edit_recruit.recruit_phone = request.POST['recruit_phone']
    edit_recruit.recruit_email = request.POST['recruit_email']
    edit_recruit.recruit_company = request.POST['recruit_company']
    edit_recruit.recruit_position = request.POST['recruit_position']
    edit_recruit.recruit_position2 = request.POST['recruit_position2']
    edit_recruit.recruit_position_detail = request.POST['recruit_position_detail']
    edit_recruit.recruit_salary = request.POST['recruit_salary']
    edit_recruit.recruit_position_detail2 = request.POST['recruit_position_detail2']
    edit_recruit.recruit_company_detail = request.POST['recruit_company_detail']
    edit_recruit.pub_date = timezone.datetime.now()
    edit_recruit.save()

    return redirect('/position_list/' + str(edit_recruit.id))