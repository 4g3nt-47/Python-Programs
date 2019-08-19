word1=list(str(input('1st wrd:\t')))
word2=list(str(input('2nd wrd:\t')))
word3=list(str(input('3rd wrd:\t')))

for x in range(0,len(word1)):
    if(word1[x] in ['a','i','e','o','u']):
        word1[x]='%'
for y in range(0,len(word2)):
    if(not word2[y] in ['a','i','e','o','u']):
        word2[y]='#'
for z in range(0,len(word3)):
    if(word3[z].islower()==True):
        word3[z]=word3[z].upper()

print(''.join(word1)+''.join(word2)+''.join(word3))
