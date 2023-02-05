players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]
    
    @classmethod
    def get_team(cls, dict):
        new_players=[]
        for item in dict:
            new_players.append(cls(item))
        return new_players



    def __repr__(self):
        display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"
        return display


# kevin = {
#     	"name": "Kevin Durant", 
#     	"age":34, 
#     	"position": "small forward", 
#     	"team": "Brooklyn Nets"
# }
# jason = {
#     	"name": "Jason Tatum", 
#     	"age":24, 
#     	"position": "small forward", 
#     	"team": "Boston Celtics"
# }
# kyrie = {
#     	"name": "Kyrie Irving", 
#     	"age":32,
#         "position": "Point Guard", 
#     	"team": "Brooklyn Nets"
# }
    
# player_kevin=Player(kevin)
# print(player_kevin.age)
# player_jason=Player(jason)
# print(player_jason.name)

# new_team = []
# for i in players:
#     new_team.append(Player(i))
# print(new_team)







