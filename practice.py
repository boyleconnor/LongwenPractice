import random
import string
import os
import curses
from zhon import hanzi


TEXTS = ["磨杵作针", "精卫填海", "刻舟求剑", "自相矛盾", "揠苗助长",
        "守株待兔", "伯乐相马", "画蛇添足", "苏秦之楚", "塞翁失马",
        "朝三暮四", "鹬蚌相争，渔人得利", "涸辙之鲋", "狐假虎威", "南辕北辙",
        "以己度人", "齐桓公为大臣具酒", "望洋兴叹", "愚公移山"]
TEXT_PATH = "texts/"
ENTER_KEY = 10  # The code for the Enter key in 


def list_texts(texts, stdscr):
    stdscr.addstr("\n课文如下：\n")
    stdscr.addstr("\t0 - ［随机］\n")
    for i in range(len(TEXTS)):
        stdscr.addstr("\t%d - %s\n" % (i+1, TEXTS[i]))


def get_selection(stdscr):
    while True:
        stdscr.addstr("请您选择一篇课文：")
        stdscr.refresh()
        curses.echo()
        selection = ''
        while True:
            c = stdscr.getkey()
            if c == '\n':
                break
            else:
                selection += c
        curses.noecho()
        if any(char not in string.digits for char in selection):
            stdscr.addstr("请您输入数码\n")
            stdscr.refresh()
        elif not (0 <= int(selection) <= len(TEXTS)):
            stdscr.addstr("请您输入以上选择之内的数码\n")  # TODO: fix this Chinese
            stdscr.refresh()
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


def main(stdscr):
    while True:
        try:
            list_texts(TEXTS, stdscr)
            text_number = get_selection(stdscr)
            if text_number == 0:
                text_index = random.randrange(len(TEXTS))
                text_number = text_index+1
            text_index = text_number-1
            text = load_text(text_index)
            breaks = break_text(text)
            stdscr.addstr("课文号：%d\n" % (text_number,))
            stdscr.refresh()
            stdscr.getch()
            stdscr.addstr("课题：%s\n" % (TEXTS[text_index],))
            stdscr.refresh()
            for i in range(len(breaks)-1):
                stdscr.getch()
                stdscr.addstr(text[breaks[i]:breaks[i+1]])
                stdscr.refresh()
        except KeyboardInterrupt:
            break
    stdscr.addstr("再见")


curses.wrapper(main)
