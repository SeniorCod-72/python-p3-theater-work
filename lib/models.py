from sqlalchemy import column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Role(Base):
    __tablename__ = "roles"
    id = column(Integer, primary_key = True)
    character_name = column(String)
    auditions = relationship('Audition', back_populates='role')


    class Audition(Base):
        __tablename__ = "auditions"
        id = column(Integer, primary_key = True)
        actor = column(String)
        location = column(String)
        phone = column(Integer)
        hired = column(Boolean, default = False)
        role_id = column(Integer, ForeignKey("roles.id"))
        
        role = relationship('Role', back_populates='auditions')

        def call_back(self):
             self.hired = True

             


        





