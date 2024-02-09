import mysql.connector

class sqlConnector:

    def __init__(self, config = dict()):
        self.__mydb = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )
        self.__mycursor = self.__mydb.cursor()
    
    def getField(self, field = str(), table = str(), condition = '1'):
        sql = f"SELECT {field} FROM {table} WHERE {condition}"
        self.__mycursor.execute(sql)
        myresult = self.__mycursor.fetchall()
        return myresult

    def updateField(self, field = str(), value = str(), table = str(), condition = '1'):
        try:
            sql = f'UPDATE {table} SET {field} = {value} WHERE {condition}'
            self.__mycursor.execute(sql)
            self.__mydb.commit()
            print(self.__mycursor.rowcount, "record(s) affected")
            return True
        except Exception as e:
            print(e)
            return False

    def insertValue(self, table: str, fields: list[str], values: list[str]):

        parsed_fields = ', '.join(str(field) for field in fields)
        parsed_values = ', '.join(str(value) for value in values)

        sql = f"INSERT INTO {table} ({fields}) VALUES ({values})"

        self.__mycursor.execute(sql)
        self.__mydb.commit()
        print(self.__mycursor.rowcount, "record inserted.")
