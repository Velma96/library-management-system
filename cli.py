import click
from models import Session, Book, Member, Transaction
import datetime

session = Session()

@click.group()
def cli():
    """Library Management System CLI"""
    pass

@click.command()
@click.argument("name")
def register_member(name):
    """Register a new member"""
    member = Member(name=name)
    session.add(member)
    session.commit()
    click.echo(f"Member {name} registered successfully!")

@click.command()
@click.argument("title")
@click.argument("author")
def add_book(title, author):
    """Add a new book"""
    book = Book(title=title, author=author)
    session.add(book)
    session.commit()
    click.echo(f"Book '{title}' by {author} added to the library!")

@click.command()
@click.argument("title")
def borrow_book(title):
    """Borrow a book"""
    book = session.query(Book).filter_by(title=title, available=1).first()
    if book:
        member_id = click.prompt("Enter your member ID", type=int)
        transaction = Transaction(book_id=book.id, member_id=member_id)
        book.available = 0
        session.add(transaction)
        session.commit()
        click.echo(f"Book '{title}' borrowed successfully!")
    else:
        click.echo("Book is not available or does not exist.")

@click.command()
@click.argument("title")
def return_book(title):
    """Return a book"""
    book = session.query(Book).filter_by(title=title, available=0).first()
    if book:
        transaction = session.query(Transaction).filter_by(book_id=book.id, returned_at=None).first()
        transaction.returned_at = datetime.datetime.utcnow()
        book.available = 1
        session.commit()
        click.echo(f"Book '{title}' returned successfully!")
    else:
        click.echo("This book is not currently borrowed.")

@click.command()
def list_books():
    """List all books"""
    books = session.query(Book).all()
    for book in books:
        status = "Available" if book.available else "Borrowed"
        click.echo(f"{book.title} by {book.author} - {status}")

cli.add_command(register_member)
cli.add_command(add_book)
cli.add_command(borrow_book)
cli.add_command(return_book)
cli.add_command(list_books)

if __name__ == "__main__":
    cli()
