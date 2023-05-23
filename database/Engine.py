from sqlalchemy import create_engine

def getEngine():
    engine = create_engine("sqlite:///db.sqlite", echo=True)
    return (engine)