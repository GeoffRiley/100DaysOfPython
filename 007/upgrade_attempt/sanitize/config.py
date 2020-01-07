DEBUG = True

# If you want sanitize to automatically run HTML markup through HTML Tidy, set
# this to 1.  Requires mxTidy <http://www.egenix.com/files/python/mxTidy.html>
# or utidylib <http://utidylib.berlios.de/>.
TIDY_MARKUP = 0

# List of Python interfaces for HTML Tidy, in order of preference.  Only useful
# if TIDY_MARKUP = 1
PREFERRED_TIDY_INTERFACES = ["uTidy", "mxTidy"]
BASE_HTML_PROCESSOR__ELEMENTS_NO_END_TAGS = [
    'area',
    'base',
    'basefont',
    'br',
    'col',
    'frame',
    'hr',
    'img',
    'input',
    'isindex',
    'link',
    'meta',
    'param'
]

HTML_SANITIZER__ACCEPTABLE_ELEMENTS = [
    'a',
    'abbr',
    'acronym',
    'address',
    'area',
    'b',
    'big',
    'blockquote',
    'br',
    'button',
    'caption',
    'center',
    'cite',
    'code',
    'col',
    'colgroup',
    'dd',
    'del',
    'dfn',
    'dir',
    'div',
    'dl',
    'dt',
    'em',
    'fieldset',
    'font',
    'form',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'hr',
    'i',
    'img',
    'input',
    'ins',
    'kbd',
    'label',
    'legend',
    'li',
    'map',
    'menu',
    'ol',
    'optgroup',
    'option',
    'p',
    'pre',
    'q',
    's',
    'samp',
    'select',
    'small',
    'span',
    'strike',
    'strong',
    'sub',
    'sup',
    'table',
    'textarea',
    'tbody',
    'td',
    'tfoot',
    'th',
    'thead',
    'tr',
    'tt',
    'u',
    'ul',
    'var'
]
HTML_SANITIZER__ACCEPTABLE_ATTRIBUTES = [
    'abbr',
    'accept',
    'accept-charset',
    'accesskey',
    'action',
    'align',
    'alt',
    'axis',
    'border',
    'cellpadding',
    'cellspacing',
    'char',
    'charoff',
    'charset',
    'checked',
    'cite',
    'class',
    'clear',
    'cols',
    'colspan',
    'color',
    'compact',
    'coords',
    'datetime',
    'dir',
    'disabled',
    'enctype',
    'for',
    'frame',
    'headers',
    'height',
    'href',
    'hreflang',
    'hspace',
    'id',
    'ismap',
    'label',
    'lang',
    'longdesc',
    'maxlength',
    'media',
    'method',
    'multiple',
    'name',
    'nohref',
    'noshade',
    'nowrap',
    'prompt',
    'readonly',
    'rel',
    'rev',
    'rows',
    'rowspan',
    'rules',
    'scope',
    'selected',
    'shape',
    'size',
    'span',
    'src',
    'start',
    'summary',
    'tabindex',
    'target',
    'title',
    'type',
    'usemap',
    'valign',
    'value',
    'vspace',
    'width'
]
# http://www.iana.org/assignments/uri-schemes.html
HTML_SANITIZER__ACCEPTABLE_URI_SCHEMES = [
    'cid',
    'crid',
    'data',
    'dav',
    'dict',
    'dns',
    'fax',
    'ftp',
    'go',
    'gopher',
    'h323',
    'http',
    'https',
    'im',
    'imap',
    'info',
    'ipp',
    'iris.beep',
    'ldap',
    'mailto',
    'mid',
    'modem',
    'news',
    'nfs',
    'nntp',
    'pres',
    'rtsp',
    'sip',
    'sips',
    'snmp',
    'tag',
    'tel',
    'telnet',
    'tftp',
    'urn',
    # unspecified
    # http://esw.w3.org/topic/UriSchemes
    'aim',
    'irc',
    'feed',
    'webcal'
]
HTML_SANITIZER__IGNORABLE_ELEMENTS = [
    'script',
    'applet',
    'style'
]
HTML_SANITIZER__RELATIVE_URIS = [
    ('a', 'href'),
    ('applet', 'codebase'),
    ('area', 'href'),
    ('blockquote', 'cite'),
    ('body', 'background'),
    ('del', 'cite'),
    ('form', 'action'),
    ('frame', 'longdesc'),
    ('frame', 'src'),
    ('iframe', 'longdesc'),
    ('iframe', 'src'),
    ('head', 'profile'),
    ('img', 'longdesc'),
    ('img', 'src'),
    ('img', 'usemap'),
    ('input', 'src'),
    ('input', 'usemap'),
    ('ins', 'cite'),
    ('link', 'href'),
    ('object', 'classid'),
    ('object', 'codebase'),
    ('object', 'data'),
    ('object', 'usemap'),
    ('q', 'cite'),
    ('script', 'src')
]
UNICODE_BOM_MAP = {
    '\x00\x00\xfe\xff': 'utf-32be',
    '\xff\xfe\x00\x00': 'utf-32le',
    '\xfe\xff##': 'utf-16be',
    '\xff\xfe##': 'utf-16le',
    '\xef\bb\bf': 'utf-8'
}
XML_BOM_MAP = {
    '\x00\x00\x00\x3c': 'utf-32be',
    '\x3c\x00\x00\x00': 'utf-32le',
    '\x00\x3c\x00\x3f': 'utf-16be',
    '\x3c\x00\x3f\x00': 'utf-16le',
    '\x3c\x3f\x78\x6d': 'utf-8',  # or equivalent
    '\x4c\x6f\xa7\x94': 'ebcdic'
}
EMAP = (
    0, 1, 2, 3, 156, 9, 134, 127, 151, 141, 142, 11, 12, 13, 14, 15,
    16, 17, 18, 19, 157, 133, 8, 135, 24, 25, 146, 143, 28, 29, 30, 31,
    128, 129, 130, 131, 132, 10, 23, 27, 136, 137, 138, 139, 140, 5, 6, 7,
    144, 145, 22, 147, 148, 149, 150, 4, 152, 153, 154, 155, 20, 21, 158, 26,
    32, 160, 161, 162, 163, 164, 165, 166, 167, 168, 91, 46, 60, 40, 43, 33,
    38, 169, 170, 171, 172, 173, 174, 175, 176, 177, 93, 36, 42, 41, 59, 94,
    45, 47, 178, 179, 180, 181, 182, 183, 184, 185, 124, 44, 37, 95, 62, 63,
    186, 187, 188, 189, 190, 191, 192, 193, 194, 96, 58, 35, 64, 39, 61, 34,
    195, 97, 98, 99, 100, 101, 102, 103, 104, 105, 196, 197, 198, 199, 200, 201,
    202, 106, 107, 108, 109, 110, 111, 112, 113, 114, 203, 204, 205, 206, 207, 208,
    209, 126, 115, 116, 117, 118, 119, 120, 121, 122, 210, 211, 212, 213, 214, 215,
    216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231,
    123, 65, 66, 67, 68, 69, 70, 71, 72, 73, 232, 233, 234, 235, 236, 237,
    125, 74, 75, 76, 77, 78, 79, 80, 81, 82, 238, 239, 240, 241, 242, 243,
    92, 159, 83, 84, 85, 86, 87, 88, 89, 90, 244, 245, 246, 247, 248, 249,
    48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 250, 251, 252, 253, 254, 255
)
