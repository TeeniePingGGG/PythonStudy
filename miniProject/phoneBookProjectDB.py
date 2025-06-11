import pymysql
conn = pymysql.connect(host='localhost', user='sample_user',
                       password='1234', db='sample_db', charset='utf8')
curs = conn.cursor()

while True:
  print("1. 입력 2.출력 3.검색 4.수정 5.삭제 6.종료")


  choiceNum = input("입력: ")

  if choiceNum == "1":

    sql = f"""insert into phonebooks(nam, phnum, adr) 
      values ('{input('이름:')}', '{input('전화번호:')}', '{input('주소:')}')"""

    curs.execute(sql)
    conn.commit()
    print("데이터가 입력됨")

  elif choiceNum == "2":
    print(f"{'출력기능':-^30}")
    sql = "select * from phonebooks"
    curs.execute(sql)
    
    rows = curs.fetchall()
    for row in rows:
        print(row[0], row[1], row[2], row[3])
        
        
  elif choiceNum == "3": 
    print(f"{'검색기능':-^30}")
    sql = "select * from phonebooks where nam like '%{0}'".format(input("검색할 이름 입력:"))
    
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        print(row[0], row[1], row[2], row[3])
        
  elif choiceNum == "4":
    print(f"{'수정기능':-^30}")
    sql = """ update phonebooks
              set nam='{1}', phnum='{2}', adr='{3}'
              where nam = '{0}'
""".format(input('수정할 이름:'), input('새로운 이름:'), input('새로운 전화번호:'), input("새로운 주소:"))

    curs.execute(sql)
    conn.commit()
    for row in rows:
        print(row[0], row[1], row[2], row[3])
    print("정보가 수정됨")
  
  elif choiceNum == "5":
    print(f"{'삭제기능':-^30}")
    iStr = input("삭제할 이름:")
    
    sql = f"delete from phonebooks where nam='{iStr}'" 
    
    curs.execute(sql)
    conn.commit()
    print("1개의 레코드가 수정됨")
    
  elif choiceNum == '6':
    print(f"{'종료합니다':-^30}")
    break
    