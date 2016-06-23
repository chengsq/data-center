
import sys
sys.path.append("../../")
from gluon import DAL, Field

db = DAL('mysql://root:123456@localhost/test',migrate_enabled=False)
db.define_table('mytable', Field('content'),format='%(content)s',migrate=False)
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

db.mytable.insert(content=json_string)
db.mytable.insert(content=json_string)
db.commit()
#select
#print db.executesql('SELECT * FROM mytable;')
rows = db().select(db.mytable.ALL)
print rows
#print rows = db().select(db.mytable.ALL)
