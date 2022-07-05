import random
book_name_list = ['海贼王','七龙珠','火影忍者','死神','噬神者',
                  '时间简史','果壳中的宇宙','青年文摘','读者',
                  '每日新闻','怪怪守护神','天龙八部','倚天屠龙记']
book_date_list = [(random.randint(1970,2019),random.randint(1,12),random.randint(1,30)) for i in range(len(book_name_list))]
book_sup = [random.randint(100,200) for i in range(len(book_name_list))]
book_com = [random.randint(100,200) for i in range(len(book_name_list))]
with open("model_obj_writer.txt","w") as f:
    model = """
book{0} = BookInfo()
book{0}.bookname = '{1}'
book{0}.bookdate = date({2},{3},{4})
book{0}.book_sup = {5}
book{0}.book_com = {6}
book{0}.save()\n\n
"""
    text = str()
    for i in range(len(book_name_list)):
        text += model.format(str(i),str(book_name_list[i]),str(book_date_list[i][0]),str(book_date_list[i][1]),str(book_date_list[i][2]),str(book_sup[i]),str(book_com[i]))
    f.write(text)
    print("OVER!!!")