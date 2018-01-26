In [1]: from apps.dojo_ninjas.models import *
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-1-becab48dde9d> in <module>()
----> 1 from apps.dojo_ninjas.models import *

ImportError: No module named apps.dojo_ninjas.models

In [2]: from dojo_ninjas.models import *

In [3]: Dojo.objects.create(name='CodingDojo Silicon Valley', city="Mountain View" , state="CA")
Out[3]: <Dojo: Dojo object>

In [4]: Dojo.objects.all().view()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-4-ad2e07e85980> in <module>()
----> 1 Dojo.objects.all().view()

AttributeError: 'QuerySet' object has no attribute 'view'

In [5]: Dojo.objects.all()
Out[5]: <QuerySet [<Dojo: Dojo object>]>

In [6]: Dojo.objects.view()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-359ee4cbb5db> in <module>()
----> 1 Dojo.objects.view()

AttributeError: 'Manager' object has no attribute 'view'

In [7]: Dojo.objects.viewall()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-7-db2edc6c1d69> in <module>()
----> 1 Dojo.objects.viewall()

AttributeError: 'Manager' object has no attribute 'viewall'

In [8]: Dojo.objects.first()
Out[8]: <Dojo: Dojo object>

In [9]: Dojo.objects.create(name='CodingDojo Seattle', city="Seattle" , state="WA")
Out[9]: <Dojo: Dojo object>

In [10]: Dojo.objects.create(name='CodingDojo New York', city="New York" , state="NY")
Out[10]: <Dojo: Dojo object>

In [11]: Ninja.objects.create(first_name='Hymie', Last_name="Hamster")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-11-dab94f5bd60c> in <module>()
----> 1 Ninja.objects.create(first_name='Hymie', Last_name="Hamster")

C:\Python27\lib\site-packages\django\db\models\manager.pyc in manager_method(self, *args, **kwargs)
     83         def create_method(name, method):
     84             def manager_method(self, *args, **kwargs):
---> 85                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     86             manager_method.__name__ = method.__name__
     87             manager_method.__doc__ = method.__doc__

C:\Python27\lib\site-packages\django\db\models\query.pyc in create(self, **kwargs)
    395         and returning the created object.
    396         """
--> 397         obj = self.model(**kwargs)
    398         self._for_write = True
    399         obj.save(force_insert=True, using=self.db)

C:\Python27\lib\site-packages\django\db\models\base.pyc in __init__(self, *args, **kwargs)
    553                     pass
    554             if kwargs:
--> 555                 raise TypeError("'%s' is an invalid keyword argument for this function" % list(kwargs)[0])
    556         super(Model, self).__init__()
    557         signals.post_init.send(sender=self.__class__, instance=self)

TypeError: 'Last_name' is an invalid keyword argument for this function

In [12]: Ninja.objects.create(first_name='Hymie', last_name="Hamster")
---------------------------------------------------------------------------
IntegrityError                            Traceback (most recent call last)
<ipython-input-12-5c9575777edc> in <module>()
----> 1 Ninja.objects.create(first_name='Hymie', last_name="Hamster")

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

IntegrityError: NOT NULL constraint failed: dojo_ninjas_ninja.dojo_id

In [13]: Ninja.objects.create(first_name='Hymie', last_name="Hamster", dojo="CodingDojo Seattle")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-13-f36508ac103d> in <module>()
----> 1 Ninja.objects.create(first_name='Hymie', last_name="Hamster", dojo="CodingDojo Seattle")

C:\Python27\lib\site-packages\django\db\models\manager.pyc in manager_method(self, *args, **kwargs)
     83         def create_method(name, method):
     84             def manager_method(self, *args, **kwargs):
---> 85                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     86             manager_method.__name__ = method.__name__
     87             manager_method.__doc__ = method.__doc__

C:\Python27\lib\site-packages\django\db\models\query.pyc in create(self, **kwargs)
    395         and returning the created object.
    396         """
--> 397         obj = self.model(**kwargs)
    398         self._for_write = True
    399         obj.save(force_insert=True, using=self.db)

C:\Python27\lib\site-packages\django\db\models\base.pyc in __init__(self, *args, **kwargs)
    535                 # checked) by the RelatedObjectDescriptor.
    536                 if rel_obj is not DEFERRED:
--> 537                     setattr(self, field.name, rel_obj)
    538             else:
    539                 if val is not DEFERRED:

