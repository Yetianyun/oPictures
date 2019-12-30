#处理某网站的数据

#处理某网站的数据
def operateText(source_file,target_file):
    fo = open(target_file,"w")
    textList = ['提交','通过','时间','内存','题目','难度','提交','查看','标签','进入','相关','推荐','展开','说明','初始','数据']
    file = open(source_file)
    charList = ['+','>','<','/']
    for line in file:
        zz = line[0:2]
        if ( zz[0:1] == "P" or zz in textList  or zz == "\n"):
            continue
        detail_line = []
        old_content = ""
        pos = 0
        if ( line.find("for") > 0):
            print(line)
            continue

        fenHao = line.split(";")
        line = ";\n".join(fenHao)
        splitContent = line.split("//")
        line = splitContent[0]
        for detail in line:
            pos += 1
            if  (  detail in charList or ""'\u4e00' <= detail <= '\u9fff' or detail == "，" or detail =="。"):
                detail_line.append(detail)
            else :
                if ( old_content != detail ):
                    detail_line.append(detail)
                old_content = detail

        now_line = ''.join(detail_line)

        fo.write(now_line)
        print(now_line)

    fo.close()
    file.close()

if __name__ == '__main__':
    # 引用测试
    source_file = "text/source.txt"
    target_file = "text/target.txt"
    operateText(source_file,target_file)
