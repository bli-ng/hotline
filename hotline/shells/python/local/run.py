from localshell import LocalShell
import sys

LocalShell('/bin/sh', sys.stdin, sys.stdout, sys.stderr)
