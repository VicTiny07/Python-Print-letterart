#please extend the console tab completely to enjoy the whole experience and see all the letter arts.

from colorama import Fore, Back
import time
import random
import pyfiglet
import sys

code_number = random.randint(1000, 9999)
count = 3

result = pyfiglet.figlet_format("Hello", font="3-d")
print(result)
print()
print(Fore.LIGHTBLUE_EX + "Welcome to the secret data base. This is MARK V",
      end="\n\n")
time.sleep(1.5)

print(Fore.YELLOW + "        _______")
print("      _/       \_")
print("     / |       | \  "
      "")
print("    /   __   __   \ "
      "")
print("   |__/((o| |o))\__|")
print("   |      | |      |")
print("   |\     |_|     /|")
print("   | \           / |")
print("    \| /  ___  \ |/")
print("     \ | / _ \ | /")
print("      \_________/")
print("       _|_____|_")
print("  ____|_________|____")
print(" /                   \ ")

time.sleep(1.5)

print("Please verify your self before starting")
time.sleep(1)
print()


def verification():
  code = "WIBYTE"
  userinput = input("Type in the following-WIBYTE : ")

  if userinput == code:
    print("Verification successful.")

  else:
    print("Verification failed. Access denied.")
    sys.exit()


verification()

time.sleep(1)
print()

USER = input(Fore.CYAN + "May I know who is accessing this?(ɹno⅄ ǝɯɐи )\n")

print(Fore.GREEN, USER, "-Agent detected. Welcome back.\n")
time.sleep(2)

Camera_Permission = 0
Camera_Permission = input(Fore.LIGHTYELLOW_EX +
                          "Allow the camera to scan your eyes (Yes/No): ")

if Camera_Permission.lower() == "yes":
  print("Access enabled")

elif Camera_Permission.lower() == "no":
  print("Access denied")
  sys.exit()
else:
  print("Invalid input")
  sys.exit()

time.sleep(1.5)

print()

print("Iris scanning now taking place...")

time.sleep(3)
print()
print()

print(
  Fore.WHITE +
  "          _,.--~=~\"~=~--.._                        _,.--~=~\"~=~--.._  ")
print(
  "      _.-\"  / \\ !   ! / \\ .                   _.-\"  / \\ !   ! / \\ .      "
)
print(
  "    ,\"     / ,` .---. `, \\    \            ,\"     / ,` .---. `, \\    \ "
)
print(
  "  .'   `~  |   /:::::\   |  ~`   '.         .'   `~  |   /:::::\   |  ~`   '.   "
)
print(
  "   `.  `~   |   \:::::/   | ~`  ~ .'         `.  `~   |   \:::::/   | ~`  ~ .' "
)
print(
  "     `.  `~ \ `, `~~~' ,` /   ~`.'             `.  `~ \ `, `~~~' ,` /   ~`.'  "
)
print(
  "       \"-._  \\ / !   ! \\ /  _.-\"             \"-._  \\ / !   ! \\ /  _.-\ "
)
print(
  "         \".__._~~-_._, ~~_.__\"                     \".__._~~-_._, ~~_.__\" "
)

print()
print()


def loading():
  animation = ["◐", "◓", "◑", "◒"]
  for _ in range(12):
    print("Loading", animation[0], end="\r")
    time.sleep(0.5)
    animation = animation[1:] + [animation[0]]


loading()
print(Back.CYAN + "S", end="\r")
time.sleep(0.1)
print("Sc", end="\r")
time.sleep(0.1)
print("Sca", end="\r")
time.sleep(0.1)
print("Scan", end="\r")
time.sleep(0.1)
print("Scann", end="\r")
time.sleep(0.1)
print("Scanni", end="\r")
time.sleep(0.1)
print("Scannin", end="\r")
time.sleep(0.1)
print("Scanning", end="\r")
time.sleep(0.1)
print("Scanning ", end="\r")
time.sleep(0.1)
print("Scanning c", end="\r")
time.sleep(0.1)
print("Scanning co", end="\r")
time.sleep(0.1)
print("Scanning com", end="\r")
time.sleep(0.1)
print("Scanning comp", end="\r")
time.sleep(0.1)
print("Scanning compl", end="\r")
time.sleep(0.1)
print("Scanning comple", end="\r")
time.sleep(0.1)
print("Scanning complet", end="\r")
time.sleep(0.1)
print("Scanning complete", end="\r")
time.sleep(0.1)
print("Scanning completed.", end="\r")
time.sleep(0.1)
print("Scanning completed. ", end="\r")
time.sleep(0.1)
print("Scanning completed. F", end="\r")
time.sleep(0.1)
print("Scanning completed. Fa", end="\r")
time.sleep(0.1)
print("Scanning completed. Fac", end="\r")
time.sleep(0.1)
print("Scanning completed. Face", end="\r")
time.sleep(0.1)
print("Scanning completed. Face ", end="\r")
time.sleep(0.1)
print("Scanning completed. Face R", end="\r")
time.sleep(0.1)
print("Scanning completed. Face Re", end="\r")
time.sleep(0.1)
print("Scanning completed. Face Rec", end="\r")
time.sleep(0.1)
print("Scanning completed. Face Reco", end="\r")
time.sleep(0.1)
print("Scanning completed. Face Recog", end="\r")
time.sleep(0.1)
print("Scanning completed. Face Recogn", end="\r")
time.sleep(0.1)
print("Scanning completed. Face Recogni", end="\r")
time.sleep(0.1)
print("Scanning completed. Face Recognis", end="\r")
time.sleep(0.1)
print("Scanning completed. Face Recognise", end="\r")
time.sleep(0.1)
print("Scanning completed. Face Recognised")
time.sleep(0.1)

print(Back.RESET)

time.sleep(0.5)
print()

print(Back.YELLOW + "Accesing your data in")
print(Back.RESET)
while count > 0:
  print(count)
  time.sleep(1)
  count = count - 1
time.sleep(1)

print()
print(Fore.BLUE + "Your vitals")
time.sleep(1)

print("Heart Rate->  /‾-   /‾\__--‾˙-   -‾˙-   -'‾˙‾‾ ")
print("           __/   \_/          \_/    \_/          ")
print()

Covid_Status = 0
Body_Temperature = 0

Covid_Status = input(Fore.MAGENTA + "Enter Covid status (Positive/Negative): ")

if Covid_Status.lower() == "positive":
  print("Access denied")
  sys.exit()
elif Covid_Status.lower() == "negative":
  print("Covid Status -> Negative")
  print("Access enabled")
else:
  print("Invalid Covid status entered")
  sys.exit()

time.sleep(2)
print()

print("Body Temperature=98", end="\n")
time.sleep(1)
print()

print("Vitals match generating your secrect code to enter the data base",
      end="/n")
time.sleep(1.5)
print()


def loading2():
  animation2 = "|/-\\"
  for _ in range(12):
    print("Loading", animation2, end="\r")

    time.sleep(0.2)

    animation2 = animation2[1:] + animation2[1]


loading2()
print("Loading complete!")

print()
print(Fore.GREEN + "Your secret code number to enter the data base is:",
      Fore.LIGHTMAGENTA_EX, code_number)

print()
print()
time.sleep(2.5)
print(Fore.YELLOW + " ____ ____ ____ ____ ____ ____ ____ ")
print("||T |||h |||a |||n |||k |||s |||! ||")
print("||__|||__|||__|||__|||__|||__|||__||")
print("|/__\|/__\|/__\|/__\|/__\|/__\|/__\|")
