
import sys
import datetime
sys.path.append("../../")
from gluon import DAL, Field

db = DAL('mysql://root:123456@localhost/test',migrate_enabled=True)
db.define_table('mytable', Field('temperature','double'),Field('pressure','double'),Field('dates','date'),\
 Field('time','time'),format='%(content)s',migrate=True)
print db._uri
print db._dbname
print db.mytable.fields
#print db.field
print db.tables

# insert data
json_string = "{  \
    'first': 1,\
    'second': 2,\
    'date': '2016-2-6',\
    'temperature': '37.5',\
    'unit': 'km'\
}";

#auth.define_tables(migrate=False)
#db.mytable.insert(temperature = 36.5,pressure = 90)
db.mytable.insert(temperature = 36.5,pressure = 90,dates = datetime.datetime.now().date(), \
time= datetime.datetime.now().time())
#db.mytable.insert()
db.commit()
#select
rows = db.executesql('SELECT  * FROM mytable ORDER BY id DESC LIMIT 5 ;')
print rows
rows = db().select(db.mytable.ALL)
#print rows
#print rows = db().select(db.mytable.ALL)
