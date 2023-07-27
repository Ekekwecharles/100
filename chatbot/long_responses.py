import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_INSTALL = """1. Clone the repo in your terminal (git clone https://github.com/Ekekwecharles/simple_shell.git)
    2. Change into the directory (cd simple_shell)
    3. Run the command (./hsh)
    4. If you are seeing the ($) prompt, Congrats you are now in our shell environment
"""
R_USAGE = """
1) ./hsh (interactive mode)
2) echo "echo 'awesome'" | ./hsh (non-interactive mode)
3) ./hsh file (the file contains all commands to be executed. each command must appear on a seperate line.)"""

R_SHELL = "In Bash, a shell refers to the command-line interface (CLI) or terminal environment where you interact with the operating system by typing commands."
R_EXAMPLE = """
root@98598560789c:~/simple_shell# ./hsh
($) pwd
/root/simple_shell
($) cd /
($) pwd
/
($) cd -
/root/simple_shell
($) pwd
/root/simple_shell
($) alias l=ls
($) alias c=clear
($) alias
l='ls'
c='clear'
($) exit
root@98598560789c:~/simple_shell#"""

R_EXIT = "Type the command (exit) to quit the shell."
R_FILE = """root@98598560789c:~/simple_shell# cat file
ls
echo "hard man"
root@98598560789c:~/simple_shell# ./hsh file
AUTHORS      env1.c        getline1.c      main.c        string1.c
boolean.c    env.c         getline.c       README.md     ........
"hard man"
root@98598560789c:~/simple_shell#"""
R_START = "Just Run the command (./hsh) Its very easy"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Can you be more specific",
                "What does that mean?",
                "Sorry I dont understand"][random.randrange(5)]
    return response