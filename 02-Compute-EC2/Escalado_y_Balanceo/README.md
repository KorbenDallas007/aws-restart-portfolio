# Escalado y Balanceo de Carga ⚖️

Implementación de alta disponibilidad y escalabilidad automática en AWS.

## 📋 Contenido

Este módulo cubre:

- **Auto Scaling**: Escalado automático de recursos
- **Load Balancing**: Distribución de tráfico
- **Failover**: Redundancia y recuperación
- **Health Checks**: Monitoreo de instancias
- **Traffic Routing**: Estrategias avanzadas

## 🎯 Laboratorios Incluidos

### Lab 174 - Escalado y Balanceo de Carga de una Arquitectura
Implementar una arquitectura escalable con ELB.

### Lab 175 - Uso de Escalado Automático en AWS (Linux)
Configurar Auto Scaling Groups con políticas dinámicas.

### Lab 176 - Route 53 Failover Routing (JAWS)
Implementar DNS failover con Route 53.

## 🔧 Componentes Clave

### Load Balancers

- **Classic Load Balancer (CLB)**: Layer 4 (Deprecated)
- **Application Load Balancer (ALB)**: Layer 7 (HTTP/HTTPS)
- **Network Load Balancer (NLB)**: Layer 4 (Ultra-high performance)
- **Gateway Load Balancer (GWLB)**: Network appliances

### Auto Scaling

- **Scaling Policies**: Target tracking, Step scaling, Simple scaling
- **Lifecycle Hooks**: Acciones personalizadas
- **Warm Pools**: Pre-warmed instances

### Route 53

- **DNS Failover**: Active-passive failover
- **Health Checks**: Endpoint monitoring
- **Routing Policies**: Latency, Geolocation, etc.

## 💡 Mejores Prácticas

✅ Usar ALB para aplicaciones web  
✅ Usar NLB para ultra-high performance  
✅ Configurar health checks apropiadamente  
✅ Implementar target tracking scaling  
✅ Usar multiple AZs para redundancia  
✅ Monitorear CloudWatch metrics  

## 📚 Recursos

- [ELB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/)
- [Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/)
- [Route 53 Documentation](https://docs.aws.amazon.com/route53/)
