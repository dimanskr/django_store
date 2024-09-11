from django.core.management import BaseCommand
from catalog.models import Product, Category
from django.apps import apps

import json
import os


class Command(BaseCommand):
    """
    Класс Команда
    """

    @staticmethod
    def _find_fixture_files(app_name):
        """
        Ищет файлы фикстур в папке fixtures приложения app_name.
        """
        fixture_files = []

        # Поиск конфига текущего приложения по имени
        try:
            app_config = apps.get_app_config(app_name)
        except LookupError:
            print(f"Приложение '{app_name}' не найдено.")
            return fixture_files

        # Путь к директории fixtures в текущем приложении
        fixtures_dir = os.path.join(app_config.path, "fixtures")

        if os.path.exists(fixtures_dir) and os.path.isdir(fixtures_dir):
            # Проверка всех файлов в директории fixtures
            for filename in os.listdir(fixtures_dir):
                # Проверяем только файлы с расширениями фикстур
                if filename.endswith(".json"):
                    fixture_path = os.path.join(fixtures_dir, filename)
                    fixture_files.append(fixture_path)
                    print(f"Найдены фикстуры: {fixture_path}")
        else:
            print(f"Папка fixtures в приложении '{app_name}' не найдена.")

        return fixture_files

    @staticmethod
    def json_read_categories(fixture_path: str) -> list[dict]:
        categories_data = []
        try:
            with open(fixture_path, "r", encoding="utf-8") as file:
                data = json.load(file)

                for row in data:
                    if row["model"] == "catalog.category":
                        category_data_json = {
                            "pk": row["pk"],
                            "name": row["fields"].get("name"),
                            "description": row["fields"].get("description"),
                        }
                        categories_data.append(category_data_json)

                print("Категории загружены из JSON")
                return categories_data
        except FileNotFoundError:
            print(f"Файл с фикстурами не найден.")
        except json.JSONDecodeError:
            print("Ошибка при декодировании JSON.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        return []

    @staticmethod
    def json_read_products(fixture_path: str) -> list[dict]:
        products_data = []
        try:
            with open(fixture_path, "r", encoding="utf-8") as file:
                data = json.load(file)

                for row in data:
                    if row["model"] == "catalog.product":
                        product_data_json = {
                            "name": row["fields"].get("name"),
                            "description": row["fields"].get("description"),
                            "preview": row["fields"].get("preview"),
                            "category": row["fields"].get("category"),
                            "price": row["fields"].get("price"),
                            "created_at": row["fields"].get("created_at"),
                            "updated_at": row["fields"].get("updated_at"),
                        }
                        products_data.append(product_data_json)

                print(f"Продукты загружены из JSON в количестве: {len(products_data)}")
                return products_data
        except FileNotFoundError:
            print(f"Файл с фикстурами не найден.")
        except json.JSONDecodeError:
            print("Ошибка при декодировании JSON.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        return []

    def handle(self, *args, **options):
        """
        Заполняет данные о продуктах и категориях в БД
        """
        # получаем список файлов фикстур в папке приложения 'catalog'
        fixtures_list = self._find_fixture_files(app_name="catalog")

        # задаем путь к первому из списка файлов фикстур если они нашлись
        if fixtures_list:
            fixtures_path = fixtures_list[0]
            print(f"Берем фикстуры из файла: {fixtures_path}")
        else:
            fixtures_path = None

        Product.objects.all().delete()
        Category.objects.all().delete()

        categories_for_create = []
        products_for_create = []

        for category in Command.json_read_categories(fixtures_path):
            categories_for_create.append(Category(**category))

        print(*categories_for_create)

        Category.objects.bulk_create(categories_for_create)

        for product in Command.json_read_products(fixtures_path):
            products_for_create.append(
                Product(
                    name=product["name"],
                    description=product["description"],
                    preview=product["preview"],
                    category=Category.objects.get(pk=product["category"]),
                    price=product["price"],
                    created_at=product["created_at"],
                    updated_at=product["updated_at"],
                )
            )

        print(*products_for_create)

        Product.objects.bulk_create(products_for_create)
