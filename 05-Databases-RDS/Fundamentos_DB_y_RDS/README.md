# Fundamentos de Bases de Datos y RDS 🗄️

Introducción a bases de datos relacionales y Amazon RDS.

## 📋 Contenido

Este módulo cubre:

- **Conceptos de BD**: Tablas, relaciones, normalización
- **SQL Basics**: SELECT, INSERT, UPDATE, DELETE
- **RDS Setup**: Lanzar instancias, configurar
- **Backup & Recovery**: PITR, snapshots
- **Security**: Encryption, IAM auth, security groups
- **Performance**: Indexes, query optimization

## 🎯 Laboratorios Incluidos

Laboratorios prácticos sobre fundamentos de bases de datos y RDS.

## 💾 Conceptos de Bases de Datos

### Elementos Básicos
- **Tables**: Estructura de datos
- **Rows**: Registros individuales
- **Columns**: Atributos
- **Primary Key**: Identificador único
- **Foreign Key**: Relaciones entre tablas
- **Indexes**: Optimización de búsqueda

### Normalización
- 1NF: Atomic values
- 2NF: No partial dependencies
- 3NF: No transitive dependencies
- BCNF: Boyce-Codd Normal Form

## 🚀 RDS Setup

### Crear una Instancia

```bash
aws rds create-db-instance \
  --db-instance-identifier mydb \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username admin \
  --master-user-password password123
```

### Configuración

- **Engine**: PostgreSQL, MySQL, etc.
- **Instance Class**: db.t3.micro, db.m5.large, etc.
- **Storage**: GP2, IO1, Aurora
- **Multi-AZ**: Disponibilidad
- **Backup Window**: Ventana de backup

## 🔐 Seguridad

### Encryption
- **At-rest**: KMS encryption
- **In-transit**: SSL/TLS
- **Transparent Data Encryption** (Oracle, SQL Server)

### Access Control
- **Security Groups**: Firewall
- **IAM DB Auth**: Token-based access
- **Database Users**: Permisos granulares

## 💡 Mejores Prácticas

✅ Usar Multi-AZ en producción  
✅ Habilitar automated backups (retención 7-35 días)  
✅ Crear snapshots antes de cambios grandes  
✅ Monitorear Enhanced Monitoring  
✅ Implementar read replicas para lectura escalar  
✅ Usar Parameter Groups para tuning  
✅ Habilitar Error Logs  

## 📚 Recursos

- [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [RDS Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Troubleshooting.html)
