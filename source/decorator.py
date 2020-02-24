def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)

    wrapped.calls = 0
    return wrapped


def txt_output(text='little nigger'):
    print(f"who's coming? {text} is")


class CountedClass:
    @counted
    def class_txt_output_1(self, txt):
        print(f'{txt}')

    @counted
    def class_txt_output_2(self, txt):
        print(f'{txt}')


c_c_instance_1 = CountedClass()
c_c_instance_1.class_txt_output_1('first instance')
print('number of calling (CountedClass):', c_c_instance_1.class_txt_output_1.calls)

c_c_instance_2 = CountedClass()
c_c_instance_2.class_txt_output_2('second instance')
c_c_instance_2.class_txt_output_2('second instance')
print(f'number of calling (CountedClass): {c_c_instance_2.class_txt_output_2.calls}\n')

getText = counted(txt_output)

getText('little D')
getText('Misha')
getText()
print('number of calling:', getText.calls)
