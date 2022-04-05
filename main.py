money = int(input("Введите сумму"))
per_cent = {"ТКБ":5.6,"СКБ":5.9,"ВТБ":4.28,"СБЕР":4.0}
TKB = int(per_cent["ТКБ"]*money/100)
CKB = int(per_cent["СКБ"]*money/100)
VTB = int(per_cent["ВТБ"]*money/100)
SBER = int(per_cent["СБЕР"]*money/100)
deposit = (TKB,CKB,VTB,SBER)
print("Депозиты:",deposit)
i = [TKB,CKB,VTB,SBER]
deposit = max(i)
print("Наибольший депозит:",deposit)