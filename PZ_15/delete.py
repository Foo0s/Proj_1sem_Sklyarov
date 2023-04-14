import sqlite3 as sql

with sql.connect("zarplata.db") as db:
    bd = db.cursor()

    #Удаление -1. Удалить все записи о больничных листах для сотрудника с именем Иван.
    db.execute("DELETE FROM Bolnichnie_listi as bl WHERE bl.[id_spec] IN (SELECT id_spec FROM Anketa WHERE name='Иван')").fetchall()

    #Удаление -2. Удалить записи о больничных листах для сотрудника с Фамилией Петров.
    db.execute("DELETE FROM Bolnichnie_listi as bl WHERE bl.[id_spec] IN (SELECT id_spec FROM Anketa WHERE surname='Петров')")

    #Удаление -3. Удалить все записи о больничных листах для сотрудника с должностью Менеджер.
    db.execute("DELETE FROM Bolnichnie_listi WHERE id_spec IN (SELECT id_spec FROM Anketa WHERE dolshonst='Менеджер')")

    #Удаление -4. Удалить все записи о больничных листах для сотрудника с отделом "Отдел продаж"
    db.execute("DELETE FROM Bolnichnie_listi WHERE id_spec IN (SELECT id_spec FROM Anketa WHERE otdel='Отдел продаж')").fetchall()

    #Удаление -5. Удалить все записи о больничных листах для сотрудника женского пола.
    db.execute("DELETE FROM Bolnichnie_listi WHERE id_spec IN (SELECt id_spec FROM Anketa WHERE sex='female')").fetchall()

    #Удаление -6. Удалить все записи о больничных листах для сотрудников старше 50 лет.
    db.execute("DELETE FROM Bolnichnie_listi WHERE id_spec IN (SELECT id_spec FROM Anketa as ank WHERE (julianday('now') - julianday(ank.[date_birth])) / 365 > 50.0)")

    #Удаление -7. Удалить все записи о неоплаченных больничных листах.
    db.execute("DELETE FROM Bolnichnie_listi WHERE buy=False").fetchall()

    #Удаление -8. Удалить все записи о больничных листах, дата окончания которых прошла.
    #Текущая дата 2023-03-01
    db.execute("DELETE FROM Bolnichnie_listi WHERE date_finall < '2023-03-01'").fetchall()

    #Удаление -9. Удалить все записи о больничных листах, начиная с определенной даты.
    #Определенная дата 2023-03-22
    db.execute("DELETE FROM Bolnichnie_listi WHERE date_start >= '2023-03-22'").fetchall()

    #Удаление -10. Удалить все записи о больничных листах, закончившихся до определенной даты.
    # Определенная дата 2023-03-04
    db.execute("DELETE FROM Bolnichnie_listi WHERE date_finall < '2023-03-04'").fetchall()

    #Удаление -11. Удалить все больничные листы сотрудника с именем Иван из таблицы Больничные листы. Повтор с заданием 1
    db.execute("DELETE FROM Bolnichnie_listi WHERE id_spec IN (SELECT id_spec FROM Anketa WHERE name='Иван')")

    #Удаление -12. Удалить все больничные листы сотрудников, чьи фамилии начинаются на букву С из таблицы Больничные листы.
    db.execute("DELETE FROM Bolnichnie_listi WHERE id_spec in (SELECT  id_spec FROM Anketa WHERE name LIKE 'С%')").fetchall()

    #Удаление -13. Удалить все больничные листы, которые еще не были оплачены, у сотрудников с должностью Менеджер из таблицы Больничные листы.
    db.execute("DELETE FROM Bolnichnie_listi WHERE id_spec IN (SELECT id_spec FROM Anketa WHERE dolshonst='Менеджер') AND buy=False").fetchall()

    #Удаление -14. Удалить все больничные листы, выписанные сотрудникам отдела IT в период с 1 января.
    db.execute("DELETE FROM Bolnichnie_listi WHERE id_spec IN (SELECT id_spec FROM Anketa WHERE otdel='IT') AND date_start > '2023-01-01'").fetchall()

    #Удаление -15. Удалить все больничные листы, связанные со сотрудниками старше 50 лет из таблицы Больничные листы. Повтор -6.
    db.execute("DELETE FROM Bolnichnie_listi WHERE id_spec IN (SELECT id_spec FROM Anketa as ank WHERE (julianday('now') - julianday(ank.[date_birth])) / 365 > 50.0)").fetchall()
