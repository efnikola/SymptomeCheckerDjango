import unittest
from .SmartChecker import Checker
from .SmartChecker import Desease

class Checkertester(unittest.TestCase):
    model=Checker()
    model.hardcode()

    def testPainNeck_Tonzylit(self):
        comId = 2
        gotSymptoms = ("Температура тела выше 37,5",
                       "Боль усиливается при глотании",
                       "Миндалины покрыты белым налетом")
        result = self.model.compute(gotSymptoms, comId)
        res=result.pop()
        print("\n",res.diagnosis)
        self.assertEqual(res.diagnosis,"Вероятен острый тонзиллит","болезнь определена неверно")


    def testPainNeck_Faringit(self):
        comId = 2
        gotSymptoms = ["Ничего из перечисленного"]
        result = self.model.compute(gotSymptoms, comId)
        res=result.pop()
        print("\n",res.diagnosis)
        self.assertEqual(res.diagnosis,"Вероятен острый фарингит","болезнь определена неверно")

    def testParAbscess(self):
        comId = 2
        gotSymptoms = ["Рот открывается с трудом и болью"]
        result = self.model.compute(gotSymptoms, comId)
        res=result.pop()
        print("\n",res.diagnosis)
        self.assertEqual(res.diagnosis,"Не исключен паратонзиллярный абсцесс","болезнь определена неверно")


    def testDiftery(self):
        comId = 2
        gotSymptoms = ["Миндалины покрыты желтым налетом"]
        result = self.model.compute(gotSymptoms, comId)
        res = result.pop()
        print("\n", res.diagnosis)
        self.assertEqual(res.diagnosis, "Не исключена дифтерия", "болезнь определена неверно")

    def testTrauma(self):
        comId = 2
        gotSymptoms = ["Боль появилась после приема пищи"]
        result = self.model.compute(gotSymptoms, comId)
        res = result.pop()
        print("\n", res.diagnosis)
        self.assertEqual(res.diagnosis, "Не исключена травма пищевода", "болезнь определена неверно")

    def testObostrTonzyll(self):
        comId = 2
        gotSymptoms = ["Врач ставил диагноз хронический тонзиллит"]
        result = self.model.compute(gotSymptoms, comId)
        res = result.pop()
        print("\n", res.diagnosis)
        self.assertEqual(res.diagnosis, "Обострение хронического тонзиллита", "болезнь определена неверно")


if __name__=='__main__':
    unittest.main()

