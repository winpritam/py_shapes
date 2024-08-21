import os
import time

def animate_rocket():
  distance_from_top = os.get_terminal_size()[1]-11
  while True:
    win_ln = os.get_terminal_size()[1]-13
    win_c = os.get_terminal_size()[0]
    mdlPoint = int(win_c/2)-4
    print("\n" * distance_from_top)
    print(f"{' '*mdlPoint}   \033[91m^\033[0m   ")
    print(f"{' '*mdlPoint}  \033[91m/ \ \033[0m ")
    print(f"{' '*mdlPoint} \033[91m/___\ \033[0m")
    print(f"{' '*mdlPoint} \033[93m|   |\033[0m ")
    print(f"{' '*mdlPoint} \033[93m| | |\033[0m ")
    print(f"{' '*mdlPoint} \033[93m| | |\033[0m ")
    print(f"{' '*mdlPoint} \033[93m| | |\033[0m ")
    print(f"{' '*mdlPoint}\033[94m/_____\ \033[0m")
    print(f"{' '*mdlPoint}  \033[92m| |\033[0m  ")
    print(f"{' '*mdlPoint}  \033[92m| |\033[0m  ")
    print(f"{' '*mdlPoint}  \033[92m| |\033[0m  ")
    # print(os.get_terminal_size()[1])
    time.sleep(0.083)
    os.system('cls')  
    distance_from_top -= 1
    if distance_from_top <= 0:
      distance_from_top = win_ln

animate_rocket()
