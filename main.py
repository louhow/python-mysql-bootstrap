#!/usr/bin/env python
from services.dao import Dao, Record
from yoyo import read_migrations
from yoyo import get_backend
from datetime import datetime


def main():
  db_url = 'root:pass@localhost:14401/mariadb'
  migration_url = 'mysql://' + db_url  # yoyo does not play nicely with pymysql
  dao_url = 'mysql+pymysql://' + db_url
  backend = get_backend(migration_url)
  migrations = read_migrations('./migrations')
  with backend.lock():
    backend.apply_migrations(backend.to_apply(migrations))

  dao = Dao(dao_url)
  record = Record(some_value='initial valure: ' + datetime.utcnow().isoformat())

  dao.insert_record(record)
  print('Inserted record with ID: ', str(record.first_table_id))

  try:
    new_record = Record(first_table_id=record.first_table_id, some_value='another val')
    dao.insert_record(new_record)
    print('Inserted record again? ', str(record.first_table_id))
    print('Should never get here')
  except KeyError:
    print('Could not insert record with same ID, as expected.')


if __name__ == '__main__':
  main()
