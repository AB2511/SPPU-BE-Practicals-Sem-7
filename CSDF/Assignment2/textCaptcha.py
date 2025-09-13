import random

def checkCaptcha(captcha, user_captcha):
    return captcha == user_captcha

def generateCaptcha(n):
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    captcha = ""
    while n:
        captcha += chrs[random.randint(0, 61)]  # fixed: pick from valid index range
        n -= 1
    return captcha

if __name__ == "__main__":
    n = 9  # length of captcha
    captcha = generateCaptcha(n)
    print("Generated CAPTCHA:", captcha)

    user_captcha = input("Enter the captcha: ")
    if checkCaptcha(captcha, user_captcha):
        print("✅ CAPTCHA Matched!")
    else:
        print("❌ CAPTCHA Not Matched")
