class Genetic:
    def __init__(self):
        pass
    
    def assess(self, myself, appear_unit):
        table = []
        for unit in appear_unit:
            if(unit.info.name == myself.info.name):
                continue
            
            info = unit.status.__dict__
            info["unit"] = unit
            
            table.append(info)
        return table
    