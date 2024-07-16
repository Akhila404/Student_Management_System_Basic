import sqlite3

class deletedata:
    def __init__(self):
        self.com = sqlite3.connect('sms.db')
        self.cur = self.com.cursor()

    def deletestudent(self, sid):
        self.cur.execute(f'''
                            DELETE FROM STUDENT
                            WHERE sid = {sid}
                        ''')
        self.com.commit()
        print("---------------------------Data Deleted Successfully------------------------------")

    def deletecourse(self, cid):
        self.cur.execute(f'''
                            DELETE FROM COURSE
                            WHERE cid = {cid}
                        ''')
        self.com.commit()
        print("---------------------------Data Deleted Successfully------------------------------")

    def deletetransaction(self, tid):
        self.cur.execute(f'''
                            DELETE FROM TRANSac
                            WHERE tid = {tid}
                        ''')
        self.com.commit()
        print("---------------------------Data Deleted Successfully------------------------------")