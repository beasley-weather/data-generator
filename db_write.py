import os
import re
import sqlite3 as sql

import user_input


ARCHIVE_SCHEMA = 'archive_schema.sql'


def overwrite_choice(file_name):
    return user_input.yesno('{} exists. Overwrite? (y/n): '.format(file_name))


def check_exists(file_name):
    if os.path.isfile(file_name):
        return True
    else:
        return False


def clear_db(file_name):
    with sql.connect(file_name) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM Archive")
        con.commit()


def create_db(file_name):
    with sql.connect(file_name) as con:
        cur = con.cursor()
        with open(ARCHIVE_SCHEMA, 'r', encoding='utf-8') as schema_file:
            cur.executescript(schema_file.read())


def write_data(time, data, file_name, temp=False, wind=False):
    with sql.connect(file_name) as con:
        cur = con.cursor()

        interval = 0
        for (x, y) in zip(time, data):
            if temp:
                cur.execute('INSERT INTO ARCHIVE (dateTime, usUnits, interval,'
                            ' outTemp) VALUES (?, 0, ?, ?)',
                            (x, interval, y))
            elif wind:
                cur.execute('INSERT INTO ARCHIVE (dateTime, usUnits, interval,'
                            ' windSpeed) VALUES (?, 0, ?, ?)',
                            (x, interval, y))
            interval += 1

        con.commit()


def write(time, data, file_name, temp=False, wind=False):
    does_exist = check_exists(file_name)
    if does_exist:
        overwrite = overwrite_choice(file_name)

    try:
        if not(does_exist):
            create_db(file_name)
            write_data(time, data, file_name, temp, wind)
        elif overwrite:
            clear_db(file_name)
            write_data(time, data, file_name, temp, wind)

    except sql.Error as sqle:
        raise Exception('Database IO failure.')
