import image_slicer

# image_slicer.slice('punks.png', 100)

for i in range(1, 11):
    for j in range(1, 11):
        if(i < 10 and j < 10):
            image_slicer.slice('punks_0'+str(i)+'_0'+str(j)+'.png', 100)
        elif(i < 10 and j >= 10):
            image_slicer.slice('punks_0'+str(i)+'_'+str(j)+'.png', 100)
        elif(i >= 10 and j < 10):
            image_slicer.slice('punks_'+str(i)+'_0'+str(j)+'.png', 100)
        else:
            image_slicer.slice('punks_'+str(i)+'_'+str(j)+'.png', 100)
