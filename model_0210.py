from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Mobile(Base):
    __tablename__ = "mobiles"
    id = Column(Integer, primary_key=True)
    number = Column(String(32))
    student_id = Column(Integer, ForeignKey("students.id"))

    def __str__(self):
        return "{}:{}".format(self.id, self.number)

    def __repr__(self):
        return self.__str__()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    phones = relationship("Mobile", backref="student")

    def __str__(self):
        return "{}:{}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    fn = os.path.join(os.path.dirname(__file__), "data.sqlite")
    fn = "sqlite:///" + fn
    engine = create_engine(fn, echo=False)
    Session = sessionmaker(bind=engine)
    sess = Session()
    # 創建完整資料庫 create_all/drop_all
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # 測試資料
    phones = [Mobile(number="0912345678"),
              Mobile(number="0922222222"),
              Mobile(number="0911111111")]
    s = Student(name="Elwing", phones=phones)
    sess.add(s)
    sess.commit()
    students = sess.query(Student).filter_by(name="Elwing")
    # .all()  .first()
    s = students.first()
    print(s)
    print(s.phones)