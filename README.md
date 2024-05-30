# Riconoscimento Facciale con Attacchi di Sicurezza

Questo progetto implementa un sistema di riconoscimento facciale e include vari attacchi di sicurezza per testare la robustezza del sistema. Di seguito sono riportate le istruzioni per eseguire il progetto.

## Struttura del Progetto

- `test_set/`: contiene le immagini del set di test.
- `test_set_cropped/`: contiene le immagini del set di test croppate utilizzando lo script `face_crop.py`.
- `face_crop.py`: script per il cropping delle immagini nel set di test.
- `DeepFool.ipynb`: notebook per eseguire l'attacco DeepFool.
- `CarliniWagner.ipynb`: notebook per eseguire l'attacco Carlini-Wagner.
- `PGD_targeted.ipynb`: notebook per eseguire l'attacco PGD mirato.
- `PGD_untargeted.ipynb`: notebook per eseguire l'attacco PGD non mirato.
- `test_clean_NN1.ipynb`: notebook per eseguire i test della rete neurale NN1 (Inception ResNet v1) sul set di test pulito.
- `test_clean_NN2.ipynb`: notebook per eseguire i test della rete neurale NN2 (ResNet50) sul set di test pulito.
- `utils.py`: script che contiene funzionalità utili richiamate nel codice.
- `resnet.py`: script che contiene la definizione della rete neurale ResNet50 (NN2).
- `inception.py`: script che contiene la definizione della rete neurale Inception ResNet v1 (NN1).

## Requisiti

Assicurati di avere installato i seguenti pacchetti Python:

- numpy
- tensorflow
- keras
- matplotlib
- jupyter

Puoi installarli usando pip:

```bash
pip install numpy tensorflow keras matplotlib jupyter
