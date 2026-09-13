import json

#加载json文件
def load_notes() -> list:
    """加载json文件"""
    try:
        with open('./week2/notes.json', 'r', encoding='utf-8') as f:
            notes = json.load(f)
            print(notes)
        return notes
    except OSError as error:
        print(error)

        return []
    except json.JSONDecodeError as error:
        print(error)

        return []

#写入json文件
def save_notes(data: dict) -> None:
    """写入json文件"""
    try:
        with open('./week2/notes.json', 'w', encoding='utf-8') as f:
            json.dump(data, f);
    except OSError as error:
        print(error)
    except json.JSONDecodeError as error:
        print(error)