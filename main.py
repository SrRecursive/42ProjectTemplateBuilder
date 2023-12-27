import os
from datetime import datetime

# Function to create respective directories
def create_dirs():
    if (not os.path.exists("include")):
        os.makedirs("include")
    if (not os.path.exists("src")):
        os.makedirs("src")
    if (not os.path.exists("utils")):
        os.makedirs("utils")

# Function to create the 42 header
def create_header(filename, username, email):
    filename_max_length = 46
    if (len(filename) > filename_max_length):
        filename = filename[:filename_max_length - 1 - len(filename)].ljust(filename_max_length - 1 - len(filename))

    author = "By: " + username + " <" + email + ">"
    author_max_length = 46
    if (len(author) > author_max_length):
        author = author[:author_max_length - 1 - len(author)].ljust(author_max_length - 1 - len(author))

    creation_date = "Created: " + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " by " + username
    creation_date_max_length = 46
    if (len(creation_date) > creation_date_max_length):
        creation_date = creation_date[:creation_date_max_length - 1 - len(creation_date)].ljust(creation_date_max_length - 1 - len(creation_date))

    update_date = "Updated: " + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " by " + username
    update_date_max_length = 46
    if (len(update_date) > update_date_max_length):
        update_date = update_date[:update_date_max_length - 1 - len(update_date)].ljust(update_date_max_length - 1 - len(update_date))

    # First line
    header = "/* " + "*" * 74 + " */\n"

    # Empty line
    header += "/* " + " " * 74 + " */\n"

    # Middle
    header += "/*" + " " * 57 + ":::" + " " * 5 + ":" * 8 + " " * 3 + "*/\n"
    header += "/*" + " " * 3 + "{}".format(filename) + " " * (filename_max_length + 6 - len(filename)) + ":+:" + " " * 5 + ":+:" + " " * 4 + ":+:" + " " * 3+ "*/\n"
    header += "/*" + " " * 53 + "+:+ +:+" + " " * 8 + "+:+" + " " * 5 + "*/\n"
    header += "/*" + " " * 3 + author + " " * (author_max_length + 2 - len(author)) + "+#+  +:+" + " " * 6 + "+#+" + " " * 8 + "*/\n"
    header += "/*" + " " * 49 + "+#" * 5 + "+" + " " * 3 + "+#+" + " " * 10 + "*/\n"
    header += "/*" + " " * 3 + creation_date + " " * (creation_date_max_length + 5 - len(creation_date)) + "#+#" + " " * 4 + "#+#" + " " * 12 + "*/\n"
    header += "/*" + " " * 3 + update_date + " " * (update_date_max_length + 4 - len(update_date)) + "#" * 3 + " " * 3 + "#" * 10 + " " * 7 + "*/\n"

    # Empty line
    header += "/* " + " " * 74 + " */\n"

    # Last line
    header += "/* " + "*" * 74 + " */\n"

    return header

# Function that generates the main file
def c_main_template(header, name):
    file = open(os.path.join("src/{}.c").format(name), 'w')
    file.write(
            '''\
{}
#include "../include/{}.h"

int\tmain(void)
{{
\tribanab();
\treturn (0);
}}
'''.format(header, name)
            )
    file.close

# Function that generates the header file
def c_header_template(header, name):
    file = open(os.path.join("include/{}.h".format(name)), 'w')
    file.write(
            '''\
{}
#ifndef {}_H
# define {}_H

/* <-- Defines Section --> */

/* <-- Libraries Section --> */

# include <stdio.h>

/* <-- Structs Section --> */

/* <-- Functions Section --> */

void\tribanab(void);

#endif
'''.format(header, name.upper(), name.upper()))
    file.close

# Function that generates the utils file
def c_utils_template(header, name):
    file = open(os.path.join("utils/utils.c"), 'w')
    file.write(
            '''\
{}
#include "../include/{}.h"

void\tribanab(void)
{{
\tprintf("Hello World, I am ribana-b from 42 Malaga c:\\n");
\treturn ;
}}
'''.format(header, name))
    file.close

