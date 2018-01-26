In [7]: Book.objects.create(name='C#', desc='really great book',created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
Out[7]: <Book: Book object>

In [8]: Book.objects.create(name='Java', desc='Java rocks!',created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
Out[8]: <Book: Book object>

In [9]: Book.objects.create(name='Python', desc='Python rocks too! when it is stable....',created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
Out[9]: <Book: Book object>

In [10]: Book.objects.create(name='PHP', desc='Pile higher programming',created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
Out[10]: <Book: Book object>

In [11]: Book.objects.create(name='Ruby', desc='Get a Ruby roundhouse!',created_at=datetime.datetime.now(), updated_at=datetime.datetimew())
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-11-0c24542eee32> in <module>()
----> 1 Book.objects.create(name='Ruby', desc='Get a Ruby roundhouse!',created_at=datetime.datetime.now(), updated_at=datetime.datetimew())

AttributeError: 'module' object has no attribute 'datetimew'

In [12]: Book.objects.create(name='Ruby', desc='Get a Ruby roundhouse!',created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
Out[12]: <Book: Book object>

In [13]: Book.objects.create(name='Ruby', desc='Get a Ruby roundhouse!',created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
Out[13]: <Book: Book object>

In [14]: Book.objects.get(id=6)
Out[14]: <Book: Book object>

In [15]: Book.objects.get(id=6).delete()
Out[15]: (1, {u'book_authors.Author_books': 0, u'book_authors.Book': 1})

In [16]: Author.objects(first_name="Spero", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="thisnote",books=Books.obj
    ...: ects.get(id=1))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-16-7c024a1bd5b3> in <module>()
----> 1 Author.objects(first_name="Spero", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="thisnote",books=Books.objects.get(id=1))

NameError: name 'Books' is not defined

In [17]: Author.objects(first_name="Spero", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="thisnote",books=Book.obje
    ...: cts.get(id=1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-17-f8c6acdeefaa> in <module>()
----> 1 Author.objects(first_name="Spero", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="thisnote",books=Book.objects.get(id=1))

TypeError: 'Manager' object is not callable

In [18]: Author.objects(first_name="Mike", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="thisnote")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-18-f9f4fd9ef1dc> in <module>()
----> 1 Author.objects(first_name="Mike", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="thisnote")

TypeError: 'Manager' object is not callable

In [19]: Author.objects(first_name="Speros", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="that note")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-19-03b1ee5db84e> in <module>()
----> 1 Author.objects(first_name="Speros", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="that note")

TypeError: 'Manager' object is not callable

In [20]: Author.objects.create(first_name="Speros", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="that note")
---------------------------------------------------------------------------
OperationalError                          Traceback (most recent call last)
<ipython-input-20-91bbde58c5ef> in <module>()
----> 1 Author.objects.create(first_name="Speros", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="that note")

C:\Python27\lib\site-packages\django\db\models\manager.pyc in manager_method(self, *args, **kwargs)
     83         def create_method(name, method):
     84             def manager_method(self, *args, **kwargs):
---> 85                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     86             manager_method.__name__ = method.__name__
     87             manager_method.__doc__ = method.__doc__

C:\Python27\lib\site-packages\django\db\models\query.pyc in create(self, **kwargs)
    397         obj = self.model(**kwargs)
    398         self._for_write = True
--> 399         obj.save(force_insert=True, using=self.db)
    400         return obj
    401

C:\Python27\lib\site-packages\django\db\models\base.pyc in save(self, force_insert, force_update, using, update_fields)
    794
    795         self.save_base(using=using, force_insert=force_insert,
--> 796                        force_update=force_update, update_fields=update_fields)
    797     save.alters_data = True
    798

C:\Python27\lib\site-packages\django\db\models\base.pyc in save_base(self, raw, force_insert, force_update, using, update_fields)
    822             if not raw:
    823                 self._save_parents(cls, using, update_fields)
--> 824             updated = self._save_table(raw, cls, force_insert, force_update, using, update_fields)
    825         # Store the database on which the object was saved
    826         self._state.db = using

C:\Python27\lib\site-packages\django\db\models\base.pyc in _save_table(self, raw, cls, force_insert, force_update, using, update_fields)
    906
    907             update_pk = bool(meta.has_auto_field and not pk_set)
--> 908             result = self._do_insert(cls._base_manager, using, fields, update_pk, raw)
    909             if update_pk:
    910                 setattr(self, meta.pk.attname, result)

C:\Python27\lib\site-packages\django\db\models\base.pyc in _do_insert(self, manager, using, fields, update_pk, raw)
    945         """
    946         return manager._insert([self], fields=fields, return_id=update_pk,
--> 947                                using=using, raw=raw)
    948
    949     def delete(self, using=None, keep_parents=False):

C:\Python27\lib\site-packages\django\db\models\manager.pyc in manager_method(self, *args, **kwargs)
     83         def create_method(name, method):
     84             def manager_method(self, *args, **kwargs):
---> 85                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     86             manager_method.__name__ = method.__name__
     87             manager_method.__doc__ = method.__doc__

C:\Python27\lib\site-packages\django\db\models\query.pyc in _insert(self, objs, fields, return_id, raw, using)
   1041         query = sql.InsertQuery(self.model)
   1042         query.insert_values(fields, objs, raw=raw)
-> 1043         return query.get_compiler(using=using).execute_sql(return_id)
   1044     _insert.alters_data = True
   1045     _insert.queryset_only = False

C:\Python27\lib\site-packages\django\db\models\sql\compiler.pyc in execute_sql(self, return_id)
   1052         with self.connection.cursor() as cursor:
   1053             for sql, params in self.as_sql():
-> 1054                 cursor.execute(sql, params)
   1055             if not (return_id and cursor):
   1056                 return

C:\Python27\lib\site-packages\django\db\backends\utils.pyc in execute(self, sql, params)
     77         start = time()
     78         try:
---> 79             return super(CursorDebugWrapper, self).execute(sql, params)
     80         finally:
     81             stop = time()

C:\Python27\lib\site-packages\django\db\backends\utils.pyc in execute(self, sql, params)
     62                 return self.cursor.execute(sql)
     63             else:
---> 64                 return self.cursor.execute(sql, params)
     65
     66     def executemany(self, sql, param_list):

C:\Python27\lib\site-packages\django\db\utils.pyc in __exit__(self, exc_type, exc_value, traceback)
     92                 if dj_exc_type not in (DataError, IntegrityError):
     93                     self.wrapper.errors_occurred = True
---> 94                 six.reraise(dj_exc_type, dj_exc_value, traceback)
     95
     96     def __call__(self, func):

C:\Python27\lib\site-packages\django\db\backends\utils.pyc in execute(self, sql, params)
     62                 return self.cursor.execute(sql)
     63             else:
---> 64                 return self.cursor.execute(sql, params)
     65
     66     def executemany(self, sql, param_list):

C:\Python27\lib\site-packages\django\db\backends\sqlite3\base.pyc in execute(self, query, params)
    335             return Database.Cursor.execute(self, query)
    336         query = self.convert_query(query)
--> 337         return Database.Cursor.execute(self, query, params)
    338
    339     def executemany(self, query, param_list):

OperationalError: database is locked

In [21]: Author.objects.create(first_name="Speros", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="that note")
Out[21]: <Author: Author object>

In [22]: Author.objects.create(first_name="John", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="that other note")
Out[22]: <Author: Author object>

In [23]: Author.objects.create(first_name="Jadee", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="darn note")
Out[23]: <Author: Author object>

In [24]: Author.objects.create(first_name="Jay", last_name="Smith", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), notes="Jay's note")
Out[24]: <Author: Author object>

In [25]: Books.Object.get(id=5).name="C#"
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-25-75e60e5eab47> in <module>()
----> 1 Books.Object.get(id=5).name="C#"

NameError: name 'Books' is not defined

In [26]: Book.Object.get(id=5).name="C#"
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-26-35314a65ffb6> in <module>()
----> 1 Book.Object.get(id=5).name="C#"

AttributeError: type object 'Book' has no attribute 'Object'

In [27]: Book.Objects.get(id=5).name="C#"
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-27-bf1b083da6d5> in <module>()
----> 1 Book.Objects.get(id=5).name="C#"

AttributeError: type object 'Book' has no attribute 'Objects'

In [28]: Book.Objects.get(id=5)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-28-da13d378ee0c> in <module>()
----> 1 Book.Objects.get(id=5)

AttributeError: type object 'Book' has no attribute 'Objects'

In [29]: Book.objects.get(id=5).name="C#"

In [30]: Author.objects.get(id=5).first_name='Ketul'

In [31]: Book.save()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-31-ed6c8e10de47> in <module>()
----> 1 Book.save()

TypeError: unbound method save() must be called with Book instance as first argument (got nothing instead)

In [32]: Author.save()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-32-c4a1beebd868> in <module>()
----> 1 Author.save()

TypeError: unbound method save() must be called with Author instance as first argument (got nothing instead)

In [33]: Author.objects.save()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-33-7bcf1736f37f> in <module>()
----> 1 Author.objects.save()

AttributeError: 'Manager' object has no attribute 'save'

In [34]: Author.objects.get(id=5).first_name='Ketul'.save()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-34-18966f3d624c> in <module>()
----> 1 Author.objects.get(id=5).first_name='Ketul'.save()

AttributeError: 'str' object has no attribute 'save'

In [35]: Author.objects.get(id=5).first_name='Ketul'

In [36]: Author.objects.save()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-36-7bcf1736f37f> in <module>()
----> 1 Author.objects.save()

AttributeError: 'Manager' object has no attribute 'save'

In [37]: a = Author.objects.get(id=5)

In [38]: a.first_name='Ketul'

In [39]: a.save()

In [40]: b = Book.objects.get(id=5)

In [41]: b.name = "C#"

In [42]: b.save()

In [43]: a = Author.objects.get(id=1)

In [44]: b = Book.objects.get(id=1)

In [45]: b.add(a)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-45-cad54b8f33f9> in <module>()
----> 1 b.add(a)

AttributeError: 'Book' object has no attribute 'add'

In [46]: b.article_set.add(a)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-46-d9c50cf26499> in <module>()
----> 1 b.article_set.add(a)

AttributeError: 'Book' object has no attribute 'article_set'

In [47]: b.objects.add(a)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-47-79105ed3f6ab> in <module>()
----> 1 b.objects.add(a)

C:\Python27\lib\site-packages\django\db\models\manager.pyc in __get__(self, instance, cls)
    184     def __get__(self, instance, cls=None):
    185         if instance is not None:
--> 186             raise AttributeError("Manager isn't accessible via %s instances" % cls.__name__)
    187
    188         if cls._meta.abstract:

AttributeError: Manager isn't accessible via Book instances

In [48]: b.name
Out[48]: u'C#'

In [49]: b.first_name
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-49-14154cdcdf36> in <module>()
----> 1 b.first_name

AttributeError: 'Book' object has no attribute 'first_name'

In [50]: a.first_name
Out[50]: u'Mike'

In [51]: a.add(b)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-51-73f363cda532> in <module>()
----> 1 a.add(b)

AttributeError: 'Author' object has no attribute 'add'

In [52]: a.books = b
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-52-e10312f0db3c> in <module>()
----> 1 a.books = b

C:\Python27\lib\site-packages\django\db\models\fields\related_descriptors.pyc in __set__(self, instance, value)
    498         )
    499         manager = self.__get__(instance)
--> 500         manager.set(value)
    501
    502

C:\Python27\lib\site-packages\django\db\models\fields\related_descriptors.pyc in set(self, objs, **kwargs)
    926             # Force evaluation of `objs` in case it's a queryset whose value
    927             # could be affected by `manager.clear()`. Refs #19816.
--> 928             objs = tuple(objs)
    929
    930             clear = kwargs.pop('clear', False)

TypeError: 'Book' object is not iterable

In [53]: a.books
Out[53]: <django.db.models.fields.related_descriptors.ManyRelatedManager at 0x7b96710>

In [54]: a.object(id=2)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-54-3c3a051a2659> in <module>()
----> 1 a.object(id=2)

AttributeError: 'Author' object has no attribute 'object'

In [55]: a.objects.get(id=2)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-55-f5b73ef82d9d> in <module>()
----> 1 a.objects.get(id=2)

C:\Python27\lib\site-packages\django\db\models\manager.pyc in __get__(self, instance, cls)
    184     def __get__(self, instance, cls=None):
    185         if instance is not None:
--> 186             raise AttributeError("Manager isn't accessible via %s instances" % cls.__name__)
    187
    188         if cls._meta.abstract:

AttributeError: Manager isn't accessible via Author instances

In [56]: a= Author.objects.get(id=2)

In [57]: a.books
Out[57]: <django.db.models.fields.related_descriptors.ManyRelatedManager at 0x7b960b8>

In [58]: a= Author.objects.get(id=1)

In [59]: a.books
Out[59]: <django.db.models.fields.related_descriptors.ManyRelatedManager at 0x7b96198>

In [60]: a.books = b
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-60-e10312f0db3c> in <module>()
----> 1 a.books = b

C:\Python27\lib\site-packages\django\db\models\fields\related_descriptors.pyc in __set__(self, instance, value)
    498         )
    499         manager = self.__get__(instance)
--> 500         manager.set(value)
    501
    502

C:\Python27\lib\site-packages\django\db\models\fields\related_descriptors.pyc in set(self, objs, **kwargs)
    926             # Force evaluation of `objs` in case it's a queryset whose value
    927             # could be affected by `manager.clear()`. Refs #19816.
--> 928             objs = tuple(objs)
    929
    930             clear = kwargs.pop('clear', False)

TypeError: 'Book' object is not iterable

In [61]: b.book_set(a)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-61-318156979998> in <module>()
----> 1 b.book_set(a)

AttributeError: 'Book' object has no attribute 'book_set'

In [62]: a.books.add(b)

In [63]: b = Book.objects.get(id=2)

In [64]: a.books.add(b)

In [65]: a= Author.objects.get(id=2)

In [66]: b = Book.objects.get(id=1)

In [67]: a.books.add(b)

In [68]: b = Book.objects.get(id=2)

In [69]: a.books.add(b)

In [70]: b = Book.objects.get(id=3)

In [71]: a.books.add(b)

In [72]: a= Author.objects.get(id=3)

In [73]: b = Book.objects.get(id=1)

In [74]: a.books.add(b)

In [75]: b = Book.objects.get(id=2)

In [76]: a.books.add(b)

In [77]: b = Book.objects.get(id=3)

In [78]: a.books.add(b)

In [79]: b = Book.objects.get(id=4)

In [80]: a.books.add(b)

In [81]: a= Author.objects.get(id=4)

In [82]: a= Author.objects.all()

In [83]: a= Author.objects.get(id=4)

In [84]: a.books.all()
Out[84]: <QuerySet []>

In [85]: b = Book.objects.all()

In [86]: a.books.add(b)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-86-4da3f4d43236> in <module>()
----> 1 a.books.add(b)

C:\Python27\lib\site-packages\django\db\models\fields\related_descriptors.pyc in add(self, *objs)
    879             db = router.db_for_write(self.through, instance=self.instance)
    880             with transaction.atomic(using=db, savepoint=False):
--> 881                 self._add_items(self.source_field_name, self.target_field_name, *objs)
    882
    883                 # If this is a symmetrical m2m relation to self, add the mirror entry in the m2m table

C:\Python27\lib\site-packages\django\db\models\fields\related_descriptors.pyc in _add_items(self, source_field_name, target_field_name, *objs)
   1026                         .filter(**{
   1027                             source_field_name: self.related_val[0],
-> 1028                             '%s__in' % target_field_name: new_ids,
   1029                         }))
   1030                 new_ids = new_ids - set(vals)

C:\Python27\lib\site-packages\django\db\models\query.pyc in filter(self, *args, **kwargs)
    792         set.
    793         """
--> 794         return self._filter_or_exclude(False, *args, **kwargs)
    795
    796     def exclude(self, *args, **kwargs):

C:\Python27\lib\site-packages\django\db\models\query.pyc in _filter_or_exclude(self, negate, *args, **kwargs)
    810             clone.query.add_q(~Q(*args, **kwargs))
    811         else:
--> 812             clone.query.add_q(Q(*args, **kwargs))
    813         return clone
    814

C:\Python27\lib\site-packages\django\db\models\sql\query.pyc in add_q(self, q_object)
   1225         existing_inner = set(
   1226             (a for a in self.alias_map if self.alias_map[a].join_type == INNER))
-> 1227         clause, _ = self._add_q(q_object, self.used_aliases)
   1228         if clause:
   1229             self.where.add(clause, AND)

C:\Python27\lib\site-packages\django\db\models\sql\query.pyc in _add_q(self, q_object, used_aliases, branch_negated, current_negated, allow_joins, split_subq)
   1251                     child, can_reuse=used_aliases, branch_negated=branch_negated,
   1252                     current_negated=current_negated, connector=connector,
-> 1253                     allow_joins=allow_joins, split_subq=split_subq,
   1254                 )
   1255                 joinpromoter.add_votes(needed_inner)

C:\Python27\lib\site-packages\django\db\models\sql\query.pyc in build_filter(self, filter_expr, branch_negated, current_negated, can_reuse, connector, allow_joins, split_subq)
   1181             else:
   1182                 lhs = MultiColSource(alias, targets, sources, field)
-> 1183             condition = lookup_class(lhs, value)
   1184             lookup_type = lookup_class.lookup_name
   1185         else:

C:\Python27\lib\site-packages\django\db\models\lookups.pyc in __init__(self, lhs, rhs)
     17     def __init__(self, lhs, rhs):
     18         self.lhs, self.rhs = lhs, rhs
---> 19         self.rhs = self.get_prep_lookup()
     20         if hasattr(self.lhs, 'get_bilateral_transforms'):
     21             bilateral_transforms = self.lhs.get_bilateral_transforms()

C:\Python27\lib\site-packages\django\db\models\fields\related_lookups.pyc in get_prep_lookup(self)
     54                 # only one as we don't get to the direct value branch otherwise.
     55                 target_field = self.lhs.output_field.get_path_info()[-1].target_fields[-1]
---> 56                 self.rhs = [target_field.get_prep_value(v) for v in self.rhs]
     57         return super(RelatedIn, self).get_prep_lookup()
     58

C:\Python27\lib\site-packages\django\db\models\fields\__init__.pyc in get_prep_value(self, value)
    944         if value is None:
    945             return None
--> 946         return int(value)
    947
    948     def contribute_to_class(self, cls, name, **kwargs):

TypeError: int() argument must be a string or a number, not 'QuerySet'

In [87]: b = Book.objects.get(id=1)

In [88]: a.books.add(b)

In [89]: b = Book.objects.get(id=2)

In [90]: a.books.add(b)

In [91]: b = Book.objects.get(id=3)

In [92]: b = Book.objects.get(id=4)

In [93]: b = Book.objects.get(id=3)

In [94]: a.books.add(b)

In [95]: b = Book.objects.get(id=4)

In [96]: a.books.add(b)

In [97]: b = Book.objects.get(id=5)

In [98]: a.books.add(b)

In [99]: Book.objects(id=3).Authors.objects.all()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-99-0c42e2bc4039> in <module>()
----> 1 Book.objects(id=3).Authors.objects.all()

TypeError: 'Manager' object is not callable

In [100]: Book.objects(id=3).Author.objects.all()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-100-81187efc2e6f> in <module>()
----> 1 Book.objects(id=3).Author.objects.all()

TypeError: 'Manager' object is not callable

In [101]: Book.objects.get(id=3).Author.objects.all()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-101-5241253170ac> in <module>()
----> 1 Book.objects.get(id=3).Author.objects.all()

AttributeError: 'Book' object has no attribute 'Author'

In [102]: b = Book.objects.get(id=3)

In [103]: a = Author.objects.all()

In [104]: b.a
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-104-98be602909d9> in <module>()
----> 1 b.a

AttributeError: 'Book' object has no attribute 'a'

In [105]: a.filter(books = b)
Out[105]: <QuerySet [<Author: Author object>, <Author: Author object>, <Author: Author object>]>

In [106]: a.filter(books = book.objects.get(id=3)).first().delete()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-106-6d2e23b8666d> in <module>()
----> 1 a.filter(books = book.objects.get(id=3)).first().delete()

NameError: name 'book' is not defined

In [107]: a.filter(books = Book.objects.get(id=3)).first().delete()
Out[107]: (4, {u'book_authors.Author': 1, u'book_authors.Author_books': 3})

In [108]: b = Books.objects.get(id=2)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-108-d13fc2396046> in <module>()
----> 1 b = Books.objects.get(id=2)

NameError: name 'Books' is not defined

In [109]: b = Book.objects.get(id=2)

In [110]: a = Author.objects.get(id=5)

In [111]: a.books.add(b)

In [112]: a = Author.objects.get(id=3)

In [113]: Book.objects.filter(authors=a)
Out[113]: <QuerySet [<Book: Book object>, <Book: Book object>, <Book: Book object>, <Book: Book object>]>

In [114]: Book.objects.filter(authors=a).name
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-114-34de38887ea7> in <module>()
----> 1 Book.objects.filter(authors=a).name

AttributeError: 'QuerySet' object has no attribute 'name'

In [115]: bs = Book.objects.filter(authors=a)

In [116]: bs.name
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-116-5f1893509cbe> in <module>()
----> 1 bs.name

AttributeError: 'QuerySet' object has no attribute 'name'

In [117]: bs.all().name
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-117-edde10751197> in <module>()
----> 1 bs.all().name

AttributeError: 'QuerySet' object has no attribute 'name'

In [118]: a = Author.objects.get(id=2)
---------------------------------------------------------------------------
DoesNotExist                              Traceback (most recent call last)
<ipython-input-118-89c548abcdd9> in <module>()
----> 1 a = Author.objects.get(id=2)

C:\Python27\lib\site-packages\django\db\models\manager.pyc in manager_method(self, *args, **kwargs)
     83         def create_method(name, method):
     84             def manager_method(self, *args, **kwargs):
---> 85                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     86             manager_method.__name__ = method.__name__
     87             manager_method.__doc__ = method.__doc__

C:\Python27\lib\site-packages\django\db\models\query.pyc in get(self, *args, **kwargs)
    383             raise self.model.DoesNotExist(
    384                 "%s matching query does not exist." %
--> 385                 self.model._meta.object_name
    386             )
    387         raise self.model.MultipleObjectsReturned(

DoesNotExist: Author matching query does not exist.

In [119]: a = Author.objects.get(id=4)

In [120]: Book.objects.filter(authors=a).name
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-120-34de38887ea7> in <module>()
----> 1 Book.objects.filter(authors=a).name

AttributeError: 'QuerySet' object has no attribute 'name'

In [121]: Book.objects.filter(authors=a)
Out[121]: <QuerySet [<Book: Book object>, <Book: Book object>, <Book: Book object>, <Book: Book object>, <Book: Book object>]>
