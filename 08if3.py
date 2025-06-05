'''
퀴즈1] 국,영,수 점수를 입력받아 평균값을 구하고 이를 통해 학점을 출력하는 
    프로그램을 작성하시오. 
    90점 이상은 A학점 
    80점 이상은 B학점
    70점 이상은 C학점
    60점 이상은 D학점    
    60점 미만은 F학점으로 판단하여 출력합니다. 
'''
num1 = int(input("국어 점수:"))
num2 = int(input("영어 점수:"))
num3 = int(input("수학 점수:"))

avg = (num1+num2+num3) / 3

if avg >= 90:
  print("A학점")
elif avg >= 80:
  print('B학점')
elif avg >= 70:
  print('C학점')
elif avg >= 60:
  print('D학점')
else:
  print("F학점")
  
print("평균점수는: ",avg)
  
'''
퀴즈2] 아이디를 먼저 입력받은 후 user_info 리스트에 등록되었다면 
패스워드를 입력받아 일치하는지 확인하는 프로그램을 작성하시오. 
여기서 패스워드는 1234로 가정합니다. 
'''
idList = ["aaa","bbb","cc"]  
id_input = input("아이디를 입력하세요:")

if id_input in idList:
  print("아이디 목록에 있습니다")
  pw_input = input("비밀번호를 입력하세요")
  if pw_input=="1234":
    print("일치합니다")
  else:
    print("일치하지않습니다.")
else:
  print("아이디목록에 없습니다")
    



