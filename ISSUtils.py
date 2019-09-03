import os
from Criterion import Criterion
import re

class Calculator:
    
    def __init__(self, criterion_obj):
        assert criterion_obj.get_critersions() is not None
        self.criterion_obj = criterion_obj

    def cal_AIS(self, diagnose_description):
        AIS = {}
        
        for body_part, regions in self.criterion_obj.get_critersions().items():
            max_score = 0
            match_str = set()
            for _, region in regions.items():
                for score, keywords in region.items():
                    match = [re.search(keyword, diagnose_description) for keyword in keywords]
                    match_str = match_str.union(set([i[0] for i in match if i]))
                    if any(match) and int(score) > max_score:
                        max_score = int(score)
            AIS[body_part]  = [max_score, ";".join(match_str)]
        return AIS
    
    def AIS_to_ISS(self, AIS):
        assert isinstance(AIS, dict) and len(AIS) != 0
        sorted_values  = sorted(AIS.values(), key=lambda x : x[0])
        top_3_values = [i[0] for i in sorted_values[-3:]]
        
        ISS =  75 if max(top_3_values) == 6 else sum([i**2 for i in top_3_values])
        return ISS