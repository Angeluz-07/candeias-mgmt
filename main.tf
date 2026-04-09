# --------------------------------------------------------------------------
# 1. DEFINICIÓN DE VARIABLES (Para fácil mantenimiento)
# --------------------------------------------------------------------------
variable "project_id" {}
variable "region" {}
variable "service_name" {}
variable "docker_image" {}


# --------------------------------------------------------------------------
# 2. CONFIGURACIÓN DEL PROVEEDOR
# --------------------------------------------------------------------------
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  # Ruta a tu llave JSON descargada de GCP
  credentials = file("credentials.json") 
  project     =  var.project_id
}


# --------------------------------------------------------------------------
# 3. RECURSO: CLOUD RUN (BACKEND)
# --------------------------------------------------------------------------
resource "google_cloud_run_v2_service" "backend" {
  name     = var.service_name
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    scaling {
      min_instance_count = 0  
      max_instance_count = 5  # Límite para controlar costos
    }

    containers {
      image = var.docker_image

      # Especificar el puerto que usa tu app (ej: 8000 para FastAPI)
      ports {
        container_port = 8000 
      }

      resources {
        limits = {
          cpu    = "1"
          memory = "512Mi"
        }
        cpu_idle = true  # <--- Esto fuerza el "Basado en solicitudes"
      }
     
      # Aquí podrías añadir variables de entorno en el futuro
      # env {
      #   name  = "DATABASE_URL"
      #   value = "..."
      # }
    }
  }
}

# --------------------------------------------------------------------------
# 4. PERMISOS: HACER LA API PÚBLICA
# --------------------------------------------------------------------------
resource "google_cloud_run_v2_service_iam_member" "public_access" {
  project  = google_cloud_run_v2_service.backend.project
  location = google_cloud_run_v2_service.backend.location
  name     = google_cloud_run_v2_service.backend.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}

# --------------------------------------------------------------------------
# 5. OUTPUTS (Resultados en consola)
# --------------------------------------------------------------------------
output "backend_url" {
  value       = google_cloud_run_v2_service.backend.uri
  description = "URL pública del backend en producción"
}