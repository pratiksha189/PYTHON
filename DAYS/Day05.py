# class Car:
#     count = 0
#     def __init__(self,make,model,price,segment="Economy"):
#         Car.count+=1
#         self._make = make
#         self._model = model
#         self._price = price
#         self._segment = segment
#         def calculate_premium(self,tenure):
#             if self._segment=="Economy":
#                 return self.price * tenure*0.05
#             else:
#                 return self.price * tenure*0.01
#         @staticmethod
#         def show_count():
#             print('Total cars :',Car.count)
#         @classmethod
#         def set_count(cls):
#         cls.count=100
