from pymongo import MongoClient
from datetime import datetime

import json
from pathlib import Path

client = MongoClient('mongodb://49.235.188.214:2368')

content = Path('data.json').read_text(encoding='utf8')

db = client.learn

for name in ('test', 'phil', 'eli'):
    for i in range(10000):
        data = json.loads(content)
        data['index'] = 1
        data['date'] = datetime.now()
        result = getattr(db, name).insert_one(data)
        if i % 100 == 0:
            print(i)
