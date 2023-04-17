import copy

text = "Hello, World!"
fruits = ["apple", "banana", "cherry"]
split_text = "apple,banana,cherry"
numbers = [1, 2, 3, 4, 5]
num_list = [3, 2, 4, 1, 5]
count_list = [1, 2, 3, 3, 4, 5]
empty_dict = {}
my_dict = {"apple" : 1, "banana" : 2, "orange" : 3}
person = {'name' : "Jhon", "age" : 30, "gender" : "male"}

# count: 문자열 내에서 특정문자가 몇 개나 있는지 세는 메서드
def method_count(text):
    count = text.count("l")
    print(count)

# find: 문자열 내에서 특정 문자열이 처음나오는 위치를 찾아주는 메서드(없을 경우 -1 리턴)
def method_find(text):
    position = text.find("World")
    print(position)

# index: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드(없을 경우 Value Error)
def metod_index(text):
    try:
        position = text.index("World")
        print(position)
    except ValueError:
        print("찾는 문자열이 없습니다.")

# join: 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 메서드
def method_join(list):
    list_ = list[:]
    joined_fruits = ", ".join(list_)
    print(joined_fruits)

# upper: 문자열 내의 모든 소문자를 대문자로 바꾸는 메서드
def method_upper(text):
    uppercase_text = text.upper()
    print(uppercase_text)

# lower: 문자열 내의 모든 대문자를 소문자로 바꾸는 메서드
def method_lower(text):
    lowercase_text = text.lower()
    print(lowercase_text)

# replace: 문자열 내에서 특정 문자열을 다른 문자열로 바꾸는 메서드
def method_replace(text):
    replaceed_text = text.replace("World", "Python")
    print(replaceed_text)

# split: 문자열을 특정 문자를 기준으로 나누는 메서드(결과는 리스트 형태로 반환)
def method_split(text):
    fruits_ = text.split(",")
    print(fruits_)

# len: 리스트의 길이를 반환하는 내장함수
def method_len(list):
    list_ = list[:]
    print(len(list_))

# del: 리스트에서 특정 요소를 삭제하는 연산자
def method_del(list):
    list_ = list[:]
    del list_[2]
    print(list_)

# append: 리스트의 맨 뒤에 새로윤 요소를 추가하는 메서드
def method_append(list):
    list_ = list[:]
    list_.append(6)
    print(list_)

# sort: 리스트를 오름차순으로 정렬하는 메서드
def method_sort(list):
    list_ = list[:]
    list_.sort()
    print(list_)

# reverse: 리스트의 요소 순서를 반대로 뒤집는 메서드
def method_reverse(list):
    list_ = list[:]
    list_.reverse()
    print(list_)

# index: 리스트에서 특정요소의 인덱스를 반환하는 메서드
def method_list_index(list):
    list_ = list[:]
    print(list_.index("banana"))

# insert: 리스트의 특정 위치에 요소를 삽입하는 메서드
def method_insert(list):
    list_ = list[:]
    list_.insert(2, 10)
    print(list_)

# remove: 리스트에서 특정 요소를 제거하는 메서드
def method_remove(list):
    list_ = list[:]
    list_.remove(3)
    print(list_)

# pop: 리스트에서 마지막 요소를 빼낸 뒤, 그 요소를 삭제하는 메서드
def method_pop(list):
    list_ = list[:]
    list_.pop(3)
    print(list_)

# count: 리스트에서 특정 요소의 개수를 세는 메서드
def method_list_count(list):
    list_ = list[:]
    print(list_.count(3))

# extend: 리스트를 확장하여 새로운 요소들을 추가하는 메서드
def method_extend():
    numbers = [1, 2, 3]
    numbers.extend([4, 5, 6])
    print(numbers)

# 딕셔너리 쌍 추가
def plus(dict):
    dict_ = copy.deepcopy(dict)
    dict_["grape"] = 4
    print(dict_)

# del: 딕셔너리에서 특정 요소를 삭제
def method_dict_del(dict):
    dict_ = copy.deepcopy(dict)
    del dict_["apple"]
    print(dict_)
    
# 딕셔너리에서 특정 key에 해당하는 value를 얻는 방법(딕셔너리에 키가 없다면 keyerror)
def print_dict(dict):
    print(dict["banana"])

# keys: 딕셔너리에서 모든 key를 리스트로 만들기
def method_keys(dict):
    key_list = list(dict.keys())
    print(key_list)

# values: 딕셔너리에서 모든 Value를 리스트로 만들기
def method_values(dict):
    value_list = list(dict.values())
    print(value_list)

# items: 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
def method_items(dict):
    items = dict.items()
    print(items)

# clear: 딕셔너리의 모든 요소를 삭제
def method_clear(dict):
    dict_ = copy.deepcopy(dict)
    dict_.clear()
    print(dict_)

# get:딕셔너리에서 지정한 키에 댛응하는 값을 반환(딕셔너리에 key사 없는 경우 None반환)
def method_get(dict):
    name = dict.get('name')
    print(name)

    email = dict.get('email')
    print(email)

    email = person.get('email', 'unknown')
    print(email)

# in: 해당 키가 딕셔너리 안에 있는지 확인
def method_in(dict):
    print('name' in dict)
    print('email' in dict)

method_count(text)
method_find(text)
metod_index(text)
method_join(fruits)
method_upper(text)
method_lower(text)
method_replace(text)
method_split(split_text)
method_len(numbers)
method_del(numbers)
method_append(numbers)
method_sort(num_list)
method_reverse(numbers)
method_list_index(fruits)
method_insert(numbers)
method_remove(numbers)
method_pop(numbers)
method_list_count(count_list)
method_extend()
plus(my_dict)
method_dict_del(my_dict)
print_dict(my_dict)
method_keys(my_dict)
method_values(my_dict)
method_items(person)
method_clear(person)
method_get(person)
method_in(person)