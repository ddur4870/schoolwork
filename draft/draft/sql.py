import sqlite3

# https://docs.python.org/2/library/sqlite3.html

# This class is a simple handler for all of our SQL database actions
# Practicing a good separation of concerns, we should only ever call 
# These functions from our models

# If you notice anything out of place here, consider it to your advantage and don't spoil the surprise

class SQLDatabase():
    id = 0;
    messageID = 0;

    # Get the database running
    def __init__(self, database_arg=":memory:"):
        self.conn = sqlite3.connect(database_arg)
        self.cur = self.conn.cursor()

    # SQLite 3 does not natively support multiple commands in a single statement
    # Using this handler restores this functionality
    # This only returns the output of the last command
    def execute(self, sql_string):
        out = None
        for string in sql_string.split(";"):
            try:
                out = self.cur.execute(string)
            except:
                pass
        return out

    # Commit changes to the database
    def commit(self):
        self.conn.commit()

    #-----------------------------------------------------------------------------
    
    # Sets up the database
    # Default admin password
    def database_setup(self):

        # Clear the database if needed
        self.execute("DROP TABLE IF EXISTS Users")
        self.execute("DROP TABLE IF EXISTS Messages")
        self.commit()

        # Create the users table
        self.execute("""CREATE TABLE Users(
            Id INT,
            username TEXT,
            password TEXT,
            age INTEGER,
            bio TEXT,
            admin INTEGER DEFAULT 0
        )""")
        self.commit()

        # Create the messages table
        self.execute("""CREATE TABLE Messages(
            Id INT,
            sender TEXT,
            recipient TEXT,
            message TEXT,
            time TEXT
        )""")
        self.commit()

        # Add our admin users
        self.add_user('Abraham', 'test', 18, admin=1)
        self.add_user('Karlo', 'test', 18, admin=1)
        self.add_user('Darby', 'test', 18, admin=1)
        self.add_user('Jermaine', 'test', 18, admin=1)
        self.add_user('Presley', 'test', 18, admin=1)

        # Some custom bios for our lovely admins
        self.update_bio("Abraham", "The coolest guy ever")
        self.update_bio("Karlo", "Karlo gay")

        # Some messages for our lovely admins
        self.add_new_message("Abraham","Abraham", "Your first message, from Abraham <3", "Friday, 05 Apr 2019 03:28 PM")
        self.add_new_message("Abraham","Karlo", "Your first message, from Abraham <3", "Friday, 05 Apr 2019 03:28 PM")
        self.add_new_message("Abraham","Darby", "Your first message, from Abraham <3", "Friday, 05 Apr 2019 03:28 PM")
        self.add_new_message("Abraham","Jermaine", "Your first message, from Abraham <3", "Friday, 05 Apr 2019 03:28 PM")
        self.add_new_message("Abraham","Presley", "Your first message, from Abraham <3", "Friday, 05 Apr 2019 03:28 PM")

    #-----------------------------------------------------------------------------
    # User handling
    #-----------------------------------------------------------------------------

    # Add a user to the database
    def add_user(self, username, password, age, admin=0):
        sql_cmd = """
                INSERT INTO Users
                VALUES({id}, '{username}', '{password}', {age}, '{bio}', {admin})
            """.format(id=self.id, 
                        username=username, 
                        password=password,
                        age=age,
                        bio="No Bio", 
                        admin=admin)

        self.execute(sql_cmd)
        self.commit()
        self.id += 1
        return True

    #-----------------------------------------------------------------------------

    # Check login credentials
    def check_credentials(self, username, password):
        sql_query = """
                SELECT 1 
                FROM Users
                WHERE username = '{username}' AND password = '{password}'
            """.format(username=username, password=password)

        self.execute(sql_query)

        # If our query returns
        if self.cur.fetchone():
            return True
        else:
            return False
    
    def get_user(self, username):
        sql_query = """
                SELECT * 
                FROM Users
                WHERE username = '{username}'
            """.format(username=username)

        self.execute(sql_query)

        return self.cur.fetchone()
    
    def update_bio(self, username, newBio):
        sql_query = """
                UPDATE Users
                SET bio = '{bio}'
                WHERE username = '{username}'
            """.format(username=username, bio=newBio)
        self.execute(sql_query)
        self.commit()

    def add_new_message(self, sender, recipient, message, time):
        sql_cmd = """
                INSERT INTO Messages
                VALUES({id}, '{sender}', '{recipient}', '{message}', '{time}')
            """.format(id = self.messageID, 
                        sender=sender, 
                        recipient=recipient,
                        message=message,
                        time=time)

        self.execute(sql_cmd)
        self.commit()
        self.messageID += 1

    def get_user_messages(self, user):
        sql_query = """
                SELECT * 
                FROM Messages
                WHERE recipient = '{user}'
            """.format(user=user)
        
        self.execute(sql_query)

        return self.cur.fetchall() #list