from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from apps.post.models import Post, Comment
from apps.user.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_groups_and_permisssions(sender, instance, created, **kawars):
  if created and instance.is_superuser:
    try:
      # TODO: Definir los permisos de POST y de COMMENTS
      post_content_type = ContentType.objects.get_for_model(Comment)
      comment_content_type = ContentType.objects.get_for_model(Comment)

      #Permisos de POST
      viem_post_permission = Permission.objects.get(codename = 'view_post', content_type = post_content_type)
      add_post_permission = Permission.objects.get(codename = 'add_post', content_type = post_content_type)
      change_post_permission = Permission.objects.get(codename = 'change_post', content_type = post_content_type)
      delete_post_permission = Permission.objects.get(codename = 'delete_post', content_type = post_content_type)

      # permisos de COMMENTS
      view_comments_permission = Permission.objects.get(codename = 'view_comments', content_type = comment_content_type)
      add_comments_permission = Permission.objects.get(codename = 'add_comments', content_type = comment_content_type)
      change_comments_permission = Permission.objects.get(codename = 'change_pos', content_type = comment_content_type)
      delete_comments_permission = Permission.objects.get(codename = 'delete_post', content_type = comment_content_type)


      # crear grupos de usuarios registrados
      registered_group, created = Group.objects.get_or_create(name="Registered")
      registered_group.permissions.add(
        viem_post_permission, 
        view_comments_permission,
        add_comments_permission,
        change_comments_permission,
        delete_comments_permission,
          # permiso para ver post
          # permiso para ver comentarios del post
          # permiso para crear comentarios del post
          # permiso para actualizar de su comentario en un post
          # permiso para borrar su comentario en un post
       )

      # crear grupos de usuarios colaboradores
      registered_group, created = Group.objects.get_or_create(name="Collaborators")
      registered_group.permissions.add(
        viem_post_permission, 
        add_post_permission,
        change_post_permission,
        delete_post_permission,
        view_comments_permission,
        add_comments_permission,
        change_comments_permission,
        delete_comments_permission,        
          # permiso para ver post
          # permiso para crear post
          # permiso para actualizar su post
          # permiso para borrar su post
          # permiso para ver comentarios del post
          # permiso para crear comentarios del post
          # permiso para actualizar de su comentario en un post
          # permiso para borrar su comentario en un post
       )


          # crear grupos de usuarios administradores
      registered_group, created = Group.objects.get_or_create(name="Admins")
      registered_group.permissions.add(
        viem_post_permission, 
        add_post_permission,
        change_post_permission,
        delete_post_permission,
        view_comments_permission,
        add_comments_permission,
        change_comments_permission,
        delete_comments_permission,
          # permiso para ver post
          # permiso para crear post
          # permiso para actualizar su post
          # permiso para borrar cualquier post
          # permiso para ver comentarios del post
          # permiso para crear comentarios del post
          # permiso para actualizar de su comentario en un post
          # permiso para borrar su comentario de cualquier post
       )
       
      print("Grupos y Permisos creados exitosamente")
    except ContentType.DoesNotExist:
      print("El tipo aun no se encuentra disponible.")
    except Permission.DoesNotExist:
      print("Uno o mas permisos no se encuentran disponibles")

    except:
      pass