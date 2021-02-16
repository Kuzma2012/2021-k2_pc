import psycopg2

def init_tpc(*args):
    conn_num = 0
    for connection in args:
        conn_num += 1
        x_id = connection.xid(42, 'transaction ID', 'connection %s' %conn_num)
        connection.tpc_begin(x_id)

def commit(*args):
    for conn in args:
        conn.tpc_commit()

def conn_close(*args):
    for conn in args:
        conn.close()

def exec_command(conn, query, params = ''):
    cur = conn.cursor()
    cur.execute(query, params)
    return cur


def main():
    connection_accounts = psycopg2.connect("dbname='db_2pc_db' user='db_2pc' host='localhost' password='db_2pc' " "port='5434'")
    connection_flights = psycopg2.connect("dbname='db_2pc_db' user='db_2pc' host='localhost' password='db_2pc' " "port='5432'")
    connection_hotels = psycopg2.connect("dbname='db_2pc_db' user='db_2pc' host='localhost' password='db_2pc' " "port='5433'")

    init_tpc(connection_flights, connection_hotels, connection_accounts)

    fly_max_id = int(exec_command(connection_flights, query = '''SELECT MAX(Booking_Id) FROM fly_booking;''').fetchone()[0])
    hotel_max_id = int(exec_command(connection_hotels, query = '''SELECT MAX(Booking_Id) FROM hotel_booking;''').fetchone()[0])

    input("Start")
    try:
        exec_command(connection_flights, query = '''insert into fly_booking(Booking_Id, Client_Name, Fly_number, Fly_From, Fly_To, Fly_Date) values (%s,%s,%s,%s,%s,%s);''', params = (fly_max_id+1, 'Nik', 'KLM 1382', 'KBP', 'AMS','01/05/2015'))
        connection_flights.tpc_prepare()
        exec_command(connection_hotels, query='''insert into hotel_booking(Booking_Id, Client_Name, Hotel_Name, Arrival, Departure) values (%s,%s,%s,%s,%s);''', params=(hotel_max_id+1, 'Nik', 'Hilton', '01/05/2015', '07/05/2015'))
        connection_hotels.tpc_prepare()
    except psycopg2.ProgrammingError:
        connection_flights.tpc_rollback()
        connection_hotels.tpc_rollback()
    else:
        try:
            exec_command(connection_accounts, query = '''UPDATE accounts SET amount = Amount - 10 WHERE Client_name = 'Nik';''')
            connection_accounts.tpc_prepare()
        except (psycopg2.ProgrammingError, psycopg2.DatabaseError) as errors:
            connection_accounts.tpc_rollback()
        else:
            # if comment first and uncomment second commit then transaction will fail and will be in wait status. If run script after that once again, fly and hotel commits will be in wait status
            commit(connection_flights, connection_hotels, connection_accounts)
            # commit(connection_flights, connection_hotels)

    conn_close(connection_flights, connection_hotels, connection_accounts)
    input("Finish")

main ()