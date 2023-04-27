import os

# PROPERTY NAME
PROPERTY_MENU_NAME = "menu_name"
PROPERTY_HANDLER = "handler"
PROPERTY_PATH = "path"
PROPERTY_STORY_NAME = "story_name"
PATH_STORY = 'story'

# MENU STATES
is_shutdown = False
menu_main = {}
view_story = {}
bookmark_list = {}


# MENU FUNCTION
def append_menu(menu_set, menu_name, handler):
    menu_set[str(len(menu_set.keys()) + 1)] = {PROPERTY_MENU_NAME: menu_name, PROPERTY_HANDLER: handler}


def exit_menu():
    global is_shutdown
    is_shutdown = True


def print_menu(menu):
    menu_numbers = list(menu.keys())
    for menu_number in menu_numbers:
        print(f"[{menu_number}] {menu[menu_number][PROPERTY_MENU_NAME]}")


def append_story(story_set, story_name, path):
    story_set[str(len(story_set.keys()) + 1)] = {PROPERTY_STORY_NAME: story_name, PROPERTY_PATH: path}


def load_stories(path):
    global view_story
    for file_name in os.listdir(path):
        append_story(view_story, os.path.splitext(file_name)[0], f"{path}/{file_name}")


def print_story():
    global view_story
    story_numbers = list(view_story.keys())
    for story_number in story_numbers:
        print(f"[{story_number}] {view_story[story_number][PROPERTY_STORY_NAME]}")


def check_story_selection(story_selection):
    global view_story
    return story_selection in view_story


def get_story(story_selection):
    global view_story
    return view_story[story_selection]


def select_story():
    story_selection = input("보고싶은 스토리 번호를 입력하세요 : ")

    if check_story_selection(story_selection) is False:
        print("없는 스토리를 고르셨어요")
        return

    selected_story = get_story(story_selection)
    print(f"{story_selection}번 이야기 \"{selected_story[PROPERTY_STORY_NAME]}\"를 읽기 시작합니다")
    with open(selected_story[PROPERTY_PATH], 'r', encoding='utf-8') as file:
        story_text = file.read()
    print(story_text)


def print_book_mark():
    print(bookmark_list)


def append_book_mark():
    bookmark = input("북마크바에 추가할 이야기를 입력하세요=>")

    if check_story_selection(bookmark) is False:
        print("없는 스토리를 고르셨어요")
        return

    bookmark_list[bookmark] = get_story(bookmark)


def remove_book_mark():
    print(bookmark_list)
    idx = input("북마크바에서 삭제할 여행지 인덱스 번호를 입력하세요")

    if idx not in bookmark_list:
        print("없는 북마크를 고르셨어요")
        return

    bookmark = bookmark_list[idx]
    del bookmark_list[idx]
    print(f"{bookmark[PROPERTY_STORY_NAME]} 이야기가 삭제되었습니다. 북마크 목록=>{bookmark_list}")


# LOAD STORY
load_stories(PATH_STORY)

# APPEND MENU
append_menu(menu_main, "무서운이야기 목록 출력", print_story)
append_menu(menu_main, "무서운이야기 읽기", select_story)
append_menu(menu_main, "무서운이야기 북마크 목록 출력", print_book_mark)
append_menu(menu_main, "무서운이야기 북마크 추가", append_book_mark)
append_menu(menu_main, "무서운이야기 북마크 삭제", remove_book_mark)
append_menu(menu_main, "종료하기", exit_menu)

while True:
    if is_shutdown:
        break

    print("_" * 50)
    print("무서운이야기 컬렉션 모음집")
    print("_" * 50)
    print_menu(menu_main)

    menu_selection = input("메뉴번호를 입력하세요 : ")

    if menu_selection not in menu_main:
        print("없는 메뉴를 선택하셨습니다")
        continue

    menu_main[menu_selection][PROPERTY_HANDLER]()

print("종료합니다")
