import random
from PIL import Image

count = 0
fail = []
TOTAL = [
    ["분석 과제 우선순위 평가 기준에서 전략적 중요도, 목표 가치와 관련이 있는 빅데이터 특성은 무엇인가?" ,  #1
    [["Value"],
    ["Volume"],
    ["Variety"],
    ["Velocity"]],[1]],

    ["다음 중 데이터 사이언티스트에게 요구되는 역량을 설명한 것으로 가장 부적절한 것은 무엇인가?" ,  #2
    [["스토리텔링, 데이터 시각화를 사용하는 등 설득력 있는 전달을 위해 Soft Skill이 필요하다."],
    ["빅데이터에 대한 이론적 지식인 Soft Skill이 필요하다."],
    ["최적의 분석 설계 및 노하우 축적하는 등 분석기술에 대한 숙련을 위해 Hard Skill이 필요하다."],
    ["창의적 사고, 호기심, 논리적 비판하는 Soft Skill이 필요하다."]] ,[2]],

    ["다음의 하둡 에코시스템 중에서 비정형 데이터 수집을 위한 시스템으로 가장 부적절한 것은 무엇인가?", #3
    [["척와(Chukwa)"],
    ["플럼(Flume)"],
    ["스크라이브(Scribe)"],
    ["피그(Pig)"]], [4]],

    ["다음 중 개인정보의 수집이용을 위해 정보주체의 동의를 받을 때 고지사항으로 가장 올바르지 않은 것은?",  # 4
     [["개인정보의 수집·이용 목적"],
      ["동의를 거부할 권리가 있다는 사실 및 동의 거부에 따른 불이익이 있는 경우에는 그 불이익의 내용"],
      ["개인정보를 수집하는 기관, 담당자 연락처"],
      ["수집하려는 개인정보의 항목"]], [3]],

    ["다음 중 인터넷상에서 제공되는 다양한 웹 사이트로 부터 소셜 네트워크 정보, 뉴스, 게시판 등의 웹 문서 및 콘텐츠를 수집하는 기술은 무엇인가?",  # 5
     [["RSS(Rich Site Summary)"],
      ["Open API."],
      ["아파치 카프카(Apach Kafka"],
      ["크롤링(Crawling)"]], [4]],

    ["다음이 설명하는 빅데이터의 유형으로 가장 올바른 것은 무엇인가?\n\n"  # 6

     "-보기-\n"
     '''
     -수집 데이터 각각이 데이터 객체로 구분\n
     -고정 필드 및 메타데이터(스키마 포함)가 정의되지 않음\n
     -텍스트 문서, 이진 파일, 이미지, 동영상 등\n\n
     '''
,
     [["1. 정형 데이터"],
        ["2. 반정형 데이터"],
        ["3. 비정형 데이터"],
        ["4. 정수형 데이터"]], [3]],

    ["다음 중 분석 가치 에스컬레이터에 대한 설명으로 가장 올바르지 않은 것은?\n\n",  # 7

     [["1. 묘사 분석은 과거에 어떤 일이 일어났고, 현재는\n"
       "무슨 일이 일어나고 있는지 확인하는 분석이다."],
        ["2. 진단 분석은 데이터를 기반으로 왜 발생했는지"
         "이유를 확인하는 분석이다."],
        ["3. 예측 분석은 무엇을 해야 할 것인지를 확인하는 분석이다."],
        ["4. 분석 가치 에스컬레이터에서는 높은 난도를 수반 하는",
         "데이터 부석은 더 많은 가치를 창출한다."]], [3]],

    ["다음 중 기업의 데이터 분석 수준을 파악하기 위한 조직 평가 성숙도 단계에 대한 설명으로 적절하지 않은 것은?\n\n", #8

     [["1. 도입 단계는 분석을 시작하는 단계로 환경과 시스템을 구축하고, 전문 담당 부서에서 분석을 수행하는 단계이다."],
        ["2. 활용 단계는 분석 결과를 실제 업무에 적용하는 단계로 분석 기법을 도입하는 단계이다."],
        ["3. 확산 단계는 전사 차원에서 분석을 관리하고 공유하는 단계이다."],
        ["4. 최적화 단계는 분석을 진화시켜서 혁신 및 성과 향상에 기여하는 단계이다."]], [1]],

    ["다음 중 CRISP-DM 분석 방법론에서의 데이터 준비 과정을 설명한 것으로 가장 적절한 것은 무엇인가?\n\n", #9

     [["1. 다양한 모델링 기법과 알고리즘을 선택하고 파라미터를 최적화한다."],
        ["2. 분석 결과 평가, 모델링 과정을 평가한다."],
        ["3. 전계 계획 수립, 모니터링과 유지보수 계획을 수립한다."],
        ["4. 분석용 데이트 세트 선택, 데이터 정제,"
         "데이터 봉합 등을 수행한다."]], [4]],

    ["다음 중 가명처리 4단계 절차에 대한 설명으로 가장 올바르지 않은 것은?", #10

     [["1. 사전준비 단계 - 가명처리 대상 항목 및 처리수준을 정의하기 위해서는 처리 목적이 적합한지 여부를 확인하고 사전 계획을 수립한다."],
        ["2. 가명처리 단계 - 가명 정보처리 시에도 목적에 부합되면 개인정보를 최대한 제공할 수 있도록 처리해야 하며, \n"
         "  가명처리 방법을 정할 때에는 처리목적, 처리(이용 또는 제공)환경, 정보의 성격 등을 종합적으로 고려한다."],
        ["3. 적정성 검토 및 추가처리 - 목적달성을 위해 적절한 수준으로 가명처리가 이루어졌는지, 재식별 가능성은 없는지 등에 대한 최종적인 판단절차를 수행한다."],
        ["4. 사후관리 - 적정성 검토 결과 가명처리가 적정하다고 판단되면 가명 정보를 본래 활용 목적을 위해서 처리할 수 있으며,\n"
         "법령에 따라 기술적, 관리적, 물리적, 안전조치를 이행한다."]], [2]],

    ["2번 다음 중 빅데이터 유형의 사례를 설명한 것으로 가장 부적절한 것은 무엇인가?",  # 11
     [["정형    - 관계형 데이터 베이스"],
      ["정형    - HTML"],
      ["반정형   - JSON, XML"],
      ["비정형 - 텍스트 문서, 이미지"]], [2]],

    ["빅데이터 플랫폼은 원천 데이터에서 정형, 반정형, 비정형 데이터를 수집하고 저장한다. 다음 중 빅데이터 수집 기술로 가장 부적절한 기법은 무엇인가?",  # 12
     [["NoSQL"],
      ["ETL"],
      ["EAI"],
      ["크롤러(Crawler)"]], [4]],

    ["데이터 거버넌스 체계에 대한 설명으로 가장 올바르지 않은 것은 ?",  # 13
     [["데이터 표준 용어 설명, 명명 규칙, 메타데이터 구축, 데이터 사전 구축 등 데이터 표준화를 관리 해야한다."],
      ["메타 데이터와  사전의 관리 원칙 수립을 해야한다."],
      ["메타데이터 및 표준 데이터를 관리하기 위한 별도의 저장소 구축은 필요 없다"],
      ["데이터 거버넌스 체계 구축 이후 표준 준수 여부를 주기적으로 점검 및 모니터링을 실시해야 한다."]], [3]],

    ["다음 분석의 대상이 무엇인지를 인지하고 있는 경우(Known), 즉 해결해야 할 문제를 알고 있고 이미 분석의 방법도 알고 있는 경우(Known)에\n"
     " 사용하는 분석 유형은 무엇인가?",  # 14
     [["최적화(Optimization)   "],
      ["솔루션(Solution)"],
      ["통찰(Insight)"],
      ["발견(Discovery)"]], [1]],

    ["빅데이터 수집 시스템에서 수집 대상이 되는 데이터를 시간관점(활용주기)에서 분류하면 실시간 데이터, 비실시간 데이터로 나눌 수 있다.\n"
     " 다음 중 실시간 데이터로 가장 부적절한 것은 무엇인가?",  # 15
     [["IoT 센서 데이터 "],
      ["네트워크 장비 로그"],
      ["구매 정보"],
      ["알람"]], [3]],

    ["다음 중 데이터 사이언티스트의 일반적인 요구 역량으로 가장 적합하지 않은 것은?",  # 16
     [["통찰력 있는 분석"],
      ["다분야 간 협력"],
      ["빅데이터에 대한 이론적 지식"],
      ["높은 지능과 과학적 지식"]], [4]],

    ["다음 중 대용량 파일을 저장하고 처리하기 위해서 개발된 파일 시스템으로 네임노드(Master)와 데이터노드(Slave)로 구성된 것은?",  # 17
     [["아파치 스파크(Apache Spark)"],
      ["얀(YARN)"],
      ["맵리듀스(Map Reduce)"],
      ["하둡 분산 파일 시스템(HDFS)"]], [4]],

    ["다음 중 개인정보 비식별 조치 방법으로 가장 올바르게 설명한 것은 무엇인가?",  # 18
     [["데이터 마스킹: 정약용, 21세 -> 박 씨, 20~30세"],
      ["데이터 범주화: 정약용, 21세 -> 정 씨, 평균 20세"],
      ["가명처리: 정약용, 21세 -> 장길산, 20대"],
      ["총계처리: 장길산 160cm, 정약용 180cm -> 학생 키 150~200cm"]], [3]],

    ["다음 중 개인정보를 목적 외의 용도로 이용하거나 제 3자에게 제공이 가능한 경우로 옳지 않는 것은?",  # 19
     [["정보주체로부터 별도의 동의를 받은 경우   "],
      ["데이터 이용 활성화를 위한 통계작성에 이용해야 할 경우"],
      ["다른 법률에 특별한 규정이 있는 경우"],
      ["범죄의 수사와 공소의 제기 및 유지를 위하여 필요한 경우"]], [2]],

    ["다음 중 l-다양성의 쏠림 공격, 유사성 공격을 보완하기 위한 프라이버시 보호 모델로 동질 집합에서 특정 정보의 분포와 전체 데이터 집합에서\n"
     "정보의 기준값 이하의 차이를 보여야 하는 모델은?",  # 20
     [["k-익명성"],
      ["k-가명성"],
      ["m-유일성"],
      ["t-근접성"]], [4]],

    # ["문제",  # 2
    #  [["보기1"],
    #   ["보기2"],
    #   ["보기3"],
    #   ["보기4"]], "정답"],
]

