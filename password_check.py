x = 1
while x < 4:        
	password = input('輸入你的密碼:')
	if password == 'shaun':
		print('登入成功')
		break
		print('已經離開break line 6') #上一行就跳出這行不會被執行
	else :          
	    x = x + 1 #剛開始寫x +1 但不會存到X, 一定要寫 x = x+1 否則不會存入到X.
	              #剛開始縮排沒弄好,導致錯誤訊息出現 unindent don snot match any outr indentation level
	    print('密碼錯誤 QQ ,請重新輸入密碼') 


