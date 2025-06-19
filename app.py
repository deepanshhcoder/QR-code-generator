# link="https://www.linkedin.com/in/deepansh-sharma12"
# generate qr 

# pip install pyqrcode pypng
#installing virtual environment
# python -m venv qr_env
# python -m venv name 

#activate virtual environment
# venv\Scripts\activate ->windows
# source venv/bin/activate --> linux/mac os

# pip install -r requirements.txt
# miniconda
# qr code decoder 

import pyqrcode
import png 
link="https://www.linkedin.com/in/deepansh-sharma12"
qr_code=pyqrcode.create(link) # qrcode
qr_code.png("linkedindeepansh.png", scale=5) #save qr as image

