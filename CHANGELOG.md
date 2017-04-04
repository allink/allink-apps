# Changelog

# Test

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

## v0.0.8

### IMPORTANT

###### SETTINGS

###### TEMPLATES

###### URLS

###### REQUIREMENTS

###### DATA MIGRATIONS

### NEW

- config: New app added in allink_apps to store project specific settings. A migrations folder (`allink_apps_migrations.config`) is necessary in every project after this version.

### FIXES


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
