def normalize(target, type = 'l1'):
    tmp = pd.DataFrame()
    su = 0
    for i in range(target.shape[1]):
        tmp = pd.concat([tmp,target.iloc[0:,i]],axis = 1)
        if(type == 'l1'):
            su = sum(tmp.iloc[0:,i])
        elif(type == 'l2'):
            for j in range(target.shape[0]):
                su += pow(target.iloc[j,i],2)
            su = pow(su,0.5)
        elif(type == 'max'):
            for j in range(target.shape[0]):
                if(tmp.iloc[j,i] > su):
                    su = tmp.iloc[j,i]
        for j in range(target.shape[0]):
            tmp.iloc[j,i] /= su
    return tmp
