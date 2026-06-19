# Almacenamiento y Archivado 📦

Gestión avanzada de almacenamiento S3, lifecycle policies y estrategias de archivado.

## 📋 Contenido

Este módulo cubre:

- **Storage Classes**: Selección apropiada
- **Lifecycle Policies**: Transiciones automáticas
- **Archivado**: Glacier y Deep Archive
- **Replicación**: Cross-region replication
- **Análisis**: S3 Storage Lens y cost optimization

## 🎯 Laboratorios Incluidos

Laboratorios prácticos sobre gestión de almacenamiento y archivado en S3.

## 📊 Estrategia de Archivado

### Patrón Recomendado

```
S3 Standard (0-30 días)
        ↓
S3 Standard-IA (30-90 días)
        ↓
S3 Glacier (90-365 días)
        ↓
S3 Deep Archive (365+ días)
```

### Lifecycle Policy Example

```json
{
  "Rules": [
    {
      "Id": "Archive after 90 days",
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "STANDARD_IA"
        },
        {
          "Days": 90,
          "StorageClass": "GLACIER"
        },
        {
          "Days": 365,
          "StorageClass": "DEEP_ARCHIVE"
        }
      ]
    }
  ]
}
```

## 💡 Casos de Uso

- **Backup & DR**: Glacier/Deep Archive
- **Compliance**: Versioning + Lock
- **Data Lake**: Intelligent-Tiering
- **Content Distribution**: S3 + CloudFront
- **Log Storage**: S3 Standard-IA

## 💰 Optimización de Costos

✅ Usar S3 Storage Lens para análisis  
✅ Implementar Intelligent-Tiering  
✅ Aprovechar Lifecycle policies  
✅ Usar One Zone-IA para backup  
✅ Consolidar buckets cuando sea posible  
✅ Revisar objetivos de recuperación (RTO/RPO)  

## 📈 Monitoreo

- **S3 Storage Lens**: Dashboard de costos
- **CloudWatch**: Metrics de acceso
- **CloudTrail**: Auditoría de acciones
- **S3 Access Logging**: Registro de solicitudes

## 📚 Recursos

- [Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Glacier Documentation](https://docs.aws.amazon.com/amazonglacier/)
- [Cost Optimization](https://docs.aws.amazon.com/AmazonS3/latest/userguide/managing-storage.html)
