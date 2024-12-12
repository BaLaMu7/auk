class Auction:
    def init(self):
        self.menu = Auction
        self.kartina = None

class App:      
    def init(self, App):
        self.App = App
            
    def register(self):
        print("Запрос на регистрацию")

    def ychastniki(self):
        print("Показывает список участников")
    
    def stavka(self):
        print("Запрос на повышение ставки")

    def stavka_up(self):
        print("Ставка повышена")

class Auction_pay:
    def init(self, Auction_pay):
        print("Ставка выйграна")

    def poluchenie_oplati(self):
        print("Получение оплаты")
    
class user:
    def init(self, user):
        self.user = user

    def user(self):
        print("Участник")

    def register(self):
        print("Регистрация")

    def place_an_kartina(self):
        print("Выбор картины")

    def delait_stavku(self):
        print("Делает ставку")

    def proverka(self):
        print("Проверка статуса ставки")


class pay:
    def init(self, dengi):
        self.platesh = dengi
    def printplatesh(self):
        print(self.platesh)

class oplata(pay):
    def init(self, dengi):
        super().init(dengi)

x = oplata("Платеж успешен")
x.printplatesh()