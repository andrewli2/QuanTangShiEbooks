#!/usr/bin/python
# encoding: utf-8

#ebook-convert 杜甫.recipe  杜甫.mobi
a='''杜甫 柳宗元 劉禹錫 王維 孟浩然 李白 白居易 杜牧 高適 元稹 李賀 韓愈 王昌齡 韋應物 岑參 賈島 溫庭筠 李商隱 劉長卿 許渾 韋莊 陸龜蒙 皮日休 張九齡 宋之問 王勃 駱賓王 張說 陳子昂 綦毋潛 王建'''
for x in a.split():
    x=x.strip()
#    print x
    #Generate author.recipe from my3.recipe, replace the belowline with x (one of the author above in str a)
    #author = '杜甫' #//@author_mark
    fw = open(x+'.recipe','w')
    with open('my3.recipe') as fr: 
        content = fr.readlines()
        for y in content:
            if 'author =' in y and '''#//@author_mark''' in y:
                y = 'author = "' +x+'"\n'
            fw.write(y)
    fr.close()
    fw.close()

    #cmds to generate mobi and epub files
    cmd = 'ebook-convert %s.recipe 全唐詩_繁體_%s.mobi' %(x,x)
    print cmd
    cmd = 'ebook-convert %s.recipe 全唐詩_繁體_%s.epub' %(x,x)
    print cmd
    #break # debug:w

        
