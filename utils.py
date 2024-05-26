from PIL import Image
import numpy as np
import torch
from PIL import Image, ImageOps
from PIL import ImageFilter
from torchvision import transforms
import tensorflow as tf
import pickle
import torch
from io import BytesIO
import cv2
#################### NN2  ######################################################################
mean_bgr = np.array([91.4953, 103.8827, 131.0912])

# load image

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
        img -= mean_bgr
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


def load_test_image_NN2(test_images_adv):
    # Prepara le immagini per la visualizzazione
    # Rimuovi la dimensione batch extra e converti nel formato channels-last
    test_images_adv = np.squeeze(test_images_adv, axis=0)
    test_images_adv = np.transpose(test_images_adv, (1, 2, 0))
    if test_images_adv.dtype != np.uint8:
        test_images_adv = (test_images_adv * 255).astype(np.uint8)


    # Carica l'immagine
    img = Image.fromarray(test_images_adv)

    
    img = add_padding(img, (224,224))
    # Converti l'immagine in un array NumPy
    img = np.array(img)

    # Applica le trasformazioni
    test_images_NN2 = transform(img)
    test_images_NN2 = test_images_NN2.unsqueeze(0)  # Aggiungi una dimensione batch
    
    return test_images_NN2

def load_test_image_NN2_preprocessed(test_images_adv):
    # Prepara le immagini per la visualizzazione
    # Rimuovi la dimensione batch extra e converti nel formato channels-last
    test_images_adv = np.squeeze(test_images_adv, axis=0)
    test_images_adv = np.transpose(test_images_adv, (1, 2, 0))
    if test_images_adv.dtype != np.uint8:
        test_images_adv = (test_images_adv * 255).astype(np.uint8)


    # Carica l'immagine
    img = Image.fromarray(test_images_adv)
    img = img.filter(ImageFilter.GaussianBlur(0.5))
    img = ImageOps.flip(img)
    img = img.resize((224,224))
    # Converti l'immagine in un array NumPy
    img = np.array(img)

    # Applica le trasformazioni
    test_images_NN2 = transform(img)
    test_images_NN2 = test_images_NN2.unsqueeze(0)  # Aggiungi una dimensione batch
    return test_images_NN2

# loadd weights
def load_state_dict(model, fname):
    """

    Arguments:
        model: model
        fname: file name of parameters converted from a Caffe model, assuming the file format is Pickle.
    """
    with open(fname, 'rb') as f:
        weights = pickle.load(f, encoding='latin1')

    own_state = model.state_dict()
    for name, param in weights.items():
        if name in own_state:
            try:
                own_state[name].copy_(torch.from_numpy(param))
            except Exception:
                raise RuntimeError('While copying the parameter named {}, whose dimensions in the model are {} and whose '\
                                   'dimensions in the checkpoint are {}.'.format(name, own_state[name].size(), param.size()))
        else:
            raise KeyError('unexpected key "{}" in state_dict'.format(name))

#################### NN1 load image ##################################################

def load_image_NN1(filename,device):
    img = Image.open(filename)
    rsz = img.resize((160, 160))
    tns = transforms.ToTensor()(rsz)
    tns.to(device)
    tns = tns.unsqueeze(0)
    return tns

#################### LABELS ############################################################

def get_labels():
    fpath = tf.keras.utils.get_file('rcmalli_vggface_labels_v2.npy',
                             "https://github.com/rcmalli/keras-vggface/releases/download/v2.0/rcmalli_vggface_labels_v2.npy",
                             cache_subdir="./")
    labels = np.load(fpath)

    return labels