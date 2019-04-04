import db
import games
class User:

    def auth(self, message):
        if (db.check_row(self) == False):
            db.insert_to_db(self)


    def game(self, select):
        if(select == 1):
            db.sub_balance(self, 100)
            res = games.game_one()
            db.add_balance(self, res)
            return res

    def add_balance(self, number):
        db.add_balance(self, number)

    def sub_balance(self, number):
        db.sub_balance(self, number)

    def check_balance(self, message):
        return db.get_balance(self)


    def withdrawal(self):
        pass

    def get_id(self):
        return self.user_id

    def get_user_name(self):
        return self.user_name

    def get_first_name(self):
        return self.first_name