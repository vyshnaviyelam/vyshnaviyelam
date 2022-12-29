import pyodbc

server = 'HCL-02-84\SQLEXPRESS'
database = 'FileSearchResults'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class EmployeeSchema:
    def creatingtable(self):
        try:
            values=cursor.execute(''' select * from EmployeeDetails_table ''')
            print(values)
            query1 = cursor.execute('''use FileSearchResults''')
            query2 = cursor.execute('''create table EmployeeDetails_table(
                                        Name varchar(100),
                                        ID int,
                                        Salary int,
                                        Project varchar(50))
                                        ''')
            cnxn.commit()
        except:
            print("table is already exist")