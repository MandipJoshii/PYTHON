SO THIS IS GOING TO BE A PROJECT SPECIALLY FOCUSED IN NUMPY AND MATPLOTLIB ONLY.
ITS A SMALL PROJECT WHICH UNWRAPS ABOUT IMAGES PROCESSING USING MATPLOTLIB 

1. IMREAD() -> 
   OUTCOME:
   IF: print(img) -> represents the pixel range from 0-1 
    WHERE 0 means no intensivness(color is set to black) and 1 means full intensivness(color set to white)  
    OUTPUT:
    [[[0.23137255 0.23137255 0.23137255 1.        ]
  [0.23921569 0.23921569 0.23921569 1.        ]
  [0.23921569 0.23921569 0.23921569 1.        ]
  ...
  [0.7176471  0.7176471  0.7176471  1.        ]
  [0.7058824  0.7058824  0.7058824  1.        ]
  [0.69803923 0.69803923 0.69803923 1.        ]]

 [[0.21568628 0.21568628 0.21568628 1.        ]
  [0.23137255 0.23137255 0.23137255 1.        ]
  [0.23921569 0.23921569 0.23921569 1.        ]
  ...
  [0.7176471  0.7176471  0.7176471  1.        ]
  [0.69803923 0.69803923 0.69803923 1.        ]
  [0.6862745  0.6862745  0.6862745  1.        ]]

 [[0.2        0.2        0.2        1.        ]
  [0.21568628 0.21568628 0.21568628 1.        ]
  [0.23137255 0.23137255 0.23137255 1.        ]
  ...
  [0.7058824  0.7058824  0.7058824  1.        ]
  [0.69803923 0.69803923 0.69803923 1.        ]
  [0.6862745  0.6862745  0.6862745  1.        ]]

 ...

 [[0.23137255 0.23137255 0.23137255 1.        ]
  [0.23137255 0.23137255 0.23137255 1.        ]
  [0.23921569 0.23921569 0.23921569 1.        ]
  ...
  [0.5411765  0.5411765  0.5411765  1.        ]
  [0.5529412  0.5529412  0.5529412  1.        ]
  [0.5764706  0.5764706  0.5764706  1.        ]]

 [[0.23137255 0.23137255 0.23137255 1.        ]
  [0.23137255 0.23137255 0.23137255 1.        ]
  [0.23137255 0.23137255 0.23137255 1.        ]
  ...
  [0.50980395 0.50980395 0.50980395 1.        ]
  [0.5294118  0.5294118  0.5294118  1.        ]
  [0.5411765  0.5411765  0.5411765  1.        ]]

 [[0.23137255 0.23137255 0.23137255 1.        ]
  [0.23137255 0.23137255 0.23137255 1.        ]
  [0.23137255 0.23137255 0.23137255 1.        ]
  ...
  [0.48235294 0.48235294 0.48235294 1.        ]
  [0.50980395 0.50980395 0.50980395 1.        ]
  [0.50980395 0.50980395 0.50980395 1.        ]]]

Why so many brackets [[[ ... ]]]?

Outer brackets = rows of pixels (image height)

Inside = pixels in that row (image width)

Inside each pixel = 4 numbers → [R, G, B, A]

So the huge array you see is the raw matrix form of your picture.

Example to make it clearer:
If you have a 2×2 image (very tiny), it might look like this:

[
  [[0,0,0,1], [1,1,1,1]],   # first row → black pixel, white pixel
  [[0.5,0.5,0.5,1], [0.2,0.2,0.2,1]]  # second row → gray, darker gray
]


That’s literally how computers see your image!

   IF: print(img.shape)
    OUTPUT:
    (427, 640, 4)
     WHERE:
     img.shape = height,width,channel
     channel could be of three types
      1.1 RGB -> RED,GREEN,BLUE
      1.2 RGBA -> ALPHA(it means opaque)
      1.3 RGBT -> TRANSPARENCY

2. WHEN I DID:



if img.ndim == 3:          
    gray_img = np.mean(img, axis=2)
else:
    gray_img = img




    WHAT DOES IT MEANS?

    IT MEANS:

    1.1 ndim == 1 or 2 or 3 or 4:

(H, W, 1) → sometimes a grayscale image stored with a singleton channel == 1

(H, W) → grayscale (height × width) == 2

(H, W, 3) → RGB color image (3 channels: Red, Green, Blue) == 3

(H, W, 4) → RGBA (RGB + Alpha/transparency) == 4

then gray_img = np.mean(axis=2) means if [r,g,b] = [100,150,200] then divide [100,150,200]/3 -> why becasuse axis = 2 means we need to count the axis starting from 0 so axis 0, axis 1, axis 2 = 3

simplified
axis = 2 => 0,1,2 = 3 value


3. clip() -> it helps to set a limit of an array in given range

 EXAMPLE: if clip() function is used in a image then,  clip(image,0,255) is set generally because rgb or 8-bit grayscale takes only 0-255 range where 0 is black and 255 is white.
 BUT ITS NOT ALWAYS SET TO 0-255 it can be more or less or in minus too, but generally 0-255 range is mostly used




take away/core concept for generating an image
define the image path -> img = mpimg.imread("path")

to grey an image ->
if img.ndim == 3:
gray_img = np.mean(img, axis = 2)
else:
gray_img = img

to bright an image ->
bright_img = gray_img + 200

bright_img = np.clip(bright_img, 0,255)
plt.imshow(bright_img, cmap = "gray")
plt.title("bright")
plt.axis("off")
plt.show()

to show contrast in an image ->
contrast_img = gray_img * 2
contrast_img = np.clip(contrast_img,0,255)
plt.imshow(constrst_img, cmap = "gray")
plt.title("contrast")
plt.axis("off")
plt.show()