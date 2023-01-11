import pymysql
connection=pymysql.connect("localhost","root","Anushka_743","ONLINE")
cursor=connection.cursor()

def delete():
    sid=input("enter item code to be deleted :")
    remove_item="DELETE FROM SHOP WHERE ITEMCODE=(%s)"
    cursor.execute(remove_item,sid)
    result=cursor.fetchall()
    if result:
        print(result)
    print("item data deleted ")
    connection.commit()
    
def search():
    while(True):
        c=int(input("""Search on the basis of:-
             1.Category
             2.Price
             """))
        if(c==1):
            scat=input("Search for items on the basis of category:")
            c="SELECT * FROM SHOP WHERE CATEGORY=%s "
            cursor.execute(c,scat)
            result = cursor.fetchall()

            for x in result:
                print(x)
            connection.commit()
        if(c==2):
            sprice=input("Search for items on the basis of price:")
            c="SELECT * FROM SHOP WHERE PRICE=%s "
            cursor.execute(c,sprice)
            result = cursor.fetchall()

            for x in result:
                print(x)
            connection.commit()
        d=input("Do you wish to continue searching for records (y/n):")
        if(d=="n" or d=="N"):
            break
    
def display():
    d="SELECT * FROM SHOP"
    cursor.execute(d)
    result = cursor.fetchall()
    for x in result:
        print(x)
    connection.commit()
    