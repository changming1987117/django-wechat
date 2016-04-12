'''
Created on Feb 9, 2015

@author: Helong, Feng

@description: scripts for internal use. Restarting uwsgi server.

'''

import sys, os, commands, re

def restart_uwsgi_process_help_func():
    print '''
    help:
        restart_uwsgi_process(filename)
        filename is the uwsgi configure file, such as uwgi.ini

    '''
def restart_uwsgi_process(filename):
    try:
        ps_string = "ps -ef | grep " + filename
        status_0, output_0 = commands.getstatusoutput(ps_string)
        print output_0
        out_put_list = output_0.split("  ")
        uwsgi_pid = out_put_list[1]
        print uwsgi_pid
        kill_str = 'kill -9 ' + uwsgi_pid
        status_1, output_1 = commands.getstatusoutput(kill_str)
        command_str = 'uwsgi --ini' + ' ' + filename
        status, output = commands.getstatusoutput(command_str)
    except Exception as e:
        print e


if __name__ == '__main__':
    if len(sys.argv) < 2:
        restart_uwsgi_process_help_func()
    elif len(sys.argv) == 2:
        restart_uwsgi_process(sys.argv[1])