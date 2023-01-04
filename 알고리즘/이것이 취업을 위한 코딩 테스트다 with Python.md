시간 복잡도 : 필요 연산 횟수
공간 복잡도 : 필요 메모리 양

ㅇ빅오 표기법 명칭 :
<img width="376" alt="default" src="https://user-images.githubusercontent.com/117712307/209524753-df3e078b-1a6b-4045-99b3-44be3634bdec.png">

단, 빅오 표기법이 항상 절대적인 것은 아님
3N^3 + 5N^2 + 1,000,000 경우 N=10 이라고 하는 경우, 상수의 영향이 큼

ㅇ출제 빈도 높음 : greedy, implementation, DFS/BFS 활용 탐색

ㅇ입력의 범위를 보고 요구하는 시간복잡도 생각하기
<img width="650" alt="스크린샷 2022-12-06 오후 1 38 13" src="https://user-images.githubusercontent.com/117712307/205816722-bbd0b673-018b-4481-af93-598be427ff74.png">
* 절대적인 기준은 아님, 대충 감잡는정도로만 이용 

ㅇ 실수 값 비교할 때 round() 함수 이용, *round(123.4567, 2) => 123.45

ㅇ 리스트
* 리스트 컴프리헨션 이용하기(2차원 리스트 초기화에 효과적)
* 비교
```
코드1 : 리스트 컴프리헨션
array = [ i for i in range(20 if % 2 == 1)]

코드2 : 일반
array = []
for i in range(2):
    if i % 2 == 1:
        array.append(i)
    
print(array)
--
[1,3,5,7,9,11,13,15,17,19]

```

ㅇ 언더바( _ )
변수 설정 없이 값 출력 원할때 사용

ㅇ 메서드
<img width="1122" alt="default" src="https://user-images.githubusercontent.com/117712307/210305807-5a7d5667-eb9e-4cfb-9e1b-915b1128de12.png">

ㅇ 튜플
튜플을 사용하면 좋은 경우
* 서로 다른 성질의 데이터를 묶어서 관리할떄
* 최단 경로 알고리즘에서(비용(실수값으로 저장), 노드번호(1,2,3,4))의 형태로 튜플 자료형 자주 사용
* 데이터를 해싱의 키 값으로 사용해야 할 때(변경 불가능 해서 리스트와 다르게 키 값 사용가능)
* 리스트보다 메모리를 효율적으로 사용해야 할 때
리스트, 튜플 순차적 데이터 저장

ㅇ 사전 자료형
키와 값을 쌍으로 데이터로 가지는 자료형

ㅇ 집합 자료형
중복 허용x 순서x
리스트 혹은 문자열을 이용해 초기화 (set() 이용 Or {}안에 , 써서 초기화)
데이터 조회 및 수정 => O(1)의 시간 소요
합집합, 교지합, 차집합 연산 가능
.add, .update, .remove

사전자료형, 집합자료형 => 순서가 없기때문에 인덱싱으로 값을 얻을 수 없음

ㅇ 기본 입출력
input(), map()
list(map(int, input().split()))
a,b,c = map(int, input().split())

ㅇ 빠르게 입력받기
sys.stdin.readline().rstrip()

ㅇ 출력 줄바꿈 방지 => end속성 이용
print(123, end=" ")

ㅇ 실전에서 유용한 표준 라이브러리
<img width="947" alt="default 713" src="https://user-images.githubusercontent.com/117712307/210587462-cac9b8cd-6165-461f-90de-ab52113675d3.png">

* 자주 사용 내장함수
eval() = 수식으로 표현된 식을 계산 한 결과를 실제 수로 반환해줌 ((3+5)*7 을 56으로 반환해줌)
sorted() = 정렬 (람다와 함꼐 공부)

* <img width="1112" alt="default" src="https://user-images.githubusercontent.com/117712307/210588203-6da2f31a-3675-4a7f-95ff-c9cb1d102915.png">

* 순열
<img width="1033" alt="default" src="https://user-images.githubusercontent.com/117712307/210588453-f1da8656-2e1a-41b9-ac26-08cc47217406.png">

* 조합
<img width="1026" alt="default" src="https://user-images.githubusercontent.com/117712307/210588598-79e86e69-f860-44a9-b46b-c81fde249a55.png">

* 중복순열 중복 조합
<img width="1095" alt="default 2" src="https://user-images.githubusercontent.com/117712307/210588844-c7ce9c86-a2ba-4900-b5fd-08c9801cd094.png">

* counter
<img width="1056" alt="default" src="https://user-images.githubusercontent.com/117712307/210588938-efe42506-ff27-4e99-bca8-3f0de466c0cf.png">

* 최대 공약수, 최소 공배수
<img width="890" alt="default" src="https://user-images.githubusercontent.com/117712307/210589238-693d5f9e-5caf-4030-850e-466b4b97c749.png">

* 


1) 그리디
- 문제에서 '가장 큰 순서대로', '가장 작은 순서대로' 같은 기준을 알게 모르게 제시해준다. 
- 코테에서 바로 문제유형 파악 힘들다면 그리디 알고리즘 의심부터 의심
