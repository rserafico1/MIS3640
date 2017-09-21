def calc_bmi(w, h):

    b = 703 * (w/(h**2))

    if b <= 18.5:
        print('Underweight')
    elif 18.5 < b < 25:
        print('Normal Weight')
    elif 25 < b < 29.9:
        print('Overweight')
    elif b >= 30:
        print('Obesity') 

w = input('Enter weight (lbs)')
h = input('Enter height (in)')
w = float(w)
h = float(h)

calc_bmi(w, h)
