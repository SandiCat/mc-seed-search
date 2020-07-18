from peewee import *

db = SqliteDatabase('people.db')

class World(Model):
    seed = BigIntegerField(primary_key=True)
    user_rating = DoubleField(null=True)
    biome_data = BlobField(null=True)
    image = BlobField(null=True)
    saved = BooleanField(default=False)

    class Meta:
        database = db