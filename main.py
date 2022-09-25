from PIL import Image
import math, time, random
imgname = input('Image: ')
img = Image.open(imgname)
rot = input('Rotate: ').lower()
if(rot not in ['', 'no', 'none', 'null']):
    img = img.rotate(-float(rot))
img.thumbnail((int(input('Output width: ')), int(input('Output height: '))))
crop = input('Crop (fx-fy-tx-ty or nothing): ').lower()
if(crop not in ['', 'no', 'none', 'null']):
    img = img.crop(tuple([int(crop.split('-')[i]) for i in range(4)]))
escape = '\x1b'
block = '█▓'
colors = [
    list('ÀÞÁÂ×ÏÄÅÇØÐÉÈÑÒÙÌËÊÓÔÚÎÍÛÜÕÃÖÆÝÀ'),
    [
        0,
        0x515252,
        0x898d90,
        0xd4d7d9,
        0x6d001a,
        0xbe0039,
        0xff4500,
        0xffa800,
        0xffd635,
        0xfff8b8,
          0xa368,
          0xcc78,
        0x7eed56,
          0x756f,
          0x9eaa,
          0xccc0,
        0x2450a4,
        0x3690ea,
        0x51e9f4,
        0x493ac1,
        0x6a5cff,
        0x94b3ff,
        0x811e9f,
        0xb44ac0,
        0xe4abff,
        0xbe107f,
        0xff3881,
        0xff99aa,
        0x6d482f,
        0x9c6926,
        0xffb470,
        0xffffff
    ]
]
def getClosestColor(color: int) -> int:
    r, g, b = eval(f'(0x{("0"*(8-len(hex(color)))+hex(color)[2:8])[0:2]}, 0x{("0"*(8-len(hex(color)))+hex(color)[2:8])[2:4]}, 0x{("0"*(8-len(hex(color)))+hex(color)[2:8])[4:6]})')
    color_diffs = []
    for __color in colors[1]:
        for _color in range(2):
            color = __color + 0x2d2d2d * _color
            if(color >= 0xffffff and __color < 0xffffff):
                continue
            cr, cg, cb = eval(f'(0x{("0"*(8-len(hex(color)))+hex(color)[2:8])[0:2]}, 0x{("0"*(8-len(hex(color)))+hex(color)[2:8])[2:4]}, 0x{("0"*(8-len(hex(color)))+hex(color)[2:8])[4:6]})')
            color_diff = math.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
            color_diffs.append((color_diff, block[_color] if __color != 0xffffff else ' ', colors[0][colors[1].index(__color)]))
    return [min(color_diffs)[1], min(color_diffs)[2]]
start = time.time()
width, height = img.size
img = [list(img.getdata())[i*width:(i+1)*width] for i in range(height)]
output = ''
for iy in range(height):
    ly = img[iy]
    for ix in range(width):
        px = ly[ix]
        output += getClosestColor(list(px)[2] + list(px)[1] * 256 + list(px)[0] * 65536)[0] * 2
    output += '\n'
output = output[0:-1] + escape
for iy in range(height):
    ly = img[iy]
    for ix in range(width):
        px = ly[ix]
        cc = getClosestColor(list(px)[2] + list(px)[1] * 256 + list(px)[0] * 65536)
        if(cc[0] == ' '):
            output += 'ÀÀ'
        else:
            output += cc[1] * 2
    output += 'A'
output = output[0:-1]
finished = time.time()
took = finished - start
try:
    file = open(f'{imgname}.textwall', 'x', encoding = 'utf8')
    filewithoutextrainfo = open(f'{imgname}.without-extra-info.textwall', 'x', encoding = 'utf8')
except FileExistsError:
    print('[i] Files exist! Overwriting!')
    file = open(f'{imgname}.textwall', 'w', encoding = 'utf8')
    filewithoutextrainfo = open(f'{imgname}.without-extra-info.textwall', 'w', encoding = 'utf8')
print(f'Took {round(took, 3)} seconds')
file.write(f'Made with T.I.M. By Matrus.\nInput: {imgname}\nRotate: {rot}\nCrop: {crop}\nOutput size:\n - Symbols: {width * 2 * height}\n - Width & Height: {width}x{height}\nTook {round(took, 3)}s ({took}s)\nWithout info - {imgname}.without-extra-info.textwall\n-*-*-\n{output}')
file.close()
filewithoutextrainfo.write(output)
filewithoutextrainfo.close()