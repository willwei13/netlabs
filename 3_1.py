def generator(dividend,divisor):
    lenghth = len(divisor)
    temp1 = dividend + '0' * (lenghth - 1)
    ans = ''
    remainder = temp1[0:len(divisor)]
    for i in range(len(dividend)):
        timp2, remainder = XOR(remainder, divisor)
        ans = ans + timp2
        if i == len(dividend) - 1:
            break
        else:
            remainder = remainder + temp1[i + lenghth]
    ans = dividend + remainder
    return ans


def verifier(dividend,divisor):
    lenghth = len(divisor)
    temp1 = dividend + '0' * (lenghth - 1)
    ans = ''
    remainder = temp1[0:len(divisor)]
    for i in range(len(dividend)):
        timp2, remainder = XOR(remainder, divisor)
        ans = ans + timp2
        if i == len(dividend) - 1:
            break
        else:
            remainder = remainder + temp1[i + lenghth]
    ans = dividend + remainder
    count = 0
    for i in range(0,len(remainder)):
        if remainder[i] == "0":
            count +=1
    if count == len(remainder):
        print("检查正确")
    else:
        print("检查错误")
    return ans


def alter(message):
    count = 0
    result = ""
    for i in range(0, len(message)):
        if message[i] == "1":
            count += 1
    for i in range(0, len(message)):
        if i == count:
            if message[i] == "1":
                result += "0"
            else:
                result += "1"
        else:
            result += message[i]
    return result


def XOR(a, b):
    ans = ''
    if a[0] == '0':
        return '0', a[1:]
    else:
        for i in range(len(a)):
            if (a[i] == '0' and b[i] == '0'):
                ans = ans + '0'
            elif (a[i] == '1' and b[i] == '1'):
                ans = ans + '0'
            else:
                ans = ans + '1'
    return '1', ans[1:]


if __name__ == '__main__':
    message = input("0和1组成的n位消息:")
    divisor = input("0和1组成的k位消息:")
    result = generator(message,divisor)
    print(generator(message,divisor))
    verifier(result,divisor)
    verifier(alter(result),divisor)