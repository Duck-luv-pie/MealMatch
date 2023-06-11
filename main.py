# Importing required modules
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import mysql.connector

#Creating Screens
class MainWindow(Screen):
    pass

class DonatorLogin(Screen):
    pass

class ReceiverLogin(Screen):
    pass

class ReceiverSearch(Screen):
    pass

class DonatorMainScreen(Screen):
    pass

class SellOrder(Screen):
    pass

class TotalDonations(Screen):
    pass

class TaxExempt(Screen):
    pass


# Custom ImageButton class
class ImageButton(ButtonBehavior, Image):
    pass
# Custom WindowManager class
class WindowManager(ScreenManager):
    pass
# Custom Widget Class
class MyGrid(Widget):
    pass

# Custom ImageButton class
class ImageButton(ButtonBehavior, Image):
    pass

kv = Builder.load_file("my.kv")



#Custom MyWidget Class
class myWidget(Widget):


    acc = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.makelist()
    def makelist(self):
        pass

#Main app class
class MyApp(App):
    pass
    def build(self):
        self.icon = r'C:\Users\Eric\PycharmProjects\MCCO_app\MCCO_pics\Price_Tag_Logo.jpg'
        Window.clearcolor = (65/255,68/255,175/255,255/255)

#         #defining my database
#         mydb = mysql.connector.connect(
#             host = "localhost",
#             user = "root",
#             passwd ="password123",
#             database = "second_db"
#         )

#         #create my cursor
#         c = mydb.cursor()

#         #create my database
#         # c.execute("CREATE DATABASE IF NOT EXISTS second_db")

#         #check to see if database was created
#         # c.execute("SHOW DATABASES")
#         # for db in c:
#         #    print(db)

#         #creating my tale:
#         c.execute("""CREATE TABLE if not exists customers(name VARCHAR(50))""")

#         #check for creation of table
#         # c.execute("SHOW TABLES")
#         # for table in c:
#         #     print(table)
#         # print (c.description)

#         #commit changes
#         mydb.commit()
#         #close connection
#         mydb.close()
#         return kv

#     def submit(self):
#         #connect to database
#         mydb = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             passwd="password123",
#             database="second_db"
#         )
#         c = mydb.cursor()
#         sql_command = "INSERT INTO customers (name) VALUES (%s)"
#         print("it reaches 4")
#         values = (self.root.ids.ReceiverName.text,)
#         print("it reaches 5")
#         print(values)
#         print("it reaches 6")

#     #
#     #     #execute SQL command
#         c.execute(sql_command, values)
#     #
#     #     #add a message
#         self.root.ids.ReceiverName.text = f'{self.root.ids.ReceiverName}'
#     #
#         self.root.ids.ReceiverName.text = ''
#     #commit changes
#         mydb.commit()
#     #close the database
#         mydb.close()
#     #
#     def show_records(self):
#         mydb = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             passwd="password123",
#             database="second_db"
#         )
#         c = mydb.cursor()
#     #
#     #
#         c.execute("SELECT * FROM customers")
#         records = c.fetchall()
#     #
#         word = ''
#     #
#         for record in records:
#             word = f'{word}\n{record[0]}'
#             self.root.ids.word_label.text = f'{word}'
#     #
#         mydb.commit()
#         mydb.close()



if __name__ == "__main__":
    MyApp().run()
