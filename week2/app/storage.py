import json

#加载json文件
def load_notes() -> dict:
    """加载json文件"""
    with open('./week2/notes.json', 'r', encoding='utf-8') as f:
        notes = json.load(f)
        print(notes)
    return notes

#写入json文件
def save_notes(data: dict) -> None:
    """写入json文件"""
    with open('./week2/notes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f);