arabic_to_decimal = {
	'٠': '0', '١': '1',	'٢': '2', '٣': '3',	'٤': '4',
	'٥': '5', '٦': '6',	'٧': '7', '٨': '8',	'٩': '9', ',':'', '.':''
}

decimal_to_roman =[(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           		(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def decimalToRoman(decimalNumber):
  romanNumber = []
  while decimalNumber>0:
    for key,value in decimal_to_roman:
      while decimalNumber >= key:
        romanNumber.append(value)
        decimalNumber = decimalNumber - key

  romanNumber = str(''.join(map(str,romanNumber)))
  print("Your Roman Digit Love is Served :)  -  "+romanNumber + '\n')


def parser(query):
  query = query.lower()
  flag = 0
  decimalNumber = []
  words = ['convert','translate','make']
  #ins = query.split() 
  for vals in query.split():
    if vals in words:
        for token in query:
          if token in arabic_to_decimal:
            decimalNumber.append(arabic_to_decimal[token])
       # decimalNumber = [int(i) for i in decimalNumber]
        decimalNumber = int(''.join(map(str, decimalNumber)))
        decimalToRoman(decimalNumber)
        flag = 1
    
  if flag == 0:
      print("You can roam around or have a coffee until you make your mind to convert Arabic to Roman :) \n ")


def main():
  reply = '1'
  while reply=='1' :
    q =input("Hey ! What's Up ! Wanna try some convesion ? \n")
    parser(q)
    reply = input("Press 1 to convert again :) or do some other stuff !\n ")
  print("Thank You !!! ")

if __name__ == '__main__':
	main()
