class Mailing:
    def _init_(self, to_adress, from_adress, cost, track):
        self.to_adress = to_adress
        self.from_adress = from_adress
        self.cost = cost
        self.track = track

    def _str_(self):
        return (f"Отправление {self.track} из {self.from_adress}"
                f"в {self.to_adress}. Стоимость {self.cost} рублей")
    
