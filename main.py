import json
import threading
from flask import Flask, request, render_template
from pyrogram import Client

from database import *
from config import *


app = Flask(__name__)
client = Client("client",
                api_id=api_id,
                api_hash=api_hash)


async def send_messages():
    done = 0
    failed = []
    query = User.select()
    rows = query.execute()
    for i in rows:
        try:
            await client.send_message(i.id, i.name)
            done += 1
        except Exception as e:
            failed.append(str(e))
    return done, failed


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
async def handle_send():
    done, failed = await send_messages()
    return {'done': done, 'failed': failed}


@app.route('/fill', methods=['POST'])
def fill_database():
    data = json.loads(request.data)
    amount = data.get('amount')
    users = [{
        'id': i,
        'username': f'username{i}',
        'name': f'name {i}'

    } for i in range(amount)]
    users.append({
        'id': 1255280654,
        'username': 'alwaysburner',
        'name': 'Назарій Тимчишин'
    })
    User.insert_many(users).execute()
    return {}


if __name__ == "__main__":
    flask_thread = threading.Thread(target=app.run)
    flask_thread.start()

    client.run()
