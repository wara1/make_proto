#! python3

import sys
import os

from modules import analyze as ana
from modules import command as cmd
'''
proto自動生成実行ファイル
'''

MAIN_PATH = os.path.dirname(__file__)

##
# @brief エントリーポイント
# @details なし
# @note なし
def main():
    analyze_command = ana.AnaCommand(sys.argv)
    command :cmd.Command = analyze_command.getCommand()
    command.execute()

if __name__ == "__main__":
    main()