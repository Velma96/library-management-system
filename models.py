from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import datetime

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    available = Column(Integer, default=1)  # 1 = Available, 0 = Borrowed

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author}, available={self.available})>"

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Member(name={self.name})>"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    member_id = Column(Integer, ForeignKey("members.id"))
    borrowed_at = Column(DateTime, default=datetime.datetime.utcnow)
    returned_at = Column(DateTime, nullable=True)

    book = relationship("Book")
    member = relationship("Member")

    def __repr__(self):
        return f"<Transaction(book={self.book_id}, member={self.member_id}, borrowed_at={self.borrowed_at})>"

# Database connection
engine = create_engine("sqlite:///library.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
