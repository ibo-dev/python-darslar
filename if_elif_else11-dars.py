# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:43:22 2023

@author: idris
"""



#yosh = int(input('yoshingizni kiriting?\n>>>'))
#if yosh <= 4:
#    print('sizga kirish bepul')
#elif yosh <= 12:
#    print('sizga kirish 5000 so\'m')
#else:
#    print('sizga kirish 8000 so\'m')
    
#yosh = int(input('yoshingiz nechchida?\n>>>'))
#if yosh <= 4:
#    narh = 0
#elif yosh <= 12:
#    narh = 5000
#else:
#    narh = 8000    
#print(f"sizga kirish {narh} som")

#yosh = int(input('yoshingiz nechchida?\n>>>'))
#if yosh <= 4:
#    narh = 0
#elif yosh <= 12:
#    narh = 5000
#elif yosh <65:
#    narh = 10000
#else:
#    narh = 8000
#print(f"qariyalarga skidka >>> {narh} som")    

#yosh = int(input('yoshingiz nechchida\n>>>'))
#if yosh <= 4:
#    narh = 0
#elif yosh <= 17:
#    narh = 5000
#elif yosh <= 65:
#    narh =10000  
#elif yosh > 65:
#    narh = 3000
#print(f"qariyalarga skidka >>> { narh} som")


#kun = input('bugun qanaqa kun?\n>>>')
#if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#    print('bugun dam olish kuni')
#else:
#    print('OPPA bugun ish kuni ekan')

#kun = input('bugun nima kun?\n>>>')
#harorat = float(input('haroratni kiriting'))
#if kun.lower() == 'yakshanba' and harorat>=30:
#    print('chumilgani kettik')
#elif kun.lower() == 'yakshanba' and harorat<30:
#    print('uyda qolamiz')

#kun = input('bugun kun nima>\n>>>')
#harorat = float(input('haroratni kirirting?\n>>>'))
#if (kun.lower() == 'shanba' or kun.lower() == 'yakshanbaga') and harorat >= 30:
#    print('chumilgani kettik')
#elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba' )and harorat < 30:
#    print('bugun dam olamiz ekan')

#narh = 15000
#choy = True
#salat = False
#if choy and salat:
#    narh = narh + 10000
#elif choy or salat:
#    narh = narh + 5000
#print(f"Jami narh { narh} so'm ")


#narh = 15000
#choy = True
#salat = False
#non = True
#kompot = True
#assorti = False
#if choy:
#    print('mijoz choy oldi')
#    narh = narh + 3000
#if salat:
#    print('mijoz salat oldi')
#    narh = narh + 5000
#if non:
#    print('mijoz non oldi')
#    narh = narh + 2000
#if kompot:
#    print('mijoz kompot oldi')
#    narh = narh + 5000
#if assorti:
#    print('mijoz assorti oldi')
#    narh = narh + 15000
#print(f"Jami {narh} so'm")    

#menu = ['osh', 'kabob', 'manti', 'somsa', 'shashlik']
#ovqat = input('nima ovqat yeysiz?\n>>>')
#if ovqat.lower() in menu:
#    print('buyurmangiz qabul qilindi')
#else:
#    print('Afsuski bunaqa taom bizda yuq')



#menu = ['osh', 'kabob', 'manti', 'somsa', 'shashlik']
#ovqat = input('nima ovqat yeysiz?\n>>>')
#if ovqat.lower()not in menu:                           #not in operatori
#    print('Afsuski bunaqa taom bizda yuq')
#else:
#    print('buyurtmangiz qabul buldi')


#menu = ['osh', 'manti', 'shashlik', 'somsa', 'kabob']
#buyurtmalar = ['osh', 'norin', 'somsa', 'shashlik']
#for  taom in buyurtmalar:
    
#    if taom in menu:
#        print(f"menuda { taom} bor")
#    else:
#        print(f"afsuski bizda { taom} yuq")


#menu = ['osh', 'qazon kabob', 'shashlik','norin', 'somsa']
#buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
#if  buyurtmalar:
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor")
#        else:
#            print(f"kechirasiz menuda {taom} yuq")
#else:
#    print('savatcha bush')



#son = int(input('juft son kiriting?\n>>>'))
#if son%2 ==0:
    
#   print('rahmat')
#else:
#    print('bu son juft emas')

#yosh = int(input('yoshingizni kiriting?\n>>>'))
#if yosh <= 4 or yosh >= 60:
#    narh = 'sizga chipta tekin'
#elif yosh <=17:
#    narh = 'chipta narhi 1000 so\'m' 
#elif yosh >=18:
#    narh = 'chipta narhi 2000 so\'m'    
    
#print(narh)


#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f"{x}>{y}")



#mahsulot = ['anor', 'sabzi', 'banan', 'uzum', 'urik', 'bodring', 'pamidor', 'piyoz']
#savat = []
#savat.append(input('savatga 1-mahsulotni qushing '))

#savat.append(input('savatga 2-mahsulotni qushing '))

#savat.append(input('savatga 3-mahsulotni qushing  '))

#savat.append(input('savatga 4-mahsulotni qushing '))

#savat.append(input('savatga 5-mahsulotni qushing '))
#if savat:
    
#    for meva in savat:
#        if meva in mahsulot:
#            print(f"dukonimizda {meva} bor")
#        else:
#            print(f"dukonimizda {meva} yo\'q")        
#else:
#    print('savatcha bush')


#mahsulotlar = ['olma', 'behi', 'nok', 'sabzi', 'xurmo', 'apelsin']
#savat =[]
#n=0
#bor =[]
#yoq =[]
#print('Iltimos 5ta mahsulot kiriting')
#while n<=5:
#	n+=1
#	savol= input(f'{n}-mahsulotni kiriting:')
#	savat.append(savol)
#for n in savat:
#	if n in mahsulotlar:
#		bor.append(n)
#	else:
#		yoq.append(n)
#if yoq:
#	print('Do`konimizda quydagi mahsulotlar yo`q ekan')
#	for a in yoq:
#		print(a.title())
#else:
#	print('Barcha mahsulotlar mavjud')

#foydalanuvchilar = ['roma', 'umar', 'fotih', 'ibo', 'yahya']
#isim = input('yangi login tanlang >>>')
#if isim in foydalanuvchilar:
    
#    print('login bant, yangi login tanlang')
#else:
#    print('xush kelibsiz')    

#son = int(input('istalgan butun son kiriting?\n>>>'))
#for n in range(2,11):
#    if not (son%n):
#        print(f"{son } soni {n} ga qoldiqsiz bulinadi")















































