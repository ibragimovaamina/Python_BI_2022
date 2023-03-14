#!/usr/bin/env python
# coding: utf-8

# # Задание 1 (2 балла)

# Напишите класс `MyDict`, который будет полностью повторять поведение обычного словаря, за исключением того, что при итерации мы должны получать и ключи, и значения.
# 
# **Модули использовать нельзя**

# In[22]:


class MyDict(dict):
    def __iter__(self):
        return zip(self.keys(), self.values())


# In[23]:


dct = MyDict({"a": 1, "b": 2, "c": 3, "d": 25})
dct


# In[33]:


for item in iter(dct):
    print(item)


# In[29]:


for key, value in dct:
    print(key, value)   


# In[30]:


for key, value in dct.items():
    print(key, value)


# In[31]:


for key in dct.keys():
    print(key)


# In[32]:


dct["c"] + dct["d"]


# # Задание 2 (2 балла)

# Напишите функцию `iter_append`, которая "добавляет" новый элемент в конец итератора, возвращая итератор, который включает изначальные элементы и новый элемент. Итерироваться по итератору внутри функции нельзя, то есть вот такая штука не принимается
# ```python
# def iter_append(iterator, item):
#     lst = list(iterator) + [item]
#     return iter(lst)
# ```
# 
# **Модули использовать нельзя**

# In[58]:


def iter_append(iterator, item):
    new_iterator = []
    while True:
        try:
            elem = next(iterator)
            new_iterator.append(elem)
        except StopIteration:
            new_iterator.append(item)
            break
    return new_iterator


# In[59]:


my_iterator = iter([1, 2, 3])
new_iterator = iter_append(my_iterator, 4)

for element in new_iterator:
    print(element)


# # Задание 3 (5 баллов)

# Представим, что мы установили себе некотoрую библиотеку, которая содержит в себе два класса `MyString` и `MySet`, которые являются наследниками `str` и `set`, но также несут и дополнительные методы.
# 
# Проблема заключается в том, что библиотеку писали не очень аккуратные люди, поэтому получилось так, что некоторые методы возвращают не тот тип данных, который мы ожидаем. Например, `MyString().reverse()` возвращает объект класса `str`, хотя логичнее было бы ожидать объект класса `MyString`.
# 
# Найдите и реализуйте удобный способ сделать так, чтобы подобные методы возвращали экземпляр текущего класса, а не родительского. При этом **код методов изменять нельзя**
# 
# **+3 дополнительных балла** за реализацию того, чтобы **унаследованные от `str` и `set` методы** также возвращали объект интересующего нас класса (то есть `MyString.replace(..., ...)` должен возвращать `MyString`). **Переопределять методы нельзя**
# 
# **Модули использовать нельзя**

# In[115]:


def wrapper_MyString(func):
    def inner_func(input_str):
        result_str = func(input_str)
        result_MyString = MyString(result_str)
        return result_MyString
    return inner_func


def wrapper_MySet(func):
    def inner_func(*args):
        result_set = func(*args)
        result_MySet = MySet(result_set)
        return result_MySet
    return inner_func
    

    

class MyString(str):
    @wrapper_MyString
    def reverse(self):
        return self[::-1]
    
    @wrapper_MyString
    def make_uppercase(self):
        return "".join([chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char for char in self])

    @wrapper_MyString
    def make_lowercase(self):
        return "".join([chr(ord(char) + 32) if 65 <= ord(char) <= 90 else char for char in self])
    
    @wrapper_MyString
    def capitalize_words(self):
        return " ".join([word.capitalize() for word in self.split()])
    
    
class MySet(set):
    def is_empty(self):
        return len(self) == 0
    
    def has_duplicates(self):
        return len(self) != len(set(self))
    
    @wrapper_MySet
    def union_with(self, other):
        return self.union(other)
    
    @wrapper_MySet
    def intersection_with(self, other):
        return self.intersection(other)
    
    @wrapper_MySet
    def difference_with(self, other):
        return self.difference(other)


# In[26]:


string_example = MyString("Aa Bb Cc")
set_example_1 = MySet({1, 2, 3, 4})
set_example_2 = MySet({3, 4, 5, 6, 6})

print(type(string_example.reverse()))
print(type(string_example.make_uppercase()))
print(type(string_example.make_lowercase()))
print(type(string_example.capitalize_words()))
print()
print(type(set_example_1.is_empty()))
print(type(set_example_2.has_duplicates()))
print(type(set_example_1.union_with(set_example_2)))
print(type(set_example_1.difference_with(set_example_2)))


# # Задание 4 (5 баллов)

# Напишите декоратор `switch_privacy`:
# 1. Делает все публичные **методы** класса приватными
# 2. Делает все приватные методы класса публичными
# 3. Dunder методы и защищённые методы остаются без изменений
# 4. Должен работать тестовый код ниже, в теле класса писать код нельзя
# 
# **Модули использовать нельзя**

# In[112]:


# Ваш код здесь
class ExampleClass:
    # Но не здесь
    def public_method(self):
        return 1
    
    def _protected_method(self):
        return 2
    
    def __private_method(self):
        return 3
    
    def __dunder_method__(self):
        pass


# In[113]:


