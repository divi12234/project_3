MARK_UP = 2.5 # The markup percentage
awholesale= 'Y'
while awholesale == 'Y' or awholesale == 'y':
    wholesale = float(input("Enter the item's wholesale cost: "))
    if  wholesale <= 0:
        print('ERROR: the cost cannot be negative or \'0\'. \nplease enter a valid number.')
        
        
    elif wholesale > 0: 
            retail = wholesale * MARK_UP
            print(f'Retail price: ${retail:,.2f}')
            awholesale = input('Do you have another item?, \n(Enter \'Y\' or \'y\' for yes): ')
        
