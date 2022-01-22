import psycopg2
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine=create_engine('postgresql://postgres:chinni@localhost:5432/alchemy', echo=False)

Session=sessionmaker(bind=engine)
session=Session()

Base=declarative_base()

class Jobs(Base):
    __tablename__='Jobs'
    
    JobId=Column(Integer, primary_key=True)
    Category=Column(String(50))
    Location=Column(String(20))
    Position=Column(String(200))
    Links=Column(String(200))

    def insertData(jobid,category,location,position,links,tableName):
        Job1=Jobs(JobId=jobid,Category=category,Location=location,Position=position,Links=links)
        session.add(Job1)
        session.commit()
    def truncateTable(tableName):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        #session.delete(Jobs)
        #session.commit()

#Base.metadata.create_all(engine)
