from email.policy import default
import codewars_test as test



def validBraces(string):
    if string[0] in ')}]':
        return False
    while "()" in string or "{}" in string or "[]" in string:
        if string in '(){}[]':
            return True
        string = string.replace("()", "")
        string = string.replace("{}", "")
        string = string.replace("[]", "")
        if len(string) == 0: return True

    return False


# test.assert_equals(validBraces("()"), True)
# test.assert_equals(validBraces("[(])"), False)
# test.assert_equals(validBraces("([{}])"), True)
# print(
#     "======================================================================================================================================="
# )
# test.assert_equals(validBraces("{}({})[]"), True)
# print(
#     "======================================================================================================================================="
# )
# test.assert_equals(validBraces("(({{[[]]}}))"), True)

test.assert_equals(validBraces("{}()[]"), True)
