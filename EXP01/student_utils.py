
# student_utils.py
# 用于解析学生成绩记录的独立模块

def parse_student(line):
    # 去除首尾空白，再根据逗号拆分字段
    fields = line.strip().split(",")

    # 检查字段数量
    if len(fields) != 2:
        raise ValueError("字段数量错误，应包含姓名和成绩")

    # 获取姓名和成绩文本
    name = fields[0].strip()
    score_text = fields[1].strip()

    # 姓名不能为空
    if not name:
        raise ValueError("姓名不能为空")

    # 将成绩转换为整数
    try:
        score = int(score_text)
    except ValueError:
        raise ValueError("成绩不是有效整数") from None

    # 检查成绩范围
    if not 0 <= score <= 100:
        raise ValueError("成绩必须在0到100之间")

    # 返回学生信息字典
    return {
        "name": name,
        "score": score
    }
