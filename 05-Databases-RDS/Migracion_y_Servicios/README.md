# Migración y Servicios Avanzados 🚀

Migración de bases de datos a RDS y características avanzadas de disponibilidad.

## 📋 Contenido

Este módulo cubre:

- **Database Migration Service (DMS)**: Migración de DBs
- **Multi-AZ**: Alta disponibilidad automática
- **Read Replicas**: Escalado de lectura
- **Aurora**: Motor de alta performance
- **Disaster Recovery**: Failover y PITR
- **Performance Tuning**: Optimización avanzada

## 🎯 Laboratorios Incluidos

### Lab 179 - Migración a Amazon RDS
Guía completa para migrar una base de datos on-premises a RDS.

## 🔄 Estrategias de Migración

### Lift and Shift (Homogeneous)
- Mismo motor: MySQL a MySQL
- Herramienta: AWS DMS
- Downtime: Mínimo
- Complejidad: Baja

### Modernización (Heterogeneous)
- Diferentes motores: Oracle a PostgreSQL
- Herramienta: AWS Schema Conversion Tool (SCT)
- Downtime: Variable
- Complejidad: Alta

### Pasos de Migración

1. **Assessment**: Evaluar database actual
2. **Planning**: Definir estrategia
3. **Schema Conversion**: SCT para cambios estructura
4. **Data Migration**: DMS para datos
5. **Testing**: Validar integridad
6. **Cutover**: Switchover final
7. **Monitoring**: Post-migration support

## 🏗️ Arquitectura de Alta Disponibilidad

### Multi-AZ Configuration

```
Primary DB (AZ-1)
    ↓ (Synchronous Replication)
Standby DB (AZ-2)
    ↓ (Auto Failover)
Secondary DB (AZ-3)
```

- Failover automático: 60-120 segundos
- Zero data loss: Replicación síncrona
- Transparente para aplicaciones

### Read Replicas

- Replicación asíncrona
- Lecturas escaladas
- Cross-region available
- Promovible a standalone

## 🔧 AWS DMS

### Fuentes Soportadas
- Oracle, MySQL, PostgreSQL
- SQL Server, Teradata
- MongoDB, DynamoDB
- S3, Kafka

### Objetivos Soportados
- RDS (todos los motores)
- Aurora
- Redshift
- DynamoDB
- ElastiCache

## 💡 Mejores Prácticas

✅ Usar DMS para migración sin downtime  
✅ Validar datos después de migración  
✅ Usar Multi-AZ para HA inmediata  
✅ Implementar read replicas para backups  
✅ Considerar Aurora para nueva infraestructura  
✅ Testear failover regularmente  
✅ Monitorear performance post-migración  
✅ Documentar cambios y configuración  

## 📊 Comparativa

| Aspecto | Multi-AZ | Read Replicas |
|--------|----------|----------------|
| **Propósito** | HA | Escalado lectura |
| **Replicación** | Síncrona | Asíncrona |
| **Failover** | Automático | Manual |
| **Datacenters** | Múltiple | Flexible |
| **Performance** | Igual | Mejor lectura |

## 📚 Recursos

- [DMS Documentation](https://docs.aws.amazon.com/dms/)
- [Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/)
- [Multi-AZ Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)
- [Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
