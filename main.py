from PIL import Image
import math, time, random
imgname = input('Image: ')
img = Image.open(imgname)
img.thumbnail((int(input('Output width: ')), int(input('Output height: '))))
crop = input('Crop: ').lower()
if(crop not in ['', 'no', 'none', 'null']):
    img = img.crop(tuple([int(crop.split(':')[i]) for i in range(4)]))
start = time.time()
escape = '\x1b'
block = '█'
colors = [
    [
        'A', #black
        '_', #dark grey
        'B', #grey
        'C', #light grey
        'X', #burgundy
        'P', #dark red
        'E', #red
        'F', #orange
        'H', #yellow
        'Y', #pale yellow
        'Q', #dark green
        'J', #green
        'I', #light green
        'R', #dark teal
        'S', #teal
        'Z', #light teal
        'M', #dark blue
        'L', #blue
        'K', #light blue
        'T', #indigo
        'U', #periwinkle
        '[', #lavender
        'O', #dark purple
        'N', #purple
        '\\',#pale purple
        ']', #magenta
        'V', #pink
        'D', #light pink
        'W', #dark brown
        'G', #brown
        '^'  #beige
    ],
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
        0x00a368,
        0x00cc78,
        0x7eed56,
        0x00756f,
        0x009eaa,
        0x00ccc0,
        0x2450a4,
        0x3690ea,
        0x51e9f4,
        0x493ac1,
        0x6a5cff,
        0x94b3ff,
        0x811e9f,
        0xb44ac0,
        0xe4abff,
        0xde107f,
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
    for color in colors[1]:
        cr, cg, cb = eval(f'(0x{("0"*(8-len(hex(color)))+hex(color)[2:8])[0:2]}, 0x{("0"*(8-len(hex(color)))+hex(color)[2:8])[2:4]}, 0x{("0"*(8-len(hex(color)))+hex(color)[2:8])[4:6]})')
        color_diff = math.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, eval(f'(0x{("0"*(8-len(hex(color)))+hex(color)[2:8])[0:2]}, 0x{("0"*(8-len(hex(color)))+hex(color)[2:8])[2:4]}, 0x{("0"*(8-len(hex(color)))+hex(color)[2:8])[4:6]})')))
    return list(min(color_diffs)[1])[2] + list(min(color_diffs)[1])[1] * 256 + list(min(color_diffs)[1])[0] * 65536
width, height = img.size
img = [list(img.getdata())[i*width:(i+1)*width] for i in range(height)]
output = ''
for iy in range(height):
    ly = img[iy]
    for ix in range(width):
        px = ly[ix]
        ind = colors[1].index(getClosestColor(list(px)[2] + list(px)[1] * 256 + list(px)[0] * 65536))
        if(ind == len(colors[0])):
            output += '  '
        else:
            output += block * 2
    output += '\n'
output = output[0:-1] + escape
for iy in range(height):
    ly = img[iy]
    for ix in range(width):
        px = ly[ix]
        ind = colors[1].index(getClosestColor(list(px)[2] + list(px)[1] * 256 + list(px)[0] * 65536))
        if(ind == len(colors[0])):
            output += 'AA'
        else:
            output += colors[0][ind] * 2
    output += 'A'
output = output[0:-1]
file = open(f'{imgname}.output-{"".join([str(random.randint(0, 9)) for i in range(random.randint(2, 7))])}', 'x', encoding = 'utf8')
finished = time.time()
took = finished - start
print(f'Took {round(took, 3)} seconds')
file.write(f'Made with T.I.M. By Matrus.\nInput: {imgname}\nCrop: {crop}\nOutput size (in symbols): {width * 2 * height}\nTook {round(took, 3)} ({took}) seconds\n-*-*-\n{output}')