import sqlite3
import datetime
now = datetime.datetime.utcnow()

CREATE_GROCERIES = "CREATE TABLE IF NOT EXISTS groceries (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"
CREATE_RENT = "CREATE TABLE IF NOT EXISTS rent (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"
CREATE_SUBSCRIPTIONS = "CREATE TABLE IF NOT EXISTS subscriptions (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"
CREATE_TRAVEL = "CREATE TABLE IF NOT EXISTS travel (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"
CREATE_GUILTY_PLEASURE = "CREATE TABLE IF NOT EXISTS guilty pleasure (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"


INSERT_GROCERIES = "INSERT INTO groceries (good, price, date) VALUES(?,?,?);"
INSERT_RENT = "INSERT INTO rent (good, price, date) VALUES(?,?,?);"
INSERT_SUBSCRIPTIONS = "INSERT INTO subscriptions (good, price, date) VALUES(?,?,?);"
INSERT_TRAVEL = "INSERT INTO travel (good, price, date) VALUES(?,?,?);"
INSERT_GUILTY_PLEASURE = "INSERT INTO guilty pleasure (good, price, date) VALUES(?,?,?);"

SELECT_ALL1 = "SELECT * FROM groceries;"
SELECT_ALL2 = "SELECT * FROM rent;"
SELECT_ALL3 = "SELECT * FROM subscriptions;"
SELECT_ALL4 = "SELECT * FROM travel;"
SELECT_ALL5 = "SELECT * FROM guilty pleasure;"


SELECT_GROCERIES = "SELECT * FROM groceries WHERE good = ? AND price = ?;"
SELECT_RENT = "SELECT * FROM rent WHERE good = ? AND price = ?;"
SELECT_SUBSCRIPTIONS = "SELECT * FROM subscriptions WHERE good = ? AND price = ?;"
SELECT_TRAVEL = "SELECT * FROM travel WHERE good = ? AND price = ?;"
SELECT_GUILTY_PLEASURE ="SELECT * FROM guilty pleasure WHERE good = ? AND price = ?;"


DELETE_GROCERIES = "DELETE FROM groceries WHERE good = ? AND price = ?;"
DELETE_RENT = "DELETE FROM rent WHERE good = ? AND price = ?;"
DELETE_SUBSCRIPTIONS = "DELETE FROM subscriptions WHERE good = ? AND price = ?;"
DELETE_TRAVEL = "DELETE FROM travel WHERE good = ? AND price = ?;"
DELETE_GUILTY_PLEASURE = "DELETE FROM guilty pleasure WHERE good = ? AND price = ?;"




###create for every table###
def create_tables():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(CREATE_OTHER)

###INSERT VALUES###

def insert_groceries(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_GROCERIES, (good, price, date))
        conn.commit()



def insert_rent(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_RENT, (good, price, date))
        conn.commit()
        c.close()

def insert_subscriptions(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_SUBSCRIPTIONS, (good, price, date))
        conn.commit()
        c.close()

def insert_travel(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_TRAVEL, (good, price, date))
        conn.commit()
        c.close()
        
def insert_guilty_pleasure(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_GUILTY_PLEASURE, (good, price, date))
        conn.commit()
        c.close()

###SELECT_ALL###



def select_all_groceries():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL1)
        #have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output





def select_all_rent():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL2)
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_all_subscriptions():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL3)
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_all_travel():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL4)
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output
    

def select_all_guilty_pleasure():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL4)
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

###SELECT SPECIFIC###

def select_grocery(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_GROCERIES, (good, price))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_rent(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_RENT, (good, price))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_subscriptions(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_SUBSCRIPTIONS, (good, price))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_travel(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_TRAVEL, (good, price))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output
    
def select_guilty_pleasure(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_GUILTY_PLEASURE, (good, price))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output


###DELETE VALUE###
def delete_grocery(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_GROCERIES, (good, price))
        conn.commit()
        c.close()

def delete_rent(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_RENT, (good, price))
        conn.commit()
        c.close()

def delete_subscriptions(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_SUBSCRIPTIONS, (good, price))
        conn.commit()
        c.close()

def delete_travel(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_TRAVEL, (good, price))
        conn.commit()
        c.close()
        
        
def delete_guilty_pleasure(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_GUILTY_PLEASURE, (good, price))
        conn.commit()
        c.close()        
