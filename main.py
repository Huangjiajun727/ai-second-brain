notes = [
    {
        "id": 1,
        "title": "Python",
        "content": "学习 Python 基础语法",
        "tag": "programming"
    },
    {
        "id": 2,
        "title": "Vue",
        "content": "学习 Vue 3",
        "tag": "frontend"
    },
    {
        "id": 3,
        "title": "FastAPI",
        "content": "学习 Python Web 后端",
        "tag": "backend"
    },
    {
        "id": 4,
        "title": "AI学习",
        "content": "从0开始的转ai从0开始的转ai从0开始的转ai",
        "tag": "programming"
    }
];

#查看全部笔记
def list_notes():
    """查看全部笔记"""
    for item in notes:
        print(f"标题是：{item['title']}，内容是{item['content']}，标签是{item['tag']}");

#根据id查看一条笔记
def get_notes(note_id):
    """根据id查看一条笔记"""
    for item in notes:
        if item['id'] == note_id:
            print(item);
            break;

#创建一条笔记，id的新增删除某项后不可靠
def create_notes(title, content, tag):
    """创建一条笔记"""
    id = len(notes) + 1;
    notes.append({
        'title': title,
        'content': content,
        'tag': tag,
        'id': id
    });

#删除笔记
def delete_notes(note_id):
    """删除笔记"""
    for item in notes:
        if item['id'] == note_id:
            notes.remove(item);
            break;

#按标题或内容搜索 如果用match会更优雅
def search_notes(keyword):
    """按标题或内容搜索"""
    data = [];
    for item in notes:
        title = item['title'];
        content = item['content'];
        tag = item['tag'];
        if keyword in title:
            data.append(item);
            continue;
        if keyword in content:
            data.append(item);
            continue;
        if keyword in tag:
            data.append(item);
            continue;
    return data;

#按标题或内容搜索 match写法
def search_notes1(keyword):
    """按标题或内容搜索 match写法"""
    data = [];
    for item in notes:
        match item:
            case {'title': title} if keyword in title:
                data.append(item);
            case {'content': content} if keyword in content:
                data.append(item);
            case {'tag': tag} if keyword in tag:
                data.append(item);
            case _:
                pass;
    return data;


#统计当前有多少篇笔记
def count_notes():
    print(f'目前共有{len(notes)}篇笔记');

#统计某个标签有多少篇笔记
def count_by_tag(tag):
    data = [item for item in notes if tag in item['tag']];
    print(f'{tag}标签当前共有{len(data)}篇笔记');

#找出所有出现过的标签并去重
def list_tags():
    data = [item['tag'] for item in notes];
    return set(data);

#找到内容最长的一篇笔记
def get_longest_note():
    data = notes[0];
    for item in notes:
        if len(item['content']) > len(data['content']):
            data = item;
    print(data);

#精确按照 tag 筛选笔记
def get_notes_by_tag(tag):
    data = [item for item in notes if tag == item['tag']];
    if len(data) > 0:
        print(data);
    else:
        print('没有找到该标签笔记');