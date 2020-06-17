#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys

"""一键拉取并上传git脚本"""


def main():
    if len(sys.argv) == 1:
        print("请输入push说明")
        return
    msg = sys.argv[1]
    res = os.popen('git pull')
    print(res.read())
    res = os.popen('git add -A')
    print(res.read())
    res = os.popen('git commit -am "%s"' % msg)
    print(res.read())



if __name__ == '__main__':
    main()