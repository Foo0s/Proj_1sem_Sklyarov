# -*- coding: utf-8 -*-
import sqlite3 as sql

def search_selects():
    #Текущий месяц март.
    with sql.connect("zarplata.db") as database:
        base = database.cursor()

        #Запрос -1. Список всех сотрудников и их должностей.
        print(base.execute("SELECT name, surname, dolshonst FROM Anketa").fetchall())

        #Запрос -2. Вывести всех сорудников и их базовые ставки.
        print()
        print(base.execute("SELECT name, surname, baze_stavka FROM Anketa").fetchall())

        #Запрос -3. Вывести список всех сотрудников, работающих в отеделе IT.
        print()
        print(base.execute("SELECT name, surname, otdel FROM Anketa WHERE otdel = 'IT'").fetchall())

        #Запрос -4. Вывести список всех сотрудников, принятых на работу после 1 января 2022 года.
        print()
        print(base.execute("SELECT name, surname, date_naim FROM Anketa WHERE date_naim > '2022.01.01'").fetchall())

        #Запрос -5. Вывести список всех больничных листов, выписанных сотрудники с id = 42.
        print()
        print(base.execute("SELECT * FROM Bolnichnie_listi WHERE id_spec = 42").fetchall())

        #Запрос -6. Список всех больничных листов, оплаченных компаний.
        print()
        print(base.execute("SELECT * FROM Bolnichnie_listi WHERE buy = True").fetchall())

        #Запрос -7. Вывести список всех сотрудников, имеющих больничные листы на текущий месяц.
        print()
        print(base.execute("SELECT * FROM Bolnichnie_listi WHERE date_start AND date_finall BETWEEN '2023.03.01' AND '2023.03.30'").fetchall())

        #Запрос -8. Вывести среднюю базовую ставку всех сотрудников.
        print()
        baze_stavka = base.execute("SELECT baze_stavka FROM Anketa").fetchall()
        numbers = list(map(lambda x: x[0], baze_stavka))
        print(f"Средняя базовая ставка всех сотрудников: {sum(numbers) // len(numbers)}")

        #Запрос -9. Вывести список всех сотрудников, имеющих базовую ставку выше 100-000.
        print()
        print(base.execute("SELECT name, surname, baze_stavka FROM Anketa WHERE baze_stavka > 100000").fetchall())

        #Запрос -10. Вывести всех сотрудников, и общее кол-во дней, проведенных ими на больничном.
        print("Все сотрудники: ")
        all_day = base.execute("SELECT an.* FROM Bolnichnie_listi bl INNER JOIN Anketa an ON bl.[id_spec]=an.[id_spec]").fetchall()
        print(all_day)
        dates_from_bl = base.execute("SELECT (strftime('%s', date_finall) - (strftime('%s', date_start))) / 86400.0 FROM Bolnichnie_listi").fetchall()
        print("Общее количество дней проведенных на больничном: {}".format(sum([k for i in dates_from_bl for k in i])))

        #Запрос -11. Вывести информацию о сотрудниках и их больничных листах за последний месяц.
        #Последний месяц - Март.
        print()
        print(base.execute("SELECT ank.*, bl.* FROM Anketa ank INNER JOIN Bolnichnie_listi bl ON bl.[id_spec]=ank.[id_spec] WHERE bl.[date_start] AND bl.[date_finall] BETWEEN '2023-03-01' AND '2023-03-31'").fetchall())

        #Запрос -12. Вывести среднюю продолжительность больничных листов сотрудниковв каждом отделе.
        print()
        all_otdel = list(set(i for i in base.execute("SELECT otdel FROM Anketa").fetchall()))
        it_bl = [base.execute(f"SELECT (strftime('%s', date_finall) - (strftime('%s', date_start))) / 86400.0 FROM Bolnichnie_listi bl INNER JOIN Anketa ank ON bl.[id_spec]=ank.[id_spec] WHERE ank.[otdel]='{i[0]}'").fetchall() for i in all_otdel]
        answer_dict = dict()
        k = 0
        for i in it_bl:
            answer_dict[all_otdel[k][0]] = sum([j for k in i for j in k]) / len([j for k in i for j in k]) if len([j for k in i for j in k]) > 0 else sum([j for k in i for j in k]) // 1
            k += 1
        print("Средняя продолжительность больничных листов сотрудников в кадом отделе: \n", answer_dict)
        
        #Запрос -13. Вывести список сотрудников и информацию о последнем больничном листе, который они оформляли.
        print()
        rest = base.execute("SELECT DISTINCT bl.[id_spec] FROM Anketa ank INNER JOIN Bolnichnie_listi bl ON bl.[id_spec]=ank.[id_spec]").fetchall()
        for i in rest:
            print(base.execute(f"SELECT ank.*, MAX(bl.[date_start]) FROM Bolnichnie_listi bl INNER JOIN Anketa ank ON bl.[id_spec]=ank.[id_spec] WHERE bl.[id_spec]={i[0]}").fetchall())

        #Запрос -14. Вывести список сотрудников информацию о первом больничном листе, который они оформляли.
        print()
        res = base.execute("SELECT DISTINCT bl.[id_spec] FROM Anketa ank INNER JOIN Bolnichnie_listi bl ON bl.[id_spec]=ank.[id_spec]").fetchall()
        for i in res:
            print(base.execute(f"SELECT ank.*, MIN(bl.[date_start]) FROM Bolnichnie_listi bl INNER JOIN Anketa ank ON bl.[id_spec]=ank.[id_spec] WHERE bl.[id_spec]={i[0]}").fetchall())
        
        #Запрос -15. Вывести список сотрудников и суммарную продолжительность их больничных листов в текущем году.
        print()
        all_info = base.execute("SELECT DISTINCT bl.[id_spec] FROM Anketa an INNER JOIN Bolnichnie_listi bl ON bl.[id_spec]=an.[id_spec]").fetchall()
        for k in all_info:
            print(base.execute(f"SELECT ank.*, SUM((strftime('%s', date_finall) - (strftime('%s', date_start))) / 86400.0) FROM Anketa ank INNER JOIN Bolnichnie_listi bl ON bl.[id_spec]=ank.[id_spec] WHERE date_start >= '2023-01-01' AND date_finall <= '2023-12-31' AND bl.[id_spec]={k[0]}").fetchall())


if __name__ == "__main__":
    search_selects()