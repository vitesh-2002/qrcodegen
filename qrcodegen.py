# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 11:16:18 2020

@author: vites
"""
def qrcode():
    import pyqrcode
    import png
    from pyqrcode import QRCode

    site = str(input('Type url of website: '))
    _cancel = ['0', 'cancel', 'exit']
    
    if str(site) in _cancel:
        print('program cancelled')
        
   
    else:
        url= pyqrcode.create(site)

        name = str(input('Save/Name the file of the QR Code: '))

        myqr = name+'.svg'
        myqrpng = name+'.png'

        url.svg(myqr, scale = 8)
        url.png(myqrpng, scale = 6)
    
        print('your qr code has been generated!')
    
    

    
    
    
for i in range(100000):
    print('\nRun QR Code Generator?: ')
    run = input('yes or no? ')
    y = ['y','Y','yes','Yes']
    n = ['n', 'N', 'no', 'No', 'cancel', '0']
    if run in y:
        print('\nType 0 anytime to stop the program\n\n')
        print('\n' + '-' + 'QR Code Generator'.center(20,'-') + '\n')
        qrcode()
    else:
        print('exiting program...')
        break
    
    
   
    







