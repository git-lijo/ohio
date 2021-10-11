import sqlite3

connection = sqlite3.connect("data.db", check_same_thread=False)

CREATE_YEARLY_COUNT_TABLE = '''CREATE TABLE IF NOT EXISTS yearly_count(
    api_well_number INTEGER,
    Oil INTEGER,
    gas INTEGER,
    brine INTEGER,
    prod_yr INTEGER,
    county TEXT,
    township TEXT,
    wellname TEXT,
    wellno TEXT,
    days INTEGER
    );'''
INSERT_YEARLY_DATA = "INSERT INTO yearly_count (api_well_number, Oil, gas, brine, county, township, prod_yr, " \
                     "wellname, wellno, days) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?); "

SELECT_YEARLY_COUNT_DATA = "SELECT * FROM yearly_count WHERE api_well_number = ?;"


def create_tables():
    with connection:
        connection.execute(CREATE_YEARLY_COUNT_TABLE)


def insert_yearly_values(api_well_number, oil, gas, brine, county, township, prod_yr, wellname, wellno, days):
    with connection:
        connection.execute(INSERT_YEARLY_DATA, (api_well_number, oil, gas, brine, county, township, prod_yr, wellname, wellno, days))


def select_yearly_count_values(api_well_number):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_YEARLY_COUNT_DATA, (api_well_number,))
        return cursor.fetchall()
