from unittest import TestCase
from  ISSUtils import *


class TestUtils(TestCase):
    def test_Calculator(self):
        test_critersions = {
            "头颈部":{'1':["头部外伤","头痛"],'2':["嗜睡"]},
            "面部": {'1':["擦伤"],'2':["角膜裂伤"]}
        }
        criterion = Criterion()
        criterion.set_critersions(test_critersions)
        cal = Calculator(criterion)
        desp = "头痛安工大撒广东省"
        AIS = cal.cal_AIS(desp)
        ISS = cal.AIS_to_ISS(AIS)
        assert ISS == 1

        desp = "头痛安工大撒广东省,角膜裂伤阿发嘎嘎理工"
        AIS = cal.cal_AIS(desp)
        ISS = cal.AIS_to_ISS(AIS)
        assert ISS == 5
