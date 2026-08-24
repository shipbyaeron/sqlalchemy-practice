from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    author: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}')>"

engine = create_engine("sqlite:///books.db")

Base.metadata.create_all(engine)

books_list = [
    Book(title="Bi mat cua Naoko", author="Higashino Keigo"),
    Book(title="Toi thay hoa vang tren co xanh", author="Nguyen Nhat Anh"),
    Book(title="Nguoi dua dieu", author="Hosseini")
]

with Session(engine) as session:
    session.add_all(books_list)
    session.commit()

with Session(engine) as session:
    books = session.scalars(select(Book)).all()
    print("---Tất cả sách---")
    for b in books:
        print(b)

with Session(engine) as session:
    stmt = select(Book).where(Book.author == "Higashino Keigo")
    keigo_books = session.scalars(stmt).all()
    print("\n---Sách của Higashino Keigo---")
    for k in keigo_books:
        print(k)

with Session(engine) as session:
    book = session.get(Book, 1)
    if book:
        book.title = "Bach da hanh"
    session.commit()