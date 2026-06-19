# Seguridad e IAM 🔐

Identity and Access Management fundamentals y security best practices en AWS.

## 📋 Contenido

Este módulo cubre:

- **IAM Users**: Creación y administración
- **Groups**: Organización de usuarios
- **Roles**: Acceso temporal y delegado
- **Policies**: Permisos granulares
- **MFA**: Autenticación multifactor
- **Access Analysis**: Auditoría de permisos

## 🎯 Conceptos Principales

### IAM Users
- Acceso programático (API keys)
- Acceso a consola (contraseña)
- Credentials rotación
- Access keys versionadas

### IAM Groups
- Membresía múltiple
- Policies adosadas
- Gestión simplificada

### IAM Roles
- AssumeRole para delegación
- Temporal credentials (STS)
- Cross-account access
- Service principals

### Policies

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::bucket-name/*"
    }
  ]
}
```

## 💡 Mejores Prácticas

✅ Nunca usar root account  
✅ Implementar MFA para privileged users  
✅ Usar roles en lugar de hardcoded keys  
✅ Rotar keys cada 90 días  
✅ Implementar least privilege  
✅ Usar AWS Secrets Manager  
✅ Regular access reviews  
✅ Usar CloudTrail para auditoría  

## 🔒 Seguridad

### MFA
- Virtual MFA devices
- Hardware MFA
- U2F security keys

### Credential Management
- AWS Secrets Manager
- Systems Manager Parameter Store
- AWS Config

## 📚 Recursos

- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [IAM Policies Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)
- [IAM Policy Examples](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html)
