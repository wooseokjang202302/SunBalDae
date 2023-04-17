import os
from multiprocessing import Process

# print('hello os')
# print('my pid is', os.getpid())


# def foo():
#     print('child process', os.getpid())
#     print('my parent is', os.getppid())


# if __name__ == '__main__':
#     print('parent process', os.getpid())
#     child = Process(target=foo).start()


# def boo():
#     print('hello, os')


# if __name__ == '__main__':
#     child1 = Process(target=boo).start()
#     child2 = Process(target=boo).start()
#     child3 = Process(target=boo).start()


def gab():
    print('This is gab')


def eul():
    print('This is eul')


def byeong():
    print('This is byeong')


if __name__ == '__main__':
    child1 = Process(target=gab).start()
    child2 = Process(target=eul).start()
    child3 = Process(target=byeong).start()
