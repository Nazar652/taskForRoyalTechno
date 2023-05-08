from peewee import *

db = SqliteDatabase("db.sqlite")


class User(Model):
    id = IntegerField()
    username = CharField()
    name = CharField()

    class Meta:
        database = db


User.delete().execute()
User.create_table()
