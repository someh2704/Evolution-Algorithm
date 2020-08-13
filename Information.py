import json
import uuid

class Information:
    def __init__(self, file):
        with open(file, 'r') as f:
            self.unit_info = json.load(f)
    
        self.tribe = self.unit_info["Name"]["tribe"]
        self.name = self.unit_info["Name"]["Name"]
        self.uuid = str(uuid.uuid4())
        self.color = self.unit_info["Appearance"]["Color"]
        self.shape = self.unit_info["Appearance"]["Shape"]
        
        self.attack_counter = 0
        self.search_counter = 0

        self.attack_flag = self.unit_info["Flag"]["AttackFlag"]
        self.search_flag = self.unit_info["Flag"]["SearchFlag"]
        
        del self.unit_info
    
if __name__ == "__main__":
    i = Information("UnitInfo/UnitInfo.json")
    print(i.__dict__)