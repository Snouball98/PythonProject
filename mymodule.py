

class Character:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"제 이름은 {self.name}입니다.")


print(f"mymodule안에서의 __name__: {__name__}")


if __name__ == "__main__" :
    wizard = Character("법사")
    wizard.speak()


#클래스가 잘 동작하는지 확인하시려면 아래의 두 코드의 주석을 해제하고 실행시켜주세요.
#wizard = Character("법사")
#wizard.speak()



#if __name__ == "__main__":
#    print (my_add(1,2))
#    print (my_sub(3,4))


