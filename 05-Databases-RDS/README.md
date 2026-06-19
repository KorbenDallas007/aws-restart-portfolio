# Databases - RDS 🗄️

Amazon RDS (Relational Database Service) - Bases de datos relacionales administradas.

## 📁 Estructura de Carpetas

### [Fundamentos_DB_y_RDS](./Fundamentos_DB_y_RDS/)
Conceptos fundamentales de bases de datos y RDS.
- SQL basics
- Database design
- RDS setup y configuration

### [Migracion_y_Servicios](./Migracion_y_Servicios/)
Migración de bases de datos y casos de uso avanzados.
- DMS (Database Migration Service)
- Multi-AZ failover
- Read replicas

## 🎯 Objetivos de Aprendizaje

- Comprender bases de datos relacionales
- Lanzar instancias RDS
- Configurar backup y recovery
- Implementar Multi-AZ para HA
- Migrar databases a AWS
- Optimizar performance

## 🔧 Conceptos Clave

### Motores Soportados
- MySQL / MariaDB
- PostgreSQL
- Oracle
- SQL Server
- Aurora

### Características

- **Managed Service**: Patching, backup automático
- **Multi-AZ**: Alta disponibilidad
- **Read Replicas**: Escalado de lectura
- **Automated Backups**: PITR (Point-in-Time Recovery)
- **Encryption**: At-rest y in-transit
- **IAM DB Auth**: Autenticación sin passwords

## 💡 Mejores Prácticas

✅ Usar Multi-AZ para producción  
✅ Habilitar automated backups  
✅ Implementar read replicas para lectura  
✅ Usar encryption en tránsito y reposo  
✅ Monitorear Enhanced Monitoring  
✅ Implementar connection pooling  
✅ Optimizar queries y indexes  
✅ Considerar Aurora para performance  

## 📊 Comparativa de Motores

| Motor | Caso de Uso | Costo |
|-------|-----------|-------|
| **PostgreSQL** | Open-source, advanced features | Bajo |
| **MySQL** | Web apps, ecommerce | Bajo |
| **Aurora** | High-performance, scale-out | Medio |
| **Oracle** | Enterprise, legacy | Alto |
| **SQL Server** | Windows ecosystem | Muy Alto |

## 📚 Recursos

- [RDS Documentation](https://docs.aws.amazon.com/rds/)
- [RDS Best Practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html)
- [Aurora Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/)
- [DMS Documentation](https://docs.aws.amazon.com/dms/)
