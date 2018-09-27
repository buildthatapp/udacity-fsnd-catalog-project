from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalog_db_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

print("Attempting to create a database session...")
try:
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
except:



#Items for Electric Guitars
category1 = Category(name = "Electric Guitars")

session.add(category1)
session.commit()


categoryItem1 = CategoryItem(name = "Fender Limited Edition Standard Stratocaster", description = "Value, tone, and limited edition style.", price = "$599.99", category = category1, user_id = 1, )

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name = "PRS John Mayer Silver Sky Electric Guitar", description = "Extraordinary attention to detail makes for a stellar signature guitar.", price = "$2299.50", category = category1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(name = "Fender Parallel Universe Troublemaker Telecaster Electric Guitar", description = "Loaded and ready to stir up some trouble.", price = "$1999.99", category = category1)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(name = "Gibson Limited Edition Les Paul Traditional Electric Guitar", description = "A beautiful evocation of Les Paul vintage tradition.", price = "$2629.99", category = category1)

session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(name = "Fender American Professional Stratocaster Maple Fingerboard", description = "The authentic original model, evolved.", price = "$1399.99", category = category1)

session.add(categoryItem5)
session.commit()







print "added catalog items!"

