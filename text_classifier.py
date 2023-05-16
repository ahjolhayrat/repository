import json

# 读取文件内容并去除空格和换行符
with open('E:/PGC_Project/output/extracted_text.txt', 'r', encoding='utf-8') as f:
    text = f.read().replace('\n', '').replace('\r', '').replace('  ', '')

# 分割文本内容
sections = text.split(' ')

# 初始化字典
data = {}

# 定义当前类别为空字符串，开始循环处理每个单词
current_section = "TitleAndAuthorsLabel"
data[current_section] = ""

# 定义类别列表和对应的类别标签
category_list = ["Abstract", "Keywords", "Introduction", "Results", "Discussion", "Methods", "Acknowledgements", "Reference"]
category_labels = ["AbstractLabel", "KeywordsLabel", "IntroductionLabel", "ResultsLabel", "DiscussionLabel", "MethodsLabel", "AcknowledgementsLabel", "ReferenceLabel"]

# 初始化类别索引
category_index = 0

# 循环处理每个单词
for word in sections:
    # 如果当前单词是下一个类别的标题，则更新当前类别索引
    if word == category_list[category_index]:
        current_section = category_labels[category_index]
        data[current_section] = ""
        category_index += 1
        # 如果已经到了最后一个类别，则将剩余部分都作为Reference
        if category_index == len(category_list):
            break
    # 将单词添加到当前类别中
    data[current_section] += " " + word

# 导出为 JSON 文件
with open('example.json', 'w') as f:
    json.dump(data, f, indent=4)
