from markupsafe import Markup, escape

# Here is a lovely bit of json injection
# Unprotected it would pop up an alert box if pushed into
# a web page
json_injection = '<script>alert(document.cookie);</script>'

# If we escape the string then any 'harmful' characters
# are automatically converted into harmless control sequences
escaped = escape(json_injection)

# If, on the other hand, the string is really wanted like that
# then using Markup indicates that the string is 'safe'
markup = Markup(json_injection)

print(f'Escaped: {escaped}')
print(f'Markup:  {markup}')

# Escaped: &lt;script&gt;alert(document.cookie);&lt;/script&gt;
# Markup:  <script>alert(document.cookie);</script>

# A marked up string with parameter replacements will have those
# parameters escaped:
str1 = '<em>Squirrels</em>'
str2 = 'Wilderness'
str3 = '"Ice bun terror"'

param_string = Markup('"This is a test." …or <b>How to get %s in a string</b>.')

print(param_string)
print(param_string % str1)
print(param_string % str2)
print(param_string % str3)

# "This is a test." …or <b>How to get %s in a string</b>.
# "This is a test." …or <b>How to get &lt;em&gt;Squirrels&lt;/em&gt; in a string</b>.
# "This is a test." …or <b>How to get Wilderness in a string</b>.
# "This is a test." …or <b>How to get &#34;Ice bun terror&#34; in a string</b>.