Q_SEQ = random.sample(range(0,len(TOTAL)),len(TOTAL))
for i in range(len(Q_SEQ)):
    print("<"+str(i+1)+"> " + TOTAL[Q_SEQ[i]][0])
    if len(TOTAL[Q_SEQ[i]]) >3 :
        path = 'C:\\Users\\JEDEE\\OneDrive\\바탕 화면\\workspace\\html,jquery\\discord\\sqlImage/'+str(Q_SEQ[i]+1)+'.jpg'
        im = Image.open(path)  # 이미지 불러오기
        im.show()  # 이미지 보여주기
    print()
    ex_rand = random.sample(range(0, 4), 4)
    for j in range(4):
        print(str(j+1)+". "+TOTAL[Q_SEQ[i]][1][ex_rand[j]][0])
    user_answer2=[]
    user_answer = input().split()
    for i2 in range(len(user_answer)):
        user_answer2.append(TOTAL[Q_SEQ[i]][1].index(TOTAL[Q_SEQ[i]][1][ex_rand[int(user_answer[i2])-1]])+1)
    user_answer2 = list(map(int, user_answer2))
    user_answer2.sort()

    if user_answer2 == TOTAL[Q_SEQ[i]][2]:
        count+=1
    else:
        fail.append([Q_SEQ[i]+1,user_answer2])
    print("\n"*100)
    # print(user_answer2, TOTAL[Q_SEQ[i]][2])
print("모든 문제가 끝났습니다.")
print("점수는 " + str(round( (count/len(TOTAL))*100 ,1))+" 점 입니다.")
fail.sort(key=lambda x : (x[0]))
print("틀린문제 " , fail )