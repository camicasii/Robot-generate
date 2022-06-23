# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from os import listdir
from PIL import Image,ImageSequence
from random import randint,seed
a={
'patch_head':randint(0,3),
'patch_body':randint(0,3),
'patch_armL':randint(0,3),
'patch_armR':randint(0,3),
'patch_legL':randint(0,3),
'patch_legR':randint(0,3),
'patch_ayes':randint(0,3),
'patch_helm':randint(0,3),
}


def print_hi(parts):
    # print(a['patch_head'])
    robotDir=['Wood Bot', 'Modern Green Bot', 'Blue Triangle', 'Golden Bot']
    # Use a breakpoint in the code line below to debug your script
    def patchHanlde(name):
        return f'assets/image/Robot Sets/{robotDir[parts[name]]}/PNGs/'

    def sortedHandle(patch):
        return sorted(listdir(patch))

    def ImageHandle(patch, index):
        return Image.open(patch + sortedHandle(patch)[index])
    patch_head = patchHanlde("patch_head")
    patch_body = patchHanlde("patch_body")
    patch_armL = patchHanlde("patch_armL")
    patch_armR = patchHanlde("patch_armR")
    patch_legL = patchHanlde("patch_legL")
    patch_legR = patchHanlde("patch_legR")
    patch_ayes = patchHanlde("patch_ayes")
    patch_helm = patchHanlde("patch_helm")

    head = ImageHandle(patch_head ,0)
    body = ImageHandle(patch_body ,1)
    armL = ImageHandle(patch_armL ,2)
    armR = ImageHandle(patch_armR ,3)
    legL = ImageHandle(patch_legL ,4)
    legR = ImageHandle(patch_legR ,5)
    ayes = ImageHandle(patch_ayes ,6)
    helm = ImageHandle(patch_helm ,7)
    def join_(a,b):
        a.paste(b,(0, 0),b)
        return a

    # print ( join2_(0,1,0))
    # z=[legR,legL,armR,armL,body,head,helm,ayes]
    z = [legL, armL, legR, armR, body, head, helm, ayes]
    k=join_(armL,legL)
    for index,value in enumerate(z):
        if(index>1):
            k=join_(k,value)
    # k.show()
    p=0.05 #proporcion
    w=int(7200*p)
    h=int(9000*p)
    print(w,h)
    # k.resize((w,h))#.save("hola.png","PNG")

    return k
    # helm.

    # print(list_dir)
      # Press Ctrl+F8 to toggle the breakpoint.

def image(pathlib,seed_):
    seed(seed_)
    image_ = {

        'patch_head': randint(0, 3),
        'patch_body': randint(0, 3),
        'patch_armL': randint(0, 3),
        'patch_armR': randint(0, 3),
        'patch_legL': randint(0, 3),
        'patch_legR': randint(0, 3),
        'patch_ayes': randint(0, 3),
        'patch_helm': randint(0, 3),
    }
    k=print_hi(image_)
    p=0.05 #proporcion
    w=int(7200*p)
    h=int(9000*p)
    k.resize((w,h)).save(pathlib,"PNG")
    return k

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(a)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
