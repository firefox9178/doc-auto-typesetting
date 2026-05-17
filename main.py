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
    text = re.sub(r"^\s+|\s+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    text = re.sub(r" +", " ", text)
    print("✅ 格式清理完成")
    return text

# 三、格式统一模块（新增v1.1）
def set_unified_format(text):
    """统一段落首行缩进，规整格式"""
    lines = text.split("\n\n")
    new_lines = []
    for para in lines:
        if para.strip():
            new_lines.append("　　" + para.strip())
    return "\n\n".join(new_lines)

# 四、文本统计模块（新增v1.1）
def text_statistics(text):
    """统计字数、段落数"""
    content_no_space = text.replace(" ","").replace("\n","")
    char_count = len(content_no_space)
    para_count = len([p for p in text.split("\n\n") if p.strip()])
    print(f"\n📊 文本统计：总字符数 {char_count}，段落数 {para_count}")
    return char_count, para_count

# 程序入口
if __name__ == "__main__":
    print("===== 简易文档自动排版工具 v1.1 =====")
    file = "test.txt"
    content = read_document(file)
    if content:
        clean_text = clean_format(content)
        unified_text = set_unified_format(clean_text)
        text_statistics(unified_text)
        print("\n----- 排版后内容 -----\n")
        print(unified_text)
        with open("formatted.txt", "w", encoding="utf-8") as f:
            f.write(unified_text)
        print("\n✅ 已保存为 formatted.txt")