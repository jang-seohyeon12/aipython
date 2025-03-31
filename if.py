def print_character(character_number):
    if character_number == 1:
        # 하츄핑
        print("""
         (\^.^/)
        (  -  -  )
         (  =^=  )
        /'`   `'\ 
        """)
        
    elif character_number == 2:
        # 고양이
        print("""
         /\_/\  
        ( o.o ) 
         > ^ <
        """)
        
    elif character_number == 3:
        # 강아지
        print("""
         / \__
        (    @\___
        /         O
       /   (_____ /
      /_____/   U
        """)
        
    else:
        print("잘못된 번호입니다. 1, 2, 3번 중 하나를 입력해주세요.")

# 캐릭터 선택
character_number = int(input("캐릭터 번호를 입력하세요 (1: 하츄핑, 2: 고양이, 3: 강아지): "))
print_character(character_number)