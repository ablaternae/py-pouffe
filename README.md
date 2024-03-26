# PoufDB (alpha version)

_Замечание по именованию: pouf (aka pouffe) это пуф, он же пуфик, в буквальном переводе означает
набивное, мягкое, или "надутое" кресло. Библиотека PoufDB версии 0.2 основана на исходном коде
[ChairDB версии 0.1](https://github.com/marten-de-vries/chairdb/blob/5cd64c7b58eef960a434da672e72c9b73e576283/chairdb/server/__init__.py#L21)._

-----

## Установка и запуск

```console
> git clone --depth=1 https://github.com/ablaternae/py-pouffe .
> pip install --upgrade .
```
```console
> poufdb --help
Usage: poufdb [OPTIONS] COMMAND [ARGS]...

Options:
  -r, --start                     Server run
  -d, --data-dir PATH             Data directory, default `%current_dir%/_data`
  --host TEXT                     Host, default `127.0.59.84`
  --port INTEGER                  Port, default `5984`
  -v, --version                   Show the version and exit
  -h, --help                      Show this message and exit
```

## документация

* https://pouchdb.com/api.html
* https://docs.couchdb.org/en/stable/api/index.html
* https://docs.couchdb.org/en/stable/api/database/common.html
* https://docs.peewee-orm.com/en/latest/peewee/database.html
* https://docs.peewee-orm.com/en/latest/peewee/models.html
* https://docs.peewee-orm.com/en/latest/peewee/playhouse.html#Introspector

## различия и особенности

* PouchDB использует md5 в \_rev ревизиях документов, здесь по-умолчанию десятисимвольный хеш; надо добавить в настройки
* В отличие от CouchDB почти везде в url применяются завершающие слеши 

## todolist & history

* [ ] сделать примеры с генерацией данных
* [ ] три варианта документации API: 
классы (методы, иерархия), управляющие константы, вспомогательная information_schema
* [ ] возможность шифрования данных (через архивацию, или шифром?) 
* [ ] большой апгрейд: пользователи, система прав и ролей 
* [ ] добавить режим админа 
* [ ] добавить в настройки выбор хеша 
* [ ] список документов
* [ ] в процессе v0.2.8 автосоздание моделей документов из `class BaseModel(pw.Model)`, 
базовая модель находится в Storage.Engine
* [ ] в процессе v0.2.7 коллекция баз данных: список, создание, удаление. синглтон находится в storage.databases
* [x] v0.2.6 engines, aka storage backends
* [x] v0.2.5 `class InformationSchema(ModuleType)` универсальный конфиг `import information_schema`
* [x] консольные команды
* древняя история

код буквально сейчас находится в разработке, все замечания и предложения шлите пул-реквестами


## License

`poufdb` распространяется по лицензии [Apache 2](https://spdx.org/licenses/Apache-2.0.html),
которая, возможно, будет изменена для коммерческого использования. Использование в академических
целях (для обучения) бесплатное.
