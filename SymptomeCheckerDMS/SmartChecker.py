import operator
class Desease:
    excludeSymptoms=[]
    strictSymptoms=[]
    services={}
    diagnosis=""
class Checker:
    somevar=0
    symptoms=[]
    deseases=[]
    curID=0
    def __init__(self):
        self.somevar=1

    def compute(self,got_symptoms,curID):
        total=dict()
        for desease in self.deseases:
            total[desease]=0
            print("Проверка...",desease.diagnosis)
            for symptom in got_symptoms:
                if symptom in desease.excludeSymptoms:
                    total[desease]=0
                    print("    Найден лишний симптом:",symptom)
                    break
                elif symptom in desease.strictSymptoms:
                    total[desease]+=2
                else:
                    total[desease]+=1
            print("    общая оценка:",total[desease])
        v = list(total.values())
        k = list(total.keys())
        res=[]
        for x,y in zip(v,k):
            if x==max(v): res.append(y)
        return res

    def hardcode(self):


        desease1=Desease()
        desease1.excludeSymptoms=["Боль появилась после приема пищи",
                                     "Миндалины покрыты желтым налетом",
                                     "Рот открывается с трудом и болью",
                                     "Врач ставил диагноз «хронический тонзиллит"]
        desease1.strictSymptoms=["Миндалины покрыты белым налетом"]

        desease1.services={0:"Консультация терапевта",
                           1:"Общий анализ крови",
                           2:"СОЭ",
                           3: "Лейкоформула",
                           4:"Мазок из зева на флору"}
        desease1.diagnosis="Вероятен острый тонзиллит"


        desease2 = Desease()
        desease2.excludeSymptoms = ["Боль усиливается при глотании",
                                       "Боль появилась после приема пищи",
                                       "Температура тела выше 37,5",
                                       "Миндалины увеличены",
                                       "Миндалины покрыты белым налетом",
                                       "Миндалины покрыты желтым налетом",
                                       "Рот открывается с трудом и болью",
                                       "Симптомы беспокоят первый день",
                                       "Симптомы беспокоят неделю и больше",
                                       "Врач ставил диагноз «хронический тонзиллит"]
        desease2.strictSymptoms = ["Ничего из перечисленного"]

        desease2.services = {0: "Консультация терапевта",
                             1: "Общий анализ крови",
                             2: "СОЭ"}
        desease2.diagnosis = "Вероятен острый фарингит"

        desease3 = Desease()
        desease3.excludeSymptoms = []
        desease3.strictSymptoms = ["Рот открывается с трудом и болью"]

        desease3.services = {0: "Консультация ЛОР врача",
                             1: "Общий анализ крови",
                             2: "СОЭ",
                             3: "Лейкоформула",
                             4: "Мазок из зева на флору"}
        desease3.diagnosis = "Не исключен паратонзиллярный абсцесс"

        desease4 = Desease()
        desease4.excludeSymptoms = []
        desease4.strictSymptoms = ["Миндалины покрыты желтым налетом"]

        desease4.services = {0: "Консультация терапевта",
                             1: "Общий анализ крови",
                             2: "СОЭ",
                             3: "Лейкоформула",
                             4: "Мазок из зева на BL+флора"}
        desease4.diagnosis = "Не исключена дифтерия"

        desease5 = Desease()
        desease5.excludeSymptoms = []
        desease5.strictSymptoms = ["Боль появилась после приема пищи"]

        desease5.services = {0: "Консультация ЛОР врача",
                             1: "Консультация хирурга",
                             2: "Фиброэзофагоскопия по назначению врача"}
        desease5.diagnosis = "Не исключена травма пищевода"


        desease6 = Desease()
        desease6.excludeSymptoms = ["Боль появилась после приема пищи",
                                    "Миндалины покрыты желтым налетом",
                                    "Рот открывается с трудом и болью"]
        desease6.strictSymptoms = ["Врач ставил диагноз «хронический тонзиллит»"]

        desease6.services = {0: "Мазок из зева на флору и чувствительность к антибиотикам",
                             1: "Общий анализ крови",
                             2: "СОЭ",
                             3: "Лейкоформула",
                             4: "Консультация ЛОР врача"}
        desease6.diagnosis = "Обострение хронического тонзиллита"


        self.deseases=[desease1,desease2,desease3,desease4,desease5,desease6]


# set("Боль усиливается при глотании",
#     "Боль появилась после приема пищи",
#     "Температура тела выше 37,5"
#     "Миндалины увеличены",
#     "Миндалины покрыты белым налетом",
#     "Миндалины покрыты желтым налетом",
#     "Рот открывается с трудом и болью",
#     "Симптомы беспокоят первый день",
#     "Симптомы беспокоят неделю и больше",
#     "Врач ставил диагноз «хронический тонзиллит")
checker=Checker()
checker.hardcode()
comId=2
gotSymptoms=("Температура тела выше 37,5",
             "Миндалины увеличены")
result=checker.compute(gotSymptoms,comId)
print("\nРезультат:")
[print("    ",x.diagnosis) for x in result]
ServicesList=[]
for x in result:
    for t in x.services.values():
        if t not in ServicesList:
            ServicesList.append(t)
print("\nРекомендованы")
[print("    ",x) for x in ServicesList]