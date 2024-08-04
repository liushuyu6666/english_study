import click
from flask import current_app, g
from pymongo import MongoClient

sentence_collection_name = "sentences"
counters_collection_name = "counters"


def get_db():
    if 'db' not in g:
        g.client = MongoClient(current_app.config['MONGO_URI'])
        g.db = g.client.get_database()
    return g.db


# init all collections
def init_db():
    db = get_db()
    db[sentence_collection_name].create_index("index", unique=True)  # Create an index on the "index" field

    # Initialize the counter for the sentences collection if it doesn't exist
    if db[counters_collection_name].find_one({"_id": sentence_collection_name}) is None:
        db[counters_collection_name].insert_one({"_id": sentence_collection_name, "seq": 0})


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('MongoDB setup completed.')


def close_db(e=None):
    client = g.pop('client', None)

    if client is not None:
        client.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def get_next_sequence_value(sequence_name):
    db = get_db()
    result = db[counters_collection_name].find_one_and_update(
        {"_id": sequence_name},
        {"$inc": {"seq": 1}},
        return_document=True
    )
    return result["seq"]
