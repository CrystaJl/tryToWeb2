import random
import json

def generate_data():
    data = []
    for i in range(10):
        data.append({
            'label': f'Data {i}',
            'values': [random.randint(0, 100) for _ in range(10)],
            'color': f'#{random.randint(0, 0xFFFFFF):06x}'
        })
    return data

# Generate data
data = generate_data()

# Convert data to JSON format
json_data = json.dumps(data)

# Save data to a file
with open('static/data.json', 'w') as file:
    file.write(json_data)
