from unittest import TestCase
from  ISSUtils import *
from Criterion import Criterion

class TestUtils(TestCase):
    def test_critersion(self):
        import re 
        criterion_obj = Criterion()
        for body_part, regions in criterion_obj.get_critersions().items():
            for _, region in regions.items():
                for score, keywords in region.items():
                    for keyword in keywords:
                        re.search(keyword, "test")
    
    def test_calculator(self):
        criterion = Criterion()
        cal = Calculator(criterion)
        desp = "头痛安工大撒广东省12根肋骨骨折"
        AIS = cal.cal_AIS(desp)
        ISS = cal.AIS_to_ISS(AIS)
        assert ISS == 9

        desp = "头痛安工大撒广东省,角膜裂伤阿发嘎嘎理工,肾上腺挫伤重度"
        AIS = cal.cal_AIS(desp)
        ISS = cal.AIS_to_ISS(AIS)
        assert ISS == 4