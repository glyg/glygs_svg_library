#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

def find_files(expression, base_path='/home/guillaume'):
        file_list = [fname for fname in os.system('find %s %s' % (str(base_path),
                                                                  str(expression)))


find . -name '.svn' -prune -o -type f -print
        


commands = []
for name1, name2 in zip(svg_clean, svg_cut):
        commands.append('cp -uR %s %s' % (name1[:-1], name2[:-1]))