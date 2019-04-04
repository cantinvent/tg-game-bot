

def number_handle(message):
    n = 0
    while n==0:
        if(message.text == "+79995551122"):
            print("HANDLED")
            n = n + 1


def number(message):
    if (message.text == "+79995551122"):
        print("HANDLED")
