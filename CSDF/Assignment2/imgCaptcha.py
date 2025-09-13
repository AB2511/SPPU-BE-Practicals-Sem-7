from captcha.image import ImageCaptcha

# Create an ImageCaptcha object
image = ImageCaptcha(width=200, height=90)

# Text to embed in CAPTCHA
captcha_text = "CyberSecurity"

# Generate the CAPTCHA image
data = image.generate(captcha_text)

# Save the image to file
image.write(captcha_text, 'CAPTCHA.png')

print("✅ CAPTCHA image generated as 'CAPTCHA.png'")
