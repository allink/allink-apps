# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import activate
from django.db import migrations


# migrate work to allink djangocms_image
def migrate_images(apps, schema_editor):
    activate('de')
# WORK
    Work = apps.get_model("work", "work")
    WorkImage = apps.get_model("work", "workImage")

    for work in Work.objects.all():
        preview_image = WorkImage.objects.filter(work=work).first()
        Work.objects.filter(id=work.id).update(preview_image=preview_image.image)
# BLOG
    Blog = apps.get_model("blog", "Blog")
    BlogImage = apps.get_model("blog", "BlogImage")

    for blog in Blog.objects.all():
        preview_image = BlogImage.objects.filter(blog=blog).first()
        Blog.objects.filter(id=blog.id).update(preview_image=preview_image.image)

# LOCATIONS
    Locations = apps.get_model("locations", "Locations")
    LocationsImage = apps.get_model("locations", "LocationsImage")

    for location in Locations.objects.all():
        preview_image = LocationsImage.objects.filter(location=location).first()
        Locations.objects.filter(id=location.id).update(preview_image=preview_image.image)

# PEOPLE
    People = apps.get_model("people", "People")
    PeopleImage = apps.get_model("people", "PeopleImage")

    for people in People.objects.all():
        preview_image = PeopleImage.objects.filter(people=people).first()
        People.objects.filter(id=people.id).update(preview_image=preview_image.image)

# TESTIMONIAL
    Testimonial = apps.get_model("testimonials", "Testimonial")
    TestimonialImage = apps.get_model("testimonials", "TestimonialImage")

    for testimonial in Testimonial.objects.all():
        preview_image = TestimonialImage.objects.filter(testimonial=testimonial).first()
        Testimonial.objects.filter(id=testimonial.id).update(preview_image=preview_image.image)

# SERVICES
    Services = apps.get_model("services", "Services")
    ServicesImage = apps.get_model("services", "ServicesImage")

    for services in Services.objects.all():
        preview_image = ServicesImage.objects.filter(services=services).first()
        Services.objects.filter(id=services.id).update(preview_image=preview_image.image)

# TOPICS
    Topics = apps.get_model("topics", "Topics")
    TopicsImage = apps.get_model("topics", "TopicsImage")

    for topics in Topics.objects.all():
        preview_image = TopicsImage.objects.filter(topics=topics).first()
        Topics.objects.filter(id=topics.id).update(preview_image=preview_image.image)


def do_nothing(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_blog_preview_image'),
        ('locations', '0013_locations_preview_image'),
        ('people', '0017_people_preview_image'),
        ('testimonials', '0013_testimonial_preview_image'),
        ('work', '0017_auto_20170503_1429'),
        ('services', '0003_services_preview_image'),
        ('topics', '0005_topics_preview_image'),
    ]

    operations = [
        migrations.RunPython(migrate_images, do_nothing),
    ]
