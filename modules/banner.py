from colorama import Fore,Back,Style
import platform,os

OsName = platform.uname()[0]

def banner():
    if OsName == "Windows":
      os.system("cls")
    else:
      os.system("clear")
    print(Fore.LIGHTWHITE_EX+"       ====   ||   ||  ||=====      //\\      ```||``` ")   
    print(Fore.LIGHTWHITE_EX+"      ||      ||   ||  ||    ||    //  \\        ||    ")  
    print(Fore.LIGHTWHITE_EX+"       ====   ||   ||  ||====||   //    \\       ||    ")
    print(Fore.LIGHTWHITE_EX+"          ||  ||   ||  || \\      //======\\  ||  ||    ")
    print(Fore.LIGHTWHITE_EX+"       ====    =====   ||  \\    //        \\ ||==||    ")
    print(Fore.CYAN+"==============================================================================")
    
    
    print(Fore.CYAN+"||\\  || ||``||    ||``  ||``|| ||\\  || ``||`` ||```|| ||``|| ||  " )
    print(Fore.CYAN+"|| \\ || ||  || __ ||    ||  || || \\ ||   ||   ||===|| ||  || ||  " )
    print(Fore.CYAN+"||  \\|| ||__||    ||__  ||__|| ||  \\||   ||   || \\    ||__|| ||==" )
    print(Style.RESET_ALL)

banner()
