import sqlite3

class readdata:
    def __init__(self):
        self.com = sqlite3.connect('sms.db')
        self.cur = self.com.cursor()

    def readstudent(self, sid):
        self.cur.execute(f'''
                            SELECT * FROM STUDENT
                            WHERE sid = {sid}
                        ''')
        row = self.cur.fetchone()
        if row:
            print("---------------------------Student Data------------------------------")
            print(row)
        else:
            print("No record found!")

    def readcourse(self, cid):
        self.cur.execute(f'''
                            SELECT * FROM COURSE
                            WHERE cid = {cid}
                        ''')
        row = self.cur.fetchone()
        if row:
            print("---------------------------Course Data------------------------------")
            print(row)
        else:
            print("No record found!")

    def readtransaction(self, tid):
        self.cur.execute(f'''
                            SELECT * FROM TRANSac
                            WHERE tid = {tid}
                        ''')
        row = self.cur.fetchone()
        if row:
            print("---------------------------Transaction Data------------------------------")
            print(row)
        else:
            print("No record found!")