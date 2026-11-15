terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}
variable "instance_count" {
  type    = number
  default = 3
}
resource "local_file" "server_config" {
  count    = var.instance_count
  filename = "${path.module}/server-${count.index + 1}.txt"
  content  = "Server ${count.index + 1} provisioned using Terraform"
}
output "provisioned_servers" {
  value = local_file.server_config[*].filename
}
