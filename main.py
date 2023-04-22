menu = 0

travel_list = []

while menu != 4: 
    print("_"*50)
    print("여행장소 관리 프로그램")
    print("_"*50)
    print("1. 여행장소 목록 출력")
    print("2. 여행장소 추가")
    print("3. 여행장소 삭제")
    print("4. 종료하기")
    
    menu = int(input("메뉴를 선택하시오=>"))

    if menu == 1:
        print (travel_list)
    elif menu == 2:
        place = input("추가할 여행지를 입력하세요=>")
        travel_list.append(place)
    elif menu == 3:
        print(travel_list)
        idx = int(input("삭제할 여행지 인덱스 번호를 입력하세요"))
        place = travel_list[idx]
        del travel_list[idx]
        print(f"[place) 여행지가 삭제되었습니다. 여행지 목록=>{travel_list}")
    else:
        print("종료합니다")
