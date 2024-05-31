# Face Recognition Security

Questo progetto implementa un sistema di riconoscimento facciale e include vari attacchi di sicurezza per testare la robustezza del sistema. Di seguito sono riportate le istruzioni per eseguire il progetto.

## Struttura del Progetto

- `test_set_cropped/`: contiene le immagini del test set iniziali che sono state ritagliate utilizzando lo script `face_crop.py`.
- `face_crop.py`: script per il cropping delle immagini nel test set.
- `DeepFoolAttack.ipynb`: notebook per eseguire l'attacco DeepFool.
- `carlini_wagner.ipynb`: notebook per eseguire l'attacco Carlini-Wagner.
- `pgd.ipynb`: notebook per eseguire l'attacco PGD.
- `test_clean_NN1.ipynb`: notebook per eseguire i test della rete neurale NN1 (Inception ResNet v1) sul test set pulito senza attacchi.
- `test_clean_NN2.ipynb`: notebook per eseguire i test della rete neurale NN2 (ResNet50) sul test set pulito senza attacchi.
- `utils.py`: script che contiene funzionalità utili richiamate nel codice.
- `RESNET.py`: script che contiene la definizione della rete neurale ResNet50 (NN2).
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
pip install numpy keras jupyter
```

## Istruzione per l'Esecuzione 
### Preparazione per l'esecuzione dei notebook
Prima di eseguire qualsiasi attacco, è necessario avere installato i seguenti pacchetti. Puoi installarli usando pip:

 ```bash
pip install facenet-pytorch
pip install Pillow
pip install -q tensorflow==2.0.0
pip install adversarial-robustness-toolbox[all]
pip install matplotlib
```
### Nota 
Se si ha intenzione di eseguire i notebook usando la GPU, si consiglia di non installare il pacchetto facenet-pytorch soprattutto in ambiente Windows. 

### Esecuzione attacchi 
Per eseguire un attacco, apri il notebook corrispondente e avvialo. Ogni notebook eseguirà l'attacco specificato sulle immagini ritagliate del test set.

- `Attacco DeepFool`: apri DeepFoolAttack.ipynb per eseguire l'attacco DeepFool.
- `Attacco Carlini-Wagner`: apri carlini_wagner.ipynb per eseguire l'attacco Carlini-Wagner untargeted e targeted.
- `Attacco PGD`: apri pgd.ipynb per eseguire l'attacco PGD untargeted e targeted.
  
### Test delle Reti Neurali sul Test Set Clean
Per testare le reti neurali NN1 e NN2 sul set di test pulito, apri i rispettivi notebook e avviali.

- `Test di NN1 (Inception ResNet V1)`: apri test_clean_NN1.ipynb per eseguire un test clean sulla rete NN1.
- `Test di NN2 (ResNet50)`: apri test_clean_NN2.ipynb per eseguire un test clean sulla rete NN2.

## Dettagli Tecnici
- `NN1 (Inception ResNet v1)`: definita nello script inception.py.
- `NN2 (ResNet50)`: definita nello script RESNET.py.
- `Funzionalità Utili`: contenute nello script utils.py, che viene richiamato nei vari notebook per eseguire operazioni comuni come la pre-elaborazione delle immagini.

## Note Finali
Per qualsiasi dubbio o problema, verifica la corretta configurazione dell'ambiente di sviluppo e la presenza di tutti i file necessari nella directory del progetto.
