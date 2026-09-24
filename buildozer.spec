[app]
title = Dim Therapy
package.name = dimtherapy
package.domain = org.arif
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 35
android.minapi = 21
android.archs = arm64-v8a
