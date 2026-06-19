# Servidores y Configuración Avanzada 🖥️

Configuración avanzada, optimización y gestión de instancias EC2.

## 📋 Contenido

Este módulo cubre:

- **Instance Types**: Selección y sizing
- **Storage Optimization**: EBS, Instance Store, S3
- **Performance Tuning**: CPU, memoria, red
- **Networking**: Elastic IPs, VPC configuration
- **Monitoring**: CloudWatch, metrics personalizadas
- **High Availability**: Multi-AZ, failover

## 🔧 Instance Types

### General Purpose (T, M)
- Balanced compute, memory, networking
- Ideal para web servers, small databases
- Ejemplos: t2.micro, m5.large

### Compute Optimized (C)
- High performance processors
- Ideal para batch processing, media encoding
- Ejemplos: c5.large, c6g.xlarge

### Memory Optimized (R, X)
- High memory-to-CPU ratio
- Ideal para databases, caches
- Ejemplos: r5.xlarge, x1.32xlarge

### Storage Optimized (I, D, H)
- High sequential read/write access
- Ideal para NoSQL, data warehouses
- Ejemplos: i3.large, d2.8xlarge

### GPU Instances (G, P)
- GPUs para ML, graphics rendering
- Ejemplos: g4dn.xlarge, p3.8xlarge

## 💾 Storage

### EBS (Elastic Block Store)
- gp3, gp2: General purpose
- io1, io2: High I/O
- st1, sc1: Throughput optimized

### Instance Store
- Temporal, high-performance
- Datos perdidos al stop/terminate

### S3
- Almacenamiento de objetos
- Persistent, durable

## 📊 Monitoreo

### CloudWatch Metrics
- CPU Utilization
- Network In/Out
- Disk Read/Write
- Custom metrics

### Alarmas
- Auto Scaling triggers
- SNS notifications
- Actions automáticas

## 💡 Mejores Prácticas

✅ Usar T2/T3 para workloads variables  
✅ Considerar Spot instances para cost-saving  
✅ Implementar monitoring proactivo  
✅ Optimizar sizing regularmente  
✅ Usar termination protection  
✅ Documentar configuraciones  
✅ Automatizar con Infrastructure as Code  

## 📚 Recursos

- [EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
- [EBS Best Practices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-best-practices.html)
- [Performance Optimization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
