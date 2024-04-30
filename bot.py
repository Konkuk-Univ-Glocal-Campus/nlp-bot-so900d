import random

# # This list contains the random responses (you can add your own or translate them into your own language too)
# random_responses = ["That is quite interesting, please tell me more.",
#                     "I see. Do go on.",
#                     "Why do you say that?",
#                     "Funny weather we've been having, isn't it?",
#                     "Let's change the subject.",
#                     "Did you catch the game last night?"]

# print("Hello, I am Marvin, the simple robot.")
# print("You can end this conversation at any time by typing 'bye'")
# print("After typing each answer, press 'enter'")
# print("How are you today?")

# while True:
#     # wait for the user to enter some text
#     user_input = input("> ")
#     if user_input.lower() == "bye":
#         # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
#         break
#     else:
#         response = random.choices(random_responses)[0]
#     print(response)

# print("It was nice talking to you, goodbye!")

random_responses = ["그거 참 흥미로운 주제네!!! 더 말해주라!",
                    "응응. 듣고 있어",
                    "왜 그렇게 말해...?",
                    "오늘 날씨 신기하다!! 그치?",
                    "이제 다른 얘기 해볼까?",
                    "어제 있었던 재밌는 얘기 해줘",
                    "너의 TMI를 알려줘"]

print("안녕!! 나는 Marvin이야! 아주 간단하고도 고능한 로봇이지 ㅎㅎ")
print("만약 이 대화를 그만두고 다른 할 일을 찾아 가야 한다면 '갈게'라고 입력해줘!")
print("너의 답을 입력한 뒤에 'enter'를 눌러줘")
print("밥은 먹었어?")

while True:
    user_input = input("> ")
    if user_input.lower() == "그만하자":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("대화 재밌었어!! 안녕~~!")
