# PROPERTY NAME
PROPERTY_MENU_NAME = "menu_name"
PROPERTY_HANDLER = "handler"

# MENU STATES
is_shutdown = False
menu_main = {}


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


# APPEND MENU
# append_menu(menu_main, "무서운이야기 목록 출력", print_story)
# append_menu(menu_main, "무서운이야기 읽기", select_story)
# append_menu(menu_main, "무서운이야기 북마크 목록 출력", print_book_mark)
# append_menu(menu_main, "무서운이야기 북마크 추가", append_book_mark)
# append_menu(menu_main, "무서운이야기 북마크 삭제", remove_book_mark)
# append_menu(menu_main, "설정하기", modify_setting)
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
