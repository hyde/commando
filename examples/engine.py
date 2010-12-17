#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implements the engine entry point commands
"""
import sys
from commando import *


class Engine(Application):

    @command(description='Engine - Turbo powered',
            epilog='Use %(prog)s {command} -h to get help on individual commands')
    @version('-v', '--version', version='%(prog)s 0.1')
    @store('-k', '--key', default='.', help="Key to start the engine")
    def main(self, params):
        """
        Will not be executed. A sub command is required. This function exists to provide
        common parameters for the subcommands and some generic stuff like version and
        metadata
        """
        pass

    @subcommand('start', help='Get it up and running')
    @true('-f', '--force', default=False)
    def start(self, params):
        """
        Start the engine.
        """
        print params.key
        print params.force

if __name__ == "__main__":
    Engine().run()