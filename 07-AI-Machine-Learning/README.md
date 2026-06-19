# AI & Machine Learning 🤖

Introducción a Machine Learning y AI con AWS SageMaker y herramientas de ML.

## 📁 Estructura de Carpetas

### [SageMaker_y_AI](./SageMaker_y_AI/)
Laboratorios prácticos con Amazon SageMaker.
- Training de modelos
- Deployment y inference
- AutoML
- Feature engineering

## 🎯 Objetivos de Aprendizaje

- Entender conceptos fundamentales de ML
- Usar SageMaker para entrenamiento y predicción
- Implementar pipelines de ML
- Desplegar modelos en producción
- Trabajar con datasets y preprocesamiento

## 🤖 Conceptos de Machine Learning

### Tipos de Aprendizaje

- **Supervised Learning**: Datos etiquetados
  - Regression: Predecir valores continuos
  - Classification: Predecir categorías

- **Unsupervised Learning**: Datos sin etiquetar
  - Clustering: Agrupar datos similares
  - Dimensionality Reduction: Reducir características

- **Reinforcement Learning**: Aprender por recompensas

### Flujo Típico de ML

```
Datos Crudos
    ↓
Limpieza y Preparación (EDA)
    ↓
Feature Engineering
    ↓
Entrenamiento
    ↓
Evaluación
    ↓
Tuning e Hiperparámetros
    ↓
Deployment
    ↓
Monitoreo
```

## 🛠️ Herramientas y Servicios

### AWS SageMaker

- **Notebooks**: Jupyter para exploración
- **Training**: Entrenamiento distribuido
- **Built-in Algorithms**: XGBoost, Linear Learner, etc.
- **AutoML**: SageMaker Autopilot
- **Endpoints**: Despliegue de modelos
- **Pipelines**: Orquestación de workflows

### Frameworks

- TensorFlow / Keras
- PyTorch
- scikit-learn
- XGBoost
- LightGBM

## 📊 Datasets Populares

| Dataset | Uso | Tamaño |
|---------|-----|--------|
| **MNIST** | Dígitos manuscritos | 70K imágenes |
| **CIFAR-10** | Objetos clasificación | 60K imágenes |
| **ImageNet** | Millones de imágenes | 14M+ imágenes |
| **Iris** | Flores clasificación | 150 muestras |
| **Titanic** | Predicción de supervivencia | 892 registros |

## 💡 Mejores Prácticas

✅ Dividir datos: Train (70%), Val (15%), Test (15%)  
✅ Normalizar/Estandarizar features  
✅ Detectar y manejar outliers  
✅ Evitar data leakage  
✅ Usar cross-validation  
✅ Documentar experimentos  
✅ Monitorear modelo en producción  
✅ Implementar retraining automático  

## 📈 Métricas de Evaluación

### Regresión
- MAE: Mean Absolute Error
- RMSE: Root Mean Square Error
- R²: Coeficiente de determinación

### Clasificación
- Accuracy: Precisión general
- Precision: Verdaderos positivos
- Recall: Detección de positivos
- F1-Score: Balance precision-recall
- ROC-AUC: Curva ROC

## 📚 Recursos

- [AWS SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/)
- [Machine Learning Mastery](https://machinelearningmastery.com/)
- [Coursera ML Course](https://www.coursera.org/learn/machine-learning)
- [Fast.ai](https://www.fast.ai/)
- [Kaggle Competitions](https://www.kaggle.com/competitions)
