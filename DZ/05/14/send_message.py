messag=["Привет","Как дела?","как нустроение"]
messags=[]
def send_message(mess):
    while mess:
        count= mess.pop()  
        messags.append(count)   

send_message(messag[:])
print( "True" if messag else "false")

def shoy_message(mess):
    for mes in mess:
        print(mes)
print(messag)    
shoy_message(messags)