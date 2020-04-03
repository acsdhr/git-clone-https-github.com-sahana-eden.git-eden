# -*- coding: utf-8 -*-

from gluon import current

def config(settings):
    """
        Template settings for Poland
        - designed to be used in a Cascade with an application template
    """

    #T = current.T

    # Pre-Populate
    settings.base.prepopulate.append("locations/PL")

    # Uncomment to restrict to specific country/countries
    settings.gis.countries.append("PL")
    # Disable the Postcode selector in the LocationSelector
    #settings.gis.postcode_selector = False

    # L10n (Localization) settings
    settings.L10n.languages["pl"] = "Polish"
    # Default timezone for users
    settings.L10n.timezone = "Europe/Warsaw"
    # Default Country Code for telephone numbers
    settings.L10n.default_country_code = 48

    settings.fin.currencies["PLN"] = "Polish Złoty"
    settings.fin.currency_default = "PLN"

# END =========================================================================