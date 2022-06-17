# import time
# import tracemalloc
#
# def _time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print("Execution time", func.__name__, ':', end - start)
#
#     return wrapper
#
#
# @_time
# def test_list():
#     l = []
#     for i in range(50000):
#         l.append(i)
#
#
# @_time
# def test_set():
#     s = set()
#     for i in range(50000):
#         s.add(i)
#
#
# @_time
# def test_tuple():
#     t = ()
#     for i in range(50000):
#         t = t + (i,)


#
#
# test_list()
# test_set()
# test_tuple()
# #
# import tracemalloc
# def _memory(func):
#     def wrapper():
#         tracemalloc.start()
#         func()
#         print(tracemalloc.get_traced_memory())
#         tracemalloc.stop()
#     return wrapper
# @_memory
# def test_list():
#     l=[]
#     for i in range(5):
#         l.append(i)
# test_list()
import xlrd
workbook=xlrd.open_workbook("c:/users/Amaresh/Documents/TestData.xlsx")
worksheet=workbook.sheet_by_name("Registration")
rows=worksheet.get_rows()
print(rows)
