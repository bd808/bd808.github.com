Title: Making Django migrations that work with MySQL 5.5 and utf8mb4
Date: 2017-04-17T04:18:24Z
Comments: True
Github_issue_id: 27
Tags: python, django, mysql, unicode, hacks

I like [Django], [MySQL], and [Unicode], but getting all three to play together
nicely can sometimes be a bit challenging. One of the more annoying things is
getting Django to make a [migration] that will create a 255 character
`CharField` that is encoded using the [utf8mb4] character set and indexed.

<!-- more -->

Out of the box, MySQL's [InnoDB] table type has a maximum index length or 767
bytes. This is enough to index 255 characters in the [utf8] encoding, but that
encoding won't work for storing any Unicode data from the [Supplementary
Multilingual Plane]. That means you can't put a [unicorn face] (🦄) or
a [slice of pizza] (🍕) into a column using this encoding. Changing to the
utf8mb4 character set will allow you to store four byte code points, but only
index 191 characters.

With MySQL 5.5.14 and later you can raise this limit to 3072 bytes by using
the [innodb_large_prefix] setting along with the Barracuda file format, file
per table storage, and dynamic row format. The first three can all be set
server wide, but the row format for the table needs to be provided in
a `CREATE TABLE` or `ALTER TABLE` statement as a `ROW_FORMAT=DYNAMIC`
attribute.

Django does not have a feature flag or setting for adding the
needed attribute. I've worked around this before by using manual database
hacking, but today I figured out a hack that you can manually apply to your
Django migration files to work around it. The trick is to edit the migration
so that the initial field creation uses a length that will fit in the 767 byte
limit, and then add a `RunSQL` to change the table's row format and an
`AlterField` to increase the field length.

``` python
 operations = [
     migrations.CreateModel(
         name='UnicodeHack',
         fields=[
             ('hack', models.CharField(unique=True, max_length=128)),
         ],
     ),
     migrations.RunSQL('ALTER TABLE unicodehack ROW_FORMAT = DYNAMIC;'),
     migrations.AlterField(
         model_name='unicodehack',
         name='hack',
         field=models.CharField(unique=True, max_length=255),
     ),
 ]
```

[Django]: https://en.wikipedia.org/wiki/Django_(web_framework)
[MySQL]: https://en.wikipedia.org/wiki/MySQL
[Unicode]: https://en.wikipedia.org/wiki/Unicode
[migration]: https://docs.djangoproject.com/en/1.8/topics/migrations/
[utf8mb4]: https://dev.mysql.com/doc/refman/5.5/en/charset-unicode-utf8mb4.html
[InnoDB]: https://dev.mysql.com/doc/refman/5.5/en/innodb-storage-engine.html
[utf8]: https://dev.mysql.com/doc/refman/5.5/en/charset-unicode-utf8.html
[Supplementary Multilingual Plane]: https://en.wikipedia.org/wiki/Plane_(Unicode)#Supplementary_Multilingual_Plane
[unicorn face]: http://emojipedia.org/unicorn-face/
[slice of pizza]: http://emojipedia.org/slice-of-pizza/
[innodb_large_prefix]: https://dev.mysql.com/doc/refman/5.5/en/innodb-parameters.html#sysvar_innodb_large_prefix
