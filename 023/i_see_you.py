from icu import Locale, TimeZone


def show_locale(locale_str):
    if isinstance(locale_str, Locale):
        locale = locale_str
    else:
        locale = Locale(locale_str)
    print(f'** Locale:  {locale}')
    print(f'Name:       {locale.getDisplayName()}')
    print(f'Local name: {locale.getDisplayName(locale)}')
    print(f'Country:    {locale.getDisplayCountry()}')
    print(f'Language:   {locale.getDisplayLanguage()}')
    print(f'Script:     {locale.getDisplayScript()}')
    print(f'Variant:    {locale.getDisplayVariant()}')


def show_timezone(zone_str):
    zone = TimeZone.createTimeZone(zone_str)
    print(f'** Zone: {str(zone):30} {zone.getDisplayName()}')


show_locale('en_GB')
show_locale('cy_GB')
show_locale('kw_GB')
show_locale('gd_GB')
show_locale('gv_IM')
show_locale('ga_IE')
show_locale('en_IE@currency=IEP')
show_locale('en_001')
show_locale('ia_001')
show_locale('eo_001')
show_locale('es_419')
show_locale('es_AR@currency=ARS')
show_locale('ar_AE')
show_locale('zh_CN')
show_locale('fr_CH@collation=phonebook;calendar=islamic-civil')
show_locale('sr_Latn_RS_REVISED@currency=USD')

show_timezone('Europe/London')
show_timezone('GMT')
show_timezone('UTC')
show_timezone('America/Los_Angeles')
show_timezone('US/Mountain')

# lls = [l for l in Locale.getAvailableLocales()]
#
# print('Locale list:')
# print('\n'.join(textwrap.wrap(', '.join(f'{l}—→{Locale(l).getDisplayName()}' for l in lls))))
