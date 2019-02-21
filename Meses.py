month, day, year = input('Date (mm/dd/aaaa): ').split('/')
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
print('Date of birth is: ')
print('%s %s of %s ' %(months[int(month) -1], day, year))