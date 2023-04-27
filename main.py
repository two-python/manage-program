import importlib
import os
import subprocess

from gtts import gTTS
from playsound import playsound

try:
    importlib.import_module('PyObjC')
except ImportError:
    subprocess.run(['pip3', 'install', 'PyObjC'])
try:
    importlib.import_module('gTTS')
except ImportError:
    subprocess.run(['pip3', 'install', 'gTTS'])
try:
    importlib.import_module('playsound')
except ImportError:
    subprocess.run(['pip3', 'install', 'playsound'])

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

# SPEED STATES
# ex) .gTTS(text, lang='ko', slow=isSlow) 
isSlow = False


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
    title_text = f"{story_selection}번 이야기 \"{selected_story[PROPERTY_STORY_NAME]}\"를 읽기 시작합니다"

    print(title_text)

    sp = gTTS(text=title_text, lang="ko", tld="co.kr", slow=isSlow)
    sp.save('title.mp3')
    playsound('title.mp3')
    os.remove('title.mp3')
    read_story(selected_story)


def read_story(story_selection):
    file_index = ""
    with open(story_selection[PROPERTY_PATH], 'r') as file:
        file_index = file.read()

    print("-" * 50)
    print(file_index)

    sp = gTTS(text=file_index, lang="ko", tld="co.kr", slow=isSlow)
    sp.save('story.mp3')
    playsound('story.mp3')
    os.remove('story.mp3')


def modify_setting():
    global isSlow
    answer = ""
    if isSlow:
        answer = input("현재 속도는 느립니다. 빠르게 설정하시겠습니까? (Y/N) : ")
    else:
        answer = input("현재 속도는 빠릅니다. 느리게 설정하시겠습니까? (Y/N) : ")
    isSlow = not isSlow if answer.upper() == "Y" else isSlow


# LOAD STORY
load_stories(PATH_STORY)

# APPEND MENU
append_menu(menu_main, "무서운이야기 목록 출력", print_story)
append_menu(menu_main, "무서운이야기 읽기", select_story)
# append_menu(menu_main, "무서운이야기 북마크 목록 출력", print_book_mark)
# append_menu(menu_main, "무서운이야기 북마크 추가", append_book_mark)
# append_menu(menu_main, "무서운이야기 북마크 삭제", remove_book_mark)
append_menu(menu_main, "속도 설정하기", modify_setting)
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
