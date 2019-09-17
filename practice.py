import random
import string
import os
from zhon import hanzi


TEXTS = ["磨杵作针", "精卫填海", "刻舟求剑", "自相矛盾", "揠苗助长",
        "守株待兔", "伯乐相马", "画蛇添足"]
TEXT_PATH = "texts/"


def list_texts(texts):
    print("课文如下：")
    print("\t0 - ［随机］")
    for i in range(len(TEXTS)):
        print("\t%d - %s" % (i+1, TEXTS[i]))

    pass


def get_selection():
    while True:
        selection = input("请您选择一篇课文：")
        if any(char not in string.digits for char in selection):
            print("请您输入数码")
        elif int(selection) >= len(TEXTS) or int(selection) < 0:
            print("请您输入以上选择之内的数码")  # TODO: fix this Chinese
        else:
            return int(selection)


def load_text(text_index):
    text_file = open(os.path.join(TEXT_PATH, TEXTS[text_index]), 'r')
    return text_file.read()


def break_text(text):
    breaks = [0]
    break_mode = False
    for i in range(len(text)):
        if text[i] in hanzi.punctuation:
            break_mode = True
        elif break_mode == True:
            break_mode = False
            breaks.append(i)
    return breaks


def display(message, *args, **kwargs):
    user_in = input(message, *args, **kwargs).lower()
    print(message, end='')
    os.system('read -n 1') # TODO: worry about portability


while True:
    try:
        list_texts(TEXTS)
        text_index = get_selection()
        if text_index == 0:
            text_index = random.randrange(len(TEXTS))
        text_number = text_index+1
        text = load_text(text_index)
        breaks = break_text(text)
        display("课文号：%d" % (text_number,))
        for i in range(len(breaks)-1):
            display(text[breaks[i]:breaks[i+1]])

    except KeyboardInterrupt:
        break
print("再见")
