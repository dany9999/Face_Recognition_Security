# Face Recognition Security

This project implements a facial recognition system and includes various security attacks to test the robustness of the system. Below are the instructions for running the project.

## Project Structure

- `test_set_cropped/`: contains the cropped test set images, generated using the `face_crop.py` script. 
- `DeepFoolAttack.ipynb`: notebook to run the DeepFool attack.
- `carlini_wagner.ipynb`: notebook to run the Carlini-Wagner attack.
- `pgd.ipynb`: notebook to run the PGD attack.
- `test_clean_NN1.ipynb`: notebook to test the NN1 neural network (Inception ResNet v1) on the clean test set without attacks.
- `test_clean_NN2.ipynb`: notebook to test the NN2 neural network (ResNet50) on the clean test set without attacks.
- `utils.py`: script containing utility functions used throughout the code.
- `RESNET.py`: ResNet50 neural network (NN2).
- `inception.py`: ResNet v1 neural network (NN1).

## Requisiti

Assicurati di avere installato i seguenti pacchetti Python:

- numpy
- keras
- jupyter

Puoi installarli usando pip:
 ```bash
pip3 install requirements.txt
```



### Note
 
If you plan to run the notebooks using a GPU, it is recommended not to install the facenet-pytorch package, especially in Windows environments.

### Running the Attacks
To execute an attack, open the corresponding notebook and run it. Each notebook performs the specified attack on the cropped test set images in untargeted and targete mode.


  
