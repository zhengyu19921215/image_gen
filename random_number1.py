import random
# import matplotlib.pyplot as plt
import xlrd
import datetime
import math
from PIL import Image,ImageDraw,ImageFont,ImageFilter
#字体的位置，不同版本的系统会有不同BuxtonSketch.ttf
font_path = 'Fonts/HiraMinPro-W3.otf'
#font_path = 'C:/Windows/Fonts/默陌肥圆手写体.ttf'

#生成验证码图片的高度和宽度
size = (160,32)
#背景颜色，默认为白色
#bgcolor = (255,255,255)
#字体颜色，默认为蓝色
fontcolor = (105,105,105)
#干扰线颜色。默认为红色
linecolor = (0,0,0)
#是否要加入干扰线
draw_line = True
#加入干扰线条数的上下限
line_number = (1,5)


def gene_line(draw,width,height):
    # begin = (random.randint(0, width), random.randint(0, height))
    # end = (random.randint(0, width), random.randint(0, height))
    begin = (0, random.randint(0, height))
    end = (74, random.randint(0, height))
    draw.line([begin, end], fill = linecolor,width=3)


def gene_code(text,path,number,font_size):
    width,height = size #宽和高
    image = Image.open('1.png') #创建图片
    img_width, img_height = image.size
    crop_width=random.randint(1,img_width-width)
    crop_height = random.randint(1, img_height -height)
    box=(crop_width,crop_height,crop_width+width,crop_height+height)
    image=image.crop(box)
    font = ImageFont.truetype(font_path,font_size) #验证码的字体
    draw = ImageDraw.Draw(image)  #创建画笔
    #text = gene_text() #生成字符串
    font_width, font_height = font.getsize(text)
    draw.text(((width - font_width) / number, (height - font_height) / number),text,\
            font= font,fill=fontcolor) #填充字符串
    #if draw_line:
     #   gene_line(draw,width,height)
    #image = image.transform((width+30,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    # image = image.transform((width+20,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    #image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
    # a = str(m)
    #aa = str(".png")
    #path = filename + text + aa
    # cv2.imwrite(path, I1)
    # image.save('idencode.jpg')
    image.save(path)
num_len=10000#生成个数
characters='0123456789'
save_filename='random1_number/'#文件保存位置
font_size=15#字体大小
len_number=[15,18]#字体位数
file_txt='number_gen1.txt'#保存ｔｘｔ文件名字

for i in range(num_len):

    random_number="".join([random.choice(characters) for j in range(0, random.choice(len_number))])
    path=datetime.datetime.now().strftime('%Y-%m-%d')+'_number_'+str(i)+'_'+str(i)+'.png'
    number = len(random_number)
    gene_code(random_number, save_filename+path, number, font_size)
    with open(file_txt, 'a') as f:
        f.write(path+'\n'+random_number+'\n')

f.close()