test_object = ExampleClass()

test_object._ExampleClass__public_method()   # Публичный метод стал приватным


# In[114]:


test_object.private_method()   # Приватный метод стал публичным


# In[115]:


test_object._protected_method()   # Защищённый метод остался защищённым


# In[116]:


test_object.__dunder_method__()   # Дандер метод не изменился


# In[117]:


hasattr(test_object, "public_method"), hasattr(test_object, "private")   # Изначальные варианты изменённых методов не сохраняются


# # Задание 5 (7 баллов)

# Напишите [контекстный менеджер](https://docs.python.org/3/library/stdtypes.html#context-manager-types) `OpenFasta`
# 
# Контекстные менеджеры это специальные объекты, которые могут работать с конструкцией `with ... as ...:`. В них нет ничего сложного, для их реализации как обычно нужно только определить только пару dunder методов. Изучите этот вопрос самостоятельно
# 
# 1. Объект должен работать как обычные файлы в питоне (наследоваться не надо, здесь лучше будет использовать **композицию**), но:
#     + При итерации по объекту мы должны будем получать не строку из файла, а специальный объект `FastaRecord`. Он будет хранить в себе информацию о последовательности. Важно, **не строки, а именно последовательности**, в fasta файлах последовательность часто разбивают на много строк
#     + Нужно написать методы `read_record` и `read_records`, которые по смыслу соответствуют `readline()` и `readlines()` в обычных файлах, но они должны выдавать не строки, а объект(ы) `FastaRecord`
# 2. Конструктор должен принимать один аргумент - **путь к файлу**
# 3. Класс должен эффективно распоряжаться памятью, с расчётом на работу с очень большими файлами
#     
# Объект `FastaRecord`. Это должен быть **датакласс** (см. про примеры декораторов в соответствующей лекции) с тремя полями:
# + `seq` - последовательность
# + `id_` - ID последовательности (это то, что в фаста файле в строке, которая начинается с `>` до первого пробела. Например, >**GTD326487.1** Species anonymous 24 chromosome) 
# + `description` - то, что осталось после ID (Например, >GTD326487.1 **Species anonymous 24 chromosome**)
# 
# 
# Напишите демонстрацию работы кода с использованием всех написанных методов, обязательно добавьте файл с тестовыми данными в репозиторий (не обязательно большой)
# 
# **Можно использовать модули из стандартной библиотеки**

# In[153]:


# Ваш код здесь


with OpenFasta(os.path.join("data", "example.fasta")) as fasta:
    # Ваш код здесь
    pass


# # Задание 6 (7 баллов)

# 1. Напишите код, который позволит получать все возможные (неуникальные) генотипы при скрещивании двух организмов. Это может быть функция или класс, что вам кажется более удобным.
# 
# Например, все возможные исходы скрещивания "Aabb" и "Aabb" (неуникальные) это
# 
# ```
# AAbb
# AAbb
# AAbb
# AAbb
# Aabb
# Aabb
# Aabb
# Aabb
# Aabb
# Aabb
# Aabb
# Aabb
# aabb
# aabb
# aabb
# aabb
# ```
# 
# 2. Напишите функцию, которая вычисляет вероятность появления определённого генотипа (его ожидаемую долю в потомстве).
# Например,
# 
# ```python
# get_offspting_genotype_probability(parent1="Aabb", parent2="Aabb", target_genotype="Аabb")   # 0.5
# 
# ```
# 
# 3. Напишите код, который выводит все уникальные генотипы при скрещивании `'АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн'` и `'АаббВвГгДДЕеЖжЗзИиЙйКкЛлМмНН'`, которые содержат в себе следующую комбинацию аллелей `'АаБбВвГгДдЕеЖжЗзИиЙйКкЛл'`
# 4. Напишите код, который расчитывает вероятность появления генотипа `'АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн'` при скрещивании `АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн` и `АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн`
# 
# Важные замечания:
# 1. Порядок следования аллелей в случае гетерозигот всегда должен быть следующим: сначала большая буква, затем маленькая (вариант `AaBb` допустим, но `aAbB` быть не должно)
# 2. Подзадачи 3 и 4 могут потребовать много вычислительного времени (до 15+ минут в зависимости от железа), поэтому убедитесь, что вы хорошо протестировали написанный вами код на малых данных перед выполнением этих задач. Если ваш код работает **дольше 20 мин**, то скорее всего ваше решение не оптимально, попытайтесь что-нибудь оптимизировать. Если оптимальное решение совсем не получается, то попробуйте из входных данных во всех заданиях убрать последний ген (это должно уменьшить время выполнения примерно в 4 раза), но **за такое решение будет снято 2 балла**
# 3. Несмотря на то, что подзадания 2, 3 и 4 возможно решить математически, не прибегая к непосредственному получению всех возможных генотипов, от вас требуется именно brute-force вариант алгоритма
# 
# **Можно использовать модули из стандартной библиотеки питона**, но **за выполнение задания без использования модулей придусмотрено +3 дополнительных балла**

# In[18]:


# Ваш код здесь (1 и 2 подзадание)


# In[20]:


# Ваш код здесь (3 подзадание)


# In[21]:


# Ваш код здесь (4 подзадание)

