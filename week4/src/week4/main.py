"""程序入口：uv run week4 会调用这里的 main()"""

from week4.notes import create_notes, list_notes, get_note, delete_notes


def main() -> None:
    """演示笔记程序的各项功能"""
    list_notes()

    # 要试下面两个功能，先补上导入：from week4.notes import create_notes, delete_notes
    create_notes('测试', '测试时间和Id', '开发')
    # get_note('61c0c7cb-dd12-4c63-abf6-11d9b64b0386')
    # delete_notes('61c0c7cb-dd12-4c63-abf6-11d9b64b0386')


if __name__ == '__main__':
    main()
