import threading
import os

# print('process id', os.getpid())


# def foo():
#     print('tread id', threading.get_native_id())
#     print('process id', os.getpid())


# if __name__ == '__main__':
#     print('process id', os.getpid())
#     thread1 = threading.Thread(target=foo).start()
#     thread2 = threading.Thread(target=foo).start()
#     thread3 = threading.Thread(target=foo).start()


# 각기 다른 작업을 하는 스레드 생성하기
def gab():
    print('This is gab')


def eul():
    print('This is eul')


def byeong():
    print('This is byeong')

if __name__ == '__main__':
    print('process id', os.getpid())
    thread1 = threading.Thread(target=gab).start()
    thread2 = threading.Thread(target=eul).start()
    thread3 = threading.Thread(target=byeong).start()