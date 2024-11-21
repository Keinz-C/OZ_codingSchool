import timeit
from sortedcontainers import SortedList

# list에 index가 없는 상황에서 brute force방식으로 탐색
# 데이터 삽입(DB에서는 INSERT와 동일)

print("리스트 생성 시작")
start_time_list = timeit.default_timer()	# 시간 측정하는 방법 내장 패키지 라이브러리
data_list = list(range(1, 300_000_001))		# range는 첫번째 인자부터 두번째 인자까지 사이의 숫자를 반환해준다. 첫 번재 인자는 포함되고 두번째 인자는 포함되지 않는다.
end_time_list = timeit.default_timer()
time_setup_list = end_time_list - start_time_list	# 최종 리스트 생성 시간을 확인하기 위해 끝난 시간에서 시작 시간을 빼준다.
print(f'리스트 생성 소요 시간: {time_setup_list:.6f} sec')


# tree(자가 균형 트리)로 index가 있는 상황에서 tree search를 통해 탐색
# 데이터 삽입(DB에서는 INSERT와 동일)
print("리스트 생성 시작")
start_time_tree = timeit.default_timer()
data_tree = SortedList(list(range(1, 300_000_001)))	
end_time_tree = timeit.default_timer()
time_setup_tree = end_time_tree - start_time_tree
print(f'트리 생성 소요 시간: {time_setup_tree:.6f} sec')


# 데이터 조회 (DB상 SELECT)
# list를 통한 탐색
def fetch_from_list(target):	# target : 찾고자 하는 책
    for data in data_list:		# brute force방식이라서 for문을 사용하여 리스트 안의 값을 하나하나 조회하도록 사용
        if data == target:
            return data_list[target]	# target과 data(list)가 일치하면 값을 반환
        

#tree를 통한 탐색
def fetch_from_tree(target):
    return data_tree[target]	# tree search 방식


# 함수를 호출하여 조회
# target 할당
target = 50_000_000

# List 조회
print("리스트 조회 시작")
time_list = timeit.default_timer()
fetch_from_list(target)		# target을 list조회용 함수에 호출
end_time_list = timeit.default_timer()	# 호출이 완료되면 조회에 사용한 시간 표시
time_fetch_list = end_time_list - start_time_list
print(f'리스트 조회 소요 시간: {time_fetch_list:.6f} sec')


# tree 조회
print("트리 조회 시작")
start_time_tree = timeit.default_timer()
fetch_from_tree(target)
end_time_tree = timeit.default_timer()
time_fetch_tree = end_time_tree - start_time_tree
print(f'트리 조회 소요 시간: {time_fetch_tree:.6f} sec')