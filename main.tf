# 1. Configuración de Terraform y Proveedor
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# 2. Grupo de Recursos
resource "azurerm_resource_group" "rg_fitness" {
  name     = "rg-${var.project_name}"
  location = var.location
}

# 3. Log Analytics
resource "azurerm_log_analytics_workspace" "logs" {
  name                = "log-${var.project_name}"
  location            = azurerm_resource_group.rg_fitness.location
  resource_group_name = azurerm_resource_group.rg_fitness.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

# 4. Entorno de Container Apps
resource "azurerm_container_app_environment" "env" {
  name                       = "env-${var.project_name}"
  location                   = azurerm_resource_group.rg_fitness.location
  resource_group_name        = azurerm_resource_group.rg_fitness.name
  log_analytics_workspace_id = azurerm_log_analytics_workspace.logs.id
}

# 5. API REST Serverless
resource "azurerm_container_app" "api" {
  name                         = "api-${var.project_name}"
  container_app_environment_id = azurerm_container_app_environment.env.id
  resource_group_name          = azurerm_resource_group.rg_fitness.name
  revision_mode                = "Single"

  template {
    container {
      name   = "python-api"
      image  = var.docker_image
      cpu    = 0.25
      memory = "0.5Gi"
    }
    
    min_replicas = 0
    max_replicas = 1
  }

  ingress {
    external_enabled = true
    target_port      = var.container_port
    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }
}

# 6. Frontend (Azure Static Web App)
resource "azurerm_static_web_app" "frontend" {
  name                = "stapp-${var.project_name}"
  resource_group_name = azurerm_resource_group.rg_fitness.name
  location            = azurerm_resource_group.rg_fitness.location
  sku_tier            = "Free"
  sku_size            = "Free"
}

# 7. Outputs
output "frontend_url" {
  value = azurerm_static_web_app.frontend.default_host_name
}

output "api_url" {
  value = azurerm_container_app.api.latest_revision_fqdn
}

output "deployment_token" {
  value     = azurerm_static_web_app.frontend.api_key
  sensitive = true
}