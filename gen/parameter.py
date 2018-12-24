# CHAR_VECTOR = "adefghjknqrstwABCDEFGHIJKLMNOPZ0123456789"
# #import string
# #characters=string.digits+string.ascii_uppercase+string.ascii_lowercase
# f1 = open("1.txt","r")
# character = f1.readlines()
# character=''.join(character)
# characters=character.replace("\n", "")
# letters=str(characters)+' '
# #letters = [letter for letter in CHAR_VECTOR]
#
# num_classes = len(letters) + 1
#
# img_w, img_h = 160, 32
#
# # Network parameters
# batch_size =256
# val_batch_size = 32
#
# downsample_factor = 4
# max_text_len = 30
size=[192,32]
gen_path='data/'#保存数据根目录
cn_font=['simsun.ttc','simhei.ttf','simkai.ttf','simfang.ttf']#中文字体(大写)
en_font=['STSONG.TTF']#其他字体字体(小写)
fonts_size=range(8,17)
captical_int_num=10#(大写整数个数)
captical_dec_num=10#(大写小数个数)
decimal_len=10#(小写小数个数)
integer_len=10#(小写整数个数)
len_number=[8,10,15,18,28]#小写位数