这个项目需要python3环境

这个项目主要用于查询成语、熟悉成语

主要功能包括：
1.查找。支持模糊查找、精确查找、正则查找（linux的*和？)
2.成语接龙。获取一个成语的成语接龙，随机接龙，不一定是最长的
3.查看成语明细。包括：发音、解释、示例、出处

示例：

idiom = idioms()
# 示例1：模糊查找
print(idiom.search('答','fuzzy'))
# 示例2：精确查找
print(idiom.search('答','exact'))
# 示例3：正则查找
print(idiom.search('*答*','regular'))

# 示例4：成语接龙
idiom.jielong("三心二意")
print("\n")
# 示例5：获取成语详细资料
print(idiom.detail("三心二意"))

# 关闭
idiom.close()