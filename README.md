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
  -a, --admin-panel               Start discrete server for admin panel
                                  (disable now)
  --host TEXT                     Host, default `0.0.0.0`
  --port INTEGER                  Port, default `5984`
  --engine [sqlite|inmemory|csv]  Backend engine (disable now)
  -v, --version                   Show the version and exit
  -h, --help                      Show this message and exit
```

## документация

* https://pouchdb.com/api.html
* https://docs.couchdb.org/en/stable/api/index.html

## todolist & history

* [ ] список документов
* [ ] вопрос сковозного ID
* [ ] v0.2.6 коллекции\базы данных: список, создание, удаление
* [x] v0.2.5 `class InformationSchema(ModuleType)` универсальный конфиг `import information_schema`
* [x] консольные команды
* древняя история

код буквально сейчас находится в разработке, все замечания и предложения шлите пул-реквестами


## License

`poufdb` распространяется по лицензии [Apache 2](https://spdx.org/licenses/Apache-2.0.html),
которая, возможно, будет изменена для коммерческого использования. Использование в академических
целях (для обучения) бесплатное.
