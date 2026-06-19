# SageMaker y AI 🚀

Amazon SageMaker para entrenamiento, evaluación y despliegue de modelos de Machine Learning.

## 📋 Contenido

Este módulo cubre:

- **Notebooks SageMaker**: Exploración de datos
- **Training Jobs**: Entrenar modelos
- **Built-in Algorithms**: Algoritmos listos para usar
- **Hyperparameter Tuning**: Optimización automática
- **Model Deployment**: Endpoints en producción
- **Batch Transform**: Predicciones batch
- **Monitoring**: CloudWatch y Model Monitor

## 🎯 Laboratorios Incluidos

Laboratorios prácticos con Amazon SageMaker.

## 🏗️ Arquitectura SageMaker

```
┌─────────────────────────────────────┐
│   SageMaker Notebook Instance       │
│   (Exploración, prototipado)        │
└────────────┬────────────────────────┘
             │
             ↓
┌─────────────────────────────────────┐
│   Training Jobs                     │
│   - Built-in Algorithms             │
│   - Custom Containers               │
│   - Hyperparameter Tuning           │
└────────────┬────────────────────────┘
             │
             ↓
┌─────────────────────────────────────┐
│   Model Registry                    │
│   (Versioning, Metadata)            │
└────────────┬────────────────────────┘
             │
             ↓
┌─────────────────────────────────────┐
│   Deployment Options                │
│   - Real-time Endpoints             │
│   - Batch Transform                 │
│   - Edge Devices                    │
└─────────────────────────────────────┘
```

## 🔧 Componentes Principales

### Notebook Instances
```bash
# Crear instancia
aws sagemaker create-notebook-instance \
  --notebook-instance-name my-notebook \
  --instance-type ml.t3.medium
```

### Training
```python
import sagemaker
from sagemaker.estimator import Estimator

# Crear estimador
estimator = Estimator(
    image_uri=image,
    role=role,
    instance_count=1,
    instance_type='ml.m5.large',
    hyperparameters={...}
)

# Entrenar
estimator.fit(training_data)
```

### Deployment
```python
# Desplegar modelo
predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large'
)

# Hacer predicciones
predictions = predictor.predict(data)
```

## 📊 Algoritmos Built-in

### Regression
- Linear Learner
- XGBoost
- Neural Networks

### Classification
- XGBoost
- Linear Learner
- Gradient Boosting

### Clustering
- K-Means
- K-NN

### Dimensionality Reduction
- PCA
- AutoEncoder

### Sequence Models
- DeepAR+
- Seq2Seq

### Text Analysis
- BlazingText
- Sequence Labeling

### Computer Vision
- Image Classification
- Object Detection
- Semantic Segmentation

## 🤖 AutoML (SageMaker Autopilot)

```python
from sagemaker.automl.automl import AutoML

automl = AutoML(
    role=role,
    target_attribute_name='target',
    output_path=output_path,
    max_runtime_per_training_job=1800,
    max_total_job_runtime=3600
)

automl.fit(training_data)
```

## 📈 Hyperparameter Tuning

```python
from sagemaker.tuner import IntegerParameter, ContinuousParameter

hyperparameter_ranges = {
    'learning_rate': ContinuousParameter(0.001, 0.1),
    'max_depth': IntegerParameter(3, 10)
}

tuner = HyperparameterTuner(
    estimator=estimator,
    objective_metric_name='validation:accuracy',
    hyperparameter_ranges=hyperparameter_ranges,
    max_parallel_jobs=4,
    max_jobs=8
)

tuner.fit(training_data)
```

## 🚀 Mejores Prácticas

✅ Usar S3 para datos y modelos  
✅ Monitorear costos de instancias  
✅ Implementar versionado de modelos  
✅ Usar Model Monitor para drift detection  
✅ Documentar hyperparámetros  
✅ Automatizar con Pipelines  
✅ Implementar A/B testing en producción  
✅ Auditar decisiones del modelo  

## 📊 Monitoreo en Producción

### Model Monitor
- Data quality monitoring
- Model quality monitoring
- Bias drift detection
- Feature attribution

### CloudWatch Integration
- Logs y métricas
- Alarmas personalizadas
- Dashboards

## 📚 Recursos

- [SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/)
- [SageMaker Examples](https://github.com/aws/amazon-sagemaker-examples)
- [SageMaker Best Practices](https://docs.aws.amazon.com/sagemaker/latest/dg/best-practices.html)
