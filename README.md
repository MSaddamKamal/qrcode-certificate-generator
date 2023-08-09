# Certificate Generator With QR-CODE

It is a simple certificate genrator tool that can help in generating different types of  certificate with in built qrcode on it.

## Demo Generated Certificate
![Demo1](https://raw.githubusercontent.com/MSaddamKamal/qrcode-certificate-generator/main/generated-certificate/Muhammad%20Saddam.png)

## Technology Stack
It is built on the following techstack.
* Python


## Features
* 'QRCode Feature On Certificates embeding details in qrcode'
* 'Generate Certificates Of Records'
* 'Add/Update Record'
* 'Delete Record By Id'
* 'List All Records'
* 'Search Record By Id'


## Installation

These libraries are required to run this software, plese install it in your system if not installed


```bash
pip3 install opencv-python

pip install qrcode

pip install Pillow

```

## Run Program

Execute `Main.py` on your desktop, follow the instructions on command line.
Following are the menu options avalibale.
```bash 
        1: 'Add/Update Record',
        2: 'Delete Record By Id',
        3: 'List All Records',
        4: 'Search Record By Id',
        5: 'Generate Certificates Of Records',
        6: 'Exit'
```

Generated Certificate can be found in `generated-certificate` directory.


## Customizations
 You can change the certficate image in the `certificate-config` according to your requirements.
 Make sure to keep the aspect ratio, or manipulate it in the `Main.py`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

