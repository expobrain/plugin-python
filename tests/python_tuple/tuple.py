()
1,
(1,)
(1, 2)
(1, 2, 3,)

foo(())
foo((1,))
foo((1, 2))
foo((1, 2,))

x[()]
x[(1,)]
x[1,]
x[(1, 2)]
x[(1, 2,)]

((), ())
((), (1,))
((), (1, 2))

[(), (1), (1,), (1, 2), (1, 2,)]

(very_long_variable_name_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa, very_long_variable_name_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa)

a, b = very_long_variable_name_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa, very_long_variable_name_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

a = (1,
     2,
     3)


def f():
    return (1, 2)
