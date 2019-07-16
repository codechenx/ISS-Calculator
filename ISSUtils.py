import os


class Criterion:
    """
    The DataClass to store ISS criterion
    Returns:
        criterion {dict} -- ISS criterion
        {"头颈部":{'1':["头部外伤","头痛"],'2':["嗜睡"]}}
    """
    def __init__(self):
        self.criterion = None
    
    def get_critersions(self):
        return self.criterion
    
    def set_critersions(self, criterion):
        self.criterion = criterion

class Calculator:
    
    def __init__(self, criterion_obj):
        assert criterion_obj.get_critersions() is not None
        self.criterion_obj = criterion_obj

    def cal_AIS(self, diagnose_description):
        AIS = {}
        for body_part, scores in self.criterion_obj.get_critersions().items():
            max_score = 0
            for score, keywords in scores.items():
                for keyword in keywords:
                    if keyword in diagnose_description and int(score) > max_score:
                        max_score = int(score)
            AIS[body_part]  = max_score
        return AIS
    
    def AIS_to_ISS(self, AIS):
        assert isinstance(AIS, dict) and len(AIS) != 0
        sorted_values  = sorted(AIS.values())
        top_3_values = sorted_values[-3:]
        ISS = sum([i**2 for i in top_3_values])
        return ISS
    





