print('Enter your weight :')
weight = float(input())
print('Enter hours trained :')
hours = float(input())
print('Enter Steps Walked')
steps = int(input())

if weight > 80:
    if hours > 2 & steps >10000 :
        print('You are in good shape')
    else :
        print('You need to train more')

elif weight < 80:
    if hours > 1 & steps > 5000 :
        print('You are in good shape')
    else :
        print('You need to train more')            
 