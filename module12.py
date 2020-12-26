money = input("Введите сумму:")
per_cent = {"ТКБ": 5.6, "СКБ": 5.9, "ВТБ": 4.28, "СБЕР": 4.0}
deposit = [int(money) * per_cent["ТКБ"], int(money) * per_cent["СКБ"], int(money) * per_cent["ВТБ"],
           int(money) * per_cent["СБЕР"]]
print(deposit)
print("Максимальная сумма которую вы можете заработать - ", max(deposit))
