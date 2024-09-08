from flask import Blueprint, jsonify, request
from .models import db, Message
import datetime

main_bp = Blueprint('main', __name__)  # No URL prefix here, routes are at the root level

@main_bp.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([{
        'id': m.id, 'content': m.content, 'timestamp': m.timestamp, 'author': m.author
    } for m in messages])

@main_bp.route('/add_message', methods=['POST'])
def add_message():
    data = request.get_json()
    message = Message(content=data['content'], timestamp=datetime.datetime.utcnow(), author=data['author'])
    db.session.add(message)
    db.session.commit()
    return jsonify({'status': 'Message added!'})
    
@main_bp.route('/', methods=['GET'])
def index():
    return "Welcome to the Discord API"
