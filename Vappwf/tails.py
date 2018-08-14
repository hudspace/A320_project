"""from peewee import *

db = SqliteDatabase('tailnumbers.db')

class aircraft_type(Model):
    a320 = CharField(max_length = 5, unique = True)
    a321 = CharField(max_length = 5, unique = True)

class Meta:
    database = db

if __name__ == '__main__':
    db.connect()
    db.create_tables([aircraft_type], safe = True)"""

class A320:

    def __init__(self, name, *args, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)


class A321:

    def __init__(self, name, *args, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)


N503JB = A320()
N504JB = A320()
N505JB = A320()
N506JB = A320()
N507JT = A320()
N508JL = A320()
N509JB = A320()
N510JB = A320()
N516JB = A320()
N517JB = A320()
N519JB = A320()
N520JB = A320()
N521JB = A320()
N523JB = A320()
N524JB = A320()
N526JL = A320()
N527JL = A320()
N529JB = A320()
N531JL = A320()
N534JB = A320()
N535JB = A320()
N536JB = A320()
N537JL = A320()
N547JB = A320()
N552JB = A320()
N554JB = A320()
N556JB = A320()
N558JB = A320()
N559JB = A320()
N561JB = A320()
N562JB = A320()
N563JB = A320()
N564JB = A320()
N565JB = A320()
N566JB = A320()
N568JB = A320()
N569JB = A320()
N570JB = A320()
N571JB = A320()
N579JB = A320()
N580JB = A320()
N583JB = A320()
N584JB = A320()
N585JB = A320()
N586JB = A320()
N587JB = A320()
N588JB = A320()
N589JB = A320()
N590JB = A320()
N591JB = A320()
N592JB = A320()
N593JB = A320()
N594JB = A320()
N595JB = A320()
N597JB = A320()
N598JB = A320()
N599JB = A320()
N603JB = A320()
N605JB = A320()
N606JB = A320()
N607JB = A320()
N608JB = A320()
N612JB = A320()
N613JB = A320()
N615JB = A320()
N618JB = A320()
N621JB = A320()
N623JB = A320()
N624JB = A320()
N625JB = A320()
N627JB = A320()
N629JB = A320()
N630JB = A320()
N632JB = A320()
N633JB = A320()
N634JB = A320()
N635JB = A320()
N636JB = A320()
N637JB = A320()
N638JB = A320()
N639JB = A320()
N640JB = A320()
N641JB = A320()
N643JB = A320()
N644JB = A320()
N645JB = A320()
N646JB = A320()
N648JB = A320()
N649JB = A320()
N651JB = A320()
N652JB = A320()
N653JB = A320()
N655JB = A320()
N656JB = A320()
N657JB = A320()
N658JB = A320()
N659JB = A320()
N661JB = A320()
N662JB = A320()
N663JB = A320()
N665JB = A320()
N703JB = A320()
N705JB = A320()
N706JB = A320()
N708JB = A320()
N709JB = A320()
N712JB = A320()
N715JB = A320()
N729JB = A320()
N746JB = A320()
N760JB = A320()
N763JB = A320()
N766JB = A320()
N768JB = A320()
N775JB = A320()
N779JB = A320()
N784JB = A320()
N789JB = A320()
N793JB = A320()
N794JB = A320()
N796JB = A320()
N804JB = A320()
N805JB = A320()
N806JB = A320()
N807JB = A320()
N809JB = A320()
N821JB = A320()
N827JB = A320()
N828JB = A320()
N834JB = A320()


N903JB = A321()
N905JB = A321()
N907JB = A321()
N913JB = A321()
N923JB = A321()
N929JB = A321()
N934JB = A321()
N935JB = A321()
N937JB = A321()
N942JB = A321()
N943JT = A321()
N944JT = A321()
N945JT = A321()
N946JL = A321()
N947JB = A321()
N948JB = A321()
N949JT = A321()
N950JT = A321()
N952JB = A321()
N954JB = A321()
N955JB = A321()
N956JT = A321()
N957JB = A321()
N958JB = A321()
N959JB = A321()
N961JT = A321()
N962JT = A321()
N964JT = A321()
N965JT = A321()
N966JT = A321()
N967JT = A321()
N968JT = A321()
N969JT = A321()
N970JB = A321()
N971JT = A321()
N972JT = A321()
N974JT = A321()
N975JT = A321()
N976JT = A321()
N978JB = A321()
N979JT = A321()
N980JT = A321()
N981JT = A321()
N982JB = A321()





