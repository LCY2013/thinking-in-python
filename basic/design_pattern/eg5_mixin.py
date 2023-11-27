def mixin(Klass, MixinKlass):
    Klass.__bases__ = (MixinKlass,) + Klass.__bases__


class Fclass(object):
    def text(self):
        print('in father class')


class S1Class(Fclass):
    pass


class MixinClass(object):
    def text(self):
        return super().text()
        # print('in MixinClass')


class S2Class(S1Class, MixinClass):
    pass


print(f' test1 : S1Class MRO : {S1Class.mro()}')
s1 = S1Class()
s1.text()

mixin(S1Class, MixinClass)
print(f' test2 : S1Class MRO : {S1Class.mro()}')
s1 = S1Class()
s1.text()

print(f' test3 : S2Class MRO : {S2Class.mro()}')
s2 = S2Class()
s2.text()
