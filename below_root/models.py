from below_root import db 

class Game(db.Model):

    __tablename__ = "games"

    game_id = db.Column(db.Integer, primary_key=True)
    epic_battle_name = db.Column(db.String, unique=True, nullable=False)
    move0 = db.Column(db.Integer)
    move1 = db.Column(db.Integer)
    move2 = db.Column(db.Integer)
    move3 = db.Column(db.Integer)
    move4 = db.Column(db.Integer)
    move5 = db.Column(db.Integer)
    move6 = db.Column(db.Integer)
    move7 = db.Column(db.Integer)
    move8 = db.Column(db.Integer)
    move9 = db.Column(db.Integer)
    move10 = db.Column(db.Integer)
    move11 = db.Column(db.Integer)
    move12 = db.Column(db.Integer)
    move13 = db.Column(db.Integer)
    move14 = db.Column(db.Integer)

    def __init__(self, epic_battle_name=None, 
                 move0=None, move1=None, move2=None,
                 move3=None, move4=None, move5=None,
                 move6=None, move7=None, move8=None,
                 move9=None, move10=None, move11=None,
                 move12=None, move13=None, move14=None, ):
        self.epic_battle_name = epic_battle_name
        self.move0=move0
        self.move1=move1
        self.move2=move2
        self.move3=move3
        self.move4=move4
        self.move5=move5
        self.move6=move6
        self.move7=move7
        self.move8=move8
        self.move9=move9
        self.move10=move10
        self.move11=move11
        self.move12=move12
        self.move13=move13
        self.move14=move14
    
    def __repr__(self):
        return "<Game {}>".format(self.epic_battle_name)
