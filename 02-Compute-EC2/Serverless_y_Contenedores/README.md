# Serverless y Contenedores 📦

Alternativas a EC2: AWS Lambda, ECS, EKS y Fargate para arquitecturas modernas.

## 📋 Contenido

Este módulo cubre:

- **AWS Lambda**: Funciones serverless
- **ECS**: Elastic Container Service
- **EKS**: Elastic Kubernetes Service
- **Fargate**: Serverless containers
- **ECR**: Elastic Container Registry

## 🎯 Conceptos Principales

### AWS Lambda
- Funciones sin servidor
- Triggers y eventos
- Concurrency y scaling automático
- Pricing: pay-per-use
- Lenguajes soportados

### Containers
- Docker basics
- Image management
- Registry (ECR)

### ECS
- Task definitions
- Services
- Launch types (EC2, Fargate)
- Scheduling

### EKS
- Kubernetes clusters
- Pods y deployments
- Ingress y services

### Fargate
- Serverless containers
- No EC2 management
- Pay-per-use pricing

## 🚀 Casos de Uso

| Servicio | Caso de Uso |
|----------|-----------|
| **Lambda** | Microservicios, APIs, procesamiento de eventos |
| **ECS** | Aplicaciones containerizadas, microservicios |
| **EKS** | Orquestación Kubernetes, aplicaciones complejas |
| **Fargate** | Containers sin gestión de infraestructura |

## 💡 Mejores Prácticas

✅ Usar Fargate para simplificar operaciones  
✅ Implementar Container Registry scanning  
✅ Configurar recursos apropiadamente  
✅ Usar CloudWatch para monitoreo  
✅ Implementar health checks  
✅ Documentar configuraciones  

## 📚 Recursos

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [ECS Documentation](https://docs.aws.amazon.com/ecs/)
- [EKS Documentation](https://docs.aws.amazon.com/eks/)
- [Fargate Documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/what-is-fargate.html)
- [Docker Documentation](https://docs.docker.com/)
