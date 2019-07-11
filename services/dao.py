from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class Dao(object):
  def __init__(self, db_url):
    engine = create_engine(db_url, pool_recycle=60, pool_pre_ping=True)
    self.Session = sessionmaker()
    self.Session.configure(bind=engine)

  def get_record(self, record_id):
    session = self.Session()
    result = session.query(Record) \
      .filter_by(first_table_id=record_id) \
      .first()
    session.close()
    return result

  def insert_record(self, record):
    s = self.Session()
    failed = True
    try:
      s.add(record)
      s.commit()  # flush and commit session changes to DB
      s.refresh(record)  # query latest record to grab the ID
      failed = False
    except IntegrityError:
      print('Unable to insert duplicate record with id ' + str(record.first_table_id))
    finally:
      s.close()

    if failed:
      raise KeyError



class Record(Base):
  __tablename__ = 'some_table'
  first_table_id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
  some_value = Column(String(20))
  create_time = Column(TIMESTAMP)
