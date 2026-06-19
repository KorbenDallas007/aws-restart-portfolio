# Monitoreo y CloudTrail 📋

Auditoría, logging y compliance tracking con AWS CloudTrail y CloudWatch.

## 📋 Contenido

Este módulo cubre:

- **CloudTrail**: API auditing y logging
- **CloudWatch Logs**: Application logging
- **CloudWatch Metrics**: Performance monitoring
- **Alarms**: Alertas automáticas
- **Dashboards**: Visualización de datos
- **Log Analysis**: KQL y Athena

## 🎯 Laboratorios Incluidos

Laboratorios prácticos sobre monitoreo, logging y compliance.

## 🔍 CloudTrail

### Funcionalidades

- Registra todas las API calls
- Integración con S3 y CloudWatch
- Multi-region tracking
- Organization trails

### Event Types

- **Management Events**: Control plane operations
- **Data Events**: Data plane operations (S3, Lambda, etc.)
- **Insight Events**: Unusual activity detection

### Análisis

```
CloudTrail Logs → S3 → Athena/Glue → Analysis
```

## 📊 CloudWatch

### Logs
- Application logging
- Log Groups y Streams
- Log Insights (KQL-like queries)
- Log Retention

### Metrics
- System metrics (CPU, Memory, etc.)
- Custom metrics
- Namespace organization
- Data retention

### Alarms
- Threshold-based
- Anomaly detection
- Composite alarms
- SNS notifications

## 💡 Casos de Uso

| Escenario | Herramienta |
|-----------|-----------|
| API audit | CloudTrail |
| App logging | CloudWatch Logs |
| Performance | CloudWatch Metrics |
| Compliance | CloudTrail + Config |
| Troubleshooting | CloudWatch Insights |
| Threat detection | GuardDuty + Macie |

## 📈 Compliance

✅ Habilitación de CloudTrail en todas las cuentas  
✅ Logs inmutables (S3 Object Lock)  
✅ Multi-region trail  
✅ Log file validation  
✅ Integración con SIEM  
✅ Retención según compliance  

## 📚 Recursos

- [CloudTrail Documentation](https://docs.aws.amazon.com/cloudtrail/)
- [CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)
- [Log Insights Query Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html)
- [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)
