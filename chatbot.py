import aiml
# Đối tượng Kernel là giao diện công khai với 
# trình thông dịch AIML
Bot= aiml.Kernel()
# Sử dụng phương thức 'learn' để tải 
# nội dung của tệp AIML vào Kernel
Bot.learn("std-startup.xml")
# Sử dụng phương thức 'respond' để tính toán phản hồi
# vào chuỗi đầu vào của người dùng. response () trả lại 
# câu trả lời của thông dịch viên, trong trường hợp này 
Bot.respond("load aiml b")


# Vòng lặp vô hạn, đọc đầu vào của người dùng từ dòng lệnh 
# và in phản hồi. 
while True:
    #  print( kernel.respond(input("Human >> ")))
    message=input(">Human: ")
    if message== "exit" :
        exit()
    else:
        response=Bot.respond(message)
        print(">Bot: "+response)