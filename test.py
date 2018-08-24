from idiomMaster import idioms


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