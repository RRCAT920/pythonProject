# -*- coding: utf-8 -*-
import threading

local_school = threading.local()


def process_student() -> None:
    student = local_school.student
    print(f'{student}({threading.current_thread().name})')


def to_run(name: str) -> None:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=to_run, args=('张三',))
t2 = threading.Thread(target=to_run, args=('李四',))
t1.start()
t2.start()
t1.join()
t2.join()
