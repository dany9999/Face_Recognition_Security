from PIL import Image
import numpy as np
import torch
from PIL import ImageOps
from torchvision import transforms
import tensorflow as tf

#################### NN2 load image ######################################################################

def load_image_NN2(filename):
    # Carica l'immagine
    img = Image.open(filename)

    # Ridimensiona l'immagine a 224x224
    img = img.resize((160, 160))

    img = add_padding(img, (224,224))
    # Converti l'immagine in un array NumPy
    img = np.array(img)

    # Applica le trasformazioni
    img = transform(img)
    img_test = img.unsqueeze(0)  # Aggiungi una dimensione batch
    
    return img_test



def transform(img):
        img = img[:, :, ::-1]  # RGB -> BGR
        img = img.astype(np.float32)
        img = img.transpose(2, 0, 1)  # C x H x W
        img = torch.from_numpy(img).float()
        return img



# Add padding to the image to make it fit into the target size.
def add_padding(image, target_size):
  
    # Calculate padding size
    width, height = image.size
    pad_width = max(0, target_size[0] - width)
    pad_height = max(0, target_size[1] - height)
    
    # Add padding
    padding = (pad_width // 2, pad_height // 2, pad_width - (pad_width // 2), pad_height - (pad_height // 2))
    padded_image = ImageOps.expand(image, padding, fill='black')
    
    return padded_image

#################### NN1 load image ##################################################

def load_image_NN1(filename):
    img = Image.open(filename)
    rsz = img.resize((160, 160))
    tns = transforms.ToTensor()(rsz)
    tns = tns.unsqueeze(0)
    return tns

#################### LABELS ############################################################

def get_labels():
    fpath = tf.keras.utils.get_file('rcmalli_vggface_labels_v2.npy',
                             "https://github.com/rcmalli/keras-vggface/releases/download/v2.0/rcmalli_vggface_labels_v2.npy",
                             cache_subdir="./")
    labels = np.load(fpath)

    return labels