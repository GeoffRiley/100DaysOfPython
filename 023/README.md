# Day 23: 28<sup>th</sup> January 2020
Try out awesome library [_PyICU_](https://github.com/ovalhub/pyicu) 
—A wrapper of International Components for Unicode C++ library ([ICU](http://site.icu-project.org/)).

## Requirements
`pip install PyICU`

## Notes
This is a library connecting Python (2 and 3) with the International Components 
for Unicode which, by default, is provided with bindings for C++ and Java.

Whilst Python 3 defaults to using Unicode for its string class, Python 2 only
used it when pushed into doing so.  _ICU_ provides its own `UnicodeString` object 
type which can be directly coerced into Python 2 `unicode` and Python 3 `str`
objects however, there is an oddity with the `UnicodeString` in that it is
mutable. This mutability extends to the point that slices are not read only! For 
example:
```pydocstring
>>> from icu import UnicodeString
>>> temp = UnicodeString('Hello World')
>>> temp
<UnicodeString: 'Hello World'>
>>> len(temp)
11
>>> str(temp)
'Hello World'
>>> temp[-5:]
<UnicodeString: 'World'>
>>> temp[-5:] = 'Geoff'
>>> str(temp)
'Hello Geoff'
>>> temp[:5] = 'Goodbye'
>>> str(temp)
'Goodbye Geoff'
```  
This is, of course, a complete departure from the expected action of a normal
Python slice—especially when it allows the assignment of a longer replacement
string as in the last example above.

## Outcome
The installation of this particular library requires a compiler and the full
set of C++ ICU libraries, precompiled wheels are not available.  This fact alone 
means that _PyICU_ would be problematic if an application was to require it in a
distribution.

As I had all pre-requisites present the package compiled and installed without 
problem. Using the library proved very simple and interrogating the locale 
database was logical and rapid.

I put together a routine to quickly try out a variety of locale specifiers:
```python
from icu import Locale

def show_locale(locale_str):
    locale = Locale(locale_str)
    print(f'** Locale:  {locale}')
    print(f'Name:       {locale.getDisplayName()}')
    print(f'Local name: {locale.getDisplayName(locale)}')
    print(f'Country:    {locale.getDisplayCountry()}')
    print(f'Language:   {locale.getDisplayLanguage()}')
    print(f'Script:     {locale.getDisplayScript()}')
    print(f'Variant:    {locale.getDisplayVariant()}')
``` 
A simple query:
```pydocstring
>>> show_locale('en_GB')
** Locale:  en_GB
Name:       English (United Kingdom)
Local name: English (United Kingdom)
Country:    United Kingdom
Language:   English
Script:     
Variant:    
``` 
Other parts of the UK &amp; Ireland:
```pydocstring
>>> show_locale('cy_GB')
** Locale:  cy_GB
Name:       Welsh (United Kingdom)
Local name: Cymraeg (Y Deyrnas Unedig)
Country:    United Kingdom
Language:   Welsh
Script:     
Variant:    
>>> show_locale('kw_GB')
** Locale:  kw_GB
Name:       Cornish (United Kingdom)
Local name: kernewek (Rywvaneth Unys)
Country:    United Kingdom
Language:   Cornish
Script:     
Variant:    
>>> show_locale('gd_GB')
** Locale:  gd_GB
Name:       Scottish Gaelic (United Kingdom)
Local name: Gàidhlig (An Rìoghachd Aonaichte)
Country:    United Kingdom
Language:   Scottish Gaelic
Script:     
Variant:    
>>> show_locale('gv_IM')
** Locale:  gv_IM
Name:       Manx (Isle of Man)
Local name: Gaelg (Ellan Vannin)
Country:    Isle of Man
Language:   Manx
Script:     
Variant:    
>>> show_locale('ga_IE')
** Locale:  ga_IE
Name:       Irish (Ireland)
Local name: Gaeilge (Éire)
Country:    Ireland
Language:   Irish
Script:     
Variant:    
>>> show_locale('en_IE@currency=IEP')
** Locale:  en_IE@currency=IEP
Name:       English (Ireland, Currency=Irish Pound)
Local name: English (Ireland, Currency=Irish Pound)
Country:    Ireland
Language:   English
Script:     
Variant:    
``` 
There are a few 'generic' locale:
```pydocstring
>>> show_locale('en_001')
** Locale:  en_001
Name:       English (World)
Local name: English (World)
Country:    World
Language:   English
Script:     
Variant:    
>>> show_locale('ia_001')
** Locale:  ia_001
Name:       Interlingua (World)
Local name: interlingua (Mundo)
Country:    World
Language:   Interlingua
Script:     
Variant:    
>>> show_locale('eo_001')
** Locale:  eo_001
Name:       Esperanto (World)
Local name: esperanto (Mondo)
Country:    World
Language:   Esperanto
Script:     
Variant:    
>>> show_locale('es_419')
** Locale:  es_419
Name:       Spanish (Latin America)
Local name: español (Latinoamérica)
Country:    Latin America
Language:   Spanish
Script:     
Variant:    
``` 
The locale can contain extra information and/or hold representations in different
character sets:
```pydocstring
>>> show_locale('es_AR@currency=ARS')
** Locale:  es_AR@currency=ARS
Name:       Spanish (Argentina, Currency=Argentine Peso)
Local name: español (Argentina, moneda=peso argentino)
Country:    Argentina
Language:   Spanish
Script:     
Variant:    
>>> show_locale('ar_AE')
** Locale:  ar_AE
Name:       Arabic (United Arab Emirates)
Local name: العربية (الإمارات العربية المتحدة)
Country:    United Arab Emirates
Language:   Arabic
Script:     
Variant:    
>>> show_locale('zh_CN')
** Locale:  zh_CN
Name:       Chinese (China)
Local name: 中文（中国）
Country:    China
Language:   Chinese
Script:     
Variant:    
>>> show_locale('fr_CH@collation=phonebook;calendar=islamic-civil')
** Locale:  fr_CH@calendar=islamic-civil;collation=phonebook
Name:       French (Switzerland, Calendar=Islamic Calendar [tabular, civil epoch], Sort Order=Phonebook Sort Order)
Local name: français (Suisse, calendrier=calendrier musulman [tabulaire, époque civile], ordre de tri=ordre de l’annuaire)
Country:    Switzerland
Language:   French
Script:     
Variant:    
>>> show_locale('sr_Latn_RS_REVISED@currency=USD')
** Locale:  sr_Latn_RS_REVISED@currency=USD
Name:       Serbian (Latin, Serbia, Revised Orthography, Currency=US Dollar)
Local name: srpski (latinica, Srbija, Revidirana ortografija, valuta=Američki dolar)
Country:    Serbia
Language:   Serbian
Script:     Latin
Variant:    Revised Orthography
```

I was unable to uncover any particular benefit from using the ICU timezone 
implementation over the standard library. It may be that there is a way to 
influence the date/time formatting through the use of the locale settings, but
none of my attempts presented any evidence for this.  With the library being 
only a wrapper around the C++ API it is not possible to look at the source to
decide what connections may be made: the vast majority of API calls are labelled
as unknown signatures.

## Comments
This library is both comprehensive and (almost) incomprehensible. There is no 
denying that the ICU database holds a great deal of useful information, but 
the lack of wheel installations for standard platforms and the less than 
complete API understanding makes the library less than useful.

It may be that an internet based service with the information would be more
useful if operated with suitable caching of results in a similar manner to 
Domain Name Servers. This would allow standard REST queries to operate without
the need for any compilation or library requirements.
