"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product
from homework.models import Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity_greater(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(5000) is False, 'Книг должно быть недостаточно'

    def test_product_check_quantity_equal(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000), 'Книг должно быть достаточно'

    def test_product_check_quantity_less(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(10), 'Книг должно быть достаточно'

    def test_product_equal(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1000)
        assert product.quantity == 0, 'Книг должно быть достаточно'

    def test_product_less(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1)
        assert product.quantity == 999, 'Книг должно быть достаточно'

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(10001)
            assert pytest.raises(ValueError), 'Ошибка покупки книг больше, чем есть'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, cart, product):
        with pytest.raises(ValueError):
            cart.add_product(product, 50)
            assert cart.products[product] == 50, 'Книг добавлены в карзину'
            cart.add_product(product, 50)
            assert cart.products[product] == 100, 'Количество книг в карзине увеличилось'
            cart.add_product(product, 1500)
            assert pytest.raises(ValueError), 'Книг недостаточно'

    def test_cart_remove_product(self, cart, product):
        cart.add_product(product, 150)
        cart.remove_product(product, 50)
        assert cart.products[product] == 100, 'Книг добавлены в карзину'
        cart.remove_product(product, 50)
        assert cart.products[product] == 50, 'Количество книг в карзине увеличилось'
        cart.remove_product(product, 1500)
        assert product not in cart.products.keys()

    def test_cart_clear(self, cart, product):
        cart.add_product(product, 150)
        cart.clear()
        assert product not in cart.products.keys(), 'Книг нет в карзине'

    def test_cart_total_price(self, cart, product):
        cart.add_product(product, 150)
        assert cart.get_total_price() == 15000, 'Стоимость всех книг в корзине'

    def test_cart_buy_greater(self, cart, product):
        with pytest.raises(ValueError):
            cart.add_product(product, 1500)
            cart.buy()
            assert pytest.raises(ValueError), 'Книг недостаточно'

    def test_cart_buy_equal(self, cart, product):
        cart.add_product(product, 1000)
        cart.buy()
        assert cart.products == {} and product.quantity == 0, 'Все книги проданы'

    def test_cart_buy_less(self, cart, product):
        cart.add_product(product, 150)
        cart.buy()
        assert cart.products == {} and product.quantity == 850, 'Часть книг продана'
