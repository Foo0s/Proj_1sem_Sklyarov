# -*- coding: utf-8 -*-
import sqlite3 as sqql
import employees

with sqql.connect("zarplata.db") as file:
    base = file.cursor()

    #Создание таблицы - Anketa.
    base.execute("""CREATE TABLE IF NOT EXISTS Anketa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            surname VARCHAR,
            date_birth DATE,
            sex VARCHAR,
            date_naim DATE,
            dolshonst VARCHAR,
            otdel VARCHAR,
            baze_stavka DECIMAL
            )""")

    #Создание таблицы - Больничные листы.
    base.execute("""CREATE TABLE IF NOT EXISTS Bolnichnie_listi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_sotryd INTEGER,
            date_start DATE,
            date_finall DATE,
            cause VARCHAR,
            diagnoz VARCHAR,
            buy BOOLEAN,
            FOREIGN KEY (id_sotryd) REFERENCES Anketa(id) ON DELETE CASCADE ON UPDATE CASCADE
            )""")


    #Заполнение таблицы.
    #base.executemany("INSERT INTO Anketa VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", employees.employes)
    #base.executemany("INSERT INTO Bolnichnie_listi VALUES(?, ?, ?, ?, ?, ?, ?)", employees.list_hospital)