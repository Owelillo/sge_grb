# Proyecto


## Creación del Modelo de Datos

### Definición del Modelo `subscription.metrics`

En primer lugar, definí un nuevo modelo llamado `subscription.metrics` para almacenar información sobre las suscripciones. Esta información incluye la cantidad de suscripciones activas, los ingresos generados, la tasa de renovación, cancelaciones y otras métricas clave.

![alt text](image.png)
### Creación de Campos

Agregué varios campos para almacenar los datos relevantes de cada métrica. Algunos campos son de tipo `Integer`, `Float`, `Date` y `Text`, dependiendo de la información que debía almacenar.

![alt text](image-1.png)

### Cálculo de Métricas

Para obtener valores derivados, implementé funciones computadas que recalculan tasas de renovación, cancelación y ARPU.

![alt text](image-2.png)


## Creación de Vistas en Odoo

### Vista de Lista (Tree View)

Para visualizar las métricas en un listado, definí una vista tipo `tree`.

![alt text](image-3.png)

### Vista de Formulario (Form View)

Para ver y editar registros individualmente, agregué una vista tipo `form`.

![alt text](image-4.png)



### Configuración de Permisos

Para gestionar permisos de usuario, creé un archivo `security/ir.model.access.csv` con permisos para acceder al modelo.

![alt text](image-5.png)


# ASÍ SE VE EL EJERCICIO

![alt text](image-6.png)

![alt text](image-7.png)