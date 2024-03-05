# PoufDB (alpha version)

_Замечание по именованию: pouf (aka pouffe) это пуф, он же пуфик, в буквальном переводе означает
 набивное, или "надутое" кресло. Библиотека PoufDB версии 0.2 основана на исходном коде
 [ChairDB версии 0.1](https://github.com/marten-de-vries/chairdb/blob/5cd64c7b58eef960a434da672e72c9b73e576283/chairdb/server/__init__.py#L21)._


-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Установка и запуск

```console
git clone --depth=1 http://%репозиторий% .
pip install --upgrade .
```
```console
poufdb
```
* `poufdb --start` запускает API сервер
* `poufdb --admin-panel` запустит отдельный сервер для панели администрирования локального сервера
* `poufdb --help` остальные опции, список пополняется



## License

`poufdb` распространяется под лицензией [Apache 2](https://spdx.org/licenses/Apache-2.0.html),
 которая, возможно, будет изменена для коммерческого использования. Использование в академических
 целях (для обучения) бесплатное.
