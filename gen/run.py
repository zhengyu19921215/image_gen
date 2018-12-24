from parameter import cn_font,fonts_size,captical_dec_num,captical_int_num,gen_path,en_font,decimal_len,integer_len,len_number,size
from integer import gen_integer,gen_decimal
from medical_gen import medical_generator
from capital_integer import  gen_capital_dec,gen_capital_int
from alphabet import gen_letter ,gen_letter_integer


print(len(alphabet_character))
capital_save_path=gen_path + 'capital/' # 大写文件保存位置
capital_file_txt = gen_path + 'capital.txt'  # 大写保存ｔｘｔ文件名字
gen_capital_dec(captical_dec_num,capital_save_path, capital_file_txt, fonts_size, cn_font)
gen_capital_int(captical_int_num,capital_save_path, capital_file_txt, fonts_size, cn_font)


number_characters = '0123456789'
alphabet_character='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
integer_save_path=gen_path + 'number/'#小写 文件保存位置
integer_file_txt=gen_path + 'number.txt'# 小写保存ｔｘｔ文件名字
gen_decimal(decimal_len,number_characters,integer_save_path,integer_file_txt,fonts_size,size,en_font)
gen_integer(integer_len, number_characters, integer_save_path , integer_file_txt, fonts_size, len_number, size, en_font)

medical_generator(cn_font,fonts_size)

alphabet_character='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_capital_character='abcdefghijklmnopqrstuvwxyz'
all_character=number_characters+alphabet_character+alphabet_capital_character
gen_letter_integer(decimal_len,all_character,integer_save_path,integer_file_txt,fonts_size,size,en_font)
gen_letter(integer_len, alphabet_character, integer_save_path , integer_file_txt, fonts_size, len_number, size, en_font)
