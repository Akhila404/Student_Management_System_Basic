
import sqlite3

class insertdata:
    def __init__(self):
        self.com = sqlite3.connect('sms.db')
        self.cur = self.com.cursor()

    def insertstudent(self, sid, sname, email, city):
        self.cur.execute(f'''
                            INSERT INTO STUDENT VALUES(
                            {sid},
                            "{sname}",
                            "{email}",
                            "{city}"
                        )   ''')                            # to get the data from users. # if we give the data it is 
        
        self.com.commit()                                   # commiting all the chnages.
        print("---------------------------Data Added Successfully------------------------------")

    def insertcourse(self, cid, coursename, sid, price):
        self.cur.execute(f'''
                            INSERT INTO COURSE VALUES(
                            {cid}, 
                            "{coursename}",
                            {sid},
                            {price}
                                ) ''')
        self.com.commit()
        print("---------------------------Data Added Successfully------------------------------")
    
    def inserttransactions(self, tid, sid, cid, method):
        self.cur.execute(f'''
                            INSERT INTO TRANSac VALUES(
                            {tid},
                            {sid},
                            {cid},
                            "{method}"

                        ) ''')
        self.com.commit()
        print("---------------------------Data Added Successfully------------------------------")




