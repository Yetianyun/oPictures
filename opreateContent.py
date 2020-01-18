#去重
def qch(zf):
    zf.replace(")"," ")
    zf.replace("("," ")
    zf = zf.strip()
    l = len(zf)
    for i in range(2,l):
        if ( l % i == 0 ):
            m = 0
            jzf = zf[0:i]
            for j in range(0,l-1,i):
                xzf = zf[j:j+i]
                if ( xzf != jzf ):
                    m = 1
                    break
            if ( m == 0 ):
                return xzf
    return zf

#处理某网站的数据
def operateText(source_file,target_file):
    fo = open(target_file,"w")
    textList = ['题目提供者','应用','题库','训练','比赛','记录','题目列表','提交','通过','时间限制','内存限制','历史分数','普及组','提交','通过','时间','内存','题目','难度','提交','查看','标签','进入','相关','推荐','展开','说明','初始','数据']
    file = open(source_file)
    charList = ['+','>','<','/']
    yw = ""
    for line in file:
        zz = line[0:2]
        if ( zz[0:1] == "P" or zz in textList  or zz == "\n"):
            continue
        detail_line = []
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
            #判断是否是汉字
            if  (  detail in charList or ""'\u4e00' <= detail <= '\u9fff' or detail == "，" or detail =="。"):
                hd = qch(yw)
                detail = qch(hd) + detail
                detail_line.append(detail)
                yw = ""
            else :
                yw += detail

        now_line = ''.join(detail_line)
        fo.write(now_line)

    fo.close()
    file.close()

if __name__ == '__main__':
    # 引用测试
    source_file = "text/source.txt"
    target_file = "text/target.txt"
    operateText(source_file,target_file)
    print("处理完成")

