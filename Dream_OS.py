import os
import sys
import time
from colorama import Fore,Back,Style
print(Fore.GREEN + Style.BRIGHT + "Dream  " +Fore.BLUE + Style.BRIGHT + "OS  " + Fore.GREEN + Style.BRIGHT +"version 1.0" + Style.RESET_ALL)
print(Fore.YELLOW + Style.BRIGHT + 'Type: \"tmoe\" to obtain more information or start the system' + Style.RESET_ALL)
print(Fore.YELLOW + Style.BRIGHT + 'If you encounter a situation where there is no response after input, it means that this program does not include this command. You can use \'pkg install --- \' to retry after version 2.0 (This version is 1.0)' + Style.RESET_ALL)
while True:
    
    abc = input(Fore.GREEN + Style.BRIGHT + "~" + Fore.YELLOW + Style.BRIGHT + "$ " + Style.RESET_ALL)
    #
    if abc.isalpha():
        if abc =="tmoe":
            print(Fore.YELLOW + Style.BRIGHT + 'Starting...    \n    Dream OS is Loading flies...' + Style.RESET_ALL)
            #Progress
            for i in range(1, 101):
              print("\r", end="")
              print(Fore.BLUE + Style.BRIGHT +"Progress: {}%: ".format(i), "▓" * (i // 2), end="" + Style.RESET_ALL )
              sys.stdout.flush()
              time.sleep(0.01)
            print("               \n                           ┌──────┤ Tmoe manager running on Android ├───────┐")
            print("                           │ 2021+patch.241011~2                            │")
            print("                           │ Command: tmoe                                  │")
            print("                           │                                                │")
            print("                           │                                                │")
            print("                           │      1  🍀 proot容器(๑•̀ㅂ•́)و✧                 │")
            print("                           │      2  🌸 chroot/unshare/systemd容器          │")
            print("                           │      3  💔 remove 移除                         │")
            print("                           │      4  🌏 区域/语言 locale/$LANG              │")
            print("                           │      5  📱 Android-win10额外选项               │")
            print("                           │      6  🌈 Configure zsh美化终端               │")
            print("                           │      7  🍧 *°▽°*update更新                    │")
            print("                           │      8  🍩 常见问题                            │")
            print("                           │      9  🐞 Report a problem(反馈问题/bug)      │")
            print(Fore.YELLOW + Style.BRIGHT +"                           │      10 修复 android 12(signal 9)              │"+ Style.RESET_ALL)
            print("                           │      0   exit 退出                             │")
            print("                           │                                                │")
            print("                           │                                                │")
            print("                           │           <Ok>               <Cancel>          │")
            print("                           │               <y>                 <n>          │")
            step1=input(Fore.YELLOW + Style.BRIGHT +"Type \'y\' or\'n\':"+ Style.RESET_ALL)
            if step1 not in ['y','n']:
                print(Fore.RED + Style.BRIGHT + "ERROR: " + Fore.YELLOW + Style.BRIGHT +"Unknown or can\'t Understand \'s command.")
            else:
                if step1 =="n":
                    print("")
                else:
                    
                    
                    print("                                                                           ")
                    print("                                                                           ")
                    print("                                                                           ")
                    print("                                                                           ")
                    print("                                                                           ")
                    print("               ┌─────────────────┤ proot容器 ├──────────────────┐")
                    print("               │ The current architecture is arm64              │")
                    print("               │ 您是想要运行arm64架构的容器,还是跨架构呢？       │")
                    print(Fore.YELLOW + Style.BRIGHT +"               │ 除向下兼容外,跨架构运行的效率可能偏低            │" + Style.RESET_ALL)
                    print("               │                                                │")
                    print("               │     1 💠 arm64发行版列表                       │")
                    print("               │     2 📑 List installed 当前已安装容器列表      │")
                    print("               │     3 ⚔️ cross-architecture 跨CPU架构          │")
                    print("               │     4 🔯 Restore 恢复/还原proot容器            │")
                    print("               │     5 📕 配置与手册                            │")
                    print("               │     0  Back to the main menu 返回主菜单      │")
                    print("               │                                                │")
                    print("               │                                                │")
                    print("               │           <Ok>               <Cancel>          │")
                    print("               │           <y>                <n>               │")
                    print("               └────────────────────────────────────────────────┘")
                    step2=input(Fore.YELLOW + Style.BRIGHT +"Type \'y\' or\'n\':"+ Style.RESET_ALL)
                    if step2 not in ['y','n']:
                        print(Fore.RED + Style.BRIGHT + "ERROR: " + Fore.YELLOW + Style.BRIGHT +"Unknown or can\'t Understand \'s command.")
                    else:
                        if step2 =="n":
                            print("")
                        else:
                            #Progress
                          for i in range(1, 101):
                              print("\r", end="")
                              print(Fore.BLUE + Style.BRIGHT +"Progress: {}%: ".format(i), "▓" * (i // 2), end="" + Style.RESET_ALL )
                              sys.stdout.flush()
                              time.sleep(0.01)
                          print(Fore.YELLOW + Style.BRIGHT +"Install success."+ Style.RESET_ALL)    
    else:
        print(Fore.RED + Style.BRIGHT + "ERROR: " + Fore.YELLOW + Style.BRIGHT +"Unknown or can\'t Understand \'s command.")
    