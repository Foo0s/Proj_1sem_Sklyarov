import sqlite3 as sql

with sql.connect("zarplata.db") as db:
    bd = db.cursor()


    #UPDATE -1. Обновить базову ставку сотрудника на определенной должности.
    db.execute("UPDATE Anketa SET baze_stavka = 33233 WHERE dolshonst='Веб-программист'AND id_spec=1")

    #UPDATE -2. Обновить отдел всех сотрудников в определенном диапазоне возраста.
    db.execute("UPDATE Anketa SET otdel='IT' WHERE ROUND((julianday('now') - julianday(date_birth)) / 365) BETWEEN 19 AND 21")

    #UPDATE -3. Обновить дату найма для сотрудника, получившего повышение.
    db.execute("UPDATE Anketa SET date_naim='2023.10.01' WHERE id_spec=1")

    #UPDATE -4. Обновить причину больничного листа для сотрудника.
    db.execute("UPDATE Bolnichnie_listi SET cause='Алкогольное отравление' WHERE id_spec=2")

    #UPDATE -5. Обновить базовую ставку сотрудника в таблице Анкета на определеный процент, использую INNER JOIN
    #с таблицей Bolnichnie_listi. При этом необходимо исключить из обновления сотрудников, у которых неоплаченные больничные листы.
    db.execute("UPDATE Anketa as ank SET baze_stavka=baze_stavka+(baze_stavka*0.15) FROM Bolnichnie_listi bl WHERE buy=False AND ank.[id_spec]=bl.[id_spec]")

    #UPDATE -6. Обновить дату начала больничного листа в таблице Больничные листы на опрд. дату, использую INNER JOIN.
    #c таблицей Anketa. При этом необходимо исключить из обновления больничные листы с уже пройденной датой начала
    # Месяц - Март, число - 14.
    db.execute("UPDATE Bolnichnie_listi as bl SET date_start='2023-03-14' FROM Anketa ank WHERE bl.[id_spec]=ank.[id_spec] AND bl.[date_start] >= '2023-03-14'")

    #UPDATE -7. Обновить причину больничного листа в таблице Больничные листы на определенное значение для всех сотрудников
    #работающих в отделе Бухгалтерия
    db.execute("UPDATE Bolnichnie_listi as bbl SET cause='Гангрена' FROM Anketa an WHERE an.[id_spec]=bbl.[id_spec] AND an.[otdel]='Бухгалтерия'")