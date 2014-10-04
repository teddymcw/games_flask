from below_root import db 
from below_root.models import Game 

db.drop_all()
db.create_all()


#mock data 
game1 = Game(epic_battle_name="mock 1", 
                 move0=None, move1=None, move2=None,
                 move3=None, move4=None, move5=None,
                 move6=None, move7=None, move8=None,
                 move9=None, move10=None, move11=None,
                 move12=None, move13=None, move14=None, )

db.session.add(game1)
db.session.commit(game1) 

games = Game.query.all()

print(games)