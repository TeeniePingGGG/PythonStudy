data_list = []

while True:
    print(" 1.입력 2.출력 3.검색 4.수정 5.삭제 6. 종료")
    choiceNum = input("선택: ")

    if choiceNum == '1':
        namee = input("성명: ")
        phnum = input("전화: ")
        adr = input("주소: ")

        person = {'이름': namee, '전화': phnum, '주소': adr}
        data_list.append(person)

        print("주소입력완료!\n")

    elif choiceNum == '2':
        print(f"{'출력기능':-^30}")
        if not data_list:
            print("저장된 데이터가 없습니다.\n")
        else:
            for p in range(len(data_list)):
                print(f"이름: {data_list[p]['이름']}")
                print(f"전화: {data_list[p]['전화']}")
                print(f"주소: {data_list[p]['주소']}")
                
                print()
                
    elif choiceNum == '3':
        print(f"{'검색기능':-^30}")
        searName = input("이름을 입력해주세요")
    
        for person in data_list:
            if person['이름'] == searName:
                print(f"이름:{person['이름']}")
                print(f"전화:{person['전화']}")
                print(f"주소:{person['주소']}")
                
    elif choiceNum == '4':
        print(f"{'수정기능':-^30}")
        
        edName = input("수정할 성명을 입력하세요:")
        
        for person in data_list:
            if person['이름'] == edName:
                print("수정할 이름, 연락처, 주소를 입력하세요")
                
                newName = input("새로운 이름:")
                newPhnum = input("새로운 전화번호:")
                newAdr = input("새로운 주소")
                
                person['이름'] = newName
                person['전화번호'] = newPhnum
                person['주소'] = newAdr
                
                print("연락처가 수정되었습니다.")
    
    elif choiceNum == '5':
        print(f"{'삭제기능':-^30}")
        
        delName = input("삭제할 성명을 입력하세요")
         
        found = False
           
        for person in data_list:
            if person['이름'] == delName:
                data_list.remove(person)
                found = True
                
                print("정보가 삭제되었습니다")
        
        if not found:
            print("일치하는 정보 없음")
    
    elif choiceNum == '6':
        print(f"{'종료합니다':-^30}")
        break
    
        
            
                    
            
        
       
        
        
        


        
        