# -*- coding: utf-8 -*-

from gluon import current

from collections import OrderedDict

def config(settings):
    """
        Maldives specific template settings for CAP: Common Alerting Protocol
    """

    T = current.T

    settings.base.system_name = T("Maldives Warning and Situational-Awareness System")

    # Default Language
    settings.L10n.default_language = "dv"

    # L10n (Localization) settings
    languages = OrderedDict([
        #("ar", "العربية"),
        ("dv", "ދިވެހި"), # Divehi (Maldives)
        ("en-US", "English"),
        #("es", "Español"),
        #("fr", "Français"),
        #("km", "ភាសាខ្មែរ"),        # Khmer
        #("mn", "Монгол хэл"),  # Mongolian
        #("my", "မြန်မာစာ"),        # Burmese
        #("ne", "नेपाली"),          # Nepali
        #("prs", "دری"),        # Dari
        #("ps", "پښتو"),        # Pashto
        #("tet", "Tetum"),
        #("th", "ภาษาไทย"),        # Thai
        #("tl", "Tagalog"), # Filipino
        #("vi", "Tiếng Việt"),   # Vietnamese
        #("zh-cn", "中文 (简体)"),
    ])
    # For MV implementation of SAMBRO
    settings.L10n.languages = languages

# END =========================================================================
