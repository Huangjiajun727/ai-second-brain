from storage import load_notes,save_notes

notes = load_notes()

#查看全部笔记
def list_notes() -> None:
    """查看全部笔记"""
    try:
        if notes:
                for item in notes:
                    print(f"标题是：{item['title']}，内容是{item['content']}，标签是{item['tag']}");
        else:
                raise Exception('当前暂无笔记');
    except Exception as error:
        print(error);
    
#根据id查看一条笔记
def get_note(note_id: int) -> None:
    """根据id查看一条笔记"""
    try:
        for item in notes:
            if item['id'] == note_id:
                print(item);
                break;
        else:
            raise Exception('未查询到该笔记！');
    except Exception as error:
        print(error);

#处理创建笔记入参校验
def handle_params(title: str, content: str, tag: str) -> None:
    """处理创建笔记入参校验"""
    error_arr = [];
    if not isinstance(title, str):
        error_arr.append(ValueError('笔记标题必须是字符串'))
    if not isinstance(content, str):
        error_arr.append(ValueError('笔记内容必须是字符串'))
    if not isinstance(tag, str):
        error_arr.append(ValueError('笔记标签必须是字符串'))
    if error_arr:
        raise ExceptionGroup('批量笔记入参传入错误', error_arr);
       

#创建一条笔记，id的新增删除某项后不可靠
def create_notes(title: str, content: str, tag: str) -> None:
    """创建一条笔记"""
    try:
        handle_params(title, content, tag);
        new_id = len(notes) + 1;
        notes.append({
            'title': title,
            'content': content,
            'tag': tag,
            'id': new_id
        });
        save_notes(notes);

        print('笔记创建成功！');
    except* ValueError as error:
        for item in error.exceptions:
            print(item);

#删除笔记
def delete_notes(note_id: int) -> None:
    """删除笔记"""
    try:
        for item in notes:
            if item['id'] == note_id:
                notes.remove(item);
                save_notes(notes);
                print('删除成功！')
                break;
        else:
            raise Exception('笔记不存在，无法删除');
    except Exception as error:
        print(error);


#按标题或内容搜索 如果用match会更优雅
def search_notes(keyword: str) -> list:
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