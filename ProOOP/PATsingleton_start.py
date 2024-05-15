
class DataBase:  # The task: create ONLY 1 DB and it should works one
    
    __instance = None

    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


    def __del__(self):  # If DB will be deleted, it will create new one
        DataBase.__instance = None


    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    
    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    
    def close(self):
        print("Закрытие соединения с БД")

    
    def read(self):
        return 'Данные из бд'


    def write(self, data):
        print(f'запись в БД создается...')


db = DataBase('root', '1212', 80)
db2 = DataBase('root2', '7676', 37)  # ссылается на первый объект, не создавая новый
print(id(db), id(db2))