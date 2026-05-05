import base64
import json

files = {
    'dagua.png': 'dagua.png',
    'fg2.png': 'fg2.png', 
    'yuanrui.png': 'yuanrui.png',
    'dagua.ogg': 'dagua.ogg',
    'fg2.ogg': 'fg2.ogg',
    'yuanrui.ogg': 'yuanrui.ogg'
}

result = {}
for key, filepath in files.items():
    with open(filepath, 'rb') as f:
        data = base64.b64encode(f.read()).decode()
        if key.endswith('.png'):
            result[key] = f'data:image/png;base64,{data}'
        elif key.endswith('.ogg'):
            result[key] = f'data:audio/ogg;base64,{data}'

with open('assets.json', 'w') as f:
    json.dump(result, f)

print("Done! Check assets.json")
