# Face Recognition Security

This project, developed as part of the **Artificial Intelligence for Cybersecurity** course at the **University of Salerno**, focuses on evaluating the robustness and security of deep learning–based **face recognition systems** when exposed to adversarial attacks.

Facial recognition is one of the most widely adopted biometric technologies worldwide — used in smartphones, surveillance, and access control systems.  
However, recent studies have shown that even highly accurate deep neural networks can be **vulnerable to adversarial perturbations**: small, imperceptible changes in input images that can cause misclassification and compromise system integrity.

The goal of this project is to:
- Assess the **vulnerability of face recognition models** (ResNet50 and Inception-ResNet v1 pre-trained on VGGFace2) to adversarial examples.  
- Evaluate different **adversarial attack techniques** such as:
  - Projected Gradient Descent (PGD)  
  - DeepFool  
  - Carlini–Wagner (CW)  
- Analyze **attack transferability** between neural networks.  
- Implement and test **defense mechanisms** (Gaussian Blur, image flipping, resizing) to improve model robustness.

Experiments were carried out using the **Adversarial Robustness Toolbox (ART)** and Python-based deep learning frameworks such as **TensorFlow** and **Keras**.  
The study provides insights into how adversarial attacks affect the performance of facial recognition systems and explores potential mitigation strategies to enhance cybersecurity in AI-based biometric authentication.


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


  