C:\Python27\lib\site-packages\django\db\models\fields\related_descriptors.pyc in __set__(self, instance, value)
    209                     instance._meta.object_name,
    210                     self.field.name,
--> 211                     self.field.remote_field.model._meta.object_name,
    212                 )
    213             )

ValueError: Cannot assign "'CodingDojo Seattle'": "Ninja.dojo" must be a "Dojo" instance.

In [14]: Ninja.objects.create(first_name='Hymie', last_name="Hamster", dojo=Dojo.objects.get(id=2))
Out[14]: <Ninja: Ninja object>

In [15]: Ninja.objects.create(first_name='Pammie', last_name="Pangoline", dojo=Dojo.objects.get(id=3))
Out[15]: <Ninja: Ninja object>

In [16]: Dojo.objects.first().ninjas.all()
Out[16]: <QuerySet []>

In [17]: Ninja.objects.first().dojo
Out[17]: <Dojo: Dojo object>

In [18]: Dojo.objects.get(id=1).delete()
Out[18]: (1, {u'dojo_ninjas.Dojo': 1, u'dojo_ninjas.Ninja': 0})

In [19]: Dojo.objects.get(id=2).delete()
Out[19]: (2, {u'dojo_ninjas.Dojo': 1, u'dojo_ninjas.Ninja': 1})

In [20]: Dojo.objects.get(id=33).delete()
---------------------------------------------------------------------------
DoesNotExist                              Traceback (most recent call last)
<ipython-input-20-f6656757666e> in <module>()
----> 1 Dojo.objects.get(id=33).delete()

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

DoesNotExist: Dojo matching query does not exist.

In [21]: Dojo.objects.get(id=3).delete()
Out[21]: (2, {u'dojo_ninjas.Dojo': 1, u'dojo_ninjas.Ninja': 1})

In [22]: Dojo.objects.create(name='CodingDojo Silicon Valley2', city="Mountain View" , state="CA")
Out[22]: <Dojo: Dojo object>

In [23]: Dojo.objects.create(name='CodingDojo Seattle2', city="Seattle" , state="WA")
Out[23]: <Dojo: Dojo object>

In [24]: Dojo.objects.create(name='CodingDojo New York2', city="New York" , state="NY")
Out[24]: <Dojo: Dojo object>

In [25]: Dojo.objects.first().ninjas.first()

In [26]: Dojo.objects.last().ninjas.first()

In [27]: Dojo.objects.get(id=1).ninjas.get(id=1)
---------------------------------------------------------------------------
DoesNotExist                              Traceback (most recent call last)
<ipython-input-27-9e5bf50e18e0> in <module>()
----> 1 Dojo.objects.get(id=1).ninjas.get(id=1)

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

DoesNotExist: Dojo matching query does not exist.

In [28]: Dojo.objects.get(id=3).ninjas.get(id=1)
---------------------------------------------------------------------------
DoesNotExist                              Traceback (most recent call last)
<ipython-input-28-fe9e331e9834> in <module>()
----> 1 Dojo.objects.get(id=3).ninjas.get(id=1)

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

DoesNotExist: Dojo matching query does not exist.

In [29]: Dojo.objects.get(id=4).ninjas.get(id=1)
---------------------------------------------------------------------------
DoesNotExist                              Traceback (most recent call last)
<ipython-input-29-1d61f8f7c882> in <module>()
----> 1 Dojo.objects.get(id=4).ninjas.get(id=1)

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

DoesNotExist: Ninja matching query does not exist.

In [30]: Dojo.objects.get(id=5).ninjas.get(id=1)
---------------------------------------------------------------------------
DoesNotExist                              Traceback (most recent call last)
<ipython-input-30-6d1b0be50e8e> in <module>()
----> 1 Dojo.objects.get(id=5).ninjas.get(id=1)

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

DoesNotExist: Ninja matching query does not exist.

In [31]: Ninja.objects.get(id=1).delete()
---------------------------------------------------------------------------
DoesNotExist                              Traceback (most recent call last)
<ipython-input-31-e1150b9019b9> in <module>()
----> 1 Ninja.objects.get(id=1).delete()

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

DoesNotExist: Ninja matching query does not exist.

In [32]: Ninja.objects.all()
Out[32]: <QuerySet []>

In [33]: Ninja.objects.all().delete()
Out[33]: (0, {u'dojo_ninjas.Ninja': 0})

In [34]: Ninja.objects.create(first_name='Hymie', last_name="Hamster", dojo=Dojo.objects.get(id=4))
Out[34]: <Ninja: Ninja object>

