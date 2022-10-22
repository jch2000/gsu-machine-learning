# Image Reconstruction using Singular Value Decomposition
# Justin Heyer

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Bring image in and make it greyscale
img_link = './tiger.jpg'
greyscale_img = Image.open(img_link).convert("L")

U, singular_vals, V_transpose = np.linalg.svd(greyscale_img, full_matrices=False)
singular_vals = np.diag(singular_vals)

for k in (1, 5, 10, 20, 40):
    plt.axis('off')
    plt.title("k = " + str(k) + " Singular Values Output")
    # Reconstructing image with k singular values
    reduced_img = U[0:, 0:k] @ singular_vals[0:k, 0:k] @ V_transpose[0:k, 0:]
    plt.imshow(reduced_img, cmap='gray', vmin=0, vmax=255)
    plt.show()
