ip = input('Введите IP: ')
ip_adress = ip.split('.')
print(ip_adress)

if ip.count('.') != 3:
    print('Адрес - это четыре числа, разделенные точками.')
elif ''.join(ip_adress).isdigit() == False:
    for num in ip_adress:
        if num.isdigit() == False:
            print(num, '- не целое число.')
        continue
else:
    yes = True
    for num in ip_adress:
        if int(num) > 255:
            print(num, 'превышает 255')
            yes = False
            break
    if yes:
        print('IP-адрес корректен.')
