#数字を半角カタカナに変換する関数
    #無量大数まで実装
    #４桁ごとに区切るってリストで返す関数
    #４桁を半角カタカナに変換する関数
"""
    ten = ["","ﾏﾝ","ｵｸ","ﾁｮｳ","ｹｲ",
           "ｶﾞｲ","ｼﾞｮ","ｼﾞｮｳ","ｺｳ","ｶﾝ",
           "ｾｲ","ｻｲ","ｺﾞｸ","ｺﾞｳｶﾞｼｬ","ｱｿｳｷﾞ",
           "ﾅﾕﾀ","ﾌｶｼｷﾞ","ﾑﾘｮｳﾀｲｽｳ"]
"""
           
def cut4(self):#４桁ごとに区切るってリストで返す関数
    self = str(self)
    if len(self) < 5:
        return [int(self)]
    m = 0
    n = len(self)%4
    out = []
    if n == 0:
        n = 4
    for i in range(len(self)//4+1):
        out.append(int(self[m:n]))
        m = n
        n += 4
    return out

def halfkana4(self,bottom=False,tyokei=False):#4=>ｼ,7=>ｼﾁ
    out = []
    one = [
        "","","ﾆ","ｻﾝ","ﾖﾝ",
        "ｺﾞ","ﾛｸ","ﾅﾅ","ﾊﾁ","ｷｭｳ"]
    one68 = [
        "","","ﾆ","ｻﾝ","ﾖﾝ",
        "ｺﾞ","ﾛｯ","ﾅﾅ","ﾊｯ","ｷｭｳ"]
    onetk = [
        "","ｲｯ","ﾆ","ｻﾝ","ﾖﾝ",
        "ｺﾞ","ﾛｸ","ﾅﾅ","ﾊｯ","ｷｭｳ"]
    ten = ["","ｼﾞｭｳ","ﾋｬｸ","ｾﾝ"]
    ten3 = ["","ｼﾞｭｳ","ﾋﾞｬｸ","ｾﾞﾝ"]
    ten68 = ["","ｼﾞｭｳ","ﾋﾟｬｸ","ｾﾝ"]
    tentk = ["","ｼﾞｭｯ","ﾋｬｸ","ｾﾝ"]
    if self >= 1000:
        if self//1000 > 0:
            if self//1000 == 3:
                out.append(one[3]+ten3[3])
            elif self//1000 == 8:
                out.append(one68[8]+ten68[3])
            else:
                out.append(one[self//1000]+ten[3])
    if self >= 100:
        if (self%1000)//100 > 0:
            if (self%1000)//100 == 3:
                out.append(one[3]+ten3[2])
            elif (self%1000)//100 == 6:
                out.append(one68[6]+ten68[2])
            elif (self%1000)//100 == 8:
                out.append(one68[8]+ten68[2])
            else:
                out.append(one[(self%1000)//100]+ten[2])
    if self >= 10:
        if (self%100)//10 > 0:
            if tyokei and self%10==0:
                out.append(one[(self%100)//10]+tentk[1])
            else:
                out.append(one[(self%100)//10]+ten[1])
    self = self%10
    if bottom:
        if self == 4:
            out.append("ｼ")
        elif self == 7:
            out.append("ｼﾁ")
        elif self == 1:
            out.append("ｲﾁ")
        elif self ==0 and out == []:
            out.append("ｾﾞﾛ")
        else:
            out.append(one[self])
    elif tyokei:
        out.append(onetk[self])
    else:
        if self > 1:
            out.append(one[self])
        if self == 1:
            out.append("ｲﾁ")
    return "".join(out)

def allkana(self):
    pass
