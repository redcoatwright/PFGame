#!/usr/bin/env python
 
import subprocess
 
command = ['tput', 'cols']
 
def get_terminal_width():
    try:
        width = int(subprocess.check_output(command))
    except OSError as e:
        print("Invalid Command '{0}': exit status ({1})".format(
              command[0], e.errno))
    except subprocess.CalledProcessError as e:
        print("Command '{0}' returned non-zero exit status: ({1})".format(
              command, e.returncode))
    else:
        return width
 
def main():
    width = get_terminal_width()
    if width:
        print(width)
 
if __name__ == "__main__":
    main()
