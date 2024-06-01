import streamlit as st
from PIL import Image
import os
from os import path
import math
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import base64
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format
from rich import print
from rich.console import Console
from rich.table import Table
import os
import getpass
from rich.progress import track
import sys

DEBUG = False
console = Console()
headerText = "M6nMjy5THr2J"


def encrypt(key, source, encode=True):
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = Random.new().read(AES.block_size)  # generate IV
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
    source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
    data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
    return base64.b64encode(data).decode() if encode else data

def decrypt(key, source, decode=True):
    if decode:
        source = base64.b64decode(source.encode())
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = source[:AES.block_size]  # extract the IV from the beginning
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])  # decrypt
    padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
    if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
        raise ValueError("Invalid padding...")
    return data[:-padding]  # remove the padding


def convertToRGB(img):
	try:
		rgba_image = img
		rgba_image.load()
		background = Image.new("RGB", rgba_image.size, (255, 255, 255))
		background.paste(rgba_image, mask = rgba_image.split()[3])
		print("[yellow]Converted image to RGB [/yellow]")
		return background
	except Exception as e:
		print("[red]Couldn't convert image to RGB [/red]- %s"%e)

def getPixelCount(img):
	width, height = Image.open(img).size
	return width*height



def encodeImage(image,message,filename):
	with console.status("[green]Encoding image..") as status:
		try:
			width, height = image.size
			pix = image.getdata()

			current_pixel = 0
			tmp=0
			# three_pixels = []
			x=0
			y=0
			for ch in message:
				binary_value = format(ord(ch), '08b')
				
				# For each character, get 3 pixels at a time
				p1 = pix[current_pixel]
				p2 = pix[current_pixel+1]
				p3 = pix[current_pixel+2]

				three_pixels = [val for val in p1+p2+p3]

				for i in range(0,8):
					current_bit = binary_value[i]

					# 0 - Even
					# 1 - Odd
					if current_bit == '0':
						if three_pixels[i]%2!=0:
							three_pixels[i]= three_pixels[i]-1 if three_pixels[i]==255 else three_pixels[i]+1
					elif current_bit == '1':
						if three_pixels[i]%2==0:
							three_pixels[i]= three_pixels[i]-1 if three_pixels[i]==255 else three_pixels[i]+1

				current_pixel+=3
				tmp+=1

				#Set 9th value
				if(tmp==len(message)):
					# Make as 1 (odd) - stop reading
					if three_pixels[-1]%2==0:
						three_pixels[-1]= three_pixels[-1]-1 if three_pixels[-1]==255 else three_pixels[-1]+1
				else:
					# Make as 0 (even) - continue reading
					if three_pixels[-1]%2!=0:
						three_pixels[-1]= three_pixels[-1]-1 if three_pixels[-1]==255 else three_pixels[-1]+1


				if DEBUG:
					print("Character: ",ch)
					print("Binary: ",binary_value)
					print("Three pixels before mod: ",three_pixels)
					print("Three pixels after mod: ",three_pixels)


				three_pixels = tuple(three_pixels)
				
				st=0
				end=3

				for i in range(0,3):
					if DEBUG:
						print("Putting pixel at ",(x,y)," to ",three_pixels[st:end])

					image.putpixel((x,y), three_pixels[st:end])
					st+=3
					end+=3

					if (x == width - 1):
						x = 0
						y += 1
					else:
						x += 1

			encoded_filename = filename.split('.')[0] + "-enc.png"
			image.save(encoded_filename)
			print("\n")
			print("[yellow]Original File: [u]%s[/u][/yellow]"%filename)
			print("[green]Image encoded and saved as [u][bold]%s[/green][/u][/bold]"%encoded_filename)

		except Exception as e:
			print("[red]An error occured - [/red]%s"%e)
			sys.exit(0)



def decodeImage(image):
	with console.status("[green]Decoding image..") as status:
		try:
			pix = image.getdata()
			current_pixel = 0
			decoded=""
			while True:
				# Get 3 pixels each time
				binary_value=""
				p1 = pix[current_pixel]
				p2 = pix[current_pixel+1]
				p3 = pix[current_pixel+2]
				three_pixels = [val for val in p1+p2+p3]

				for i in range(0,8):
					if three_pixels[i]%2==0:
						# add 0
						binary_value+="0"
					elif three_pixels[i]%2!=0:
						# add 1
						binary_value+="1"


				#Convert binary value to ascii and add to string
				binary_value.strip()
				ascii_value = int(binary_value,2)
				decoded+=chr(ascii_value)
				current_pixel+=3

				if DEBUG:
					print("Binary: ",binary_value)
					print("Ascii: ",ascii_value)
					print("Character: ",chr(ascii_value))

				if three_pixels[-1]%2!=0:
					# stop reading
					break

			# print("Decoded: %s"%decoded)
			return decoded
		except Exception as e:
			print("[red]An error occured - [/red]%s"%e)
			sys.exit()

# Streamlit app layout
st.title("IMGHIDE - Steganography Tool")

# Sidebar options
st.sidebar.title("Choose an operation:")
operation = st.sidebar.radio("", ("Encode", "Decode"))

# Encode section
if operation == "Encode":
    st.header("Encode a message in an image")

    # File upload
    image_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    # Message input
    message = st.text_area("Enter your message")

    # Password input
    password = st.text_input("Password (optional)", type="password")

    # Encode button
    if st.button("Encode"):
        if image_file is not None and message:
            try:
                image = Image.open(image_file)
                if image.mode != 'RGB':
                    image = convertToRGB(image)
                newimg = image.copy()

                cipher = message
                if password:
                    cipher = encrypt(key=password.encode(), source=message.encode())
                    cipher = headerText + cipher

                encodeImage(image=newimg, message=cipher, filename='encrypted_image.png')

                st.success("Image encoded successfully!")
                st.download_button("Download encoded image", newimg)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please select an image and enter a message.")

# Decode section
elif operation == "Decode":
    st.header("Decode a message from an image")

    # File upload
    image_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    # Password input
    password = st.text_input("Password (if used during encoding)", type="password")

    # Decode button
    if st.button("Decode"):
        if image_file is not None:
            try:
                image = Image.open(image_file)
                decoded_text = decodeImage(image)

                if password:
                    header = decoded_text[:len(headerText)]
                    if header.strip() == headerText:
                        decoded_text = decoded_text[len(headerText):]
                        decrypted = decrypt(key=password.encode(), source=decoded_text)
                        decoded_text = decrypted.decode()
                    else:
                        st.error("Incorrect password!")
                        decoded_text = None

                if decoded_text:
                    st.success("Message decoded successfully!")
                    st.write(decoded_text)
                else:
                    st.error("No message found or incorrect password.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please select an image.")

# # Run the Streamlit app
# if __name__ == "__main__":
#     st.run()