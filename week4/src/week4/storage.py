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

# 数据文件定位：以本文件位置为基准向上回溯到项目根（week4/）。
# 不能再用 './week4/notes.json' 这种相对路径——它依赖「当前工作目录」，
# 一旦换目录启动（比如 uv run week4）就会找不到文件。
# parents[0]=src/week4  parents[1]=src  parents[2]=week4
PROJECT_ROOT = Path(__file__).resolve().parents[2]
NOTES_FILE = PROJECT_ROOT / 'notes.json'


#加载json文件
def load_notes() -> list:
    """加载json文件"""
    try:
        logger.info('加载json文件')
        print(f'{NOTES_FILE} {NOTES_FILE.name} {NOTES_FILE.parent} {NOTES_FILE.suffix}')
        with NOTES_FILE.open('r', encoding='utf-8') as f:
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
        # ensure_ascii=False 让中文原样写入，indent=2 便于人眼查看
        with NOTES_FILE.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info('写入完成')
    except OSError as error:
        logger.error('写入文件出错')
        print(error)
    except json.JSONDecodeError as error:
        logger.error('json文件出错')
        print(error)
