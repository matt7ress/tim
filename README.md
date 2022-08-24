# tim
Turn your images to textwall.cc art.
---
Using this script is simple.

Open it, type image name, output size, what part you want to crop and copy result.

```bash
$ python3 main.py
Image: патур.png
Output width: 100
Output height: 100
Crop: 50:75:75:100
Took 4.494 seconds
$ ls
патур.png     патур.png.output-0952
main.py       
$ cat патур.png.output-0952
Made with T.I.M. By Matrus.
Input: патур.png
Crop: 50:75:75:100
Output size (in symbols): 1250
Took 4.494 (4.4941550827026367) seconds
-*-*-
```
Part after -\*-\*- is text you need to copy and paste to textwall.cc.

Requirements
---
The only thing you need is Pillow.
```bash
$ pip3 install pillow
```
