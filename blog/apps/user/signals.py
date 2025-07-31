

def create_groups_and_permisssions(sender, instance, created, **kawars):
  if created and instance.is_superuser:
    try:
      pass
    except