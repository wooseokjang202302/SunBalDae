phone_book = {"Jhon": "123-4567", "Jane": "234-5678", "Max": "345-6789"}

def search():
    name = yield
    while True:
        if name in phone_book:
            phone_number = phone_book[name]
        else:
            phone_number = "Cannot find the name in the phone book."
        name = yield phone_number

# 코루틴 객체 생성
search_corutine = search()
next(search_corutine)

# 검색 예시
result = search_corutine.send("Jhon")
print(result)

result = search_corutine.send("Jane")
print(result)

result = search_corutine.send("Sarah")
print(result)
