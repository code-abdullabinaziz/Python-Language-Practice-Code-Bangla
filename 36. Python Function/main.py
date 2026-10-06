roles = ["admin", "user", "admin", "moderator", "user", "admin"]

roles_count = {}

for role in roles:
  roles_count.setdefault(role, 0)
  roles_count[role] += 1
  
print(roles_count)

