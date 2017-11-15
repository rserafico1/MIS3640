trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}

def speak_Chinese(number):
    '''
    number: an integer, 0<=number<=999
    Returns: a string that is the number in Chinese
    '''
    if int(number) < 11:
        return trans[number]
    elif int(number) < 20:
        return 'shi ' + trans[number[1]]
    elif int(number) < 100 and int(number[1]) == 0:
        return trans[number[0]] + ' shi'
    elif int(number) < 100 and int(number[1]) != 0:
        return trans[number[0]] + ' shi ' + trans[number[1]]
    elif int(number) > 100 and int(number[1]) != 0 and int(number[2]) != 0:
        return trans[number[0]] + ' bai ' + trans[number[1]] + ' ' + 'shi' + ' ' + trans[number[2]]
    elif int(number) > 100 and int(number[2]) == 0:
        return trans[number[0]] + ' ' + 'bai'
    elif int(number) > 100 and int(number[2]) != 0:
        return trans[number[0]] + ' ' + 'bai' + ' ' + trans[number[1]] + ' ' + trans[number[2]]
         
def main():
    print(speak_Chinese('36')) # san shi liu
    print(speak_Chinese('20')) # er shi
    print(speak_Chinese('16')) # shi liu
    print(speak_Chinese('200')) # er bai
    print(speak_Chinese('109')) # yi bai ling jiu
    print(speak_Chinese('999')) # jiu bai jiu shi jiu
 
if __name__ == '__main__':
    main()
