
hello = "Merhaba"
userName = "Ayse"
totalText = hello + " " + userName
print(totalText)

totalText = "{message} {name}".format(message=hello, name=userName)
print(totalText)

#f-string
totalText = f"Hoşgeldiniz {userName}"
print(totalText)