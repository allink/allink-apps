# Changelog

Each release is divided into the following main categories:

- IMPORTANT: These changes might not be backward compatible and require updating existing code. (If not applied correctly your update will fail)
    - SETTINGS: change your setting.py accordingly
    - TEMPLATES: if templates form allink_core are overridden, you have to double apply these changes
    - URLS: changes to urls.py
    - REQUIREMENTS: new or changed requirements
    - DATA MIGRATIONS: stuff to migrate by hand or create data migrations manually
- NEW: New features or plugins
- FIXES: General bugfixes

The version numbers referring to the version in [allink_core](git@github.com/allink/allink-core.git).

## v0.0.10 (under development)

### IMPORTANT

###### SETTINGS
- Contact Form: `TIME_CHOICES` (in `allink_apps/contact/models.py`) had to be updated for the core development project. If you require the old default, make sure to adjust the time choices after updating allink_apps:
```python
TIME_CHOICES = (
    (None, _(u'-- between --')),
    (1, u'08:00-10:00'),
    (2, u'10:00-12:00'),
    (3, u'12:00-14:00'),
    (4, u'14:00-16:00'),
    (5, u'16:00-18:00'),
    (6, u'18:00-20:00'),
)
```

###### TEMPLATES
- people job_function (which it was used in teojakob for example) was substituted with property 'units'. You now have to add categories (with identifier='units') and tag th person with it. this allowes us to categories people without having to maintain both fields 'unit' and categories

###### URLS

###### REQUIREMENTS

###### DATA MIGRATIONS
- update with caution in projects whcih still use inline images to display galleries (hdf, mfgz, ..?) we added a field preview_image (not a property anymore) the galleries are now added as a plugin inside the content_palceholder
 -> and if you update make sure you migrate the images! (see data_migrations/0017_migrate_preview_image.py)

### NEW

- App Content Template: `app_content.html` added. All plugin templates (grid_static, list, ...) should from now on extend from this template instead of `app_content_base.html` (both work, but `app_content_base.html` can NOT be overwritten on a project basis). Globally modifying block content can now be done by adding a `/templates/app_content/app_content.html` file in your project folder.

### FIXES

## v0.0.9

### IMPORTANT

###### SETTINGS

###### TEMPLATES

###### URLS

###### REQUIREMENTS

###### DATA MIGRATIONS

- when making migrations on projects it's important, that the field "active" on each model gets renamed to "is_active".
  The field must not be deleted and created as new, else data gets lost

### NEW

- Contact Form: The dataLayer event `contact-form.sent` has been added for Google Tag Manager.
- Forms: The `form.html` template is not extended from `form_base.html` (which of course has various `blocks`) for easier project specific changes.

### FIXES

- Members Plugin: Templates in progress
- Members Plugin: allauth account views return success url or renderd template
    - needs testing in project with member app
- field "active" renamed to "is_active" on all models
- category nav in case no categories are selected fixed
- Clases inherting from Base Model: Separated filter and categories fieldsets, applied default ordering on querysets
- Made opening hours field in locations app translatable

## v0.0.8

### IMPORTANT

###### SETTINGS

###### TEMPLATES

###### URLS

###### REQUIREMENTS

###### DATA MIGRATIONS

- all apps now have logic for showing the detail gallery (if a gallery is added in header_content placeholder it will be displayed in favor of the inline_images form model.) Also the max_count of the inline is set to one! (So future Galleries have to be )
- testemonials: firstname and lastname are not translated anymore.
    - migration "0000_testemonials_migrate_firstname_lastname.py", including datamigration for this change can be found in "allink_apps.data_migrations". Ajust number for projects.
    - The fields old_lastname and old_firstname can be removed in a next release

### NEW

- config: New app added in allink_apps to store project specific settings. A migrations folder (`allink_apps_migrations.config`) is necessary in every project after this version.
- python 3 compatibility



### FIXES
- people: manager was still looking for field "lastname". is now looking for it correctly on the main table.


## v0.0.7

### IMPORTANT

###### SETTINGS

###### TEMPLATES
- allink_locations: text field removed and lead added.

###### URLS

###### REQUIREMENTS

###### DATA MIGRATIONS
- people: firstname and lastname are not translated anymore.
    - migration "0019_migrate_firstname_lastname.py", including datamigration for this change can be found in "allink_apps.data_migrations". Ajust number for projects.
    - The fields old_lastname and old_firstname can be removed in a next release
- allink_locations: text field removed and lead added. (migrate location text)

### NEW
- When creating a new News or Event entry the category News or Events is set as an initial value in the form.
- App Plugins now support AND operator for filtering categories

### FIXES
- Replaced TranslatedAutoSlugifyMixin by AllinkTranslatedAutoSlugifyMixin in all apps. This tries not to use default slugs.


## v0.0.6

### IMPORTANT

###### SETTINGS

###### TEMPLATES

###### URLS

###### REQUIREMENTS

###### DATA MIGRATIONS

### NEW
- header_placeholder added to all apps

### FIXES
