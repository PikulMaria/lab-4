import os
import pypyodbc

pypyodbc.win_compact_mdb('Test1.mdb', 'TestOne.mdb')
file_size = os.stat('TestOne').st_size
print(file_size)
