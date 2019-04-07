import sql

db = sql.SQLDatabase()
db.database_setup()

print(db.get_user("Abraham"))
print(db.get_user("poo"))