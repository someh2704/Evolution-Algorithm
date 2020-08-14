import json
import uuid

class Status:
    def __init__(self, file):
        with open(file, 'r') as f:
            self.unit_info = json.load(f)
            
        self.size = self.unit_info["Appearance"]["Size"]
        
        self.health = self.unit_info["Stats"]["Health"]["Health"]
        self.max_health = self.unit_info["Stats"]["Health"]["MaxHealth"]
        self.armor = self.unit_info["Stats"]["Health"]["Armor"]
        self.health_regen = self.unit_info["Stats"]["Health"]["HealthRegen"]
        
        self.damage = self.unit_info["Stats"]["Attack"]["Damage"]
        self.attack_range = self.unit_info["Stats"]["Attack"]["Range"]
        self.sight = self.unit_info["Stats"]["Attack"]["Sight"]
        
        self.walk_speed = self.unit_info["Stats"]["Move"]["WalkSpeed"]
        self.run_speed = self.unit_info["Stats"]["Move"]["RunSpeed"]
        self.jump_range = self.unit_info["Stats"]["Move"]["JumpRange"]
        
        self.max_age = self.unit_info["Stats"]["MaxAge"]
        self.stamina = self.unit_info["Stats"]["Stamina"]
        
        self.attack_delay = self.unit_info["Delay"]["AttackDelay"]
        self.search_delay = self.unit_info["Delay"]["SearchDelay"]
        self.birth_delay = self.unit_info["Delay"]["BirthDelay"]
        
        del self.unit_info
        
if __name__ == "__main__":
    s = Status("UnitInfo/UnitInfo.json")
    print(s.__dict__)