# Function that generates the Makefile template
def c_makefile_template(name):
    file = open(os.path.join("Makefile"), 'w')
    file.write(
            '''\
# ========================================================================== #

# <-- Color Library --> #

# <-- Text Color --> #
T_BLACK = \\033[30m
T_RED = \\033[31m
T_GREEN = \\033[32m
T_YELLOW = \\033[33m
T_BLUE = \\033[34m
T_MAGENTA = \\033[35m
T_CYAN = \\033[36m
T_WHITE = \\033[37m

# <-- Text Style --> #
BOLD = \\033[1m
ITALIC = \\033[2m
UNDERLINE = \\033[3m
STRIKETHROUGH = \\033[4m

# <-- Background Color --> #
B_RED = \\033[31m
B_BLACK = \\033[30m
B_GREEN = \\033[32m
B_YELLOW = \\033[33m
B_BLUE = \\033[34m
B_MAGENTA = \\033[35m
B_CYAN = \\033[36m
B_WHITE = \\033[37m

# <-- Reset Everything --> #
RESET = \\033[0m

# ========================================================================== #

# <-- Library\'s Name --> #
NAME = {}

# <-- Compilation Command --> #
CC = gcc

# <-- Compilation Flags --> #
CFLAGS = -Wall -Wextra -Werror

# <-- Remove Command -->#
RM = rm -rf

# <-- Directories --> #
SRC_DIR = src/
UTILS_DIR = utils/
OBJ_DIR = obj/

# <-- Files --> #
SRC_FILES = {}.c
UTILS_FILES = utils.c

# <-- Directories + Files --> #
SRC = $(addprefix $(SRC_DIR), $(SRC_FILES))
UTILS = $(addprefix $(UTILS_DIR), $(UTILS_FILES))

# <-- Objects --> #
OBJ = $(patsubst $(SRC_DIR)%.c, $(OBJ_DIR)%.o, $(SRC)) \\
 \t\t$(patsubst $(UTILS_DIR)%.c, $(OBJ_DIR)%.o, $(UTILS))

# ========================================================================== #

# <-- Main Target --> #
all: $(NAME)

# <--Library Creation--> #
$(NAME): $(OBJ_DIR) $(OBJ)
\t@echo \"$(T_YELLOW)$(BOLD)Objects $(RESET)$(T_GREEN)created successfully$(RESET)\"
\t@$(CC) $(OBJ) -o $(NAME) # Use this if you want to create a program
\t@#ar rcs $(NAME) $(OBJ) # Use this if you want to create a library
\t@echo \"$(T_MAGENTA)$(BOLD)$(NAME) $(RESET)$(T_GREEN)created successfully$(RESET)\"

# <-- Object Directory Creation --> #
$(OBJ_DIR):
\t@mkdir -p $(OBJ_DIR)

# <-- Objects Creation --> #
$(OBJ_DIR)%.o: $(SRC_DIR)%.c
\t@$(CC) $(CFLAGS) -c $< -o $@

$(OBJ_DIR)%.o: $(UTILS_DIR)%.c
\t@$(CC) $(CFLAGS) -c $< -o $@

# <-- Objects Destruction --> #
clean:
\t@$(RM) $(OBJ_DIR)
\t@echo \"$(T_YELLOW)$(BOLD)Objects $(RESET)$(T_RED)destroyed successfully$(RESET)\"

# <-- Clean Execution + {} Destruction --> #
fclean: clean
\t@$(RM) $(NAME) *.out
\t@echo \"$(T_MAGENTA)$(BOLD)$(NAME) $(RESET)$(T_RED)destroyed successfully$(RESET)\"

# <-- Fclean Execution + All Execution --> #
re: fclean all

# <-- Color testing --> #

colortesting:
\t@echo "$(T_BLACK)Black text"
\t@echo "$(T_RED)Red text"
\t@echo "$(T_GREEN)Green text"
\t@echo "$(T_YELLOW)Yellow text"
\t@echo "$(T_BLUE)Blue text"
\t@echo "$(T_MAGENTA)Magenta text"
\t@echo "$(T_CYAN)Cyan text"
\t@echo "$(T_WHITE)White text$(RESET)"
\t@echo "$(BOLD)"
\t@echo "$(T_BLACK)Bold Black text"
\t@echo "$(T_RED)Bold Red text"
\t@echo "$(T_GREEN)Bold Green text"
\t@echo "$(T_YELLOW)Bold Yellow text"
\t@echo "$(T_BLUE)Bold Blue text"
\t@echo "$(T_MAGENTA)Bold Magenta text"
\t@echo "$(T_CYAN)Bold Cyan text"
\t@echo "$(T_WHITE)Bold White text$(RESET)"

# <-- Targets Declaration --> #
.PHONY = all clean fclean re colortesting 

# ========================================================================== #
'''.format(name, name, name))
    file.close

# Main function
def main():
    project_name = input('Introduce the name of the project: ')
    # You can replace input() with your login
    username = input('Introduce your login: ')
    # You can replace input() with your email
    email = input('Introduce your email: ')
    create_dirs()
    c_main_template(create_header("{}.c".format(project_name), username, email), project_name)
    c_header_template(create_header("{}.h".format(project_name), username, email), project_name)
    c_utils_template(create_header("{}.c".format(project_name), username, email), project_name)
    c_makefile_template(project_name)

if (__name__ == "__main__"):
    main()
