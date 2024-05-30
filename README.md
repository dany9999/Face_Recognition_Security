# Face Recognition Security

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
```

## Istruzione per l'Esecuzione 
### Preparazione del Test Set Cropped
Prima di eseguire qualsiasi attacco, è necessario preparare le immagini croppate del set di test. Esegui lo script face_crop.py:

 ```bash
python face_crop.py
```
Questo script processerà le immagini nella cartella test_set/ e salverà le versioni croppate nella cartella test_set_cropped/.

### Esecuzione attacchi 
Per eseguire un attacco, apri il notebook corrispondente e avvialo. Ogni notebook eseguirà l'attacco specificato sulle immagini croppate del set di test.

  Attacco DeepFool: apri DeepFool.ipynb e esegui tutte le celle.
  Attacco Carlini-Wagner: apri CarliniWagner.ipynb e esegui tutte le celle.
  Attacco PGD mirato: apri PGD_targeted.ipynb e esegui tutte le celle.
  Attacco PGD non mirato: apri PGD_untargeted.ipynb e esegui tutte le celle.
  
### Test delle Reti Neurali sul Test Set Clean
Per testare le reti neurali NN1 e NN2 sul set di test pulito, apri i rispettivi notebook e avviali.

  Test di NN1 (Inception ResNet v1): apri test_clean_NN1.ipynb e esegui tutte le celle.
  Test di NN2 (ResNet50): apri test_clean_NN2.ipynb e esegui tutte le celle.

## Dettagli Tecnici
NN1 (Inception ResNet v1): Definita nello script inception.py.
NN2 (ResNet50): Definita nello script resnet.py.
Funzionalità Utili: Contenute nello script utils.py, che viene richiamato nei vari notebook per eseguire operazioni comuni come la pre-elaborazione delle immagini e la valutazione delle prestazioni delle reti.

## Note Finali
Assicurati di eseguire tutti gli script e i notebook nell'ordine corretto per garantire che i dati siano processati correttamente e che i risultati degli attacchi siano validi. Per qualsiasi dubbio o problema, verifica la corretta configurazione dell'ambiente di sviluppo e la presenza di tutti i file necessari nella directory del progetto.
