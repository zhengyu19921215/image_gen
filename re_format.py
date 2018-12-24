f = open("字库.txt","r")
characters = f.readlines()
characters=''.join(characters)
characters=characters.replace("\n", "")

f1= open("data_test.txt","r")
file_labels = f1.readlines()
for i in range(len(file_labels)):
    number_label=file_labels[i].split()
    label=''
    for j in range(1,11):
        label=label+characters[int(number_label[j])-1]

    with open('test.txt','a') as label_file:
        label_file.write(number_label[0]+'\n'+label+'\n')


