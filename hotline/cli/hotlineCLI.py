import cmd, sys, os, subprocess, queue, io, time, threading

class hotlineCLI(cmd.Cmd):
    intro = '\nWelcome to Hotline, where all your sessions callback! Type help or ? to list hotline commands.\n'
    prompt = '(hotline)> '
    file = None

    def do_shell(shelf, s):
        os.system("../shells/python/local/localshell.py")
    def help_shell(self):
        print("execute shell commands")
    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def do_exit(self, s):
        return True
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
        hotlineCLI().cmdloop()
