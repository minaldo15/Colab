# 주어진 문자열에서 숫자, 문자, 기호가
# 각각 몇개인지를 판단하는 함수를 작성해보시오.
target_str = '123강아지 !@#'

def check(target_str):
    count_alp = 0
    count_num = 0
    count_els = 0
    lst_target = list(target_str)
    for i in lst_target:
        if i.isalpha() == True:
            count_alp += 1
        elif i.isnumeric() == True:
            count_num += 1
        elif i == ' ':
            pass
        else:
            count_els += 1
    return f'문자: {count_alp}개, 숫자: {count_num}개, 기호: {count_els}개' 
print(check(target_str))

# 문자: 3개, 숫자: 3개, 기호: 3개

