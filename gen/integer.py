import random
# import matplotlib.pyplot as plt
import xlrd
import datetime
from PIL import Image,ImageDraw,ImageFont,ImageFilter
#字体的位置，不同版本的系统会有不同BuxtonSketch.ttf
# font_path = 'Fonts/HiraMinPro-W3.otf'

#font_path = 'C:/Windows/Fonts/默陌肥圆手写体.ttf'


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


def gene_code(text,path,number,font_size,size,font_path):
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
# (decimal_len,characters,save_path,file_txt,font_size,size,font_path,k)
def gen_decimal(num_len,characters,save_path,file_txt,fonts_size,size,fonts_path):
    #########################生成小数
    for i in range(num_len):
        font_size = random.choice(fonts_size)
        font_path = 'Fonts/' + random.choice(fonts_path)
        random_number1 = "".join([random.choice(characters) for j in range(0, random.choice(range(1,6)))])

        if random_number1[0]==0:
            continue
        random_number2 = "".join([random.choice(characters) for j in range(0, random.choice(range(1, 3)))])
        random_number=random_number1+'.'+random_number2
        image_name=datetime.datetime.now().strftime('%Y-%m-%d')+'_decimal_'+str(font_size)+'_'+str(i)+\
                   '_'+str(i)+'.png'
        number = len(random_number)

        gene_code(random_number, save_path+image_name, number, font_size,size,font_path)
        with open(file_txt, 'a') as f:
            print(random_number)
            f.write(image_name+'\n'+random_number+'\n')

    f.close()
def gen_integer(num_len,characters,save_path,file_txt,fonts_size,len_number,size,fonts_path):
    #########################生成整数
    for i in range(num_len):
        font_size = random.choice(fonts_size)
        font_path = 'Fonts/' + random.choice(fonts_path)
        random_number="".join([random.choice(characters) for j in range(0, random.choice(len_number))])
        image_name=datetime.datetime.now().strftime('%Y-%m-%d')+'_integer_'+str(font_size)+'_'+str(i)\
                   +'_'+str(i)+'.png'
        number = len(random_number)
        gene_code(random_number, save_path+image_name, number, font_size,size,font_path)
        with open(file_txt, 'a') as f:
            print(random_number)
            f.write(image_name+'\n'+random_number+'\n')

    f.close()




