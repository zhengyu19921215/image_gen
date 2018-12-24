import datetime
import random
import os
from PIL import Image
from skimage import transform,data
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
num_len=1001
characters='0145789'
save_filename='capital_point/'
meansure1=['元','拾','佰','仟']
meansure2=['角','分']
number=['零','壹','肆','伍','柒','捌','玖']
font_size=15

for i in range(num_len):
    random_number1 = "".join([random.choice(characters) for j in range(0, random.choice(range(1,5)))])
    random_number2 = "".join([random.choice(characters) for j in range(0, random.choice(range(1, 3)))])
    path=datetime.datetime.now().strftime('%Y-%m-%d')+'_point_number_'+str(i)+'.png'
    save_path=save_filename+path
    file_number=''

    for j in range(len(random_number1)):
        if random_number1[j]=='0':
            meansure_number1 = meansure1[len(random_number1) - j - 1]
            file_number = file_number + meansure_number1
            continue
        file_number=file_number+number[int(random_number1[j])]
        meansure_number1=meansure1[len(random_number1)-j-1]
        file_number=file_number+meansure_number1

    for z in range(len(random_number2)):
        if random_number2[z]=='0':
            continue
        file_number=file_number+number[int(random_number2[z])]
        meansure_number2 = meansure2[z]
        file_number=file_number+meansure_number2

    file_number=file_number+'整'


    len_number = len(file_number)
    gene_code(file_number, save_path, len_number, font_size)
    with open('capital_point.txt', 'a') as f:
        f.write(path + '\n' + file_number + '\n')
f.close()

