# -*- coding: utf-8 -*-

from gluon import current

from collections import OrderedDict

def config(settings):
    """
        Philippines specific template settings for CAP: Common Alerting Protocol
    """

    T = current.T

    settings.base.system_name = T("Philippines Warning and Situational-Awareness System")

    # Default Language
    settings.L10n.default_language = "tl"

    # L10n (Localization) settings
    languages = OrderedDict([
        #("ar", "العربية"),
        #("dv", "ދިވެހި"), # Divehi (Maldives)
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
        ("tl", "Tagalog"), # Filipino
        #("vi", "Tiếng Việt"),   # Vietnamese
        #("zh-cn", "中文 (简体)"),
    ])
    # For PH implementation of SAMBRO
    settings.L10n.languages = languages

    # for creating location from SAME geocodes
    settings.cap.same_code = "PSGC"

    # Name of Method used to create bulletin
    # This may vary according to organisation implementing it
    settings.cap.form_bulletin = "form_ocd"

# END =========================================================================
