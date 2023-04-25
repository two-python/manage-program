menu = 0

bookmark_list = []

while menu != 4: 
    print("_"*50)
    print("무서운 이야 프로그램")
    print("_"*50)
    print("1. 북마크 목록 출력")
    print("2. 북마크 추가")
    print("3. 북마크바 삭제")
    print("4. 종료하기")
    
    menu = int(input("메뉴를 선택하시오=>"))

    if menu == 1:
        print (bookmark_list)
    elif menu == 2:
        bookmark = input("북마크바에 추가할 이야기를 입력하세요=>")
        bookmark_list.append(bookmark)
    elif menu == 3:
        print(bookmark_list)
        idx = int(input("북마크바에서 삭제할 여행지 인덱스 번호를 입력하세요"))
        bookmark = bookmark_list[idx]
        del bookmark_list[idx]
        print(f"{bookmark} 이야기가 삭제되었습니다. 북마크 목록=>{bookmark_list}")
    else:
        print("종료합니다")
