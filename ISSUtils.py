import os
from Criterion import Criterion
import re

class Calculator:
    
    def __init__(self, criterion_obj):
        assert criterion_obj.get_critersions() is not None
        self.criterion_obj = criterion_obj

    def cal_AIS(self, diagnose_description):
        AIS = {}
        re = []
        diagnose_description = diagnose_description.upper()
        for body_part, content in self.criterion_obj.get_critersions().items():
            if any([True if i in diagnose_description else False for i in content["exclude"]]):
                continue
            if not any([True if i in diagnose_description else False for i in content["include"]]):
                continue
            max_score = 0
            max_part = body_part
            for _score_, _keywords_ in content["score"].items():
                for _keyword_ in _keywords_:
                    if isinstance(_keyword_[0][0], list):
                        for i in _keyword_[0]:
                            for j in _keyword_[1]:
                                if i[0] in  diagnose_description and j in diagnose_description and _score_ > max_score:
                                    max_score = _score_
                    else:
                        if all([True if m in diagnose_description else False for m in _keyword_[0]]):
                            for j in _keyword_[1]:
                                if j in diagnose_description and _score_ > max_score:
                                    max_score = _score_
            
            re.append([body_part, max_score])
        return re if re else ["NULL", 0]
    
    def AIS_to_ISS(self, AIS):
        assert isinstance(AIS, dict) and len(AIS) != 0
        sorted_values  = sorted(AIS.values(), key=lambda x : x[0])
        top_3_values = [i[0] for i in sorted_values[-3:]]
        
        ISS =  75 if max(top_3_values) == 6 else sum([i**2 for i in top_3_values])
        return ISS