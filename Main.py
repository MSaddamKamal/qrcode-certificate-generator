# Sotware Name: Course Certificate Manager Software With QR
# Created By: Muhammad Saddam


## Short Description
# The software is intended to generate certificate for particular course
# using HashMap Data Structure on the go.

## Features Of Software
# 'QRCode Feature On Certificates embeding Student Information'
# 'Generate Certificates Of Records'
# 'Add/Update Record'
# 'Delete Record By Id'
# 'List All Records'
# 'Search Record By Id'



# imports
import cv2
import pathlib
import os
# include HashMap DataStructure Class
import HashMap
import qrcode
from PIL import Image, ImageDraw, ImageFont

# path to font
FONT = "C:/WINDOWS/FONTS/ITCEDSCR.ttf"

# path to dummy certificate
CERTIFICATE = str(pathlib.Path().resolve()).replace(os.sep, '/')+'/certificate-conifg/certificate-sketch.png'
PATH = str(pathlib.Path().resolve()).replace(os.sep, '/')+'/certificate-conifg'
SAVEPATH = str(pathlib.Path().resolve()).replace(os.sep, '/')+'/generated-certificate'

class Certificate:

  def __init__(self):
    # creating the instance of HashMap Class
    self.hashMapDBForRecords = HashMap.Hashmap()


  def print_options(self):
    # Menu Options
    menu_options = {
        1: 'Add/Update Record',
        2: 'Delete Record By Id',
        3: 'List All Records',
        4: 'Search Record By Id',
        5: 'Generate Certificates Of Records',
        6: 'Exit',
    }
    for key in menu_options.keys():

        print ('\t\t\t\t\t',key, '--', menu_options[key] )



  def showMenu(self):
    while(True):
        
        print('\n\t\t\t**********Use The Menu Below To Operate********** ','\n')
        self.print_options()
        option = ''
        try:
            print('\n')
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...','\n')
        if option == 1:
            # Taking input from the user to add/update record in HashMap
           self.collectInput()
        elif option == 2:
            # Taking input from the user to delete item from hashmap
            recordIdentifier = input('Please enter record Id or Key to delete item... \n')
            self.hashMapDBForRecords.deleteRecordByKey(recordIdentifier)
        elif option == 3:
            # Taking input from the user to list all item in hashmap
            self.hashMapDBForRecords.listAllRecords()
        elif option == 4:
            # Taking input from the user to search an item from hashmap
            recordIdentifier = input('Please enter record Id or Key to search item... \n')
            self.hashMapDBForRecords.searchRecordByKey(recordIdentifier)
        elif option == 5:
            # Generating Certificate of all the users in the hashmap datastrucure
            for eachRecord in self.hashMapDBForRecords.dummyArray:
                if(eachRecord != []):
                    for subRecord in eachRecord:
                        self.generateCertificate(subRecord[1]['name'],subRecord[1])

            print('\n\t**You can find your generated software in the following folder**','\n')
            print('\n\t',SAVEPATH,'\n')
        elif option == 6:
            print('\n\t\t\t******Thanks You For Using Our Software..Good Bye!*******','\n')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.','\n')


  def collectInput(self):
      takeInput = 1
      # looping till the user exit the program
      while takeInput:
        print('\n\t\t\t**********Note The Student Id Should Be Unique********** ')
        print('\n\t\t\t****If You Input The Same Id The Record Will Be Updated**** ')
        # collecting input from user
        studentId = input("Enter Student Id : \t")
        studentName = input("Enter Student Name : \t")
        courseName = input("Enter Course Name : \t")
        obtainedMarks = input("Enter Obtained Marks : \t")
        # saving data to hashmap in object or Dictionary form
        self.hashMapDBForRecords.addRecord(studentId,{ "id" : studentId , "name" : studentName,"course" : courseName,"marks" : obtainedMarks })
       
        answer = input("Do You Want to Create Another Certificate?\t yes = 1 and no = 0 \t Default Option is Yes   ") 
        if answer == 0 or answer == '0':
            break

  def generateCertificate(self,name,record):


    # adjusting position to write name on the certificate
    text_y_position = 900 

    # opens the image
    img = Image.open(CERTIFICATE, mode ='r')
      
    # gets the image width
    image_width = img.width
      
    # gets the image height
    image_height = img.height 

    # creates a drawing canvas overlay 
    # on top of the image
    draw = ImageDraw.Draw(img)

    # gets the font object from the 
    # font file (TTF)
    font = ImageFont.truetype(
        FONT,
        200
    )

    text_width, _ = draw.textsize(name, font = font)

    # writing the name of student on the certificate image
    draw.text(
        (
            (image_width - text_width) / 2,
            400
        ),
        name,
        font = font,fill="#000000"  )

    # saves the image in png format
    img.save(f"{SAVEPATH}/{name}.png")
    
    # intializing qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    # embeding student full record information on Qrcode 
    qr.add_data(record)
    # making qrcode image and setting its background and fore ground color
    img2 = qr.make_image(fill_color="black", back_color="#edc09a").convert('RGB')
    img2.save(f"{PATH}/qrCode.png")
    s_img = cv2.imread(f"{PATH}/qrCode.png")
    s_img = cv2.resize(s_img,(300,300))
    l_img = cv2.imread(f"{SAVEPATH}/{name}.png")
    x_offset=y_offset=50
    l_img[y_offset+780:y_offset+780+s_img.shape[0], x_offset+750:x_offset+750+s_img.shape[1]] = s_img
    cv2.imwrite(f"{SAVEPATH}/{name}.png",l_img)



Certificate().showMenu()