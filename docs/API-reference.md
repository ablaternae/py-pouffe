---
layout:
title: Api
navigation: 2
---

#  API

В запросах следует ориентироваться на https://docs.couchdb.org/en/stable/api/basics.html

Формат ответов и опции подгоняются по https://pouchdb.com/api.html

## API Basics

1. HTTP request methods
    * GET чаще всего служит для информационных запросов
    * POST внесение данных. ответ на запрос без тела предположительно равен ответу на аналогичный GET
    * PUT, DELETE,
    * HEAD только в специальных случаях
    * COPY не поддерживается (и не планируется)

2. Request Headers не учитываются
3. Request URLs чаще всего содержат концевой слеш

4. Response Headers
    * Cache-control автоматически
    * Content-length присутствует, как правило, для всех ответов, размер контента в байтах
    * Content-type всегда "application/json; charset=utf-8". text/* не поддерживается.
    * Etag в разработке
    * X-Pouch-Response-Time X-Pouch-Request-ID возможно, будут введены с логированием запросов

5. HTTP Status Codes
Стандартно. На неподдерживаемые запросы отвечает 405, 406 или 400.

-----

## Server

### GET / POST /
если сервер работает
Status Codes: 200 OK
```json
{
    "pouchdb": "%welcome_string%",
    "id": "f63bf3fd8e77500404cb273a3b5e1927553f678d5b2ea19fcd1c5b0b335c8259",
    "uuid": "a7705eff-eb91-11ee-b295-a6ca50ecdda5",
    "vendor": "ablaternae.github.io/py-pouffe",
    "version": "0.2.xxx"
}
```
когда сервер не работает, ответ будет любой другой

**NB: ответ не содержит** `{"ok":True}`




### GET /_active_tasks

доступно только в режиме админа



