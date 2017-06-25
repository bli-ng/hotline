import cmd, sys, os, subprocess, queue, io, time, threading

completions = [
    'shell',
    'clear',
    'ifconfig',
    'exit',
    'lhost',
    'set'
    ]
lhost = ''
rhost = ''
lport = ''
rport = ''

class hotlineCLI(cmd.Cmd):
    intro = '\nWelcome to Hotline, where all your sessions callback! Type help or ? to list hotline commands.\n'
    prompt = '(hotline)> '
    file = None


#Set instruction
    def do_set(shelf, s):
        s, ip = s.split(' ', 1)
        if s == 'lhost':
            print("set lhost = " + ip)
        elif s == 'rhost':
            print("set rhost = " + ip)
        elif s == 'lport':
            print("set lport = " + ip)
        elif s =='rport':
            print("set rport = " + ip)
        else:
            print(s+ "not found")
#List of all commands and instructions
    def do_shell(shelf, s):
        subprocess.Popen(("../shells/python/local/run.py"), shell=True)
    def do_clear(shelf, s):
        os.system("clear")
    def do_ifconfig(shelf, s):
        subprocess.call(['sudo ifconfig'], shell=True)
        
#Documentation for all commands
    def help_shell(self):
        print("execute shell commands")
    def help_exit(self):
        print("exit hotline")
    def help_clear(self):
        print("clear screen")
    def help_ifconfig(self):
        print("display ifconfig informaton")
        
#Command line interface instructions
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

#Auto Completion 
def complete_add(self, text, line, begidx, endidx):
            mline = line.partition(' ')[2]
            offs = len(mline) - len(text)
            return [s[offs:] for s in completions if s.startswith(mline)]
if __name__ == '__main__':
    hotlineCLI().cmdloop()
    hotlineCLI().emptyline()
        
