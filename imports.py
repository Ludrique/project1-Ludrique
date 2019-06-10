import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://ifpqmojeoylmmh:c498994ee062217d6428cf0b6c6dcbffcd2bab03a270b8e2eddab4c29c1d2045@ec2-54-235-167-210.compute-1.amazonaws.com:5432/dbi6d7nlegte50")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books(isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                   {"isbn":isbn, "title":title,"author":author, "year":year})
        db.commit()

if __name__ == '__main__':
    main()
