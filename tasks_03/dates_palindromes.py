days = range(32)
months = range(13)
years = range(10000)
for year in years:
    for month in months:
        for day in days:
            if year == 0 or month == 0 or day == 0:
                date = '1.2.3'
            elif day < 10 and month < 10:
                date = f'0{days[day]}.0{months[month]}.{years[year]}'
            elif day < 10:
                date = f'0{days[day]}.{months[month]}.{years[year]}'
            elif month < 10:
                date = f'{days[day]}.0{months[month]}.{years[year]}'
            else:
                date = f'{days[day]}.{months[month]}.{years[year]}'
            date_palindrome = list(date.replace('.', ''))
            date_palindrome.reverse()
            if date_palindrome == list(date.replace('.', '')):
                print(date)