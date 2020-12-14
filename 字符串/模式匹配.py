import re
match=re.match('Hello (.*)','Hello world')
match.group(1)

'world'

match.groups()
('world',)