
import sqlite3

class updatedata:
    def __init__(self):
        self.com = sqlite3.connect('sms.db')
        self.cur = self.com.cursor()

    def updatestudent(self, field, sid, new_value):
        if field == "1":
            self.cur.execute(f'''
                                UPDATE STUDENT SET
                                sname = "{new_value}"
                                WHERE sid = {sid}
                            ''')
        elif field == "2":
            self.cur.execute(f'''
                                UPDATE STUDENT SET
                                email = "{new_value}"
                                WHERE sid = {sid}
                            ''')
        elif field == "3":
            self.cur.execute(f'''
                                UPDATE STUDENT SET
                                city = "{new_value}"
                                WHERE sid = {sid}
                            ''')
        else:
            print("Invalid field!")
            return

        self.com.commit()
        print("---------------------------Data Updated Successfully------------------------------")

    def updatecourse(self, field, sid, new_value):
        if field == "1":
            self.cur.execute(f'''
                                UPDATE COURSE SET
                                cid = "{new_value}"
                                WHERE sid = {sid}
                            ''')
        elif field == "2":
            self.cur.execute(f'''
                                UPDATE COURSE SET
                                coursename = "{new_value}"
                                WHERE sid = {sid}
                            ''')
        elif field == "3":
            self.cur.execute(f'''
                                UPDATE COURSE SET
                                price = {new_value}
                                WHERE sid = {sid}
                            ''')
        else:
            print("Invalid field!")
            return

        self.com.commit()
        print("---------------------------Data Updated Successfully------------------------------")

    def updatetransaction(self, field, sid, new_value):
        if field == "1":
            self.cur.execute(f'''
                                UPDATE TRANSac SET
                                tid = {new_value}
                                WHERE sid = {sid}
                            ''')
        elif field == "2":
            self.cur.execute(f'''
                                UPDATE TRANSac SET
                                cid = {new_value}
                                WHERE sid = {sid}
                            ''')
        elif field == "3":
            self.cur.execute(f'''
                                UPDATE TRANSac SET
                                method = "{new_value}"
                                WHERE sid = {sid}
                            ''')
        else:
            print("Invalid field!")
            return

        self.com.commit()
        print("---------------------------Data Updated Successfully------------------------------")



