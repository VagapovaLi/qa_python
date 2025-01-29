import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_success(self):
        collector = BooksCollector()
        collector.add_new_book('ф')

        assert 'ф' in collector.books_genre

    def test_long_book_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Жареные зеленые помидоры в кафе Полустанок')

        assert len(collector.books_genre) == 0

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')

        assert collector.books_genre['Мастер и Маргарита'] == 'Фантастика'

    def test_get_book_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Неизвестная книга')

        assert collector.get_book_genre('Неизвестная книга') == ''


    def test_books_with_specific_genre_print_book(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Анна Каренина')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        collector.set_book_genre('Анна Каренина', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Мастер и Маргарита', 'Анна Каренина']
        assert collector.get_books_with_specific_genre('Ужасы') == []


    @pytest.mark.parametrize('name, genre, expected_genre',
                             (('Мастер и Маргарита','Фантастика', 'Фантастика'),
                              ('Хирург','Триллер','')))

    def test_get_book_genre(self, name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == expected_genre

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита','Фантастика')


        expected_genres = {
            'Мастер и Маргарита' : 'Фантастика'
        }

        assert collector.get_books_genre() == expected_genres


    def test_get_books_for_children_with_children_books( self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', 'Комедии')

        expected_books = [
            'Ревизор'
        ]

        assert collector.get_books_for_children() == expected_books


    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')

        expected_books_favorites = [
            'Мастер и Маргарита'
        ]

        assert collector.favorites == expected_books_favorites and len(collector.favorites) == 1

    def test_add_book_in_favorites_not_repeated(self):
        collector = BooksCollector()
        collector.add_new_book('Анна Каренина')
        collector.add_new_book('Анна Каренина')
        collector.add_book_in_favorites('Анна Каренина')

        expected_books_favorites = [
            'Анна Каренина'
        ]

        assert collector.favorites == expected_books_favorites and len(collector.favorites) == 1

    def test_delete_book_from_favorite_success(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.delete_book_from_favorites('Мастер и Маргарита')

        expected_books_favorites =[]

        assert collector.favorites == expected_books_favorites



    def test_get_list_of_favorites_book(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Анна Каренина')
        collector.add_new_book('1984')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.add_book_in_favorites('Анна Каренина')


        expected_books_favorites =[
            'Мастер и Маргарита',
            'Анна Каренина']

        assert collector.favorites == expected_books_favorites