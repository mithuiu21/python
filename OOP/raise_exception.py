
# try:
#     raise MemoryError('memory error')
# except MemoryError as e:
#     print(e)

class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def handle(self):
        print("accident occured. take detour")

try:
    raise Accident('crash between two cars')
except Accident as e:
    e.handle()


#finally()
# def process_file():
#     try:
#         #f = open("c:\\code\\data.txt")
#         x = 1/0
#     except FileNotFoundError as e:
#         print("inside except")

#     finally:
#         print("cleaning up file")
#         x.close()
 
# process_file()