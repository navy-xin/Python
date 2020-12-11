"""
1.出拳
    玩家：手动输入
    电脑：1.固定：剪刀 2.随即
2.判断输赢
    2.1 玩家获胜
    2.2 平局
    2.3 电脑获胜
"""

# 1.出拳
# 玩家


play = int(input('请出拳：0=石头；1=剪刀；2=布'))
# 电脑
coumputer = 1
# 2.判断输赢
# 玩家获胜
if ((play == 0) and (coumputer == 1)) or ((play == 1) and (coumputer == 2)) or ((play ==2) and (coumputer == 0)):
    print('玩家获胜，恭喜恭喜')
elif play == coumputer:
    print('平局，你别走，再来一次。')
else:
    print('电脑获胜，你不行！')