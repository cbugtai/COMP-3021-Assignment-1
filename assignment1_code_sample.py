import os
import pymysql
from urllib.request import urlopen

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}
    #OWASP A02:2021 is a cryptographic failure because it does not authenticate properly or validate the session;
    #database credentials are hardcoded into the source code, exposing sensitive data.

def get_user_input():
    user_input = input('Enter your name: ')
    return user_input
    #OWASP A01:2021 this is broken access control because there is no access control or validation, meaning
    #anyone can trigger get_user_input() and/or send_email() potentially exposing user data and triggering unwanted emails.

def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')
    #OWASP A05:2021 this is a security misconfiguration issue, as the send_email() function uses os.system, which can allow
    #command injection if the body contains special characters or malicious code.

def get_data():
    url = 'http://insecure-api.com/get-data'
    #OWASP A08:2021 this is an insecure communication issue because the API uses HTTP instead of HTTPS, 
    #which could allow attackers to intercept or modify the data in transit (man-in-the-middle attacks).

    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    #OWASP A03:2021 this is an injection issue due to the query constructed using string concatenation with user input,
    #meaning a user can put input SQL into the query and inject malicious code.
    send_email('admin@example.com', 'User Input', user_input)