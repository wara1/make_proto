#! python3

import sys
import os

from modules.analyze.ana_command import AnaCommand
from modules.event.event import Event

'''
proto自動生成実行ファイル
'''

MAIN_PATH = os.path.dirname(__file__)

##
# @brief エントリーポイント
# @details なし
# @note なし
def main():
    print("テスト")
    # コマンドライン引数解析
    analyze_command = AnaCommand(sys.argv)
    event = analyze_command.getEvent()
    event.execute()

# ダウンロード

# 実行

# 文字コード変換

if __name__ == "__main__":
    main()