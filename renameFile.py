import os

# os.rename('punks_'+str('01')+'_'+str('01')+'_'+str('01')+'_'+str('01')+'.png',
#           'punk'+str(((int('01')-1)*(int('01')-1))+(int('01')*int('01')))+'.png')

for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            for l in range(1, 11):
                if(type(i) is not str and int(i) < 10):
                    i = '0' + str(i)
                if(type(j) is not str and int(j) < 10):
                    j = '0' + str(j)
                if(type(k) is not str and int(k) < 10):
                    k = '0' + str(k)
                if(type(l) is not str and int(l) < 10):
                    l = '0' + str(l)
                os.rename('punks_'+str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)+'.png',
                          'punk'+str(((int(i)-1)*1000)+((int(j)-1)*100)+((int(k)-1)*10)+int(l))+'.png')
