def asal(a):
    sayac=0
    for i in range(2,101):
        toplam=0

        for j in range(1,i+1):
            if(i%j==0):
                toplam+=1
        if (toplam==2):
            print(i)
            sayac+=1
           
        if(sayac==a):
            break
          
sayi=int(input("Kaç tane asal bulmak istediğinizi girin:"))
asal(sayi)