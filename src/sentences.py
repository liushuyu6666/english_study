from datetime import datetime

from flask import Blueprint, request, jsonify

from .db import get_db, get_next_sequence_value, sentence_collection_name

bp = Blueprint('sentences', __name__, url_prefix='/sentence')

collection_name = "sentences"


@bp.route('/create', methods=['POST'])
def create():
    try:
        data = request.json
        index = get_next_sequence_value(sentence_collection_name)
        english_entry = {
            "index": index,
            "timestamp": datetime.utcnow(),
            "words": data["words"],
            "expression": data["expression"],
            "note": data["note"],
            "source": data["source"]
        }
        db = get_db()
        result = db[collection_name].insert_one(english_entry)
        return jsonify({"message": "Record added", "id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@bp.route('/list', methods=['GET'])
def get_english():
    try:
        db = get_db()
        entries = list(db[collection_name].find())
        for entry in entries:
            entry["_id"] = str(entry["_id"])
            entry["timestamp"] = entry["timestamp"].isoformat()
        return jsonify(entries), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400