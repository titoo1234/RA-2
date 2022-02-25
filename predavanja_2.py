# kombinacija = '10101'
# tab=[1,2,3,4,5]
# z = zip(kombinacija,tab)
# for i in z:
#     print(i)
    
    
def najdalse_podzaporedje(tab):
    resitev = [1 for i in range(len(tab))]
    
    for i in range(len(tab)-2,-1,-1):
        naj = 0
        for j in range(len(tab)-1,i,-1):
            if tab[j] > tab [i]:
                trenutna = resitev[j]
                if trenutna > naj:
                    naj = trenutna
        resitev[i] += naj
    return max(resitev)
            
a = najdalse_podzaporedje([51,2,3,4])
b = najdalse_podzaporedje([2,5,1,6,3,2,8])
c = najdalse_podzaporedje([5,4,3,2,1])
print(a)
print(b)
print(c)


def najdalse(tab):
    resitev = [(1,[i]) for i in range(len(tab))]
    for i in range(len(tab)-2,-1,-1):
        naj = 0
        ind = i
        for j in range(len(tab)-1,i,-1):
            if tab[j] > tab [i]:
                trenutna = resitev[j][0]
                if trenutna > naj:
                    naj = trenutna
                    ind = j
        resitev[i][1].extend(resitev[ind][1])
        nova = resitev[i][1]
        resitev[i]= (resitev[i][0] + naj,nova)
        
    return resitev
b = najdalse([2,5,1,6,3,2,8])
print(b)