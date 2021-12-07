#
# Jalgraves
# 2021
#

output "labels" {
  value = one(data.external.labels[*].result)
}
