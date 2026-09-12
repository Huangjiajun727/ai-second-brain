class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def show(self):
        print(f'标题是{self.title}')
        print(f'内容是{self.content}')

    def update_notes(self, title: str, content: str):
        self.title = title
        self.content = content

n1 = Note('学习Python', '我今天学了很多')
n2 = Note('打游戏', '我今天完了Steam游戏')
n1.show()
n2.show()
n1.update_notes('学习AI', '我今天学了Python')
n1.show()