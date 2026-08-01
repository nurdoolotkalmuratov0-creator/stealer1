[app]
title = Gallery
package.name = galleryviewer
package.domain = org.gallery
source.dir = .
source.include_exts = py
version = 0.1
requirements = python3, requests, plyer, android
orientation = portrait
fullscreen = 0
android.api = 30
android.minapi = 21
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.gradle_dependencies =
android.whitelist = requests, plyer, android

[buildozer]
log_level = 1
warn_on_root = 0