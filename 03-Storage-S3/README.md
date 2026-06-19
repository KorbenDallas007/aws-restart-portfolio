# Storage - S3 🪣

Amazon S3 (Simple Storage Service) es el servicio de almacenamiento de objetos más popular de AWS.

## 📁 Estructura de Carpetas

### [Almacenamiento_y_Archivado](./Almacenamiento_y_Archivado/)
Gestión de almacenamiento, access tiers y políticas de archivado.
- Storage classes (S3, Glacier, Deep Archive)
- Lifecycle policies
- Replicación

## 🎯 Objetivos de Aprendizaje

- Entender S3 storage classes
- Implementar políticas de acceso
- Configurar lifecycle management
- Optimizar costos de almacenamiento
- Implementar archivado automático

## 🔧 Conceptos Clave

### Storage Classes

| Clase | Uso | Costo | Latencia |
|-------|-----|-------|----------|
| **S3 Standard** | Datos frecuentes | Alto | Bajo |
| **S3 Standard-IA** | Infrecuente (30+ días) | Medio | Bajo |
| **S3 One Zone-IA** | Backup infrecuente | Bajo | Bajo |
| **S3 Intelligent-Tiering** | Variando acceso | Dinámico | Bajo |
| **S3 Glacier** | Archivado (horas) | Muy bajo | Alto |
| **S3 Deep Archive** | Archivado (12h) | Mínimo | Muy alto |

### Características

- **Buckets**: Contenedores de objetos
- **Objects**: Archivos con metadata
- **Keys**: Identificador único
- **Versioning**: Control de versiones
- **Lifecycle**: Transiciones automáticas
- **Replication**: DR y redundancia

## 💡 Mejores Prácticas

✅ Usar Intelligent-Tiering para cargas variadas  
✅ Implementar Lifecycle policies  
✅ Habilitar versioning para datos críticos  
✅ Usar S3 Transfer Acceleration  
✅ Implementar encryption (SSE-S3, SSE-KMS)  
✅ Monitorear costos con S3 Storage Lens  
✅ Implementar access logging  

## 📚 Recursos

- [S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Storage Classes Comparison](https://aws.amazon.com/s3/storage-classes/)
- [S3 Best Practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/BestPractices.html)
