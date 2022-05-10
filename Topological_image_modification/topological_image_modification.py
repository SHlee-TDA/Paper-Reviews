def image_smoothing(image, k=3):
    w, h = image.shape
    smoothing_image = image.copy()
    l = (k-1)//2
    
    for i in range(0,w):
        for j in range(0,h):
            if i < l:
                lc = 0
                rc = i+l+1
            elif i > w-l-1:
                lc = i-l
                rc = -1
            else:
                lc = i-l
                rc = i+l+1

            if j < l :
                uc = 0
                bc = j+l+1
            elif j > h-l-1:
                uc = j-l
                bc = -1
            else :
                uc = j-l
                bc = j+l+1
            
            Nk = image[lc:rc, uc:bc]
            smoothing_image[i,j] = np.mean(Nk)
    return smoothing_image

    
def border_modification(image, l = 1):
    w, h = image.shape
    modified_image = image.copy()
    low_value = 1#np.min(image)
    for i in range(0,l+1):
        modified_image[i,:] = low_value
        modified_image[h-i-1,:] = low_value
        modified_image[:,i] = low_value
        modified_image[:,w-i-1] = low_value
    
    return modified_image
