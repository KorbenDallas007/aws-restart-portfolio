param (
    [Parameter(Mandatory=$true, HelpMessage="Por favor, ingresa el mensaje del commit")]
    [string]$Mensaje
)

Write-Host "?? Iniciando proceso de automatización DevOps..." -ForegroundColor Cyan

# 1. Agregar todos los cambios
git add .

# 2. Hacer el commit
git commit -m "feat(aws): $Mensaje"

# 3. Subir a GitHub
git push -u origin main

Write-Host "? ¡Portafolio sincronizado exitosamente en GitHub!" -ForegroundColor Green
