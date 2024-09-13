def test_function():
    def inner_function():
        print('в области видимости test_function')
    inner_function()

test_function()
# inner_function() функция inner_function находится вне зоны видимости за пределами функции test_function поэтому ее выозов невозможен
