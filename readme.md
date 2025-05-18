# MF-FLow

MLOps adalah membangun pipeline otomatis untuk melatih, mengevaluasi, dan men-deploy model ML secara berkelanjutan (CI/CD untuk ML). Tools seperti MLflow, Kubeflow, atau Airflow bisa sangat berguna.

 MLflow adalah tool penting untuk melacak eksperimen ML (parameter, metrik, artefak) dan mengelola reproducibility proyek.  mencatat hasil eksperimen Anda, dan MLflow Projects untuk mengemas kode ML Anda agar dapat direproduksi di berbagai lingkungan. Integrasikan MLflow ke dalam workflow TensorFlow dan LLM Anda.


apt install python3.10-venv
python3 -m venv venv
source /venv/bin/activate


pip install mlflow

![ss](./screenshoot/1.png)


mlflow ui

![ss](./screenshoot/2.png)

![ss](./screenshoot/3.png)


python3 train.py

[ss](./screenshoot/4.png)


[ss](./screenshoot/5.png)


