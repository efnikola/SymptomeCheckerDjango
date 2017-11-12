import operator
class Desease:
    excludeSymptoms=[]
    strictSymptoms=[]
    services={}
    diagnosis=""
    anyElse=False
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
                    if(desease.anyElse==False):
                        total[desease]=0
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
        desease1.anyElse=True


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
        desease2.anyElse=False

        desease3 = Desease()
        desease3.excludeSymptoms = []
        desease3.strictSymptoms = ["Рот открывается с трудом и болью"]

        desease3.services = {0: "Консультация ЛОР врача",
                             1: "Общий анализ крови",
                             2: "СОЭ",
                             3: "Лейкоформула",
                             4: "Мазок из зева на флору"}
        desease3.diagnosis = "Не исключен паратонзиллярный абсцесс"
        desease1.anyElse=True

        desease4 = Desease()
        desease4.excludeSymptoms = []
        desease4.strictSymptoms = ["Миндалины покрыты желтым налетом"]

        desease4.services = {0: "Консультация терапевта",
                             1: "Общий анализ крови",
                             2: "СОЭ",
                             3: "Лейкоформула",
                             4: "Мазок из зева на BL+флора"}
        desease4.diagnosis = "Не исключена дифтерия"
        desease1.anyElse=True

        desease5 = Desease()
        desease5.excludeSymptoms = []
        desease5.strictSymptoms = ["Боль появилась после приема пищи"]

        desease5.services = {0: "Консультация ЛОР врача",
                             1: "Консультация хирурга",
                             2: "Фиброэзофагоскопия по назначению врача"}
        desease5.diagnosis = "Не исключена травма пищевода"
        desease1.anyElse=True


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
        desease1.anyElse=True


        desease7 = Desease()
        desease7.excludeSymptoms = ["Отходит много мокроты",
                                    "Температура выше 39,5",
                                    "Беспокоит неделю и больше",
                                    "Голос осиплый" ]
        desease7.strictSymptoms = []
        desease7.services = {0: "Консультация терапевта"}
        desease7.diagnosis = "ОРЗ"
        desease1.anyElse=True


        desease8 = Desease()
        desease8.excludeSymptoms = ["Мокрота откашливается",
                                    "Отходит много мокроты",
                                    "Температура до 37,5",
                                    "Беспокоит неделю и больше"]
        desease8.strictSymptoms = ["Температура 38-39,5",
                                   "Температура выше 39,5"]
        desease8.services = {0: "Консультация терапевта"}
        desease8.diagnosis = "Вероятен грипп"
        desease1.anyElse=False


        desease9 = Desease()
        desease9.excludeSymptoms = []
        desease9.strictSymptoms = ["Отходит много мокроты"]
        desease9.services = {0:"цФЛГ или Rg лёгких",
                             1:"Кл.ан.крови",
                             2:"Консультация терапевта"}
        desease9.diagnosis = "Вероятна пневмония"
        desease1.anyElse=False




        self.deseases=[desease1,desease2,desease3,desease4,desease5,desease6,
                       desease7,desease8,desease9
                       ]


# "Мокрота не откашливается",
# "Мокрота откашливается",
# "Отходит много мокроты",3
# "Беспокоит первый день",
# "Беспокоит меньше недели",5
# "Температура до 37,5",
# "Температура 38-39,5",7
# "Температура выше 39,5",
# "Беспокоит неделю и больше",9
# "Голос осиплый",
# "Чувство нехватки воздуха (одышка)"

checker=Checker()
checker.hardcode()
comId=2
gotSymptoms=("Температура тела выше 37,5",
             "Миндалины увеличены",
             "Голос осиплый")
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