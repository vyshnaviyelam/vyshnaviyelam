import pyodbc
conn=pyodbc.connect('Driver={SQL Server};'
                    'Server=HCL-02-84\SQLEXPRESS;'
                    'Database=FileSearchResults;'
                    'Trusted_Connection=yes;')
cursor=conn.cursor()
cursor.execute('''INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                  VALUES
                  ('E:\MainFolderA3\MainFolder2\Sampletext.txt',3,'Sampletext.txt'),
                  ('F:\MainFolderA4\MainFolder2\MainFolder3\MainFolder4\Sampletext2.txt',2,'Sampletext2.txt')''')
conn.commit();
cursor.execute('Select * From FileSearchResults_table')