In [35]: Ninja.objects.create(first_name='Sammie', last_name="Hamster", dojo=Dojo.objects.get(id=4))
Out[35]: <Ninja: Ninja object>

In [36]: Ninja.objects.create(first_name='Tammie', last_name="Hamster", dojo=Dojo.objects.get(id=4))
Out[36]: <Ninja: Ninja object>

In [37]: Ninja.objects.create(first_name='Gary', last_name="Gar", dojo=Dojo.objects.get(id=5))
Out[37]: <Ninja: Ninja object>

In [38]: Ninja.objects.create(first_name='Lary', last_name="Gar", dojo=Dojo.objects.get(id=5))
Out[38]: <Ninja: Ninja object>

In [39]: Ninja.objects.create(first_name='Bary', last_name="Gar", dojo=Dojo.objects.get(id=5))
Out[39]: <Ninja: Ninja object>

In [40]: Ninja.objects.create(first_name='Billy', last_name="Bat", dojo=Dojo.objects.get(id=6))
Out[40]: <Ninja: Ninja object>

In [41]: Ninja.objects.create(first_name='Willy', last_name="Bat", dojo=Dojo.objects.get(id=6))
Out[41]: <Ninja: Ninja object>

In [42]: Ninja.objects.create(first_name='Nilly', last_name="Bat", dojo=Dojo.objects.get(id=6))
Out[42]: <Ninja: Ninja object>

In [43]: Dojo.objects(id=4).ninjas.objects.all()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-43-e2b3815df9ed> in <module>()
----> 1 Dojo.objects(id=4).ninjas.objects.all()

TypeError: 'Manager' object is not callable

In [44]: Dojo.objects(id=4).ninja.objects.all()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-44-c1b087961d54> in <module>()
----> 1 Dojo.objects(id=4).ninja.objects.all()

TypeError: 'Manager' object is not callable

In [45]: Ninja.objects.filter(dojo="*Seattle*")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-45-0172b889c841> in <module>()
----> 1 Ninja.objects.filter(dojo="*Seattle*")

C:\Python27\lib\site-packages\django\db\models\manager.pyc in manager_method(self, *args, **kwargs)
     83         def create_method(name, method):
     84             def manager_method(self, *args, **kwargs):
---> 85                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     86             manager_method.__name__ = method.__name__
     87             manager_method.__doc__ = method.__doc__

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
     98                 # as we don't get to the direct value branch otherwise.
     99                 target_field = self.lhs.output_field.get_path_info()[-1].target_fields[-1]
--> 100                 self.rhs = target_field.get_prep_value(self.rhs)
    101
    102         return super(RelatedLookupMixin, self).get_prep_lookup()

C:\Python27\lib\site-packages\django\db\models\fields\__init__.pyc in get_prep_value(self, value)
    944         if value is None:
    945             return None
--> 946         return int(value)
    947
    948     def contribute_to_class(self, cls, name, **kwargs):

ValueError: invalid literal for int() with base 10: '*Seattle*'

In [46]: Ninja.objects.filter(dojo="*Seattle")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-46-ae8fc7f3e63b> in <module>()
----> 1 Ninja.objects.filter(dojo="*Seattle")

C:\Python27\lib\site-packages\django\db\models\manager.pyc in manager_method(self, *args, **kwargs)
     83         def create_method(name, method):
     84             def manager_method(self, *args, **kwargs):
---> 85                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     86             manager_method.__name__ = method.__name__
     87             manager_method.__doc__ = method.__doc__

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
     98                 # as we don't get to the direct value branch otherwise.
     99                 target_field = self.lhs.output_field.get_path_info()[-1].target_fields[-1]
--> 100                 self.rhs = target_field.get_prep_value(self.rhs)
    101
    102         return super(RelatedLookupMixin, self).get_prep_lookup()

C:\Python27\lib\site-packages\django\db\models\fields\__init__.pyc in get_prep_value(self, value)
    944         if value is None:
    945             return None
--> 946         return int(value)
    947
    948     def contribute_to_class(self, cls, name, **kwargs):

ValueError: invalid literal for int() with base 10: '*Seattle'

In [47]: Ninja.objects.filter(name="CodingDojo Seattle2")
---------------------------------------------------------------------------
FieldError                                Traceback (most recent call last)
<ipython-input-47-b00313774de8> in <module>()
----> 1 Ninja.objects.filter(name="CodingDojo Seattle2")

