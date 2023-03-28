
import json
player_id = 80011
def append_data(data,player_id,player_level,money,inventory):
        filename="player/saved/id_%i_data.json" % (player_id) 
        with open (filename,'w') as f:
             json.dump(data, f,indent=2)
             del data
        with open ("player/saved/id_80011_data.json") as json_file:
            data = json.load(json_file)
            temp = data
            input = {"id": player_id }, {"level": player_level }, {"money": 1111111 }, {"inventory": {"slot0": 11, "slot1": 800, "slot2": 801, "slot3": 801, "slot10": 800, "slot21": 80011, "slot22": 80011}},{"storage": [80011]}
            temp.append(input)
data = 1
append_data(data)