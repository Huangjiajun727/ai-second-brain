"""程序入口：uv run notes 会调用这里的 main()"""

import asyncio

from notes.service import create_notes1
from notes.request import root


def main() -> None:
    """演示笔记程序的各项功能"""
    # list_notes()

    # 要试下面两个功能，先补上导入：from notes.service import create_notes, delete_notes
    # create_notes('测试', '测试时间和Id', '开发')
    get_note("61c0c7cb-dd12-4c63-abf6-11d9b64b0386")
    # delete_notes('61c0c7cb-dd12-4c63-abf6-11d9b64b0386')
    # create_notes1({"title": "测试", "content": "测试字典入参", "tag": "测试"})


print(asyncio.run(root()))

if __name__ == "__main__":
    main()
