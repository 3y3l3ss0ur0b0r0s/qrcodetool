# This was written by 3y3l3ss0ur0b0r0s on 03/18/2022.
    # GitHub: https://github.com/3y3l3ss0ur0b0r0s

import os
import qrcode
from os.path import exists
from pyzbar.pyzbar import decode
from PIL import Image

def use_tool():
    dir=os.path.dirname(__file__)
    path=r'{}/QR Code Tool Outputs'.format(dir)

    try:
        os.makedirs(path)
    except OSError:
        pass

    stop_program=False
    valid_response=False
    response_confirmed=False

    while stop_program==False:
        print("\n\t============================\n\t\tQR Code Tool\n\t============================")
        user_input=input("\n\tEnter 1 to encode a QR code.\n\tEnter 2 to decode a QR code.\n\tEnter 3 to exit.\n\t")
        if user_input=='1':
            qr=qrcode.QRCode(version=1,box_size=10,border=2)

            while not response_confirmed:
                data=input("\n\tWhat do you want to encode?\n\t")
                answer=input("\n\tAre you sure? Enter 1 for yes, enter 2 for no.\n\t")
                if answer=='1':
                    response_confirmed=True
                elif answer=='2':
                    continue
                else:
                    continue
                qr.add_data(data)

            response_confirmed=False
            while not response_confirmed:
                fill=input("\n\t6-digit hex code for fill color? Don't include the # symbol.\n\t")
                answer=input("\n\tAre you sure? Enter 1 for yes, enter 2 for no.\n\t")
                if answer=='1':
                    while not valid_response:
                        if len(fill)!=6:
                            print("\n\tThe hex code must be 6-digits.")
                            fill=input("\n\t6-digit hex code for fill color? Don't include the # symbol.\n\t")
                        else:
                            valid_response=True
                        response_confirmed=True
                elif answer=='2':
                    continue
                else:
                    continue

                valid_response=False
                response_confirmed=False
                back=input("\n\t6-digit hex code for background color? Don't include the # symbol.\n\t")
                answer=input("\n\tAre you sure? Enter 1 for yes, enter 2 for no.\n\t")
                if answer=='1':
                    while not valid_response:
                        if len(back)!=6:
                            print("\n\tThe hex code must be 6-digits.")
                            fill=input("\n\t6-digit hex code for back color? Don't include the # symbol.\n\t")
                        else:
                            valid_response=True
                        response_confirmed=True
                elif answer=='2':
                    continue
                else:
                    continue

                img=qr.make_image(fill_color='#'+fill,back_color='#'+back)

                image_name=input("\n\tWhat do you want to call it?\n\t")
                location=path+'/'+image_name+'.png'

                img.save(location)

        elif user_input=='2':
            response_confirmed=False
            valid_response=False
            while not response_confirmed:
                file_path=input("\n\tWhat do you want to decode?\n\t")
                answer=input("\n\tAre you sure? Enter 1 for yes, enter 2 for no.\n\t")
                if answer=='1':
                    while not valid_response:
                        file_path=file_path.replace('\"','')
                        if os.path.exists(file_path)==True:
                            img=Image.open(file_path)
                            result=decode(img)
                            print("\n\tDecoded QR code:","\n\t",result)
                            valid_response=True
                        else:
                            file_path=input("\n\tThat file doesn't exist...try a different one? Include the path, without quotation marks.\n\t")
                            continue
                        response_confirmed=True
                elif answer=='2':
                    continue
                else:
                    continue

        elif user_input=='3':
            stop_program=True
        else:
            print("\nThat was not valid input. Try again, please!")

if __name__=='__main__':
    use_tool()
