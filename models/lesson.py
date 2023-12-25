from models.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey,Table
from sqlalchemy.orm import relationship

association_table = Table('association',
                          Base.matadata,Column('lesson_id',Integer,ForeignKey('lessons.id')),
                          Column('group.id',Integer,ForeignKey('groups.id')))


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    lesson_title = (Column(String(250), nullable=False))
    groups = relationship('Group', secondary=association_table, backref='group_lesson' )




