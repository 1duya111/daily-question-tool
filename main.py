import random
import datetime
questions = [
    "你这周做过最正确的决定是什么？",  
    "你最近在玩什么游戏？",
    "最近有么有发现好吃的外卖？",
    "截至目前你是否实现了自己一个小小的目标？",
    "爱吃甜的还是辣的？"
]

while True:
    print("\n==== 每日一问小工具 ====")
    print("1. 抽取问题并回答")
    print("2. 查看所有历史记录")
    print("3. 退出程序")
    choice = input("请选择操作 (输入数字 1-3): ")
    if choice == "1":
     current_questions = random.choice(questions)
     answer = input(current_questions +"\n我的回答：")   #先输出问题，再回答，再输出回答
     today = datetime.date.today()
     with open("my_answers.txt", "a", encoding="utf-8") as f:
            f.write(f"[{today}] 问题：{current_questions}\n")
            f.write(f"回答：{answer}\n")
            f.write("-------------------\n")
            print("✅ 回答已保存！")
     
    elif choice == "2":
       print("\n==== 历史记录 ====")
       try:                  #“我接下来要做一件事，但这事儿有可能会搞砸，我先试试看。”
            # "r" 表示 read（只读模式）
            with open("my_answers.txt", "r", encoding="utf-8") as f:   #把日记拿出来读一下再放回去
                print(f.read())          #读出来
       except FileNotFoundError:
            # 如果文件还没生成（第一次用），就提示一下，不要报错崩溃
            print("你还没有回答过任何问题哦！")
    elif choice == "3":
         print("👋 再见！下次再来记一笔。")
         break
    else :
        print("⚠️ 无效输入，请重新输入 1、2 或 3。")
