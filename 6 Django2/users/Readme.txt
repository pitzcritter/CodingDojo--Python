In [1]: from apps.user_login.models import User

In [2]: User.objects.create(first_name="Michael", last_name="Jordan", email="mike@jumpman.com", age=23)
Out[2]: <User: mike@jumpman.com>

In [3]: User.objects.create(first_name="Charlie", last_name="Brown", email="Charlie@Brown.com", age=6)
Out[3]: <User: Charlie@Brown.com>

In [4]: User.objects.create(first_name="Snoopy", last_name="Dog", email="Snoopy@BDog.com", age=3)
Out[4]: <User: Snoopy@BDog.com>

In [5]: User.objects.create(first_name="Linus", last_name="van Pelt", email="Linus@vanPelt.com", age=6)
Out[5]: <User: Linus@vanPelt.com>

In [6]: Users.objects.get(id=1).delete()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-6-ba5f85408dc8> in <module>()
----> 1 Users.objects.get(id=1).delete()

NameError: name 'Users' is not defined

In [7]: User.objects.get(id=1).delete()
Out[7]: (1, {u'user_login.User': 1})

In [8]: User.objects.all()
Out[8]: <QuerySet [<User: Charlie@Brown.com>, <User: Snoopy@BDog.com>, <User: Linus@vanPelt.com>]>

In [9]: User.objects.last()
Out[9]: <User: Linus@vanPelt.com>

In [10]: User.objects.first()
Out[10]: <User: Charlie@Brown.com>

In [11]: User.objects.all().order_by("last_name")
Out[11]: <QuerySet [<User: Charlie@Brown.com>, <User: Snoopy@BDog.com>, <User: Linus@vanPelt.com>]>

In [12]: thisUser = User.objects.get(id=3).last_name = "something"

In [13]: thisUser.save()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-13-7d6a88165efa> in <module>()
----> 1 thisUser.save()

AttributeError: 'str' object has no attribute 'save'

In [14]: thisUser.save()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-14-7d6a88165efa> in <module>()
----> 1 thisUser.save()

AttributeError: 'str' object has no attribute 'save'

In [15]: User.objects.last()
Out[15]: <User: Linus@vanPelt.com>

In [16]: thisUser = User.objects.get(id=3).last_name = "something"

In [17]: thisUser.save()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-17-7d6a88165efa> in <module>()
----> 1 thisUser.save()

AttributeError: 'str' object has no attribute 'save'

In [18]: thisUser = User.objects.get(id=3).last_name

In [19]: thisUser
Out[19]: u'Dog'

In [20]: User.objects.all()
Out[20]: <QuerySet [<User: Charlie@Brown.com>, <User: Snoopy@BDog.com>, <User: Linus@vanPelt.com>]>

In [21]: User.objects.get(id=3).last_name
Out[21]: u'Dog'

In [22]: thisUser = User.objects.get(id=3).last_name = "something"

In [23]: thisUser.save()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-23-7d6a88165efa> in <module>()
----> 1 thisUser.save()

AttributeError: 'str' object has no attribute 'save'

In [24]: User.objects.get(id=4).delete()
Out[24]: (1, {u'user_login.User': 1})
