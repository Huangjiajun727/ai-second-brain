import json
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)
logger = logging.getLogger('storage.py')



#加载json文件
def load_notes() -> list:
    """加载json文件"""
    try:
        logger.info('加载json文件')
        p = Path('./week3/notes.json')
        print(f'{p} {p.name} {p.parent} {p.suffix}')
        with open('./week3/notes.json', 'r', encoding='utf-8') as f:
            notes = json.load(f)
            print(notes)
        logger.info('结束加载json文件')
        return notes
    except OSError as error:
        logger.error('加载json文件出错')
        print(error)

        return []
    except json.JSONDecodeError as error:
        logger.error('json文件出错')
        print(error)

        return []

#写入json文件
def save_notes(data: dict) -> None:
    """写入json文件"""
    try:
        logger.info('准备写入Json')
        with open('./week3/notes.json', 'w', encoding='utf-8') as f:
            json.dump(data, f);
        logger.info('写入完成')
    except OSError as error:
        logger.error('写入文件出错')
        print(error)
    except json.JSONDecodeError as error:
        logger.error('json文件出错')
        print(error)