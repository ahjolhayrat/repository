# PDF Text Processor

这个项目使用 Python 编写，旨在处理 PDF 文档。其功能包括：从 PDF 文档提取文本、将文本初步分类，然后使用 GPT-3 进一步优化文本。

## 安装

1. 克隆此仓库：
2. 进入项目目录：
3. 安装所需的 Python 包：

## 使用

1. 在 `pdf_extractor.py` 文件中，将 `pdf_path` 变量替换为你的 PDF 文件路径。
2. 在 `gpt_text_cleaner.py` 文件中，将 `openai.api_key` 替换为你的 OpenAI API 密钥。
3. 运行程序：
4. 该程序将从 PDF 提取文本，对文本进行初步分类，并使用 GPT-3 进行清理。清理后的文本将打印到控制台。

## 注意事项

在上传代码到 GitHub 之前，确保已删除所有敏感信息，例如 API 密钥等。可以使用环境变量或配置文件来管理这些敏感信息。
