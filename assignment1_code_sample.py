import os
import pymysql
from urllib.request import urlopen

# Broken Access Control
"""
Permitting viewing or editing someone else's account 
by providing its unique identifier (insecure direct object references)
"""
#Identification and Authentication Failures
"""
Uses plain text, encrypted, or weakly hashed passwords data stores
"""
db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

#Injection
"""
User-supplied data is not validated, filtered, or sanitized by the application.
"""
def get_user_input():
    user_input = input('Enter your name: ')
    return user_input


def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

#Vulnerable and Outdated Components
"""
You are likely vulnerable:

If you do not know the versions of all components you use (both client-side and server-side). 
This includes components you directly use as well as nested dependencies.
"""
def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data


#Injection
"""
User-supplied data is not validated, filtered, or sanitized by the application.
"""
def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

# Broken Access Control
"""
Permitting viewing or editing someone else's account 
by providing its unique identifier (insecure direct object references)
"""
if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
