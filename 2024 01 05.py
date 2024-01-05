#建立一個叫做GAME的類別
#這邊的init建構子是用來初始化物件，讓我能夠在創建物件時可以設定它的屬性。
#這個類別有三個屬性，分別是player_name,player_id,player_skill_LV，以self為名稱

class GAME:
    def __init__ (self,player_name,player_id,player_skill_LV):

#對三個物件進行初始化
        self.name = player_name
        self.id = player_id
        self.skillLV = player_skill_LV
# 定義字串self，這樣我在創建物件時只需要輸入類別中的數值就可以回傳到第11行中，並移地11行的樣式顯示各個Player的資料
    def __str__ (self):
        return f"Name:{self.name}\nID:{self.id}\nSkill_LV:{self.skillLV}\n"
# 定義第一個副函式，可以顯示出Player的資訊
    def show_info(self):
        print(f"Player Information:\n{self}")

# 定義第二個副函式，可以讓玩家的技能等級升等
    def level_up(self):
        self.skillLV += 1
        print(f"Player {self.name} leveled up! New skill level: {self.skillLV}")

# 定義第三個副函式，讓玩家可更改姓名
    def change_name(self, new_name):
        self.name = new_name
        print(f"Player name changed to: {self.name}")

#這邊創建三個物件Player1~3，這三個物件會把三個我所輸入的三個屬性的值回傳到我定義的字串中，並以該方式顯示出來
Player1 = GAME ("NekoTaro",38107398,18)
Player2 = GAME ("DraGOD"  ,54739521,20)    
Player3 = GAME ("TK030"   ,63458752,10)


while True:
    #這邊我加入了choice，這樣我就可以依輸入的數字來方便查詢各個Player的資料，當輸入的值不符合現有的選項時，會要你再試一次
    #並且在選擇某個玩家以後，可以選擇升級技能等級或更改玩家姓名，如果沒有要執行以上動作就以選項3退出，一樣當輸入的至值不符現在的選項時，會要你再試一次
    print ("1.Player1\n")
    print ("2.Player2\n")
    print ("2.Player3\n")

    choice = input("Please enter the number to see the player's info:\n")

    if choice == "1":
        # 呼叫第一個玩家資訊
        Player1.show_info()
        # 對玩家資料執行動作的選單
        print("1.Level Up Skill\n")
        print("2.Change Name\n")
        print("3.Exit Menu\n")
        choice = input("Please enter the number to operate the Player's info:\n")

        #升級技能等級
        if choice == "1":
            Player1.level_up()
        #輸入新名字
        elif choice == "2":
            new_name = input("Enter the new name: ")
            Player1.change_name(new_name)
        #退出
        elif choice == "3":
            print("Exiting...")
            break
        #輸入錯誤時
        else:
            print ("Sorry,there was a misinput OR there was no operate option available,please try again!")



    elif choice == "2":
        # 呼叫第二個玩家資訊
        Player2.show_info()
        # 對玩家資料執行動作的選單
        print("1.Level Up Skill\n")
        print("2.Change Name\n")
        print("3.Exit Menu\n")
        choice = input("Please enter the number to operate the Player's info:\n")

        #升級技能等級
        if choice == "1":
            Player2.level_up()
        #輸入新名字
        elif choice == "2":
            new_name = input("Enter the new name: ")
            Player2.change_name(new_name)
        #退出
        elif choice == "3":
            print("Exiting...")
            break
        #輸入錯誤時
        else:
            print ("Sorry,there was a misinput OR there was no operate option available,please try again!")


    elif choice == "3":
        # 呼叫第三個玩家資訊
        Player3.show_info()
        # 對玩家資料執行動作的選單
        print("1.Level Up Skill\n")
        print("2.Change Name\n")
        print("3.Exit Menu\n")
        choice = input("Please enter the number to operate the Player's info:\n")

        #升級技能等級
        if choice == "1":
            Player3.level_up()
        #輸入新名字
        elif choice == "2":
            new_name = input("Enter the new name: ")
            Player3.change_name(new_name)
        #退出           
        elif choice == "3":
            print("Exiting...")
            break
        #輸入錯誤時
        else:
            print ("Sorry,there was a misinput OR there was no operate option available,please try again!")

    #當沒有玩家資訊或輸入錯誤時
    else: 
        print ("Sorry,there was a misinput OR there is no info of this player,please try again!")
