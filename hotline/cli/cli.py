#!/usr/bin/env python
# coding=utf-8

import cmd2
from hotline import SessionManager
from hotline.listener import TCPListener

class cli(cmd2.Cmd):
    intro = "\nWelcome to Hotline, where all your sessions callback! Type help for ? to list commands/options.\n"
    prompt = '(hotline)>'
    file = None
    default_to_shell = True
    lhost = 0
    lport = 0
    rhost = 0
    rport = 0

    def do_set(self, s):
        s, ip = s.split(' ', 1)
        if s.lower() == 'lhost':
            try:
                self.lhost=ip
                print("set LHOST => ", self.lhost)
            except:
                print(sys.exec_info()[0])
        elif s.lower() == 'rhost':
            try:
                self.rhost=ip
                print("set RHOST => ", self.rhost)
            except:
                print(sys.exec_info()[0])
        elif s.lower() == 'lport':
            try:
                self.lport=ip
                print("set LPORT => ", self.lport)
            except:
                print(sys.exec_info()[0])
        elif s.lower() == 'rport':
            try:
                self.rport=ip
                print("set RPORT => ", self.rport)
            except:
                print(sys.exec_info()[0])
        else:
            print("cannot find variable -- ", s)
    
    def do_handler(self, s):

        if self.lhost is 0:
            print("Please Set LHOST")
        elif self.lport is 0:
            print("Please Set LPORT")
        else:
            hotline = SessionManager()
            hotline.add_listener(TCPListener(str(self.lhost),int(self.lport)))
    
    def do_options(self, s):
        global lhost,rhost,lport,rport
        print("Options:")
        print("----------------")
        print("LHOST = ",self.lhost)
        print("LPORT = ",self.lport)
        print("RHOST = ",self.rhost)
        print("LPORT = ",self.rport)
        print("----------------")



    def help_set(self):
        print("\nSet handler/payload options")
    def help_shell(self):
        print("\nexecute commands in shell")

if __name__ == '__main__':
    cli().cmdloop()
    cli.emptyline()