C:\Python27\lib\site-packages\django\db\models\manager.pyc in manager_method(self, *args, **kwargs)
     83         def create_method(name, method):
     84             def manager_method(self, *args, **kwargs):
---> 85                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     86             manager_method.__name__ = method.__name__
     87             manager_method.__doc__ = method.__doc__

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
   1131         if not arg:
   1132             raise FieldError("Cannot parse keyword query %r" % arg)
-> 1133         lookups, parts, reffed_expression = self.solve_lookup_type(arg)
   1134         if not allow_joins and len(parts) > 1:
   1135             raise FieldError("Joined field references are not permitted in this query")

C:\Python27\lib\site-packages\django\db\models\sql\query.pyc in solve_lookup_type(self, lookup)
   1017             if expression:
   1018                 return expression_lookups, (), expression
-> 1019         _, field, _, lookup_parts = self.names_to_path(lookup_splitted, self.get_meta())
   1020         field_parts = lookup_splitted[0:len(lookup_splitted) - len(lookup_parts)]
   1021         if len(lookup_parts) == 0:

C:\Python27\lib\site-packages\django\db\models\sql\query.pyc in names_to_path(self, names, opts, allow_many, fail_on_missing)
   1325                     available = sorted(field_names + list(self.annotation_select))
   1326                     raise FieldError("Cannot resolve keyword %r into field. "
-> 1327                                      "Choices are: %s" % (name, ", ".join(available)))
   1328                 break
   1329             # Check if we need any joins for concrete inheritance cases (the

FieldError: Cannot resolve keyword 'name' into field. Choices are: dojo, dojo_id, first_name, id, last_name

In [48]: Ninja.objects.filter(name=Dojo.objects.get(id=4))
---------------------------------------------------------------------------
FieldError                                Traceback (most recent call last)
<ipython-input-48-4dcbd8b8b11a> in <module>()
----> 1 Ninja.objects.filter(name=Dojo.objects.get(id=4))

C:\Python27\lib\site-packages\django\db\models\manager.pyc in manager_method(self, *args, **kwargs)
     83         def create_method(name, method):
     84             def manager_method(self, *args, **kwargs):
---> 85                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     86             manager_method.__name__ = method.__name__
     87             manager_method.__doc__ = method.__doc__

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
   1131         if not arg:
   1132             raise FieldError("Cannot parse keyword query %r" % arg)
-> 1133         lookups, parts, reffed_expression = self.solve_lookup_type(arg)
   1134         if not allow_joins and len(parts) > 1:
   1135             raise FieldError("Joined field references are not permitted in this query")

C:\Python27\lib\site-packages\django\db\models\sql\query.pyc in solve_lookup_type(self, lookup)
   1017             if expression:
   1018                 return expression_lookups, (), expression
-> 1019         _, field, _, lookup_parts = self.names_to_path(lookup_splitted, self.get_meta())
   1020         field_parts = lookup_splitted[0:len(lookup_splitted) - len(lookup_parts)]
   1021         if len(lookup_parts) == 0:

C:\Python27\lib\site-packages\django\db\models\sql\query.pyc in names_to_path(self, names, opts, allow_many, fail_on_missing)
   1325                     available = sorted(field_names + list(self.annotation_select))
   1326                     raise FieldError("Cannot resolve keyword %r into field. "
-> 1327                                      "Choices are: %s" % (name, ", ".join(available)))
   1328                 break
   1329             # Check if we need any joins for concrete inheritance cases (the

FieldError: Cannot resolve keyword 'name' into field. Choices are: dojo, dojo_id, first_name, id, last_name

In [49]: Ninja.objects.filter(dojo=Dojo.objects.get(id=4))
Out[49]: <QuerySet [<Ninja: Ninja object>, <Ninja: Ninja object>, <Ninja: Ninja object>]>

In [50]: Ninja.objects.filter(dojo=Dojo.objects.get(id=5))
Out[50]: <QuerySet [<Ninja: Ninja object>, <Ninja: Ninja object>, <Ninja: Ninja object>]>

In [51]: Ninja.objects.filter(dojo=Dojo.objects.get(id=))
  File "<ipython-input-51-ce8f4d220dd5>", line 1
    Ninja.objects.filter(dojo=Dojo.objects.get(id=))
                                                  ^
SyntaxError: invalid syntax


In [52]: Ninja.objects.filter(dojo=Dojo.objects.get(id=6))
Out[52]: <QuerySet [<Ninja: Ninja object>, <Ninja: Ninja object>, <Ninja: Ninja object>]>
