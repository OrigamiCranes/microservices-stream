from app import app, db
from .models import EURUSD
from flask import render_template, request
import random, json, pandas
from sqlalchemy import and_, func


@app.route('/stream/<epic>', methods=['GET'])
def stream(epic):
    settings = request.json

    # get db_table size to assure no out of range values
    # generate rng value of datasteam
    size = db.session.query(eval(epic)).count()
    stream_start = random.randrange(1, size - settings['block_size'])

    # get data_block between two values
    db_query = db.session.query(eval(epic)).filter(and_(EURUSD.id >= stream_start), (EURUSD.id <= (stream_start + settings['block_size']-1))).statement

    data_frame = pandas.read_sql_query(db_query, db.session.bind)
    data_block = data_frame.to_json(orient='split')

    return json.loads(data_block)
