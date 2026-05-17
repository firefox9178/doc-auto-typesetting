import re

# 一、文档读取模块
def read_document(file_path):
    """读取txt文档，处理异常"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        print("✅ 文档读取成功")
        return content
    except FileNotFoundError:
        print("❌ 错误：文件不存在")
        return None
    except Exception as e:
        print(f"❌ 读取失败：{e}")
        return None

# 二、格式清理模块
def clean_format(text):
    """清理多余空格、空行、特殊字符"""
    if not text:
        return ""
    # 1. 去除行首尾空格
    text = re.sub(r"^\s+|\s+$", "", text, flags=re.MULTILINE)
    # 2. 多个空行合并为1个
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    # 3. 清理连续多余空格
    text = re.sub(r" +", " ", text)
    print("✅ 格式清理完成")
    return text

# 程序入口
if __name__ == "__main__":
    print("===== 简易文档自动排版工具 v1.0 =====")
    file = "test.txt"
    content = read_document(file)
    if content:
        clean_text = clean_format(content)
        # 输出清理后结果
        print("\n----- 清理后内容 -----\n")
        print(clean_text)
        # 保存清理后的文件
        with open("cleaned.txt", "w", encoding="utf-8") as f:
            f.write(clean_text)
        print("\n✅ 已保存为 cleaned.txt")