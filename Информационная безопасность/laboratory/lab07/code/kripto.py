real_str ="Что-то_написанное____"
key_str ="С Новым Годом, друзья!"

def xor_str(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip (xs, ys))

xored = xor_str(real_str, key_str)
print(xored.encode("utf-8").hex())

xored_second = xor_str(real_str, xored)
print(xored_second)

xored_third = xor_str(key_str, xored)
print(xored_third)