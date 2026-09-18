import sys
from pathlib import Path


def 失败(消息):
    sys.stderr.write(消息 + "\n")
    raise SystemExit(1)


def 读数(文本):
    if not 文本.isdigit():
        return None
    if len(文本) > 1 and 文本[0] == "0":
        return None
    值 = int(文本)
    if 值 < 1 or 值 > 999:
        return None
    return 值


def 主():
    路径 = Path("布料")
    if not 路径.is_file():
        失败("找不到布料")
    原文 = 路径.read_text(encoding="utf-8")
    if 原文 == "":
        失败("布料不对")
    行 = 原文.split("\n")
    if 行 and 行[-1] == "":
        行.pop()
    if len(行) != 2:
        失败("布料不对")
    幅 = 行[0].split(" ")
    宽 = 行[1].split(" ")
    if len(幅) != 2 or 幅[0] != "布幅" or len(宽) != 2 or 宽[0] != "片宽":
        失败("布料不对")
    布幅 = 读数(幅[1])
    片宽 = 读数(宽[1])
    if 布幅 is None or 片宽 is None:
        失败("布料不对")
    片 = 0
    余 = 布幅
    while 余 >= 片宽:
        余 -= 片宽
        片 += 1
    if 片 == 0:
        失败("不够裁")
    sys.stdout.write("%s片\n" % 片)


if __name__ == "__main__":
    主()
