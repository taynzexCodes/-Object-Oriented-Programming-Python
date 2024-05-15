class DataBase_from_2nd_app:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }


    def __init__(self):
        self.__dict__ = self.__shared_attrs
"""
th1 = DataBase_from_2nd_app()   # Одинаковое пространство имен
th2 = DataBase_from_2nd_app()
""" 