import getpass
import numpy as np
import mysql.connector

print("\n\n\n\n\n\n================================================================================\n\n\n")
print("            *-------------------------------------------------------*")
print("\n                                 WELCOME! TO                          ")
print("                                     TICKETNOW                        \n")
print("                      *--------------------------------*")
print("\n\n\n================================================================================\n\n\n\n\n\n")
restart = 'Y'

while restart not in ('N', 'NO', 'n', 'no'):
    print("                                       1.LOGIN\n")
    option = int(input("                               PRESS 1 TO CONTINUE:"))
    print("                            ---------------------")
    print("                             PROJECT DEVELOPED BY")
    print("                            ---------------------")
    print("                                  Aswathy")
    print("                                  AmalRaj")
    print("                                  Alkka")
    print("                                  Arjun Krishna")
    print("                                  SreeLakshmi M\n\n")

    if option == 1:
        print("\n\nLOGIN :-")
        username = input("USERNAME:")
        if username in ('amal', 'AMAL', 'Amal', 'sreelakshmi', 'SREELAKSHMI', 'Sreelakshmi', 'alkka', 'ALKKA', 'Alkka', 'arjun', 'ARJUN', 'Arjun', 'aswathy', 'ASWATHY', 'Aswathy'):
            code = "password"
            password = getpass.getpass(prompt="PASSWORD:")

            if code == password:
                print("\n==========================================\n")
                print("*USER ACCEPTED*\n")

                print("MAIN MENU")
                print("1.MOVIE BOOKING")
                print("2.COMING SOON")
                print("3.MOST RATED MOVIE")
                print("4.TOTAL SALES\n\n")
                mm = int(input("SELECT YOUR OPTION"))

                if mm == 1:
                    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="movie")
                    mycursor = mydb.cursor()
                    mycursor.execute("select * from movie")
                    myrecords = mycursor.fetchall()
                    for x in myrecords:
                        print(x)

                    movie = int(input("\n\nSELECT THE MOVIE:"))
                    print("\n==========================================\n")
                    print("LOADING\n")
                    print("============================================\n")

                if mm == 2:
                    print("\n\nCOMING SOON\n")
                    print("LUCIFER")
                    print("ENDGAME")
                    print("JUSTICE LEAGUE")
                    print("BAAGHI 2\n\n")
                    continue

                if mm == 3:
                    print("\n\nMOST RATED MOVIE")
                    print("BLACK PANTHER")
                    continue

                if mm == 4:
                    print("\n\nTOTAL SALES")
                    print("\nCURRENT SALES FOR THE DAY:")
                    ts = np.random.randint(1, 10000)
                    print(ts)
                    continue

                print("============================================\n")

                mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="movie")
                mycursor = mydb.cursor()
                mycursor.execute("select * from movie")
                myrecords = mycursor.fetchall()
                for x in myrecords:
                    print(x)

                movie = int(input("\n\nSELECT THE MOVIE:"))
                print("\n==========================================\n")
                print("LOADING\n")
                print("============================================\n")

            else:
                print("\n==========================================\n")
                print("*USER REJECTED*\n")
                print("============================================\n")
                continue

        else:
            print("============================================\n")
            print("*USER REJECTED*\n")
            print("============================================\n")
            continue

    else:
        print("============================================\n")
        print("INVALID OPTION\n")
        print("============================================\n")
        continue

    if movie == 1:
        print("\n\n1.YES")
        print("2.NO")
        book = int(input("\n\nPROCEED TO BOOKING:"))

    elif movie == 2:
        print("\n\n1.YES")
        print("2.NO")
        book = int(input("\n\nPROCEED TO BOOKING:"))

    elif movie == 3:
        print("\n\n1.YES")
        print("2.NO")
        book = int(input("\n\nPROCEED TO BOOKING:"))

    elif movie == 4:
        print("\n\n1.YES")
        print("2.NO")
        book = int(input("\n\nPROCEED TO BOOKING:"))

    elif movie == 5:
        print("\n\n1.YES")
        print("2.NO")
        book = int(input("\n\nPROCEED TO BOOKING:"))

    else:
        print("============================================\n")
        print("SELECT A MOVIE FROM THE LIST\n")
        print("============================================\n")
        continue

    if book == 1:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="screen")
        mycursor = mydb.cursor()
        mycursor.execute("select * from screen_list")
        myrecords = mycursor.fetchall()
        for y in myrecords:
            print(y)

        th = int(input("SELECT SCREEN:"))

    elif book == 2:
        continue

    if th == 1:
        print("\n\n1.TODAY")
        print("2.TOMORROW")
        day = int(input("\n\nSELECT SCREEN:"))

    elif th == 2:
        print("\n\n1.TODAY")
        print("2.TOMORROW")
        day = int(input("\n\nSELECT SCREEN:"))

    elif th == 3:
        print("\n\n1.TODAY")
        print("2.TOMORROW\n\n")
        day = int(input("\n\nSELECT SCREEN:"))

    else:
        continue

    if day == 1:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="time")
        mycursor = mydb.cursor()
        mycursor.execute("select * from show_time")
        myrecords = mycursor.fetchall()
        for x in myrecords:
            print(x)

        the = int(input("\n\nSELECT SHOW TIME:"))
        prs = 230
        seat = int(input("\n\nSELECT NO OF SEATS:"))
        r = prs * seat

    elif day == 2:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="time")
        mycursor = mydb.cursor()
        mycursor.execute("select * from show_time2")
        myrecords = mycursor.fetchall()
        for x in myrecords:
            print(x)

        the = int(input("\n\nSELECT SHOW TIME:"))
        prs = 230
        seat = int(input("\n\nSELECT NO OF SEATS:"))
        r = prs * seat

    else:
        continue

    if the == 1:
        a = np.random.randint(1, 50, seat)
        print("\n\nYOUR SEAT NO IS:", a)

        b = np.arange(1, 10, 1)
        c = np.arange(10, 20, 1)
        d = np.arange(20, 30, 1)
        e = np.arange(30, 40, 1)
        f = np.arange(40, 50, 1)

        print("\n\nSCREEN THIS WAY")
        print("A:", b)
        print("B:", c)
        print("C:", d)
        print("D:", e)
        print("E:", f)

        print("\n\nPAYMENT METHOD")
        print("1.CREDIT/DEBIT")
        print("2.PAYTM")
        print("3.NET BANKING")
        print("4.CASH")
        ab = int(input("\n\nSELECT PAYMENT METHOD:"))

    elif the == 2:
        a = np.random.randint(1, 50, seat)
        print("\n\nYOUR SEAT NO IS:", a)

        b1 = np.arange(1, 10, 1)
        c1 = np.arange(10, 20, 1)
        d1 = np.arange(20, 30, 1)
        e1 = np.arange(30, 40, 1)
        f1 = np.arange(40, 50, 1)

        print("\n\nSCREEN THIS WAY")
        print("A:", b1)
        print("B:", c1)
        print("C:", d1)
        print("D:", e1)
        print("E:", f1)

        print("\n\nPAYMENT METHOD")
        print("1.CREDIT/DEBIT")
        print("2.PAYTM")
        print("3.NET BANKING")
        print("4.CASH")
        ab = int(input("\n\nSELECT PAYMENT METHOD:"))

    elif the == 3:
        a = np.random.randint(1, 50, seat)
        print("\n\nYOUR SEAT NO IS:", a)

        b2 = np.arange(1, 10, 1)
        c2 = np.arange(10, 20, 1)
        d2 = np.arange(20, 30, 1)
        e2 = np.arange(30, 40, 1)
        f2 = np.arange(40, 50, 1)

        print("\n\nSCREEN THIS WAY")
        print("A:", b2)
        print("B:", c2)
        print("C:", d2)
        print("D:", e2)
        print("E:", f2)

        print("\n\nPAYMENT METHOD")
        print("1.CREDIT/DEBIT")
        print("2.PAYTM")
        print("3.NET BANKING")
        print("4.CASH")
        ab = int(input("\n\nSELECT PAYMENT METHOD:"))

    else:
        continue

    if ab == 1:
        num = int(input("\n\nENTER CARD NUMBER:"))
        mm = int(input("MM:"))
        yyyy = int(input("YYYY:"))
        cvv = int(input("CVV:"))
        print("\n\n============================================\n")
        print("LOADING\n")
        print("=========================================\n\n")

        print("AMOUNT=\n")
        print(r)
        print("\n\n1.YES")
        ps = int(input("\n\nPROCEED TO PAY:"))

    elif ab == 2:
        pay = int(input("\n\nENTER PAYTM REGISTERED PHONE NUMBER:"))
        pas = input("ENTER PASSWORD:")
        print("\n\n============================================\n")
        print("LOADING\n")
        print("==============================================\n\n")

        print("AMOUNT=")
        print(r)
        print("\n\n1.YES")
        ps = int(input("\n\nPROCEED TO PAY:"))

    elif ab == 3:
        bnk = str(input("\n\nSELECT YOUR BANK:"))
        ac = int(input("AC NO:"))
        pas = input("PASSWORD:")
        otp = int(input("ENTER OTP SENT TO PHONE:"))
        print("\n\n============================================\n")
        print("LOADING\n")
        print("==============================================\n\n")

        print("\n\nAMOUNT=")
        print(r)
        print("\n\n1.YES")
        ps = int(input("\n\nPROCEED TO PAY:"))

    elif ab == 4:
        print("AMOUNT=")
        print(r)
        print("\n\n1.YES")
        ps = int(input("\n\nPROCEED TO PAY:"))

    else:
        print("\n\n============================================\n")
        print("OPTION UNAVAILABLE\n")
        print("==============================================\n\n")

    if ps == 1:
        print(" ________________________________________________________________________ ")
        print("                                  MOVIES NOW                                   ")
        print(" DATE:                                                                                ")
        print("                                                                                           ")
        print("                                                                                           ")
        print("                           YOUR SEAT NO IS:", a)
        print("                                                                                          ")
        print("========================================================================")
        print("                                                                                          ")
        print("                   THANK YOU FOR USING OUR SERVICE                     ")
        print("________________________________________________________________________")

        exi = int(input("PRESS 1 TO EXIT:"))
        if exi == 1:
            exit
        break

    else:
        print("\n\n============================================\n")
        print("OPTION UNAVAILABLE\n")
        print("==============================================\n\n")




