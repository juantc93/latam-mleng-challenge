# README    

Este repositorio contiene el reto de código para Latam Airlines.
```
testLatam
├─ app
│  ├─ main.py
│  ├─ models
│  │  └─ model_v0.pkl
│  ├─ src
│  │  ├─ models
│  │  │  ├─ predict.py
│  │  │  ├─ predict_v0.json
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     ├─ predict.cpython-39.pyc
│  │  │     └─ __init__.cpython-39.pyc
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     └─ __init__.cpython-39.pyc
│  ├─ __init__.py
│  └─ __pycache__
│     └─ main.cpython-39.pyc
├─ Challenge - ML Engineer.pdf
├─ dataset_SCL.csv
├─ Dockerfile
├─ env
│  ├─ Include
│  ├─ Lib
│  │  └─ site-packages
│  │     ├─ 2ec0e72aa72355e6eccf__mypyc.cp39-win_amd64.pyd
│  │     ├─ adodbapi
│  │     │  ├─ adodbapi.py
│  │     │  ├─ ado_consts.py
│  │     │  ├─ apibase.py
│  │     │  ├─ examples
│  │     │  │  ├─ db_print.py
│  │     │  │  ├─ db_table_names.py
│  │     │  │  ├─ xls_read.py
│  │     │  │  ├─ xls_write.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ db_print.cpython-39.pyc
│  │     │  │     ├─ db_table_names.cpython-39.pyc
│  │     │  │     ├─ xls_read.cpython-39.pyc
│  │     │  │     └─ xls_write.cpython-39.pyc
│  │     │  ├─ is64bit.py
│  │     │  ├─ license.txt
│  │     │  ├─ process_connect_string.py
│  │     │  ├─ readme.txt
│  │     │  ├─ remote.py
│  │     │  ├─ schema_table.py
│  │     │  ├─ setup.py
│  │     │  ├─ test
│  │     │  │  ├─ adodbapitest.py
│  │     │  │  ├─ adodbapitestconfig.py
│  │     │  │  ├─ dbapi20.py
│  │     │  │  ├─ is64bit.py
│  │     │  │  ├─ setuptestframework.py
│  │     │  │  ├─ test_adodbapi_dbapi20.py
│  │     │  │  ├─ tryconnection.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ adodbapitest.cpython-39.pyc
│  │     │  │     ├─ adodbapitestconfig.cpython-39.pyc
│  │     │  │     ├─ dbapi20.cpython-39.pyc
│  │     │  │     ├─ is64bit.cpython-39.pyc
│  │     │  │     ├─ setuptestframework.cpython-39.pyc
│  │     │  │     ├─ test_adodbapi_dbapi20.cpython-39.pyc
│  │     │  │     └─ tryconnection.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ adodbapi.cpython-39.pyc
│  │     │     ├─ ado_consts.cpython-39.pyc
│  │     │     ├─ apibase.cpython-39.pyc
│  │     │     ├─ is64bit.cpython-39.pyc
│  │     │     ├─ process_connect_string.cpython-39.pyc
│  │     │     ├─ remote.cpython-39.pyc
│  │     │     ├─ schema_table.cpython-39.pyc
│  │     │     ├─ setup.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ anyio
│  │     │  ├─ abc
│  │     │  │  ├─ _resources.py
│  │     │  │  ├─ _sockets.py
│  │     │  │  ├─ _streams.py
│  │     │  │  ├─ _subprocesses.py
│  │     │  │  ├─ _tasks.py
│  │     │  │  ├─ _testing.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _resources.cpython-39.pyc
│  │     │  │     ├─ _sockets.cpython-39.pyc
│  │     │  │     ├─ _streams.cpython-39.pyc
│  │     │  │     ├─ _subprocesses.cpython-39.pyc
│  │     │  │     ├─ _tasks.cpython-39.pyc
│  │     │  │     ├─ _testing.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ from_thread.py
│  │     │  ├─ lowlevel.py
│  │     │  ├─ py.typed
│  │     │  ├─ pytest_plugin.py
│  │     │  ├─ streams
│  │     │  │  ├─ buffered.py
│  │     │  │  ├─ file.py
│  │     │  │  ├─ memory.py
│  │     │  │  ├─ stapled.py
│  │     │  │  ├─ text.py
│  │     │  │  ├─ tls.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ buffered.cpython-39.pyc
│  │     │  │     ├─ file.cpython-39.pyc
│  │     │  │     ├─ memory.cpython-39.pyc
│  │     │  │     ├─ stapled.cpython-39.pyc
│  │     │  │     ├─ text.cpython-39.pyc
│  │     │  │     ├─ tls.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ to_process.py
│  │     │  ├─ to_thread.py
│  │     │  ├─ _backends
│  │     │  │  ├─ _asyncio.py
│  │     │  │  ├─ _trio.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _asyncio.cpython-39.pyc
│  │     │  │     ├─ _trio.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _core
│  │     │  │  ├─ _compat.py
│  │     │  │  ├─ _eventloop.py
│  │     │  │  ├─ _exceptions.py
│  │     │  │  ├─ _fileio.py
│  │     │  │  ├─ _resources.py
│  │     │  │  ├─ _signals.py
│  │     │  │  ├─ _sockets.py
│  │     │  │  ├─ _streams.py
│  │     │  │  ├─ _subprocesses.py
│  │     │  │  ├─ _synchronization.py
│  │     │  │  ├─ _tasks.py
│  │     │  │  ├─ _testing.py
│  │     │  │  ├─ _typedattr.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _compat.cpython-39.pyc
│  │     │  │     ├─ _eventloop.cpython-39.pyc
│  │     │  │     ├─ _exceptions.cpython-39.pyc
│  │     │  │     ├─ _fileio.cpython-39.pyc
│  │     │  │     ├─ _resources.cpython-39.pyc
│  │     │  │     ├─ _signals.cpython-39.pyc
│  │     │  │     ├─ _sockets.cpython-39.pyc
│  │     │  │     ├─ _streams.cpython-39.pyc
│  │     │  │     ├─ _subprocesses.cpython-39.pyc
│  │     │  │     ├─ _synchronization.cpython-39.pyc
│  │     │  │     ├─ _tasks.cpython-39.pyc
│  │     │  │     ├─ _testing.cpython-39.pyc
│  │     │  │     ├─ _typedattr.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ from_thread.cpython-39.pyc
│  │     │     ├─ lowlevel.cpython-39.pyc
│  │     │     ├─ pytest_plugin.cpython-39.pyc
│  │     │     ├─ to_process.cpython-39.pyc
│  │     │     ├─ to_thread.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ anyio-3.6.2.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ argcomplete
│  │     │  ├─ bash_completion.d
│  │     │  │  └─ python-argcomplete
│  │     │  ├─ completers.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ finders.py
│  │     │  ├─ io.py
│  │     │  ├─ lexers.py
│  │     │  ├─ packages
│  │     │  │  ├─ _argparse.py
│  │     │  │  ├─ _shlex.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _argparse.cpython-39.pyc
│  │     │  │     ├─ _shlex.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ shell_integration.py
│  │     │  ├─ _check_console_script.py
│  │     │  ├─ _check_module.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ completers.cpython-39.pyc
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ finders.cpython-39.pyc
│  │     │     ├─ io.cpython-39.pyc
│  │     │     ├─ lexers.cpython-39.pyc
│  │     │     ├─ shell_integration.cpython-39.pyc
│  │     │     ├─ _check_console_script.cpython-39.pyc
│  │     │     ├─ _check_module.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ argcomplete-3.0.8.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.rst
│  │     │  ├─ METADATA
│  │     │  ├─ NOTICE
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ asttokens
│  │     │  ├─ astroid_compat.py
│  │     │  ├─ asttokens.py
│  │     │  ├─ line_numbers.py
│  │     │  ├─ mark_tokens.py
│  │     │  ├─ py.typed
│  │     │  ├─ util.py
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ astroid_compat.cpython-39.pyc
│  │     │     ├─ asttokens.cpython-39.pyc
│  │     │     ├─ line_numbers.cpython-39.pyc
│  │     │     ├─ mark_tokens.cpython-39.pyc
│  │     │     ├─ util.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ asttokens-2.2.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ attr
│  │     │  ├─ converters.py
│  │     │  ├─ converters.pyi
│  │     │  ├─ exceptions.py
│  │     │  ├─ exceptions.pyi
│  │     │  ├─ filters.py
│  │     │  ├─ filters.pyi
│  │     │  ├─ py.typed
│  │     │  ├─ setters.py
│  │     │  ├─ setters.pyi
│  │     │  ├─ validators.py
│  │     │  ├─ validators.pyi
│  │     │  ├─ _cmp.py
│  │     │  ├─ _cmp.pyi
│  │     │  ├─ _compat.py
│  │     │  ├─ _config.py
│  │     │  ├─ _funcs.py
│  │     │  ├─ _make.py
│  │     │  ├─ _next_gen.py
│  │     │  ├─ _typing_compat.pyi
│  │     │  ├─ _version_info.py
│  │     │  ├─ _version_info.pyi
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  └─ __pycache__
│  │     │     ├─ converters.cpython-39.pyc
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ filters.cpython-39.pyc
│  │     │     ├─ setters.cpython-39.pyc
│  │     │     ├─ validators.cpython-39.pyc
│  │     │     ├─ _cmp.cpython-39.pyc
│  │     │     ├─ _compat.cpython-39.pyc
│  │     │     ├─ _config.cpython-39.pyc
│  │     │     ├─ _funcs.cpython-39.pyc
│  │     │     ├─ _make.cpython-39.pyc
│  │     │     ├─ _next_gen.cpython-39.pyc
│  │     │     ├─ _version_info.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ attrs
│  │     │  ├─ converters.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ filters.py
│  │     │  ├─ py.typed
│  │     │  ├─ setters.py
│  │     │  ├─ validators.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  └─ __pycache__
│  │     │     ├─ converters.cpython-39.pyc
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ filters.cpython-39.pyc
│  │     │     ├─ setters.cpython-39.pyc
│  │     │     ├─ validators.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ attrs-23.1.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ backcall
│  │     │  ├─ backcall.py
│  │     │  ├─ _signatures.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ backcall.cpython-39.pyc
│  │     │     ├─ _signatures.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ backcall-0.2.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ black
│  │     │  ├─ brackets.cp39-win_amd64.pyd
│  │     │  ├─ brackets.py
│  │     │  ├─ cache.cp39-win_amd64.pyd
│  │     │  ├─ cache.py
│  │     │  ├─ comments.cp39-win_amd64.pyd
│  │     │  ├─ comments.py
│  │     │  ├─ concurrency.py
│  │     │  ├─ const.cp39-win_amd64.pyd
│  │     │  ├─ const.py
│  │     │  ├─ debug.py
│  │     │  ├─ files.py
│  │     │  ├─ handle_ipynb_magics.cp39-win_amd64.pyd
│  │     │  ├─ handle_ipynb_magics.py
│  │     │  ├─ linegen.cp39-win_amd64.pyd
│  │     │  ├─ linegen.py
│  │     │  ├─ lines.cp39-win_amd64.pyd
│  │     │  ├─ lines.py
│  │     │  ├─ mode.cp39-win_amd64.pyd
│  │     │  ├─ mode.py
│  │     │  ├─ nodes.cp39-win_amd64.pyd
│  │     │  ├─ nodes.py
│  │     │  ├─ numerics.cp39-win_amd64.pyd
│  │     │  ├─ numerics.py
│  │     │  ├─ output.py
│  │     │  ├─ parsing.cp39-win_amd64.pyd
│  │     │  ├─ parsing.py
│  │     │  ├─ py.typed
│  │     │  ├─ report.py
│  │     │  ├─ rusty.cp39-win_amd64.pyd
│  │     │  ├─ rusty.py
│  │     │  ├─ strings.cp39-win_amd64.pyd
│  │     │  ├─ strings.py
│  │     │  ├─ trans.cp39-win_amd64.pyd
│  │     │  ├─ trans.py
│  │     │  ├─ _width_table.cp39-win_amd64.pyd
│  │     │  ├─ _width_table.py
│  │     │  ├─ __init__.cp39-win_amd64.pyd
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ brackets.cpython-39.pyc
│  │     │     ├─ cache.cpython-39.pyc
│  │     │     ├─ comments.cpython-39.pyc
│  │     │     ├─ concurrency.cpython-39.pyc
│  │     │     ├─ const.cpython-39.pyc
│  │     │     ├─ debug.cpython-39.pyc
│  │     │     ├─ files.cpython-39.pyc
│  │     │     ├─ handle_ipynb_magics.cpython-39.pyc
│  │     │     ├─ linegen.cpython-39.pyc
│  │     │     ├─ lines.cpython-39.pyc
│  │     │     ├─ mode.cpython-39.pyc
│  │     │     ├─ nodes.cpython-39.pyc
│  │     │     ├─ numerics.cpython-39.pyc
│  │     │     ├─ output.cpython-39.pyc
│  │     │     ├─ parsing.cpython-39.pyc
│  │     │     ├─ report.cpython-39.pyc
│  │     │     ├─ rusty.cpython-39.pyc
│  │     │     ├─ strings.cpython-39.pyc
│  │     │     ├─ trans.cpython-39.pyc
│  │     │     ├─ _width_table.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ black-23.3.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ AUTHORS.md
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ blackd
│  │     │  ├─ middlewares.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ middlewares.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ blib2to3
│  │     │  ├─ Grammar.txt
│  │     │  ├─ LICENSE
│  │     │  ├─ PatternGrammar.txt
│  │     │  ├─ pgen2
│  │     │  │  ├─ conv.cp39-win_amd64.pyd
│  │     │  │  ├─ conv.py
│  │     │  │  ├─ driver.cp39-win_amd64.pyd
│  │     │  │  ├─ driver.py
│  │     │  │  ├─ grammar.cp39-win_amd64.pyd
│  │     │  │  ├─ grammar.py
│  │     │  │  ├─ literals.cp39-win_amd64.pyd
│  │     │  │  ├─ literals.py
│  │     │  │  ├─ parse.cp39-win_amd64.pyd
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ pgen.cp39-win_amd64.pyd
│  │     │  │  ├─ pgen.py
│  │     │  │  ├─ token.cp39-win_amd64.pyd
│  │     │  │  ├─ token.py
│  │     │  │  ├─ tokenize.cp39-win_amd64.pyd
│  │     │  │  ├─ tokenize.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ conv.cpython-39.pyc
│  │     │  │     ├─ driver.cpython-39.pyc
│  │     │  │     ├─ grammar.cpython-39.pyc
│  │     │  │     ├─ literals.cpython-39.pyc
│  │     │  │     ├─ parse.cpython-39.pyc
│  │     │  │     ├─ pgen.cpython-39.pyc
│  │     │  │     ├─ token.cpython-39.pyc
│  │     │  │     ├─ tokenize.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ pygram.cp39-win_amd64.pyd
│  │     │  ├─ pygram.py
│  │     │  ├─ pytree.cp39-win_amd64.pyd
│  │     │  ├─ pytree.py
│  │     │  ├─ README
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ pygram.cpython-39.pyc
│  │     │     ├─ pytree.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ certifi
│  │     │  ├─ cacert.pem
│  │     │  ├─ core.py
│  │     │  ├─ py.typed
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ core.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ certifi-2022.12.7.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ chardet
│  │     │  ├─ big5freq.py
│  │     │  ├─ big5prober.py
│  │     │  ├─ chardistribution.py
│  │     │  ├─ charsetgroupprober.py
│  │     │  ├─ charsetprober.py
│  │     │  ├─ cli
│  │     │  │  ├─ chardetect.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ chardetect.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ codingstatemachine.py
│  │     │  ├─ codingstatemachinedict.py
│  │     │  ├─ cp949prober.py
│  │     │  ├─ enums.py
│  │     │  ├─ escprober.py
│  │     │  ├─ escsm.py
│  │     │  ├─ eucjpprober.py
│  │     │  ├─ euckrfreq.py
│  │     │  ├─ euckrprober.py
│  │     │  ├─ euctwfreq.py
│  │     │  ├─ euctwprober.py
│  │     │  ├─ gb2312freq.py
│  │     │  ├─ gb2312prober.py
│  │     │  ├─ hebrewprober.py
│  │     │  ├─ jisfreq.py
│  │     │  ├─ johabfreq.py
│  │     │  ├─ johabprober.py
│  │     │  ├─ jpcntx.py
│  │     │  ├─ langbulgarianmodel.py
│  │     │  ├─ langgreekmodel.py
│  │     │  ├─ langhebrewmodel.py
│  │     │  ├─ langhungarianmodel.py
│  │     │  ├─ langrussianmodel.py
│  │     │  ├─ langthaimodel.py
│  │     │  ├─ langturkishmodel.py
│  │     │  ├─ latin1prober.py
│  │     │  ├─ macromanprober.py
│  │     │  ├─ mbcharsetprober.py
│  │     │  ├─ mbcsgroupprober.py
│  │     │  ├─ mbcssm.py
│  │     │  ├─ metadata
│  │     │  │  ├─ languages.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ languages.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ resultdict.py
│  │     │  ├─ sbcharsetprober.py
│  │     │  ├─ sbcsgroupprober.py
│  │     │  ├─ sjisprober.py
│  │     │  ├─ universaldetector.py
│  │     │  ├─ utf1632prober.py
│  │     │  ├─ utf8prober.py
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ big5freq.cpython-39.pyc
│  │     │     ├─ big5prober.cpython-39.pyc
│  │     │     ├─ chardistribution.cpython-39.pyc
│  │     │     ├─ charsetgroupprober.cpython-39.pyc
│  │     │     ├─ charsetprober.cpython-39.pyc
│  │     │     ├─ codingstatemachine.cpython-39.pyc
│  │     │     ├─ codingstatemachinedict.cpython-39.pyc
│  │     │     ├─ cp949prober.cpython-39.pyc
│  │     │     ├─ enums.cpython-39.pyc
│  │     │     ├─ escprober.cpython-39.pyc
│  │     │     ├─ escsm.cpython-39.pyc
│  │     │     ├─ eucjpprober.cpython-39.pyc
│  │     │     ├─ euckrfreq.cpython-39.pyc
│  │     │     ├─ euckrprober.cpython-39.pyc
│  │     │     ├─ euctwfreq.cpython-39.pyc
│  │     │     ├─ euctwprober.cpython-39.pyc
│  │     │     ├─ gb2312freq.cpython-39.pyc
│  │     │     ├─ gb2312prober.cpython-39.pyc
│  │     │     ├─ hebrewprober.cpython-39.pyc
│  │     │     ├─ jisfreq.cpython-39.pyc
│  │     │     ├─ johabfreq.cpython-39.pyc
│  │     │     ├─ johabprober.cpython-39.pyc
│  │     │     ├─ jpcntx.cpython-39.pyc
│  │     │     ├─ langbulgarianmodel.cpython-39.pyc
│  │     │     ├─ langgreekmodel.cpython-39.pyc
│  │     │     ├─ langhebrewmodel.cpython-39.pyc
│  │     │     ├─ langhungarianmodel.cpython-39.pyc
│  │     │     ├─ langrussianmodel.cpython-39.pyc
│  │     │     ├─ langthaimodel.cpython-39.pyc
│  │     │     ├─ langturkishmodel.cpython-39.pyc
│  │     │     ├─ latin1prober.cpython-39.pyc
│  │     │     ├─ macromanprober.cpython-39.pyc
│  │     │     ├─ mbcharsetprober.cpython-39.pyc
│  │     │     ├─ mbcsgroupprober.cpython-39.pyc
│  │     │     ├─ mbcssm.cpython-39.pyc
│  │     │     ├─ resultdict.cpython-39.pyc
│  │     │     ├─ sbcharsetprober.cpython-39.pyc
│  │     │     ├─ sbcsgroupprober.cpython-39.pyc
│  │     │     ├─ sjisprober.cpython-39.pyc
│  │     │     ├─ universaldetector.cpython-39.pyc
│  │     │     ├─ utf1632prober.cpython-39.pyc
│  │     │     ├─ utf8prober.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ chardet-5.1.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ charset_normalizer
│  │     │  ├─ api.py
│  │     │  ├─ assets
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ cd.py
│  │     │  ├─ cli
│  │     │  │  ├─ normalizer.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ normalizer.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ constant.py
│  │     │  ├─ legacy.py
│  │     │  ├─ md.cp39-win_amd64.pyd
│  │     │  ├─ md.py
│  │     │  ├─ md__mypyc.cp39-win_amd64.pyd
│  │     │  ├─ models.py
│  │     │  ├─ py.typed
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ api.cpython-39.pyc
│  │     │     ├─ cd.cpython-39.pyc
│  │     │     ├─ constant.cpython-39.pyc
│  │     │     ├─ legacy.cpython-39.pyc
│  │     │     ├─ md.cpython-39.pyc
│  │     │     ├─ models.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ charset_normalizer-3.1.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ click
│  │     │  ├─ core.py
│  │     │  ├─ decorators.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ formatting.py
│  │     │  ├─ globals.py
│  │     │  ├─ parser.py
│  │     │  ├─ py.typed
│  │     │  ├─ shell_completion.py
│  │     │  ├─ termui.py
│  │     │  ├─ testing.py
│  │     │  ├─ types.py
│  │     │  ├─ utils.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _termui_impl.py
│  │     │  ├─ _textwrap.py
│  │     │  ├─ _winconsole.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ core.cpython-39.pyc
│  │     │     ├─ decorators.cpython-39.pyc
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ formatting.cpython-39.pyc
│  │     │     ├─ globals.cpython-39.pyc
│  │     │     ├─ parser.cpython-39.pyc
│  │     │     ├─ shell_completion.cpython-39.pyc
│  │     │     ├─ termui.cpython-39.pyc
│  │     │     ├─ testing.cpython-39.pyc
│  │     │     ├─ types.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ _compat.cpython-39.pyc
│  │     │     ├─ _termui_impl.cpython-39.pyc
│  │     │     ├─ _textwrap.cpython-39.pyc
│  │     │     ├─ _winconsole.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ click-8.1.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.rst
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ colorama
│  │     │  ├─ ansi.py
│  │     │  ├─ ansitowin32.py
│  │     │  ├─ initialise.py
│  │     │  ├─ tests
│  │     │  │  ├─ ansitowin32_test.py
│  │     │  │  ├─ ansi_test.py
│  │     │  │  ├─ initialise_test.py
│  │     │  │  ├─ isatty_test.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ winterm_test.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ansitowin32_test.cpython-39.pyc
│  │     │  │     ├─ ansi_test.cpython-39.pyc
│  │     │  │     ├─ initialise_test.cpython-39.pyc
│  │     │  │     ├─ isatty_test.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     ├─ winterm_test.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ win32.py
│  │     │  ├─ winterm.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ ansi.cpython-39.pyc
│  │     │     ├─ ansitowin32.cpython-39.pyc
│  │     │     ├─ initialise.cpython-39.pyc
│  │     │     ├─ win32.cpython-39.pyc
│  │     │     ├─ winterm.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ colorama-0.4.6.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ comm
│  │     │  ├─ base_comm.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ base_comm.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ comm-0.1.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ contourpy
│  │     │  ├─ chunk.py
│  │     │  ├─ enum_util.py
│  │     │  ├─ py.typed
│  │     │  ├─ util
│  │     │  │  ├─ bokeh_renderer.py
│  │     │  │  ├─ bokeh_util.py
│  │     │  │  ├─ data.py
│  │     │  │  ├─ mpl_renderer.py
│  │     │  │  ├─ mpl_util.py
│  │     │  │  ├─ renderer.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ bokeh_renderer.cpython-39.pyc
│  │     │  │     ├─ bokeh_util.cpython-39.pyc
│  │     │  │     ├─ data.cpython-39.pyc
│  │     │  │     ├─ mpl_renderer.cpython-39.pyc
│  │     │  │     ├─ mpl_util.cpython-39.pyc
│  │     │  │     ├─ renderer.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _contourpy.cp39-win_amd64.pyd
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ chunk.cpython-39.pyc
│  │     │     ├─ enum_util.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ contourpy-1.0.7.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ cycler-0.11.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ cycler.py
│  │     ├─ datamodel_code_generator
│  │     │  ├─ format.py
│  │     │  ├─ http.py
│  │     │  ├─ imports.py
│  │     │  ├─ model
│  │     │  │  ├─ base.py
│  │     │  │  ├─ dataclass.py
│  │     │  │  ├─ enum.py
│  │     │  │  ├─ improts.py
│  │     │  │  ├─ pydantic
│  │     │  │  │  ├─ base_model.py
│  │     │  │  │  ├─ custom_root_type.py
│  │     │  │  │  ├─ dataclass.py
│  │     │  │  │  ├─ imports.py
│  │     │  │  │  ├─ types.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base_model.cpython-39.pyc
│  │     │  │  │     ├─ custom_root_type.cpython-39.pyc
│  │     │  │  │     ├─ dataclass.cpython-39.pyc
│  │     │  │  │     ├─ imports.cpython-39.pyc
│  │     │  │  │     ├─ types.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ rootmodel.py
│  │     │  │  ├─ template
│  │     │  │  │  ├─ dataclass.jinja2
│  │     │  │  │  ├─ Enum.jinja2
│  │     │  │  │  ├─ pydantic
│  │     │  │  │  │  ├─ BaseModel.jinja2
│  │     │  │  │  │  ├─ BaseModel_root.jinja2
│  │     │  │  │  │  ├─ Config.jinja2
│  │     │  │  │  │  └─ dataclass.jinja2
│  │     │  │  │  └─ root.jinja2
│  │     │  │  ├─ types.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ dataclass.cpython-39.pyc
│  │     │  │     ├─ enum.cpython-39.pyc
│  │     │  │     ├─ improts.cpython-39.pyc
│  │     │  │     ├─ rootmodel.cpython-39.pyc
│  │     │  │     ├─ types.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ parser
│  │     │  │  ├─ base.py
│  │     │  │  ├─ jsonschema.py
│  │     │  │  ├─ openapi.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ jsonschema.cpython-39.pyc
│  │     │  │     ├─ openapi.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ reference.py
│  │     │  ├─ types.py
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ format.cpython-39.pyc
│  │     │     ├─ http.cpython-39.pyc
│  │     │     ├─ imports.cpython-39.pyc
│  │     │     ├─ reference.cpython-39.pyc
│  │     │     ├─ types.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ datamodel_code_generator-0.18.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ dateutil
│  │     │  ├─ easter.py
│  │     │  ├─ parser
│  │     │  │  ├─ isoparser.py
│  │     │  │  ├─ _parser.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ isoparser.cpython-39.pyc
│  │     │  │     ├─ _parser.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ relativedelta.py
│  │     │  ├─ rrule.py
│  │     │  ├─ tz
│  │     │  │  ├─ tz.py
│  │     │  │  ├─ win.py
│  │     │  │  ├─ _common.py
│  │     │  │  ├─ _factories.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ tz.cpython-39.pyc
│  │     │  │     ├─ win.cpython-39.pyc
│  │     │  │     ├─ _common.cpython-39.pyc
│  │     │  │     ├─ _factories.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ tzwin.py
│  │     │  ├─ utils.py
│  │     │  ├─ zoneinfo
│  │     │  │  ├─ dateutil-zoneinfo.tar.gz
│  │     │  │  ├─ rebuild.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ rebuild.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _common.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ easter.cpython-39.pyc
│  │     │     ├─ relativedelta.cpython-39.pyc
│  │     │     ├─ rrule.cpython-39.pyc
│  │     │     ├─ tzwin.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ _common.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ debugpy
│  │     │  ├─ adapter
│  │     │  │  ├─ clients.py
│  │     │  │  ├─ components.py
│  │     │  │  ├─ launchers.py
│  │     │  │  ├─ servers.py
│  │     │  │  ├─ sessions.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ clients.cpython-39.pyc
│  │     │  │     ├─ components.cpython-39.pyc
│  │     │  │     ├─ launchers.cpython-39.pyc
│  │     │  │     ├─ servers.cpython-39.pyc
│  │     │  │     ├─ sessions.cpython-39.pyc
│  │     │  │     ├─ __init__.cpython-39.pyc
│  │     │  │     └─ __main__.cpython-39.pyc
│  │     │  ├─ common
│  │     │  │  ├─ json.py
│  │     │  │  ├─ log.py
│  │     │  │  ├─ messaging.py
│  │     │  │  ├─ singleton.py
│  │     │  │  ├─ sockets.py
│  │     │  │  ├─ stacks.py
│  │     │  │  ├─ timestamp.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ json.cpython-39.pyc
│  │     │  │     ├─ log.cpython-39.pyc
│  │     │  │     ├─ messaging.cpython-39.pyc
│  │     │  │     ├─ singleton.cpython-39.pyc
│  │     │  │     ├─ sockets.cpython-39.pyc
│  │     │  │     ├─ stacks.cpython-39.pyc
│  │     │  │     ├─ timestamp.cpython-39.pyc
│  │     │  │     ├─ util.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ launcher
│  │     │  │  ├─ debuggee.py
│  │     │  │  ├─ handlers.py
│  │     │  │  ├─ output.py
│  │     │  │  ├─ winapi.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ debuggee.cpython-39.pyc
│  │     │  │     ├─ handlers.cpython-39.pyc
│  │     │  │     ├─ output.cpython-39.pyc
│  │     │  │     ├─ winapi.cpython-39.pyc
│  │     │  │     ├─ __init__.cpython-39.pyc
│  │     │  │     └─ __main__.cpython-39.pyc
│  │     │  ├─ public_api.py
│  │     │  ├─ server
│  │     │  │  ├─ api.py
│  │     │  │  ├─ attach_pid_injected.py
│  │     │  │  ├─ cli.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ api.cpython-39.pyc
│  │     │  │     ├─ attach_pid_injected.cpython-39.pyc
│  │     │  │     ├─ cli.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ ThirdPartyNotices.txt
│  │     │  ├─ _vendored
│  │     │  │  ├─ force_pydevd.py
│  │     │  │  ├─ pydevd
│  │     │  │  │  ├─ pydevconsole.py
│  │     │  │  │  ├─ pydevd.py
│  │     │  │  │  ├─ pydevd_attach_to_process
│  │     │  │  │  │  ├─ add_code_to_python_process.py
│  │     │  │  │  │  ├─ attach_amd64.dll
│  │     │  │  │  │  ├─ attach_amd64.pdb
│  │     │  │  │  │  ├─ attach_pydevd.py
│  │     │  │  │  │  ├─ attach_script.py
│  │     │  │  │  │  ├─ attach_x86.dll
│  │     │  │  │  │  ├─ attach_x86.pdb
│  │     │  │  │  │  ├─ common
│  │     │  │  │  │  │  ├─ python.h
│  │     │  │  │  │  │  ├─ py_custom_pyeval_settrace.hpp
│  │     │  │  │  │  │  ├─ py_custom_pyeval_settrace_310.hpp
│  │     │  │  │  │  │  ├─ py_custom_pyeval_settrace_311.hpp
│  │     │  │  │  │  │  ├─ py_custom_pyeval_settrace_common.hpp
│  │     │  │  │  │  │  ├─ py_settrace.hpp
│  │     │  │  │  │  │  ├─ py_utils.hpp
│  │     │  │  │  │  │  ├─ py_version.hpp
│  │     │  │  │  │  │  └─ ref_utils.hpp
│  │     │  │  │  │  ├─ inject_dll_amd64.exe
│  │     │  │  │  │  ├─ inject_dll_amd64.pdb
│  │     │  │  │  │  ├─ inject_dll_x86.exe
│  │     │  │  │  │  ├─ inject_dll_x86.pdb
│  │     │  │  │  │  ├─ linux_and_mac
│  │     │  │  │  │  │  ├─ attach.cpp
│  │     │  │  │  │  │  ├─ compile_linux.sh
│  │     │  │  │  │  │  ├─ compile_mac.sh
│  │     │  │  │  │  │  ├─ compile_manylinux.cmd
│  │     │  │  │  │  │  ├─ lldb_prepare.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     └─ lldb_prepare.cpython-39.pyc
│  │     │  │  │  │  ├─ README.txt
│  │     │  │  │  │  ├─ run_code_on_dllmain_amd64.dll
│  │     │  │  │  │  ├─ run_code_on_dllmain_amd64.pdb
│  │     │  │  │  │  ├─ run_code_on_dllmain_x86.dll
│  │     │  │  │  │  ├─ run_code_on_dllmain_x86.pdb
│  │     │  │  │  │  ├─ winappdbg
│  │     │  │  │  │  │  ├─ breakpoint.py
│  │     │  │  │  │  │  ├─ compat.py
│  │     │  │  │  │  │  ├─ crash.py
│  │     │  │  │  │  │  ├─ debug.py
│  │     │  │  │  │  │  ├─ disasm.py
│  │     │  │  │  │  │  ├─ event.py
│  │     │  │  │  │  │  ├─ interactive.py
│  │     │  │  │  │  │  ├─ module.py
│  │     │  │  │  │  │  ├─ process.py
│  │     │  │  │  │  │  ├─ registry.py
│  │     │  │  │  │  │  ├─ search.py
│  │     │  │  │  │  │  ├─ sql.py
│  │     │  │  │  │  │  ├─ system.py
│  │     │  │  │  │  │  ├─ textio.py
│  │     │  │  │  │  │  ├─ thread.py
│  │     │  │  │  │  │  ├─ util.py
│  │     │  │  │  │  │  ├─ win32
│  │     │  │  │  │  │  │  ├─ advapi32.py
│  │     │  │  │  │  │  │  ├─ context_amd64.py
│  │     │  │  │  │  │  │  ├─ context_i386.py
│  │     │  │  │  │  │  │  ├─ dbghelp.py
│  │     │  │  │  │  │  │  ├─ defines.py
│  │     │  │  │  │  │  │  ├─ gdi32.py
│  │     │  │  │  │  │  │  ├─ kernel32.py
│  │     │  │  │  │  │  │  ├─ ntdll.py
│  │     │  │  │  │  │  │  ├─ peb_teb.py
│  │     │  │  │  │  │  │  ├─ psapi.py
│  │     │  │  │  │  │  │  ├─ shell32.py
│  │     │  │  │  │  │  │  ├─ shlwapi.py
│  │     │  │  │  │  │  │  ├─ user32.py
│  │     │  │  │  │  │  │  ├─ version.py
│  │     │  │  │  │  │  │  ├─ wtsapi32.py
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     ├─ advapi32.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ context_amd64.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ context_i386.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ dbghelp.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ defines.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ gdi32.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ kernel32.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ ntdll.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ peb_teb.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ psapi.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ shell32.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ shlwapi.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ user32.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ wtsapi32.cpython-39.pyc
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ window.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ breakpoint.cpython-39.pyc
│  │     │  │  │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │  │  │     ├─ crash.cpython-39.pyc
│  │     │  │  │  │  │     ├─ debug.cpython-39.pyc
│  │     │  │  │  │  │     ├─ disasm.cpython-39.pyc
│  │     │  │  │  │  │     ├─ event.cpython-39.pyc
│  │     │  │  │  │  │     ├─ interactive.cpython-39.pyc
│  │     │  │  │  │  │     ├─ module.cpython-39.pyc
│  │     │  │  │  │  │     ├─ process.cpython-39.pyc
│  │     │  │  │  │  │     ├─ registry.cpython-39.pyc
│  │     │  │  │  │  │     ├─ search.cpython-39.pyc
│  │     │  │  │  │  │     ├─ sql.cpython-39.pyc
│  │     │  │  │  │  │     ├─ system.cpython-39.pyc
│  │     │  │  │  │  │     ├─ textio.cpython-39.pyc
│  │     │  │  │  │  │     ├─ thread.cpython-39.pyc
│  │     │  │  │  │  │     ├─ util.cpython-39.pyc
│  │     │  │  │  │  │     ├─ window.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ windows
│  │     │  │  │  │  │  ├─ attach.cpp
│  │     │  │  │  │  │  ├─ attach.h
│  │     │  │  │  │  │  ├─ compile_windows.bat
│  │     │  │  │  │  │  ├─ inject_dll.cpp
│  │     │  │  │  │  │  ├─ py_win_helpers.hpp
│  │     │  │  │  │  │  ├─ run_code_in_memory.hpp
│  │     │  │  │  │  │  ├─ run_code_on_dllmain.cpp
│  │     │  │  │  │  │  ├─ stdafx.cpp
│  │     │  │  │  │  │  ├─ stdafx.h
│  │     │  │  │  │  │  └─ targetver.h
│  │     │  │  │  │  ├─ _always_live_program.py
│  │     │  │  │  │  ├─ _check.py
│  │     │  │  │  │  ├─ _test_attach_to_process.py
│  │     │  │  │  │  ├─ _test_attach_to_process_linux.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ add_code_to_python_process.cpython-39.pyc
│  │     │  │  │  │     ├─ attach_pydevd.cpython-39.pyc
│  │     │  │  │  │     ├─ attach_script.cpython-39.pyc
│  │     │  │  │  │     ├─ _always_live_program.cpython-39.pyc
│  │     │  │  │  │     ├─ _check.cpython-39.pyc
│  │     │  │  │  │     ├─ _test_attach_to_process.cpython-39.pyc
│  │     │  │  │  │     └─ _test_attach_to_process_linux.cpython-39.pyc
│  │     │  │  │  ├─ pydevd_file_utils.py
│  │     │  │  │  ├─ pydevd_plugins
│  │     │  │  │  │  ├─ django_debug.py
│  │     │  │  │  │  ├─ extensions
│  │     │  │  │  │  │  ├─ README.md
│  │     │  │  │  │  │  ├─ types
│  │     │  │  │  │  │  │  ├─ pydevd_helpers.py
│  │     │  │  │  │  │  │  ├─ pydevd_plugins_django_form_str.py
│  │     │  │  │  │  │  │  ├─ pydevd_plugin_numpy_types.py
│  │     │  │  │  │  │  │  ├─ pydevd_plugin_pandas_types.py
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     ├─ pydevd_helpers.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ pydevd_plugins_django_form_str.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ pydevd_plugin_numpy_types.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ pydevd_plugin_pandas_types.cpython-39.pyc
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ jinja2_debug.py
│  │     │  │  │  │  ├─ pydevd_line_validation.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ django_debug.cpython-39.pyc
│  │     │  │  │  │     ├─ jinja2_debug.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_line_validation.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ pydevd_tracing.py
│  │     │  │  │  ├─ pydev_app_engine_debug_startup.py
│  │     │  │  │  ├─ pydev_coverage.py
│  │     │  │  │  ├─ pydev_ipython
│  │     │  │  │  │  ├─ inputhook.py
│  │     │  │  │  │  ├─ inputhookglut.py
│  │     │  │  │  │  ├─ inputhookgtk.py
│  │     │  │  │  │  ├─ inputhookgtk3.py
│  │     │  │  │  │  ├─ inputhookpyglet.py
│  │     │  │  │  │  ├─ inputhookqt4.py
│  │     │  │  │  │  ├─ inputhookqt5.py
│  │     │  │  │  │  ├─ inputhooktk.py
│  │     │  │  │  │  ├─ inputhookwx.py
│  │     │  │  │  │  ├─ matplotlibtools.py
│  │     │  │  │  │  ├─ qt.py
│  │     │  │  │  │  ├─ qt_for_kernel.py
│  │     │  │  │  │  ├─ qt_loaders.py
│  │     │  │  │  │  ├─ README
│  │     │  │  │  │  ├─ version.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ inputhook.cpython-39.pyc
│  │     │  │  │  │     ├─ inputhookglut.cpython-39.pyc
│  │     │  │  │  │     ├─ inputhookgtk.cpython-39.pyc
│  │     │  │  │  │     ├─ inputhookgtk3.cpython-39.pyc
│  │     │  │  │  │     ├─ inputhookpyglet.cpython-39.pyc
│  │     │  │  │  │     ├─ inputhookqt4.cpython-39.pyc
│  │     │  │  │  │     ├─ inputhookqt5.cpython-39.pyc
│  │     │  │  │  │     ├─ inputhooktk.cpython-39.pyc
│  │     │  │  │  │     ├─ inputhookwx.cpython-39.pyc
│  │     │  │  │  │     ├─ matplotlibtools.cpython-39.pyc
│  │     │  │  │  │     ├─ qt.cpython-39.pyc
│  │     │  │  │  │     ├─ qt_for_kernel.cpython-39.pyc
│  │     │  │  │  │     ├─ qt_loaders.cpython-39.pyc
│  │     │  │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ pydev_pysrc.py
│  │     │  │  │  ├─ pydev_run_in_console.py
│  │     │  │  │  ├─ pydev_sitecustomize
│  │     │  │  │  │  ├─ sitecustomize.py
│  │     │  │  │  │  ├─ __not_in_default_pythonpath.txt
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ sitecustomize.cpython-39.pyc
│  │     │  │  │  ├─ setup_pydevd_cython.py
│  │     │  │  │  ├─ _pydevd_bundle
│  │     │  │  │  │  ├─ pydevconsole_code.py
│  │     │  │  │  │  ├─ pydevd_additional_thread_info.py
│  │     │  │  │  │  ├─ pydevd_additional_thread_info_regular.py
│  │     │  │  │  │  ├─ pydevd_api.py
│  │     │  │  │  │  ├─ pydevd_breakpoints.py
│  │     │  │  │  │  ├─ pydevd_bytecode_utils.py
│  │     │  │  │  │  ├─ pydevd_code_to_source.py
│  │     │  │  │  │  ├─ pydevd_collect_bytecode_info.py
│  │     │  │  │  │  ├─ pydevd_comm.py
│  │     │  │  │  │  ├─ pydevd_command_line_handling.py
│  │     │  │  │  │  ├─ pydevd_comm_constants.py
│  │     │  │  │  │  ├─ pydevd_concurrency_analyser
│  │     │  │  │  │  │  ├─ pydevd_concurrency_logger.py
│  │     │  │  │  │  │  ├─ pydevd_thread_wrappers.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ pydevd_concurrency_logger.cpython-39.pyc
│  │     │  │  │  │  │     ├─ pydevd_thread_wrappers.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ pydevd_console.py
│  │     │  │  │  │  ├─ pydevd_constants.py
│  │     │  │  │  │  ├─ pydevd_custom_frames.py
│  │     │  │  │  │  ├─ pydevd_cython.c
│  │     │  │  │  │  ├─ pydevd_cython.cp39-win_amd64.pyd
│  │     │  │  │  │  ├─ pydevd_cython.pxd
│  │     │  │  │  │  ├─ pydevd_cython.pyx
│  │     │  │  │  │  ├─ pydevd_cython_wrapper.py
│  │     │  │  │  │  ├─ pydevd_daemon_thread.py
│  │     │  │  │  │  ├─ pydevd_defaults.py
│  │     │  │  │  │  ├─ pydevd_dont_trace.py
│  │     │  │  │  │  ├─ pydevd_dont_trace_files.py
│  │     │  │  │  │  ├─ pydevd_exec2.py
│  │     │  │  │  │  ├─ pydevd_extension_api.py
│  │     │  │  │  │  ├─ pydevd_extension_utils.py
│  │     │  │  │  │  ├─ pydevd_filtering.py
│  │     │  │  │  │  ├─ pydevd_frame.py
│  │     │  │  │  │  ├─ pydevd_frame_utils.py
│  │     │  │  │  │  ├─ pydevd_gevent_integration.py
│  │     │  │  │  │  ├─ pydevd_import_class.py
│  │     │  │  │  │  ├─ pydevd_io.py
│  │     │  │  │  │  ├─ pydevd_json_debug_options.py
│  │     │  │  │  │  ├─ pydevd_net_command.py
│  │     │  │  │  │  ├─ pydevd_net_command_factory_json.py
│  │     │  │  │  │  ├─ pydevd_net_command_factory_xml.py
│  │     │  │  │  │  ├─ pydevd_plugin_utils.py
│  │     │  │  │  │  ├─ pydevd_process_net_command.py
│  │     │  │  │  │  ├─ pydevd_process_net_command_json.py
│  │     │  │  │  │  ├─ pydevd_referrers.py
│  │     │  │  │  │  ├─ pydevd_reload.py
│  │     │  │  │  │  ├─ pydevd_resolver.py
│  │     │  │  │  │  ├─ pydevd_runpy.py
│  │     │  │  │  │  ├─ pydevd_safe_repr.py
│  │     │  │  │  │  ├─ pydevd_save_locals.py
│  │     │  │  │  │  ├─ pydevd_signature.py
│  │     │  │  │  │  ├─ pydevd_source_mapping.py
│  │     │  │  │  │  ├─ pydevd_stackless.py
│  │     │  │  │  │  ├─ pydevd_suspended_frames.py
│  │     │  │  │  │  ├─ pydevd_thread_lifecycle.py
│  │     │  │  │  │  ├─ pydevd_timeout.py
│  │     │  │  │  │  ├─ pydevd_traceproperty.py
│  │     │  │  │  │  ├─ pydevd_trace_api.py
│  │     │  │  │  │  ├─ pydevd_trace_dispatch.py
│  │     │  │  │  │  ├─ pydevd_trace_dispatch_regular.py
│  │     │  │  │  │  ├─ pydevd_utils.py
│  │     │  │  │  │  ├─ pydevd_vars.py
│  │     │  │  │  │  ├─ pydevd_vm_type.py
│  │     │  │  │  │  ├─ pydevd_xml.py
│  │     │  │  │  │  ├─ _debug_adapter
│  │     │  │  │  │  │  ├─ debugProtocol.json
│  │     │  │  │  │  │  ├─ debugProtocolCustom.json
│  │     │  │  │  │  │  ├─ pydevd_base_schema.py
│  │     │  │  │  │  │  ├─ pydevd_schema.py
│  │     │  │  │  │  │  ├─ pydevd_schema_log.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ __main__pydevd_gen_debug_adapter_protocol.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ pydevd_base_schema.cpython-39.pyc
│  │     │  │  │  │  │     ├─ pydevd_schema.cpython-39.pyc
│  │     │  │  │  │  │     ├─ pydevd_schema_log.cpython-39.pyc
│  │     │  │  │  │  │     ├─ __init__.cpython-39.pyc
│  │     │  │  │  │  │     └─ __main__pydevd_gen_debug_adapter_protocol.cpython-39.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ pydevconsole_code.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_additional_thread_info.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_additional_thread_info_regular.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_api.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_breakpoints.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_bytecode_utils.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_code_to_source.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_collect_bytecode_info.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_comm.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_command_line_handling.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_comm_constants.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_console.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_constants.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_custom_frames.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_cython_wrapper.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_daemon_thread.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_defaults.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_dont_trace.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_dont_trace_files.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_exec2.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_extension_api.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_extension_utils.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_filtering.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_frame.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_frame_utils.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_gevent_integration.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_import_class.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_io.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_json_debug_options.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_net_command.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_net_command_factory_json.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_net_command_factory_xml.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_plugin_utils.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_process_net_command.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_process_net_command_json.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_referrers.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_reload.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_resolver.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_runpy.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_safe_repr.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_save_locals.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_signature.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_source_mapping.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_stackless.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_suspended_frames.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_thread_lifecycle.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_timeout.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_traceproperty.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_trace_api.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_trace_dispatch.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_trace_dispatch_regular.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_utils.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_vars.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_vm_type.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_xml.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _pydevd_frame_eval
│  │     │  │  │  │  ├─ pydevd_frame_evaluator.c
│  │     │  │  │  │  ├─ pydevd_frame_evaluator.cp39-win_amd64.pyd
│  │     │  │  │  │  ├─ pydevd_frame_evaluator.pxd
│  │     │  │  │  │  ├─ pydevd_frame_evaluator.pyx
│  │     │  │  │  │  ├─ pydevd_frame_evaluator.template.pyx
│  │     │  │  │  │  ├─ pydevd_frame_eval_cython_wrapper.py
│  │     │  │  │  │  ├─ pydevd_frame_eval_main.py
│  │     │  │  │  │  ├─ pydevd_frame_tracing.py
│  │     │  │  │  │  ├─ pydevd_modify_bytecode.py
│  │     │  │  │  │  ├─ release_mem.h
│  │     │  │  │  │  ├─ vendored
│  │     │  │  │  │  │  ├─ bytecode
│  │     │  │  │  │  │  │  ├─ bytecode.py
│  │     │  │  │  │  │  │  ├─ cfg.py
│  │     │  │  │  │  │  │  ├─ concrete.py
│  │     │  │  │  │  │  │  ├─ flags.py
│  │     │  │  │  │  │  │  ├─ instr.py
│  │     │  │  │  │  │  │  ├─ peephole_opt.py
│  │     │  │  │  │  │  │  ├─ tests
│  │     │  │  │  │  │  │  │  ├─ test_bytecode.py
│  │     │  │  │  │  │  │  │  ├─ test_cfg.py
│  │     │  │  │  │  │  │  │  ├─ test_code.py
│  │     │  │  │  │  │  │  │  ├─ test_concrete.py
│  │     │  │  │  │  │  │  │  ├─ test_flags.py
│  │     │  │  │  │  │  │  │  ├─ test_instr.py
│  │     │  │  │  │  │  │  │  ├─ test_misc.py
│  │     │  │  │  │  │  │  │  ├─ test_peephole_opt.py
│  │     │  │  │  │  │  │  │  ├─ util_annotation.py
│  │     │  │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │  │     ├─ test_bytecode.cpython-39.pyc
│  │     │  │  │  │  │  │  │     ├─ test_cfg.cpython-39.pyc
│  │     │  │  │  │  │  │  │     ├─ test_code.cpython-39.pyc
│  │     │  │  │  │  │  │  │     ├─ test_concrete.cpython-39.pyc
│  │     │  │  │  │  │  │  │     ├─ test_flags.cpython-39.pyc
│  │     │  │  │  │  │  │  │     ├─ test_instr.cpython-39.pyc
│  │     │  │  │  │  │  │  │     ├─ test_misc.cpython-39.pyc
│  │     │  │  │  │  │  │  │     ├─ test_peephole_opt.cpython-39.pyc
│  │     │  │  │  │  │  │  │     ├─ util_annotation.cpython-39.pyc
│  │     │  │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     ├─ bytecode.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ cfg.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ concrete.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ flags.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ instr.cpython-39.pyc
│  │     │  │  │  │  │  │     ├─ peephole_opt.cpython-39.pyc
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ bytecode-0.13.0.dev0.dist-info
│  │     │  │  │  │  │  │  ├─ COPYING
│  │     │  │  │  │  │  │  ├─ direct_url.json
│  │     │  │  │  │  │  │  ├─ INSTALLER
│  │     │  │  │  │  │  │  ├─ METADATA
│  │     │  │  │  │  │  │  ├─ RECORD
│  │     │  │  │  │  │  │  ├─ REQUESTED
│  │     │  │  │  │  │  │  ├─ top_level.txt
│  │     │  │  │  │  │  │  └─ WHEEL
│  │     │  │  │  │  │  ├─ pydevd_fix_code.py
│  │     │  │  │  │  │  ├─ README.txt
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ pydevd_fix_code.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ pydevd_frame_eval_cython_wrapper.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_frame_eval_main.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_frame_tracing.cpython-39.pyc
│  │     │  │  │  │     ├─ pydevd_modify_bytecode.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _pydev_bundle
│  │     │  │  │  │  ├─ fsnotify
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ pydev_console_utils.py
│  │     │  │  │  │  ├─ pydev_imports.py
│  │     │  │  │  │  ├─ pydev_import_hook.py
│  │     │  │  │  │  ├─ pydev_ipython_console.py
│  │     │  │  │  │  ├─ pydev_ipython_console_011.py
│  │     │  │  │  │  ├─ pydev_is_thread_alive.py
│  │     │  │  │  │  ├─ pydev_localhost.py
│  │     │  │  │  │  ├─ pydev_log.py
│  │     │  │  │  │  ├─ pydev_monkey.py
│  │     │  │  │  │  ├─ pydev_monkey_qt.py
│  │     │  │  │  │  ├─ pydev_override.py
│  │     │  │  │  │  ├─ pydev_umd.py
│  │     │  │  │  │  ├─ pydev_versioncheck.py
│  │     │  │  │  │  ├─ _pydev_calltip_util.py
│  │     │  │  │  │  ├─ _pydev_completer.py
│  │     │  │  │  │  ├─ _pydev_execfile.py
│  │     │  │  │  │  ├─ _pydev_filesystem_encoding.py
│  │     │  │  │  │  ├─ _pydev_getopt.py
│  │     │  │  │  │  ├─ _pydev_imports_tipper.py
│  │     │  │  │  │  ├─ _pydev_jy_imports_tipper.py
│  │     │  │  │  │  ├─ _pydev_log.py
│  │     │  │  │  │  ├─ _pydev_saved_modules.py
│  │     │  │  │  │  ├─ _pydev_sys_patch.py
│  │     │  │  │  │  ├─ _pydev_tipper_common.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ pydev_console_utils.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_imports.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_import_hook.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_ipython_console.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_ipython_console_011.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_is_thread_alive.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_localhost.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_log.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_monkey.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_monkey_qt.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_override.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_umd.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_versioncheck.cpython-39.pyc
│  │     │  │  │  │     ├─ _pydev_calltip_util.cpython-39.pyc
│  │     │  │  │  │     ├─ _pydev_completer.cpython-39.pyc
│  │     │  │  │  │     ├─ _pydev_execfile.cpython-39.pyc
│  │     │  │  │  │     ├─ _pydev_filesystem_encoding.cpython-39.pyc
│  │     │  │  │  │     ├─ _pydev_getopt.cpython-39.pyc
│  │     │  │  │  │     ├─ _pydev_imports_tipper.cpython-39.pyc
│  │     │  │  │  │     ├─ _pydev_jy_imports_tipper.cpython-39.pyc
│  │     │  │  │  │     ├─ _pydev_log.cpython-39.pyc
│  │     │  │  │  │     ├─ _pydev_saved_modules.cpython-39.pyc
│  │     │  │  │  │     ├─ _pydev_sys_patch.cpython-39.pyc
│  │     │  │  │  │     ├─ _pydev_tipper_common.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _pydev_runfiles
│  │     │  │  │  │  ├─ pydev_runfiles.py
│  │     │  │  │  │  ├─ pydev_runfiles_coverage.py
│  │     │  │  │  │  ├─ pydev_runfiles_nose.py
│  │     │  │  │  │  ├─ pydev_runfiles_parallel.py
│  │     │  │  │  │  ├─ pydev_runfiles_parallel_client.py
│  │     │  │  │  │  ├─ pydev_runfiles_pytest2.py
│  │     │  │  │  │  ├─ pydev_runfiles_unittest.py
│  │     │  │  │  │  ├─ pydev_runfiles_xml_rpc.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ pydev_runfiles.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_runfiles_coverage.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_runfiles_nose.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_runfiles_parallel.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_runfiles_parallel_client.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_runfiles_pytest2.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_runfiles_unittest.cpython-39.pyc
│  │     │  │  │  │     ├─ pydev_runfiles_xml_rpc.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ pydevconsole.cpython-39.pyc
│  │     │  │  │     ├─ pydevd.cpython-39.pyc
│  │     │  │  │     ├─ pydevd_file_utils.cpython-39.pyc
│  │     │  │  │     ├─ pydevd_tracing.cpython-39.pyc
│  │     │  │  │     ├─ pydev_app_engine_debug_startup.cpython-39.pyc
│  │     │  │  │     ├─ pydev_coverage.cpython-39.pyc
│  │     │  │  │     ├─ pydev_pysrc.cpython-39.pyc
│  │     │  │  │     ├─ pydev_run_in_console.cpython-39.pyc
│  │     │  │  │     └─ setup_pydevd_cython.cpython-39.pyc
│  │     │  │  ├─ _pydevd_packaging.py
│  │     │  │  ├─ _util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ force_pydevd.cpython-39.pyc
│  │     │  │     ├─ _pydevd_packaging.cpython-39.pyc
│  │     │  │     ├─ _util.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ public_api.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ debugpy-1.6.7.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ decorator-5.1.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ pbr.json
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ decorator.py
│  │     ├─ distutils-precedence.pth
│  │     ├─ dns
│  │     │  ├─ asyncbackend.py
│  │     │  ├─ asyncquery.py
│  │     │  ├─ asyncresolver.py
│  │     │  ├─ dnssec.py
│  │     │  ├─ dnssectypes.py
│  │     │  ├─ e164.py
│  │     │  ├─ edns.py
│  │     │  ├─ entropy.py
│  │     │  ├─ enum.py
│  │     │  ├─ exception.py
│  │     │  ├─ flags.py
│  │     │  ├─ grange.py
│  │     │  ├─ immutable.py
│  │     │  ├─ inet.py
│  │     │  ├─ ipv4.py
│  │     │  ├─ ipv6.py
│  │     │  ├─ message.py
│  │     │  ├─ name.py
│  │     │  ├─ namedict.py
│  │     │  ├─ node.py
│  │     │  ├─ opcode.py
│  │     │  ├─ py.typed
│  │     │  ├─ query.py
│  │     │  ├─ quic
│  │     │  │  ├─ _asyncio.py
│  │     │  │  ├─ _common.py
│  │     │  │  ├─ _sync.py
│  │     │  │  ├─ _trio.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _asyncio.cpython-39.pyc
│  │     │  │     ├─ _common.cpython-39.pyc
│  │     │  │     ├─ _sync.cpython-39.pyc
│  │     │  │     ├─ _trio.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ rcode.py
│  │     │  ├─ rdata.py
│  │     │  ├─ rdataclass.py
│  │     │  ├─ rdataset.py
│  │     │  ├─ rdatatype.py
│  │     │  ├─ rdtypes
│  │     │  │  ├─ ANY
│  │     │  │  │  ├─ AFSDB.py
│  │     │  │  │  ├─ AMTRELAY.py
│  │     │  │  │  ├─ AVC.py
│  │     │  │  │  ├─ CAA.py
│  │     │  │  │  ├─ CDNSKEY.py
│  │     │  │  │  ├─ CDS.py
│  │     │  │  │  ├─ CERT.py
│  │     │  │  │  ├─ CNAME.py
│  │     │  │  │  ├─ CSYNC.py
│  │     │  │  │  ├─ DLV.py
│  │     │  │  │  ├─ DNAME.py
│  │     │  │  │  ├─ DNSKEY.py
│  │     │  │  │  ├─ DS.py
│  │     │  │  │  ├─ EUI48.py
│  │     │  │  │  ├─ EUI64.py
│  │     │  │  │  ├─ GPOS.py
│  │     │  │  │  ├─ HINFO.py
│  │     │  │  │  ├─ HIP.py
│  │     │  │  │  ├─ ISDN.py
│  │     │  │  │  ├─ L32.py
│  │     │  │  │  ├─ L64.py
│  │     │  │  │  ├─ LOC.py
│  │     │  │  │  ├─ LP.py
│  │     │  │  │  ├─ MX.py
│  │     │  │  │  ├─ NID.py
│  │     │  │  │  ├─ NINFO.py
│  │     │  │  │  ├─ NS.py
│  │     │  │  │  ├─ NSEC.py
│  │     │  │  │  ├─ NSEC3.py
│  │     │  │  │  ├─ NSEC3PARAM.py
│  │     │  │  │  ├─ OPENPGPKEY.py
│  │     │  │  │  ├─ OPT.py
│  │     │  │  │  ├─ PTR.py
│  │     │  │  │  ├─ RP.py
│  │     │  │  │  ├─ RRSIG.py
│  │     │  │  │  ├─ RT.py
│  │     │  │  │  ├─ SMIMEA.py
│  │     │  │  │  ├─ SOA.py
│  │     │  │  │  ├─ SPF.py
│  │     │  │  │  ├─ SSHFP.py
│  │     │  │  │  ├─ TKEY.py
│  │     │  │  │  ├─ TLSA.py
│  │     │  │  │  ├─ TSIG.py
│  │     │  │  │  ├─ TXT.py
│  │     │  │  │  ├─ URI.py
│  │     │  │  │  ├─ X25.py
│  │     │  │  │  ├─ ZONEMD.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ AFSDB.cpython-39.pyc
│  │     │  │  │     ├─ AMTRELAY.cpython-39.pyc
│  │     │  │  │     ├─ AVC.cpython-39.pyc
│  │     │  │  │     ├─ CAA.cpython-39.pyc
│  │     │  │  │     ├─ CDNSKEY.cpython-39.pyc
│  │     │  │  │     ├─ CDS.cpython-39.pyc
│  │     │  │  │     ├─ CERT.cpython-39.pyc
│  │     │  │  │     ├─ CNAME.cpython-39.pyc
│  │     │  │  │     ├─ CSYNC.cpython-39.pyc
│  │     │  │  │     ├─ DLV.cpython-39.pyc
│  │     │  │  │     ├─ DNAME.cpython-39.pyc
│  │     │  │  │     ├─ DNSKEY.cpython-39.pyc
│  │     │  │  │     ├─ DS.cpython-39.pyc
│  │     │  │  │     ├─ EUI48.cpython-39.pyc
│  │     │  │  │     ├─ EUI64.cpython-39.pyc
│  │     │  │  │     ├─ GPOS.cpython-39.pyc
│  │     │  │  │     ├─ HINFO.cpython-39.pyc
│  │     │  │  │     ├─ HIP.cpython-39.pyc
│  │     │  │  │     ├─ ISDN.cpython-39.pyc
│  │     │  │  │     ├─ L32.cpython-39.pyc
│  │     │  │  │     ├─ L64.cpython-39.pyc
│  │     │  │  │     ├─ LOC.cpython-39.pyc
│  │     │  │  │     ├─ LP.cpython-39.pyc
│  │     │  │  │     ├─ MX.cpython-39.pyc
│  │     │  │  │     ├─ NID.cpython-39.pyc
│  │     │  │  │     ├─ NINFO.cpython-39.pyc
│  │     │  │  │     ├─ NS.cpython-39.pyc
│  │     │  │  │     ├─ NSEC.cpython-39.pyc
│  │     │  │  │     ├─ NSEC3.cpython-39.pyc
│  │     │  │  │     ├─ NSEC3PARAM.cpython-39.pyc
│  │     │  │  │     ├─ OPENPGPKEY.cpython-39.pyc
│  │     │  │  │     ├─ OPT.cpython-39.pyc
│  │     │  │  │     ├─ PTR.cpython-39.pyc
│  │     │  │  │     ├─ RP.cpython-39.pyc
│  │     │  │  │     ├─ RRSIG.cpython-39.pyc
│  │     │  │  │     ├─ RT.cpython-39.pyc
│  │     │  │  │     ├─ SMIMEA.cpython-39.pyc
│  │     │  │  │     ├─ SOA.cpython-39.pyc
│  │     │  │  │     ├─ SPF.cpython-39.pyc
│  │     │  │  │     ├─ SSHFP.cpython-39.pyc
│  │     │  │  │     ├─ TKEY.cpython-39.pyc
│  │     │  │  │     ├─ TLSA.cpython-39.pyc
│  │     │  │  │     ├─ TSIG.cpython-39.pyc
│  │     │  │  │     ├─ TXT.cpython-39.pyc
│  │     │  │  │     ├─ URI.cpython-39.pyc
│  │     │  │  │     ├─ X25.cpython-39.pyc
│  │     │  │  │     ├─ ZONEMD.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ CH
│  │     │  │  │  ├─ A.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ A.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ dnskeybase.py
│  │     │  │  ├─ dsbase.py
│  │     │  │  ├─ euibase.py
│  │     │  │  ├─ IN
│  │     │  │  │  ├─ A.py
│  │     │  │  │  ├─ AAAA.py
│  │     │  │  │  ├─ APL.py
│  │     │  │  │  ├─ DHCID.py
│  │     │  │  │  ├─ HTTPS.py
│  │     │  │  │  ├─ IPSECKEY.py
│  │     │  │  │  ├─ KX.py
│  │     │  │  │  ├─ NAPTR.py
│  │     │  │  │  ├─ NSAP.py
│  │     │  │  │  ├─ NSAP_PTR.py
│  │     │  │  │  ├─ PX.py
│  │     │  │  │  ├─ SRV.py
│  │     │  │  │  ├─ SVCB.py
│  │     │  │  │  ├─ WKS.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ A.cpython-39.pyc
│  │     │  │  │     ├─ AAAA.cpython-39.pyc
│  │     │  │  │     ├─ APL.cpython-39.pyc
│  │     │  │  │     ├─ DHCID.cpython-39.pyc
│  │     │  │  │     ├─ HTTPS.cpython-39.pyc
│  │     │  │  │     ├─ IPSECKEY.cpython-39.pyc
│  │     │  │  │     ├─ KX.cpython-39.pyc
│  │     │  │  │     ├─ NAPTR.cpython-39.pyc
│  │     │  │  │     ├─ NSAP.cpython-39.pyc
│  │     │  │  │     ├─ NSAP_PTR.cpython-39.pyc
│  │     │  │  │     ├─ PX.cpython-39.pyc
│  │     │  │  │     ├─ SRV.cpython-39.pyc
│  │     │  │  │     ├─ SVCB.cpython-39.pyc
│  │     │  │  │     ├─ WKS.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ mxbase.py
│  │     │  │  ├─ nsbase.py
│  │     │  │  ├─ svcbbase.py
│  │     │  │  ├─ tlsabase.py
│  │     │  │  ├─ txtbase.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ dnskeybase.cpython-39.pyc
│  │     │  │     ├─ dsbase.cpython-39.pyc
│  │     │  │     ├─ euibase.cpython-39.pyc
│  │     │  │     ├─ mxbase.cpython-39.pyc
│  │     │  │     ├─ nsbase.cpython-39.pyc
│  │     │  │     ├─ svcbbase.cpython-39.pyc
│  │     │  │     ├─ tlsabase.cpython-39.pyc
│  │     │  │     ├─ txtbase.cpython-39.pyc
│  │     │  │     ├─ util.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ renderer.py
│  │     │  ├─ resolver.py
│  │     │  ├─ reversename.py
│  │     │  ├─ rrset.py
│  │     │  ├─ serial.py
│  │     │  ├─ set.py
│  │     │  ├─ tokenizer.py
│  │     │  ├─ transaction.py
│  │     │  ├─ tsig.py
│  │     │  ├─ tsigkeyring.py
│  │     │  ├─ ttl.py
│  │     │  ├─ update.py
│  │     │  ├─ version.py
│  │     │  ├─ versioned.py
│  │     │  ├─ win32util.py
│  │     │  ├─ wire.py
│  │     │  ├─ xfr.py
│  │     │  ├─ zone.py
│  │     │  ├─ zonefile.py
│  │     │  ├─ zonetypes.py
│  │     │  ├─ _asyncbackend.py
│  │     │  ├─ _asyncio_backend.py
│  │     │  ├─ _curio_backend.py
│  │     │  ├─ _immutable_ctx.py
│  │     │  ├─ _trio_backend.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ asyncbackend.cpython-39.pyc
│  │     │     ├─ asyncquery.cpython-39.pyc
│  │     │     ├─ asyncresolver.cpython-39.pyc
│  │     │     ├─ dnssec.cpython-39.pyc
│  │     │     ├─ dnssectypes.cpython-39.pyc
│  │     │     ├─ e164.cpython-39.pyc
│  │     │     ├─ edns.cpython-39.pyc
│  │     │     ├─ entropy.cpython-39.pyc
│  │     │     ├─ enum.cpython-39.pyc
│  │     │     ├─ exception.cpython-39.pyc
│  │     │     ├─ flags.cpython-39.pyc
│  │     │     ├─ grange.cpython-39.pyc
│  │     │     ├─ immutable.cpython-39.pyc
│  │     │     ├─ inet.cpython-39.pyc
│  │     │     ├─ ipv4.cpython-39.pyc
│  │     │     ├─ ipv6.cpython-39.pyc
│  │     │     ├─ message.cpython-39.pyc
│  │     │     ├─ name.cpython-39.pyc
│  │     │     ├─ namedict.cpython-39.pyc
│  │     │     ├─ node.cpython-39.pyc
│  │     │     ├─ opcode.cpython-39.pyc
│  │     │     ├─ query.cpython-39.pyc
│  │     │     ├─ rcode.cpython-39.pyc
│  │     │     ├─ rdata.cpython-39.pyc
│  │     │     ├─ rdataclass.cpython-39.pyc
│  │     │     ├─ rdataset.cpython-39.pyc
│  │     │     ├─ rdatatype.cpython-39.pyc
│  │     │     ├─ renderer.cpython-39.pyc
│  │     │     ├─ resolver.cpython-39.pyc
│  │     │     ├─ reversename.cpython-39.pyc
│  │     │     ├─ rrset.cpython-39.pyc
│  │     │     ├─ serial.cpython-39.pyc
│  │     │     ├─ set.cpython-39.pyc
│  │     │     ├─ tokenizer.cpython-39.pyc
│  │     │     ├─ transaction.cpython-39.pyc
│  │     │     ├─ tsig.cpython-39.pyc
│  │     │     ├─ tsigkeyring.cpython-39.pyc
│  │     │     ├─ ttl.cpython-39.pyc
│  │     │     ├─ update.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     ├─ versioned.cpython-39.pyc
│  │     │     ├─ win32util.cpython-39.pyc
│  │     │     ├─ wire.cpython-39.pyc
│  │     │     ├─ xfr.cpython-39.pyc
│  │     │     ├─ zone.cpython-39.pyc
│  │     │     ├─ zonefile.cpython-39.pyc
│  │     │     ├─ zonetypes.cpython-39.pyc
│  │     │     ├─ _asyncbackend.cpython-39.pyc
│  │     │     ├─ _asyncio_backend.cpython-39.pyc
│  │     │     ├─ _curio_backend.cpython-39.pyc
│  │     │     ├─ _immutable_ctx.cpython-39.pyc
│  │     │     ├─ _trio_backend.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ dnspython-2.3.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ email_validator
│  │     │  ├─ deliverability.py
│  │     │  ├─ exceptions_types.py
│  │     │  ├─ py.typed
│  │     │  ├─ rfc_constants.py
│  │     │  ├─ syntax.py
│  │     │  ├─ validate_email.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ deliverability.cpython-39.pyc
│  │     │     ├─ exceptions_types.cpython-39.pyc
│  │     │     ├─ rfc_constants.cpython-39.pyc
│  │     │     ├─ syntax.cpython-39.pyc
│  │     │     ├─ validate_email.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ email_validator-2.0.0.post2.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ executing
│  │     │  ├─ executing.py
│  │     │  ├─ py.typed
│  │     │  ├─ version.py
│  │     │  ├─ _exceptions.py
│  │     │  ├─ _position_node_finder.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ executing.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     ├─ _exceptions.cpython-39.pyc
│  │     │     ├─ _position_node_finder.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ executing-1.2.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ fastapi
│  │     │  ├─ applications.py
│  │     │  ├─ background.py
│  │     │  ├─ concurrency.py
│  │     │  ├─ datastructures.py
│  │     │  ├─ dependencies
│  │     │  │  ├─ models.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ models.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ encoders.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ exception_handlers.py
│  │     │  ├─ logger.py
│  │     │  ├─ middleware
│  │     │  │  ├─ asyncexitstack.py
│  │     │  │  ├─ cors.py
│  │     │  │  ├─ gzip.py
│  │     │  │  ├─ httpsredirect.py
│  │     │  │  ├─ trustedhost.py
│  │     │  │  ├─ wsgi.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ asyncexitstack.cpython-39.pyc
│  │     │  │     ├─ cors.cpython-39.pyc
│  │     │  │     ├─ gzip.cpython-39.pyc
│  │     │  │     ├─ httpsredirect.cpython-39.pyc
│  │     │  │     ├─ trustedhost.cpython-39.pyc
│  │     │  │     ├─ wsgi.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ openapi
│  │     │  │  ├─ constants.py
│  │     │  │  ├─ docs.py
│  │     │  │  ├─ models.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ constants.cpython-39.pyc
│  │     │  │     ├─ docs.cpython-39.pyc
│  │     │  │     ├─ models.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ params.py
│  │     │  ├─ param_functions.py
│  │     │  ├─ py.typed
│  │     │  ├─ requests.py
│  │     │  ├─ responses.py
│  │     │  ├─ routing.py
│  │     │  ├─ security
│  │     │  │  ├─ api_key.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ http.py
│  │     │  │  ├─ oauth2.py
│  │     │  │  ├─ open_id_connect_url.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ api_key.cpython-39.pyc
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ http.cpython-39.pyc
│  │     │  │     ├─ oauth2.cpython-39.pyc
│  │     │  │     ├─ open_id_connect_url.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ staticfiles.py
│  │     │  ├─ templating.py
│  │     │  ├─ testclient.py
│  │     │  ├─ types.py
│  │     │  ├─ utils.py
│  │     │  ├─ websockets.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ applications.cpython-39.pyc
│  │     │     ├─ background.cpython-39.pyc
│  │     │     ├─ concurrency.cpython-39.pyc
│  │     │     ├─ datastructures.cpython-39.pyc
│  │     │     ├─ encoders.cpython-39.pyc
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ exception_handlers.cpython-39.pyc
│  │     │     ├─ logger.cpython-39.pyc
│  │     │     ├─ params.cpython-39.pyc
│  │     │     ├─ param_functions.cpython-39.pyc
│  │     │     ├─ requests.cpython-39.pyc
│  │     │     ├─ responses.cpython-39.pyc
│  │     │     ├─ routing.cpython-39.pyc
│  │     │     ├─ staticfiles.cpython-39.pyc
│  │     │     ├─ templating.cpython-39.pyc
│  │     │     ├─ testclient.cpython-39.pyc
│  │     │     ├─ types.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ websockets.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ fastapi-0.95.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ fontTools
│  │     │  ├─ afmLib.py
│  │     │  ├─ agl.py
│  │     │  ├─ cffLib
│  │     │  │  ├─ specializer.py
│  │     │  │  ├─ width.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ specializer.cpython-39.pyc
│  │     │  │     ├─ width.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ colorLib
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ geometry.py
│  │     │  │  ├─ table_builder.py
│  │     │  │  ├─ unbuilder.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ builder.cpython-39.pyc
│  │     │  │     ├─ errors.cpython-39.pyc
│  │     │  │     ├─ geometry.cpython-39.pyc
│  │     │  │     ├─ table_builder.cpython-39.pyc
│  │     │  │     ├─ unbuilder.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ config
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ cu2qu
│  │     │  │  ├─ benchmark.py
│  │     │  │  ├─ cli.py
│  │     │  │  ├─ cu2qu.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ ufo.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ benchmark.cpython-39.pyc
│  │     │  │     ├─ cli.cpython-39.pyc
│  │     │  │     ├─ cu2qu.cpython-39.pyc
│  │     │  │     ├─ errors.cpython-39.pyc
│  │     │  │     ├─ ufo.cpython-39.pyc
│  │     │  │     ├─ __init__.cpython-39.pyc
│  │     │  │     └─ __main__.cpython-39.pyc
│  │     │  ├─ designspaceLib
│  │     │  │  ├─ split.py
│  │     │  │  ├─ statNames.py
│  │     │  │  ├─ types.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ split.cpython-39.pyc
│  │     │  │     ├─ statNames.cpython-39.pyc
│  │     │  │     ├─ types.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ encodings
│  │     │  │  ├─ codecs.py
│  │     │  │  ├─ MacRoman.py
│  │     │  │  ├─ StandardEncoding.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ codecs.cpython-39.pyc
│  │     │  │     ├─ MacRoman.cpython-39.pyc
│  │     │  │     ├─ StandardEncoding.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ feaLib
│  │     │  │  ├─ ast.py
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ error.py
│  │     │  │  ├─ lexer.py
│  │     │  │  ├─ location.py
│  │     │  │  ├─ lookupDebugInfo.py
│  │     │  │  ├─ parser.py
│  │     │  │  ├─ variableScalar.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ast.cpython-39.pyc
│  │     │  │     ├─ builder.cpython-39.pyc
│  │     │  │     ├─ error.cpython-39.pyc
│  │     │  │     ├─ lexer.cpython-39.pyc
│  │     │  │     ├─ location.cpython-39.pyc
│  │     │  │     ├─ lookupDebugInfo.cpython-39.pyc
│  │     │  │     ├─ parser.cpython-39.pyc
│  │     │  │     ├─ variableScalar.cpython-39.pyc
│  │     │  │     ├─ __init__.cpython-39.pyc
│  │     │  │     └─ __main__.cpython-39.pyc
│  │     │  ├─ fontBuilder.py
│  │     │  ├─ help.py
│  │     │  ├─ merge
│  │     │  │  ├─ base.py
│  │     │  │  ├─ cmap.py
│  │     │  │  ├─ layout.py
│  │     │  │  ├─ options.py
│  │     │  │  ├─ tables.py
│  │     │  │  ├─ unicode.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ cmap.cpython-39.pyc
│  │     │  │     ├─ layout.cpython-39.pyc
│  │     │  │     ├─ options.cpython-39.pyc
│  │     │  │     ├─ tables.cpython-39.pyc
│  │     │  │     ├─ unicode.cpython-39.pyc
│  │     │  │     ├─ util.cpython-39.pyc
│  │     │  │     ├─ __init__.cpython-39.pyc
│  │     │  │     └─ __main__.cpython-39.pyc
│  │     │  ├─ misc
│  │     │  │  ├─ arrayTools.py
│  │     │  │  ├─ bezierTools.py
│  │     │  │  ├─ classifyTools.py
│  │     │  │  ├─ cliTools.py
│  │     │  │  ├─ configTools.py
│  │     │  │  ├─ cython.py
│  │     │  │  ├─ dictTools.py
│  │     │  │  ├─ eexec.py
│  │     │  │  ├─ encodingTools.py
│  │     │  │  ├─ etree.py
│  │     │  │  ├─ filenames.py
│  │     │  │  ├─ fixedTools.py
│  │     │  │  ├─ intTools.py
│  │     │  │  ├─ loggingTools.py
│  │     │  │  ├─ macCreatorType.py
│  │     │  │  ├─ macRes.py
│  │     │  │  ├─ plistlib
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ psCharStrings.py
│  │     │  │  ├─ psLib.py
│  │     │  │  ├─ psOperators.py
│  │     │  │  ├─ py23.py
│  │     │  │  ├─ roundTools.py
│  │     │  │  ├─ sstruct.py
│  │     │  │  ├─ symfont.py
│  │     │  │  ├─ testTools.py
│  │     │  │  ├─ textTools.py
│  │     │  │  ├─ timeTools.py
│  │     │  │  ├─ transform.py
│  │     │  │  ├─ treeTools.py
│  │     │  │  ├─ vector.py
│  │     │  │  ├─ visitor.py
│  │     │  │  ├─ xmlReader.py
│  │     │  │  ├─ xmlWriter.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ arrayTools.cpython-39.pyc
│  │     │  │     ├─ bezierTools.cpython-39.pyc
│  │     │  │     ├─ classifyTools.cpython-39.pyc
│  │     │  │     ├─ cliTools.cpython-39.pyc
│  │     │  │     ├─ configTools.cpython-39.pyc
│  │     │  │     ├─ cython.cpython-39.pyc
│  │     │  │     ├─ dictTools.cpython-39.pyc
│  │     │  │     ├─ eexec.cpython-39.pyc
│  │     │  │     ├─ encodingTools.cpython-39.pyc
│  │     │  │     ├─ etree.cpython-39.pyc
│  │     │  │     ├─ filenames.cpython-39.pyc
│  │     │  │     ├─ fixedTools.cpython-39.pyc
│  │     │  │     ├─ intTools.cpython-39.pyc
│  │     │  │     ├─ loggingTools.cpython-39.pyc
│  │     │  │     ├─ macCreatorType.cpython-39.pyc
│  │     │  │     ├─ macRes.cpython-39.pyc
│  │     │  │     ├─ psCharStrings.cpython-39.pyc
│  │     │  │     ├─ psLib.cpython-39.pyc
│  │     │  │     ├─ psOperators.cpython-39.pyc
│  │     │  │     ├─ py23.cpython-39.pyc
│  │     │  │     ├─ roundTools.cpython-39.pyc
│  │     │  │     ├─ sstruct.cpython-39.pyc
│  │     │  │     ├─ symfont.cpython-39.pyc
│  │     │  │     ├─ testTools.cpython-39.pyc
│  │     │  │     ├─ textTools.cpython-39.pyc
│  │     │  │     ├─ timeTools.cpython-39.pyc
│  │     │  │     ├─ transform.cpython-39.pyc
│  │     │  │     ├─ treeTools.cpython-39.pyc
│  │     │  │     ├─ vector.cpython-39.pyc
│  │     │  │     ├─ visitor.cpython-39.pyc
│  │     │  │     ├─ xmlReader.cpython-39.pyc
│  │     │  │     ├─ xmlWriter.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ mtiLib
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ __init__.cpython-39.pyc
│  │     │  │     └─ __main__.cpython-39.pyc
│  │     │  ├─ otlLib
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ error.py
│  │     │  │  ├─ maxContextCalc.py
│  │     │  │  ├─ optimize
│  │     │  │  │  ├─ gpos.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ gpos.cpython-39.pyc
│  │     │  │  │     ├─ __init__.cpython-39.pyc
│  │     │  │  │     └─ __main__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ builder.cpython-39.pyc
│  │     │  │     ├─ error.cpython-39.pyc
│  │     │  │     ├─ maxContextCalc.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ pens
│  │     │  │  ├─ areaPen.py
│  │     │  │  ├─ basePen.py
│  │     │  │  ├─ boundsPen.py
│  │     │  │  ├─ cairoPen.py
│  │     │  │  ├─ cocoaPen.py
│  │     │  │  ├─ cu2quPen.py
│  │     │  │  ├─ filterPen.py
│  │     │  │  ├─ freetypePen.py
│  │     │  │  ├─ hashPointPen.py
│  │     │  │  ├─ momentsPen.py
│  │     │  │  ├─ perimeterPen.py
│  │     │  │  ├─ pointInsidePen.py
│  │     │  │  ├─ pointPen.py
│  │     │  │  ├─ qtPen.py
│  │     │  │  ├─ qu2cuPen.py
│  │     │  │  ├─ quartzPen.py
│  │     │  │  ├─ recordingPen.py
│  │     │  │  ├─ reportLabPen.py
│  │     │  │  ├─ reverseContourPen.py
│  │     │  │  ├─ roundingPen.py
│  │     │  │  ├─ statisticsPen.py
│  │     │  │  ├─ svgPathPen.py
│  │     │  │  ├─ t2CharStringPen.py
│  │     │  │  ├─ teePen.py
│  │     │  │  ├─ transformPen.py
│  │     │  │  ├─ ttGlyphPen.py
│  │     │  │  ├─ wxPen.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ areaPen.cpython-39.pyc
│  │     │  │     ├─ basePen.cpython-39.pyc
│  │     │  │     ├─ boundsPen.cpython-39.pyc
│  │     │  │     ├─ cairoPen.cpython-39.pyc
│  │     │  │     ├─ cocoaPen.cpython-39.pyc
│  │     │  │     ├─ cu2quPen.cpython-39.pyc
│  │     │  │     ├─ filterPen.cpython-39.pyc
│  │     │  │     ├─ freetypePen.cpython-39.pyc
│  │     │  │     ├─ hashPointPen.cpython-39.pyc
│  │     │  │     ├─ momentsPen.cpython-39.pyc
│  │     │  │     ├─ perimeterPen.cpython-39.pyc
│  │     │  │     ├─ pointInsidePen.cpython-39.pyc
│  │     │  │     ├─ pointPen.cpython-39.pyc
│  │     │  │     ├─ qtPen.cpython-39.pyc
│  │     │  │     ├─ qu2cuPen.cpython-39.pyc
│  │     │  │     ├─ quartzPen.cpython-39.pyc
│  │     │  │     ├─ recordingPen.cpython-39.pyc
│  │     │  │     ├─ reportLabPen.cpython-39.pyc
│  │     │  │     ├─ reverseContourPen.cpython-39.pyc
│  │     │  │     ├─ roundingPen.cpython-39.pyc
│  │     │  │     ├─ statisticsPen.cpython-39.pyc
│  │     │  │     ├─ svgPathPen.cpython-39.pyc
│  │     │  │     ├─ t2CharStringPen.cpython-39.pyc
│  │     │  │     ├─ teePen.cpython-39.pyc
│  │     │  │     ├─ transformPen.cpython-39.pyc
│  │     │  │     ├─ ttGlyphPen.cpython-39.pyc
│  │     │  │     ├─ wxPen.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ qu2cu
│  │     │  │  ├─ benchmark.py
│  │     │  │  ├─ cli.py
│  │     │  │  ├─ qu2cu.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ benchmark.cpython-39.pyc
│  │     │  │     ├─ cli.cpython-39.pyc
│  │     │  │     ├─ qu2cu.cpython-39.pyc
│  │     │  │     ├─ __init__.cpython-39.pyc
│  │     │  │     └─ __main__.cpython-39.pyc
│  │     │  ├─ subset
│  │     │  │  ├─ cff.py
│  │     │  │  ├─ svg.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ cff.cpython-39.pyc
│  │     │  │     ├─ svg.cpython-39.pyc
│  │     │  │     ├─ util.cpython-39.pyc
│  │     │  │     ├─ __init__.cpython-39.pyc
│  │     │  │     └─ __main__.cpython-39.pyc
│  │     │  ├─ svgLib
│  │     │  │  ├─ path
│  │     │  │  │  ├─ arc.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ shapes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ arc.cpython-39.pyc
│  │     │  │  │     ├─ parser.cpython-39.pyc
│  │     │  │  │     ├─ shapes.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ t1Lib
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ tfmLib.py
│  │     │  ├─ ttLib
│  │     │  │  ├─ macUtils.py
│  │     │  │  ├─ removeOverlaps.py
│  │     │  │  ├─ scaleUpem.py
│  │     │  │  ├─ sfnt.py
│  │     │  │  ├─ standardGlyphOrder.py
│  │     │  │  ├─ tables
│  │     │  │  │  ├─ asciiTable.py
│  │     │  │  │  ├─ BitmapGlyphMetrics.py
│  │     │  │  │  ├─ B_A_S_E_.py
│  │     │  │  │  ├─ C_B_D_T_.py
│  │     │  │  │  ├─ C_B_L_C_.py
│  │     │  │  │  ├─ C_F_F_.py
│  │     │  │  │  ├─ C_F_F__2.py
│  │     │  │  │  ├─ C_O_L_R_.py
│  │     │  │  │  ├─ C_P_A_L_.py
│  │     │  │  │  ├─ DefaultTable.py
│  │     │  │  │  ├─ D_S_I_G_.py
│  │     │  │  │  ├─ D__e_b_g.py
│  │     │  │  │  ├─ E_B_D_T_.py
│  │     │  │  │  ├─ E_B_L_C_.py
│  │     │  │  │  ├─ F_F_T_M_.py
│  │     │  │  │  ├─ F__e_a_t.py
│  │     │  │  │  ├─ grUtils.py
│  │     │  │  │  ├─ G_D_E_F_.py
│  │     │  │  │  ├─ G_M_A_P_.py
│  │     │  │  │  ├─ G_P_K_G_.py
│  │     │  │  │  ├─ G_P_O_S_.py
│  │     │  │  │  ├─ G_S_U_B_.py
│  │     │  │  │  ├─ G__l_a_t.py
│  │     │  │  │  ├─ G__l_o_c.py
│  │     │  │  │  ├─ H_V_A_R_.py
│  │     │  │  │  ├─ J_S_T_F_.py
│  │     │  │  │  ├─ L_T_S_H_.py
│  │     │  │  │  ├─ M_A_T_H_.py
│  │     │  │  │  ├─ M_E_T_A_.py
│  │     │  │  │  ├─ M_V_A_R_.py
│  │     │  │  │  ├─ otBase.py
│  │     │  │  │  ├─ otConverters.py
│  │     │  │  │  ├─ otData.py
│  │     │  │  │  ├─ otTables.py
│  │     │  │  │  ├─ otTraverse.py
│  │     │  │  │  ├─ O_S_2f_2.py
│  │     │  │  │  ├─ sbixGlyph.py
│  │     │  │  │  ├─ sbixStrike.py
│  │     │  │  │  ├─ S_I_N_G_.py
│  │     │  │  │  ├─ S_T_A_T_.py
│  │     │  │  │  ├─ S_V_G_.py
│  │     │  │  │  ├─ S__i_l_f.py
│  │     │  │  │  ├─ S__i_l_l.py
│  │     │  │  │  ├─ table_API_readme.txt
│  │     │  │  │  ├─ ttProgram.py
│  │     │  │  │  ├─ TupleVariation.py
│  │     │  │  │  ├─ T_S_I_B_.py
│  │     │  │  │  ├─ T_S_I_C_.py
│  │     │  │  │  ├─ T_S_I_D_.py
│  │     │  │  │  ├─ T_S_I_J_.py
│  │     │  │  │  ├─ T_S_I_P_.py
│  │     │  │  │  ├─ T_S_I_S_.py
│  │     │  │  │  ├─ T_S_I_V_.py
│  │     │  │  │  ├─ T_S_I__0.py
│  │     │  │  │  ├─ T_S_I__1.py
│  │     │  │  │  ├─ T_S_I__2.py
│  │     │  │  │  ├─ T_S_I__3.py
│  │     │  │  │  ├─ T_S_I__5.py
│  │     │  │  │  ├─ T_T_F_A_.py
│  │     │  │  │  ├─ V_D_M_X_.py
│  │     │  │  │  ├─ V_O_R_G_.py
│  │     │  │  │  ├─ V_V_A_R_.py
│  │     │  │  │  ├─ _a_n_k_r.py
│  │     │  │  │  ├─ _a_v_a_r.py
│  │     │  │  │  ├─ _b_s_l_n.py
│  │     │  │  │  ├─ _c_i_d_g.py
│  │     │  │  │  ├─ _c_m_a_p.py
│  │     │  │  │  ├─ _c_v_a_r.py
│  │     │  │  │  ├─ _c_v_t.py
│  │     │  │  │  ├─ _f_e_a_t.py
│  │     │  │  │  ├─ _f_p_g_m.py
│  │     │  │  │  ├─ _f_v_a_r.py
│  │     │  │  │  ├─ _g_a_s_p.py
│  │     │  │  │  ├─ _g_c_i_d.py
│  │     │  │  │  ├─ _g_l_y_f.py
│  │     │  │  │  ├─ _g_v_a_r.py
│  │     │  │  │  ├─ _h_d_m_x.py
│  │     │  │  │  ├─ _h_e_a_d.py
│  │     │  │  │  ├─ _h_h_e_a.py
│  │     │  │  │  ├─ _h_m_t_x.py
│  │     │  │  │  ├─ _k_e_r_n.py
│  │     │  │  │  ├─ _l_c_a_r.py
│  │     │  │  │  ├─ _l_o_c_a.py
│  │     │  │  │  ├─ _l_t_a_g.py
│  │     │  │  │  ├─ _m_a_x_p.py
│  │     │  │  │  ├─ _m_e_t_a.py
│  │     │  │  │  ├─ _m_o_r_t.py
│  │     │  │  │  ├─ _m_o_r_x.py
│  │     │  │  │  ├─ _n_a_m_e.py
│  │     │  │  │  ├─ _o_p_b_d.py
│  │     │  │  │  ├─ _p_o_s_t.py
│  │     │  │  │  ├─ _p_r_e_p.py
│  │     │  │  │  ├─ _p_r_o_p.py
│  │     │  │  │  ├─ _s_b_i_x.py
│  │     │  │  │  ├─ _t_r_a_k.py
│  │     │  │  │  ├─ _v_h_e_a.py
│  │     │  │  │  ├─ _v_m_t_x.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ asciiTable.cpython-39.pyc
│  │     │  │  │     ├─ BitmapGlyphMetrics.cpython-39.pyc
│  │     │  │  │     ├─ B_A_S_E_.cpython-39.pyc
│  │     │  │  │     ├─ C_B_D_T_.cpython-39.pyc
│  │     │  │  │     ├─ C_B_L_C_.cpython-39.pyc
│  │     │  │  │     ├─ C_F_F_.cpython-39.pyc
│  │     │  │  │     ├─ C_F_F__2.cpython-39.pyc
│  │     │  │  │     ├─ C_O_L_R_.cpython-39.pyc
│  │     │  │  │     ├─ C_P_A_L_.cpython-39.pyc
│  │     │  │  │     ├─ DefaultTable.cpython-39.pyc
│  │     │  │  │     ├─ D_S_I_G_.cpython-39.pyc
│  │     │  │  │     ├─ D__e_b_g.cpython-39.pyc
│  │     │  │  │     ├─ E_B_D_T_.cpython-39.pyc
│  │     │  │  │     ├─ E_B_L_C_.cpython-39.pyc
│  │     │  │  │     ├─ F_F_T_M_.cpython-39.pyc
│  │     │  │  │     ├─ F__e_a_t.cpython-39.pyc
│  │     │  │  │     ├─ grUtils.cpython-39.pyc
│  │     │  │  │     ├─ G_D_E_F_.cpython-39.pyc
│  │     │  │  │     ├─ G_M_A_P_.cpython-39.pyc
│  │     │  │  │     ├─ G_P_K_G_.cpython-39.pyc
│  │     │  │  │     ├─ G_P_O_S_.cpython-39.pyc
│  │     │  │  │     ├─ G_S_U_B_.cpython-39.pyc
│  │     │  │  │     ├─ G__l_a_t.cpython-39.pyc
│  │     │  │  │     ├─ G__l_o_c.cpython-39.pyc
│  │     │  │  │     ├─ H_V_A_R_.cpython-39.pyc
│  │     │  │  │     ├─ J_S_T_F_.cpython-39.pyc
│  │     │  │  │     ├─ L_T_S_H_.cpython-39.pyc
│  │     │  │  │     ├─ M_A_T_H_.cpython-39.pyc
│  │     │  │  │     ├─ M_E_T_A_.cpython-39.pyc
│  │     │  │  │     ├─ M_V_A_R_.cpython-39.pyc
│  │     │  │  │     ├─ otBase.cpython-39.pyc
│  │     │  │  │     ├─ otConverters.cpython-39.pyc
│  │     │  │  │     ├─ otData.cpython-39.pyc
│  │     │  │  │     ├─ otTables.cpython-39.pyc
│  │     │  │  │     ├─ otTraverse.cpython-39.pyc
│  │     │  │  │     ├─ O_S_2f_2.cpython-39.pyc
│  │     │  │  │     ├─ sbixGlyph.cpython-39.pyc
│  │     │  │  │     ├─ sbixStrike.cpython-39.pyc
│  │     │  │  │     ├─ S_I_N_G_.cpython-39.pyc
│  │     │  │  │     ├─ S_T_A_T_.cpython-39.pyc
│  │     │  │  │     ├─ S_V_G_.cpython-39.pyc
│  │     │  │  │     ├─ S__i_l_f.cpython-39.pyc
│  │     │  │  │     ├─ S__i_l_l.cpython-39.pyc
│  │     │  │  │     ├─ ttProgram.cpython-39.pyc
│  │     │  │  │     ├─ TupleVariation.cpython-39.pyc
│  │     │  │  │     ├─ T_S_I_B_.cpython-39.pyc
│  │     │  │  │     ├─ T_S_I_C_.cpython-39.pyc
│  │     │  │  │     ├─ T_S_I_D_.cpython-39.pyc
│  │     │  │  │     ├─ T_S_I_J_.cpython-39.pyc
│  │     │  │  │     ├─ T_S_I_P_.cpython-39.pyc
│  │     │  │  │     ├─ T_S_I_S_.cpython-39.pyc
│  │     │  │  │     ├─ T_S_I_V_.cpython-39.pyc
│  │     │  │  │     ├─ T_S_I__0.cpython-39.pyc
│  │     │  │  │     ├─ T_S_I__1.cpython-39.pyc
│  │     │  │  │     ├─ T_S_I__2.cpython-39.pyc
│  │     │  │  │     ├─ T_S_I__3.cpython-39.pyc
│  │     │  │  │     ├─ T_S_I__5.cpython-39.pyc
│  │     │  │  │     ├─ T_T_F_A_.cpython-39.pyc
│  │     │  │  │     ├─ V_D_M_X_.cpython-39.pyc
│  │     │  │  │     ├─ V_O_R_G_.cpython-39.pyc
│  │     │  │  │     ├─ V_V_A_R_.cpython-39.pyc
│  │     │  │  │     ├─ _a_n_k_r.cpython-39.pyc
│  │     │  │  │     ├─ _a_v_a_r.cpython-39.pyc
│  │     │  │  │     ├─ _b_s_l_n.cpython-39.pyc
│  │     │  │  │     ├─ _c_i_d_g.cpython-39.pyc
│  │     │  │  │     ├─ _c_m_a_p.cpython-39.pyc
│  │     │  │  │     ├─ _c_v_a_r.cpython-39.pyc
│  │     │  │  │     ├─ _c_v_t.cpython-39.pyc
│  │     │  │  │     ├─ _f_e_a_t.cpython-39.pyc
│  │     │  │  │     ├─ _f_p_g_m.cpython-39.pyc
│  │     │  │  │     ├─ _f_v_a_r.cpython-39.pyc
│  │     │  │  │     ├─ _g_a_s_p.cpython-39.pyc
│  │     │  │  │     ├─ _g_c_i_d.cpython-39.pyc
│  │     │  │  │     ├─ _g_l_y_f.cpython-39.pyc
│  │     │  │  │     ├─ _g_v_a_r.cpython-39.pyc
│  │     │  │  │     ├─ _h_d_m_x.cpython-39.pyc
│  │     │  │  │     ├─ _h_e_a_d.cpython-39.pyc
│  │     │  │  │     ├─ _h_h_e_a.cpython-39.pyc
│  │     │  │  │     ├─ _h_m_t_x.cpython-39.pyc
│  │     │  │  │     ├─ _k_e_r_n.cpython-39.pyc
│  │     │  │  │     ├─ _l_c_a_r.cpython-39.pyc
│  │     │  │  │     ├─ _l_o_c_a.cpython-39.pyc
│  │     │  │  │     ├─ _l_t_a_g.cpython-39.pyc
│  │     │  │  │     ├─ _m_a_x_p.cpython-39.pyc
│  │     │  │  │     ├─ _m_e_t_a.cpython-39.pyc
│  │     │  │  │     ├─ _m_o_r_t.cpython-39.pyc
│  │     │  │  │     ├─ _m_o_r_x.cpython-39.pyc
│  │     │  │  │     ├─ _n_a_m_e.cpython-39.pyc
│  │     │  │  │     ├─ _o_p_b_d.cpython-39.pyc
│  │     │  │  │     ├─ _p_o_s_t.cpython-39.pyc
│  │     │  │  │     ├─ _p_r_e_p.cpython-39.pyc
│  │     │  │  │     ├─ _p_r_o_p.cpython-39.pyc
│  │     │  │  │     ├─ _s_b_i_x.cpython-39.pyc
│  │     │  │  │     ├─ _t_r_a_k.cpython-39.pyc
│  │     │  │  │     ├─ _v_h_e_a.cpython-39.pyc
│  │     │  │  │     ├─ _v_m_t_x.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ ttCollection.py
│  │     │  │  ├─ ttFont.py
│  │     │  │  ├─ ttGlyphSet.py
│  │     │  │  ├─ ttVisitor.py
│  │     │  │  ├─ woff2.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ macUtils.cpython-39.pyc
│  │     │  │     ├─ removeOverlaps.cpython-39.pyc
│  │     │  │     ├─ scaleUpem.cpython-39.pyc
│  │     │  │     ├─ sfnt.cpython-39.pyc
│  │     │  │     ├─ standardGlyphOrder.cpython-39.pyc
│  │     │  │     ├─ ttCollection.cpython-39.pyc
│  │     │  │     ├─ ttFont.cpython-39.pyc
│  │     │  │     ├─ ttGlyphSet.cpython-39.pyc
│  │     │  │     ├─ ttVisitor.cpython-39.pyc
│  │     │  │     ├─ woff2.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ ttx.py
│  │     │  ├─ ufoLib
│  │     │  │  ├─ converters.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ etree.py
│  │     │  │  ├─ filenames.py
│  │     │  │  ├─ glifLib.py
│  │     │  │  ├─ kerning.py
│  │     │  │  ├─ plistlib.py
│  │     │  │  ├─ pointPen.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ validators.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ converters.cpython-39.pyc
│  │     │  │     ├─ errors.cpython-39.pyc
│  │     │  │     ├─ etree.cpython-39.pyc
│  │     │  │     ├─ filenames.cpython-39.pyc
│  │     │  │     ├─ glifLib.cpython-39.pyc
│  │     │  │     ├─ kerning.cpython-39.pyc
│  │     │  │     ├─ plistlib.cpython-39.pyc
│  │     │  │     ├─ pointPen.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     ├─ validators.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ unicode.py
│  │     │  ├─ unicodedata
│  │     │  │  ├─ Blocks.py
│  │     │  │  ├─ OTTags.py
│  │     │  │  ├─ ScriptExtensions.py
│  │     │  │  ├─ Scripts.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ Blocks.cpython-39.pyc
│  │     │  │     ├─ OTTags.cpython-39.pyc
│  │     │  │     ├─ ScriptExtensions.cpython-39.pyc
│  │     │  │     ├─ Scripts.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ varLib
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ cff.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ featureVars.py
│  │     │  │  ├─ instancer
│  │     │  │  │  ├─ featureVars.py
│  │     │  │  │  ├─ names.py
│  │     │  │  │  ├─ solver.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ featureVars.cpython-39.pyc
│  │     │  │  │     ├─ names.cpython-39.pyc
│  │     │  │  │     ├─ solver.cpython-39.pyc
│  │     │  │  │     ├─ __init__.cpython-39.pyc
│  │     │  │  │     └─ __main__.cpython-39.pyc
│  │     │  │  ├─ interpolatable.py
│  │     │  │  ├─ interpolate_layout.py
│  │     │  │  ├─ iup.py
│  │     │  │  ├─ merger.py
│  │     │  │  ├─ models.py
│  │     │  │  ├─ mutator.py
│  │     │  │  ├─ mvar.py
│  │     │  │  ├─ plot.py
│  │     │  │  ├─ stat.py
│  │     │  │  ├─ varStore.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ builder.cpython-39.pyc
│  │     │  │     ├─ cff.cpython-39.pyc
│  │     │  │     ├─ errors.cpython-39.pyc
│  │     │  │     ├─ featureVars.cpython-39.pyc
│  │     │  │     ├─ interpolatable.cpython-39.pyc
│  │     │  │     ├─ interpolate_layout.cpython-39.pyc
│  │     │  │     ├─ iup.cpython-39.pyc
│  │     │  │     ├─ merger.cpython-39.pyc
│  │     │  │     ├─ models.cpython-39.pyc
│  │     │  │     ├─ mutator.cpython-39.pyc
│  │     │  │     ├─ mvar.cpython-39.pyc
│  │     │  │     ├─ plot.cpython-39.pyc
│  │     │  │     ├─ stat.cpython-39.pyc
│  │     │  │     ├─ varStore.cpython-39.pyc
│  │     │  │     ├─ __init__.cpython-39.pyc
│  │     │  │     └─ __main__.cpython-39.pyc
│  │     │  ├─ voltLib
│  │     │  │  ├─ ast.py
│  │     │  │  ├─ error.py
│  │     │  │  ├─ lexer.py
│  │     │  │  ├─ parser.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ast.cpython-39.pyc
│  │     │  │     ├─ error.cpython-39.pyc
│  │     │  │     ├─ lexer.cpython-39.pyc
│  │     │  │     ├─ parser.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ afmLib.cpython-39.pyc
│  │     │     ├─ agl.cpython-39.pyc
│  │     │     ├─ fontBuilder.cpython-39.pyc
│  │     │     ├─ help.cpython-39.pyc
│  │     │     ├─ tfmLib.cpython-39.pyc
│  │     │     ├─ ttx.cpython-39.pyc
│  │     │     ├─ unicode.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ fonttools-4.39.3.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ genson
│  │     │  ├─ cli.py
│  │     │  ├─ schema
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ node.py
│  │     │  │  ├─ strategies
│  │     │  │  │  ├─ array.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ object.py
│  │     │  │  │  ├─ scalar.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ array.cpython-39.pyc
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ object.cpython-39.pyc
│  │     │  │  │     ├─ scalar.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ builder.cpython-39.pyc
│  │     │  │     ├─ node.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ cli.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ genson-1.2.2-py3.9.egg-info
│  │     │  ├─ dependency_links.txt
│  │     │  ├─ entry_points.txt
│  │     │  ├─ installed-files.txt
│  │     │  ├─ PKG-INFO
│  │     │  ├─ SOURCES.txt
│  │     │  ├─ top_level.txt
│  │     │  └─ zip-safe
│  │     ├─ h11
│  │     │  ├─ py.typed
│  │     │  ├─ tests
│  │     │  │  ├─ data
│  │     │  │  │  └─ test-file
│  │     │  │  ├─ helpers.py
│  │     │  │  ├─ test_against_stdlib_http.py
│  │     │  │  ├─ test_connection.py
│  │     │  │  ├─ test_events.py
│  │     │  │  ├─ test_headers.py
│  │     │  │  ├─ test_helpers.py
│  │     │  │  ├─ test_io.py
│  │     │  │  ├─ test_receivebuffer.py
│  │     │  │  ├─ test_state.py
│  │     │  │  ├─ test_util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ helpers.cpython-39.pyc
│  │     │  │     ├─ test_against_stdlib_http.cpython-39.pyc
│  │     │  │     ├─ test_connection.cpython-39.pyc
│  │     │  │     ├─ test_events.cpython-39.pyc
│  │     │  │     ├─ test_headers.cpython-39.pyc
│  │     │  │     ├─ test_helpers.cpython-39.pyc
│  │     │  │     ├─ test_io.cpython-39.pyc
│  │     │  │     ├─ test_receivebuffer.cpython-39.pyc
│  │     │  │     ├─ test_state.cpython-39.pyc
│  │     │  │     ├─ test_util.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _abnf.py
│  │     │  ├─ _connection.py
│  │     │  ├─ _events.py
│  │     │  ├─ _headers.py
│  │     │  ├─ _readers.py
│  │     │  ├─ _receivebuffer.py
│  │     │  ├─ _state.py
│  │     │  ├─ _util.py
│  │     │  ├─ _version.py
│  │     │  ├─ _writers.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ _abnf.cpython-39.pyc
│  │     │     ├─ _connection.cpython-39.pyc
│  │     │     ├─ _events.cpython-39.pyc
│  │     │     ├─ _headers.cpython-39.pyc
│  │     │     ├─ _readers.cpython-39.pyc
│  │     │     ├─ _receivebuffer.cpython-39.pyc
│  │     │     ├─ _state.cpython-39.pyc
│  │     │     ├─ _util.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     ├─ _writers.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ h11-0.14.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ idna
│  │     │  ├─ codec.py
│  │     │  ├─ compat.py
│  │     │  ├─ core.py
│  │     │  ├─ idnadata.py
│  │     │  ├─ intranges.py
│  │     │  ├─ package_data.py
│  │     │  ├─ py.typed
│  │     │  ├─ uts46data.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ codec.cpython-39.pyc
│  │     │     ├─ compat.cpython-39.pyc
│  │     │     ├─ core.cpython-39.pyc
│  │     │     ├─ idnadata.cpython-39.pyc
│  │     │     ├─ intranges.cpython-39.pyc
│  │     │     ├─ package_data.cpython-39.pyc
│  │     │     ├─ uts46data.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ idna-3.4.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ importlib_metadata
│  │     │  ├─ py.typed
│  │     │  ├─ _adapters.py
│  │     │  ├─ _collections.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _functools.py
│  │     │  ├─ _itertools.py
│  │     │  ├─ _meta.py
│  │     │  ├─ _py39compat.py
│  │     │  ├─ _text.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ _adapters.cpython-39.pyc
│  │     │     ├─ _collections.cpython-39.pyc
│  │     │     ├─ _compat.cpython-39.pyc
│  │     │     ├─ _functools.cpython-39.pyc
│  │     │     ├─ _itertools.cpython-39.pyc
│  │     │     ├─ _meta.cpython-39.pyc
│  │     │     ├─ _py39compat.cpython-39.pyc
│  │     │     ├─ _text.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ importlib_metadata-6.5.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ importlib_resources
│  │     │  ├─ abc.py
│  │     │  ├─ py.typed
│  │     │  ├─ readers.py
│  │     │  ├─ simple.py
│  │     │  ├─ tests
│  │     │  │  ├─ data01
│  │     │  │  │  ├─ binary.file
│  │     │  │  │  ├─ subdirectory
│  │     │  │  │  │  ├─ binary.file
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ utf-16.file
│  │     │  │  │  ├─ utf-8.file
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ data02
│  │     │  │  │  ├─ one
│  │     │  │  │  │  ├─ resource1.txt
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ subdirectory
│  │     │  │  │  │  └─ subsubdir
│  │     │  │  │  │     └─ resource.txt
│  │     │  │  │  ├─ two
│  │     │  │  │  │  ├─ resource2.txt
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ namespacedata01
│  │     │  │  │  ├─ binary.file
│  │     │  │  │  ├─ utf-16.file
│  │     │  │  │  └─ utf-8.file
│  │     │  │  ├─ test_compatibilty_files.py
│  │     │  │  ├─ test_contents.py
│  │     │  │  ├─ test_custom.py
│  │     │  │  ├─ test_files.py
│  │     │  │  ├─ test_open.py
│  │     │  │  ├─ test_path.py
│  │     │  │  ├─ test_read.py
│  │     │  │  ├─ test_reader.py
│  │     │  │  ├─ test_resource.py
│  │     │  │  ├─ update-zips.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ zipdata01
│  │     │  │  │  ├─ ziptestdata.zip
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ zipdata02
│  │     │  │  │  ├─ ziptestdata.zip
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _compat.py
│  │     │  │  ├─ _path.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ test_compatibilty_files.cpython-39.pyc
│  │     │  │     ├─ test_contents.cpython-39.pyc
│  │     │  │     ├─ test_custom.cpython-39.pyc
│  │     │  │     ├─ test_files.cpython-39.pyc
│  │     │  │     ├─ test_open.cpython-39.pyc
│  │     │  │     ├─ test_path.cpython-39.pyc
│  │     │  │     ├─ test_read.cpython-39.pyc
│  │     │  │     ├─ test_reader.cpython-39.pyc
│  │     │  │     ├─ test_resource.cpython-39.pyc
│  │     │  │     ├─ update-zips.cpython-39.pyc
│  │     │  │     ├─ util.cpython-39.pyc
│  │     │  │     ├─ _compat.cpython-39.pyc
│  │     │  │     ├─ _path.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _adapters.py
│  │     │  ├─ _common.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _itertools.py
│  │     │  ├─ _legacy.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ abc.cpython-39.pyc
│  │     │     ├─ readers.cpython-39.pyc
│  │     │     ├─ simple.cpython-39.pyc
│  │     │     ├─ _adapters.cpython-39.pyc
│  │     │     ├─ _common.cpython-39.pyc
│  │     │     ├─ _compat.cpython-39.pyc
│  │     │     ├─ _itertools.cpython-39.pyc
│  │     │     ├─ _legacy.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ importlib_resources-5.12.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ inflect
│  │     │  ├─ py.typed
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ inflect-5.6.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ ipykernel
│  │     │  ├─ comm
│  │     │  │  ├─ comm.py
│  │     │  │  ├─ manager.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ comm.cpython-39.pyc
│  │     │  │     ├─ manager.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ compiler.py
│  │     │  ├─ connect.py
│  │     │  ├─ control.py
│  │     │  ├─ datapub.py
│  │     │  ├─ debugger.py
│  │     │  ├─ displayhook.py
│  │     │  ├─ embed.py
│  │     │  ├─ eventloops.py
│  │     │  ├─ gui
│  │     │  │  ├─ gtk3embed.py
│  │     │  │  ├─ gtkembed.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ gtk3embed.cpython-39.pyc
│  │     │  │     ├─ gtkembed.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ heartbeat.py
│  │     │  ├─ inprocess
│  │     │  │  ├─ blocking.py
│  │     │  │  ├─ channels.py
│  │     │  │  ├─ client.py
│  │     │  │  ├─ constants.py
│  │     │  │  ├─ ipkernel.py
│  │     │  │  ├─ manager.py
│  │     │  │  ├─ socket.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_kernel.py
│  │     │  │  │  ├─ test_kernelmanager.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_kernel.cpython-39.pyc
│  │     │  │  │     ├─ test_kernelmanager.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ blocking.cpython-39.pyc
│  │     │  │     ├─ channels.cpython-39.pyc
│  │     │  │     ├─ client.cpython-39.pyc
│  │     │  │     ├─ constants.cpython-39.pyc
│  │     │  │     ├─ ipkernel.cpython-39.pyc
│  │     │  │     ├─ manager.cpython-39.pyc
│  │     │  │     ├─ socket.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ iostream.py
│  │     │  ├─ ipkernel.py
│  │     │  ├─ jsonutil.py
│  │     │  ├─ kernelapp.py
│  │     │  ├─ kernelbase.py
│  │     │  ├─ kernelspec.py
│  │     │  ├─ log.py
│  │     │  ├─ parentpoller.py
│  │     │  ├─ pickleutil.py
│  │     │  ├─ py.typed
│  │     │  ├─ pylab
│  │     │  │  ├─ backend_inline.py
│  │     │  │  ├─ config.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ backend_inline.cpython-39.pyc
│  │     │  │     ├─ config.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ resources
│  │     │  │  ├─ logo-32x32.png
│  │     │  │  ├─ logo-64x64.png
│  │     │  │  └─ logo-svg.svg
│  │     │  ├─ serialize.py
│  │     │  ├─ tests
│  │     │  │  ├─ conftest.py
│  │     │  │  ├─ test_async.py
│  │     │  │  ├─ test_comm.py
│  │     │  │  ├─ test_connect.py
│  │     │  │  ├─ test_debugger.py
│  │     │  │  ├─ test_embed_kernel.py
│  │     │  │  ├─ test_eventloop.py
│  │     │  │  ├─ test_heartbeat.py
│  │     │  │  ├─ test_io.py
│  │     │  │  ├─ test_ipkernel_direct.py
│  │     │  │  ├─ test_jsonutil.py
│  │     │  │  ├─ test_kernel.py
│  │     │  │  ├─ test_kernelapp.py
│  │     │  │  ├─ test_kernelspec.py
│  │     │  │  ├─ test_kernel_direct.py
│  │     │  │  ├─ test_message_spec.py
│  │     │  │  ├─ test_parentpoller.py
│  │     │  │  ├─ test_pickleutil.py
│  │     │  │  ├─ test_start_kernel.py
│  │     │  │  ├─ test_zmq_shell.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ _asyncio_utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ conftest.cpython-39.pyc
│  │     │  │     ├─ test_async.cpython-39.pyc
│  │     │  │     ├─ test_comm.cpython-39.pyc
│  │     │  │     ├─ test_connect.cpython-39.pyc
│  │     │  │     ├─ test_debugger.cpython-39.pyc
│  │     │  │     ├─ test_embed_kernel.cpython-39.pyc
│  │     │  │     ├─ test_eventloop.cpython-39.pyc
│  │     │  │     ├─ test_heartbeat.cpython-39.pyc
│  │     │  │     ├─ test_io.cpython-39.pyc
│  │     │  │     ├─ test_ipkernel_direct.cpython-39.pyc
│  │     │  │     ├─ test_jsonutil.cpython-39.pyc
│  │     │  │     ├─ test_kernel.cpython-39.pyc
│  │     │  │     ├─ test_kernelapp.cpython-39.pyc
│  │     │  │     ├─ test_kernelspec.cpython-39.pyc
│  │     │  │     ├─ test_kernel_direct.cpython-39.pyc
│  │     │  │     ├─ test_message_spec.cpython-39.pyc
│  │     │  │     ├─ test_parentpoller.cpython-39.pyc
│  │     │  │     ├─ test_pickleutil.cpython-39.pyc
│  │     │  │     ├─ test_start_kernel.cpython-39.pyc
│  │     │  │     ├─ test_zmq_shell.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     ├─ _asyncio_utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ trio_runner.py
│  │     │  ├─ zmqshell.py
│  │     │  ├─ _eventloop_macos.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ compiler.cpython-39.pyc
│  │     │     ├─ connect.cpython-39.pyc
│  │     │     ├─ control.cpython-39.pyc
│  │     │     ├─ datapub.cpython-39.pyc
│  │     │     ├─ debugger.cpython-39.pyc
│  │     │     ├─ displayhook.cpython-39.pyc
│  │     │     ├─ embed.cpython-39.pyc
│  │     │     ├─ eventloops.cpython-39.pyc
│  │     │     ├─ heartbeat.cpython-39.pyc
│  │     │     ├─ iostream.cpython-39.pyc
│  │     │     ├─ ipkernel.cpython-39.pyc
│  │     │     ├─ jsonutil.cpython-39.pyc
│  │     │     ├─ kernelapp.cpython-39.pyc
│  │     │     ├─ kernelbase.cpython-39.pyc
│  │     │     ├─ kernelspec.cpython-39.pyc
│  │     │     ├─ log.cpython-39.pyc
│  │     │     ├─ parentpoller.cpython-39.pyc
│  │     │     ├─ pickleutil.cpython-39.pyc
│  │     │     ├─ serialize.cpython-39.pyc
│  │     │     ├─ trio_runner.cpython-39.pyc
│  │     │     ├─ zmqshell.cpython-39.pyc
│  │     │     ├─ _eventloop_macos.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ ipykernel-6.22.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ ipykernel_launcher.py
│  │     ├─ IPython
│  │     │  ├─ conftest.py
│  │     │  ├─ consoleapp.py
│  │     │  ├─ core
│  │     │  │  ├─ alias.py
│  │     │  │  ├─ application.py
│  │     │  │  ├─ async_helpers.py
│  │     │  │  ├─ autocall.py
│  │     │  │  ├─ builtin_trap.py
│  │     │  │  ├─ compilerop.py
│  │     │  │  ├─ completer.py
│  │     │  │  ├─ completerlib.py
│  │     │  │  ├─ crashhandler.py
│  │     │  │  ├─ debugger.py
│  │     │  │  ├─ display.py
│  │     │  │  ├─ displayhook.py
│  │     │  │  ├─ displaypub.py
│  │     │  │  ├─ display_functions.py
│  │     │  │  ├─ display_trap.py
│  │     │  │  ├─ error.py
│  │     │  │  ├─ events.py
│  │     │  │  ├─ excolors.py
│  │     │  │  ├─ extensions.py
│  │     │  │  ├─ formatters.py
│  │     │  │  ├─ getipython.py
│  │     │  │  ├─ guarded_eval.py
│  │     │  │  ├─ history.py
│  │     │  │  ├─ historyapp.py
│  │     │  │  ├─ inputsplitter.py
│  │     │  │  ├─ inputtransformer.py
│  │     │  │  ├─ inputtransformer2.py
│  │     │  │  ├─ interactiveshell.py
│  │     │  │  ├─ latex_symbols.py
│  │     │  │  ├─ logger.py
│  │     │  │  ├─ macro.py
│  │     │  │  ├─ magic.py
│  │     │  │  ├─ magics
│  │     │  │  │  ├─ auto.py
│  │     │  │  │  ├─ basic.py
│  │     │  │  │  ├─ code.py
│  │     │  │  │  ├─ config.py
│  │     │  │  │  ├─ display.py
│  │     │  │  │  ├─ execution.py
│  │     │  │  │  ├─ extension.py
│  │     │  │  │  ├─ history.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ namespace.py
│  │     │  │  │  ├─ osm.py
│  │     │  │  │  ├─ packaging.py
│  │     │  │  │  ├─ pylab.py
│  │     │  │  │  ├─ script.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ auto.cpython-39.pyc
│  │     │  │  │     ├─ basic.cpython-39.pyc
│  │     │  │  │     ├─ code.cpython-39.pyc
│  │     │  │  │     ├─ config.cpython-39.pyc
│  │     │  │  │     ├─ display.cpython-39.pyc
│  │     │  │  │     ├─ execution.cpython-39.pyc
│  │     │  │  │     ├─ extension.cpython-39.pyc
│  │     │  │  │     ├─ history.cpython-39.pyc
│  │     │  │  │     ├─ logging.cpython-39.pyc
│  │     │  │  │     ├─ namespace.cpython-39.pyc
│  │     │  │  │     ├─ osm.cpython-39.pyc
│  │     │  │  │     ├─ packaging.cpython-39.pyc
│  │     │  │  │     ├─ pylab.cpython-39.pyc
│  │     │  │  │     ├─ script.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ magic_arguments.py
│  │     │  │  ├─ oinspect.py
│  │     │  │  ├─ page.py
│  │     │  │  ├─ payload.py
│  │     │  │  ├─ payloadpage.py
│  │     │  │  ├─ prefilter.py
│  │     │  │  ├─ profile
│  │     │  │  │  └─ README_STARTUP
│  │     │  │  ├─ profileapp.py
│  │     │  │  ├─ profiledir.py
│  │     │  │  ├─ prompts.py
│  │     │  │  ├─ pylabtools.py
│  │     │  │  ├─ release.py
│  │     │  │  ├─ shellapp.py
│  │     │  │  ├─ splitinput.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ 2x2.jpg
│  │     │  │  │  ├─ 2x2.png
│  │     │  │  │  ├─ bad_all.py
│  │     │  │  │  ├─ daft_extension
│  │     │  │  │  │  ├─ daft_extension.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ daft_extension.cpython-39.pyc
│  │     │  │  │  ├─ nonascii.py
│  │     │  │  │  ├─ nonascii2.py
│  │     │  │  │  ├─ print_argv.py
│  │     │  │  │  ├─ refbug.py
│  │     │  │  │  ├─ simpleerr.py
│  │     │  │  │  ├─ tclass.py
│  │     │  │  │  ├─ test_alias.py
│  │     │  │  │  ├─ test_application.py
│  │     │  │  │  ├─ test_async_helpers.py
│  │     │  │  │  ├─ test_autocall.py
│  │     │  │  │  ├─ test_compilerop.py
│  │     │  │  │  ├─ test_completer.py
│  │     │  │  │  ├─ test_completerlib.py
│  │     │  │  │  ├─ test_debugger.py
│  │     │  │  │  ├─ test_display.py
│  │     │  │  │  ├─ test_displayhook.py
│  │     │  │  │  ├─ test_events.py
│  │     │  │  │  ├─ test_extension.py
│  │     │  │  │  ├─ test_formatters.py
│  │     │  │  │  ├─ test_guarded_eval.py
│  │     │  │  │  ├─ test_handlers.py
│  │     │  │  │  ├─ test_history.py
│  │     │  │  │  ├─ test_imports.py
│  │     │  │  │  ├─ test_inputsplitter.py
│  │     │  │  │  ├─ test_inputtransformer.py
│  │     │  │  │  ├─ test_inputtransformer2.py
│  │     │  │  │  ├─ test_inputtransformer2_line.py
│  │     │  │  │  ├─ test_interactiveshell.py
│  │     │  │  │  ├─ test_iplib.py
│  │     │  │  │  ├─ test_logger.py
│  │     │  │  │  ├─ test_magic.py
│  │     │  │  │  ├─ test_magic_arguments.py
│  │     │  │  │  ├─ test_magic_terminal.py
│  │     │  │  │  ├─ test_oinspect.py
│  │     │  │  │  ├─ test_page.py
│  │     │  │  │  ├─ test_paths.py
│  │     │  │  │  ├─ test_prefilter.py
│  │     │  │  │  ├─ test_profile.py
│  │     │  │  │  ├─ test_prompts.py
│  │     │  │  │  ├─ test_pylabtools.py
│  │     │  │  │  ├─ test_run.py
│  │     │  │  │  ├─ test_shellapp.py
│  │     │  │  │  ├─ test_splitinput.py
│  │     │  │  │  ├─ test_ultratb.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bad_all.cpython-39.pyc
│  │     │  │  │     ├─ nonascii.cpython-39.pyc
│  │     │  │  │     ├─ nonascii2.cpython-39.pyc
│  │     │  │  │     ├─ print_argv.cpython-39.pyc
│  │     │  │  │     ├─ refbug.cpython-39.pyc
│  │     │  │  │     ├─ simpleerr.cpython-39.pyc
│  │     │  │  │     ├─ tclass.cpython-39.pyc
│  │     │  │  │     ├─ test_alias.cpython-39.pyc
│  │     │  │  │     ├─ test_application.cpython-39.pyc
│  │     │  │  │     ├─ test_async_helpers.cpython-39.pyc
│  │     │  │  │     ├─ test_autocall.cpython-39.pyc
│  │     │  │  │     ├─ test_compilerop.cpython-39.pyc
│  │     │  │  │     ├─ test_completer.cpython-39.pyc
│  │     │  │  │     ├─ test_completerlib.cpython-39.pyc
│  │     │  │  │     ├─ test_debugger.cpython-39.pyc
│  │     │  │  │     ├─ test_display.cpython-39.pyc
│  │     │  │  │     ├─ test_displayhook.cpython-39.pyc
│  │     │  │  │     ├─ test_events.cpython-39.pyc
│  │     │  │  │     ├─ test_extension.cpython-39.pyc
│  │     │  │  │     ├─ test_formatters.cpython-39.pyc
│  │     │  │  │     ├─ test_guarded_eval.cpython-39.pyc
│  │     │  │  │     ├─ test_handlers.cpython-39.pyc
│  │     │  │  │     ├─ test_history.cpython-39.pyc
│  │     │  │  │     ├─ test_imports.cpython-39.pyc
│  │     │  │  │     ├─ test_inputsplitter.cpython-39.pyc
│  │     │  │  │     ├─ test_inputtransformer.cpython-39.pyc
│  │     │  │  │     ├─ test_inputtransformer2.cpython-39.pyc
│  │     │  │  │     ├─ test_inputtransformer2_line.cpython-39.pyc
│  │     │  │  │     ├─ test_interactiveshell.cpython-39.pyc
│  │     │  │  │     ├─ test_iplib.cpython-39.pyc
│  │     │  │  │     ├─ test_logger.cpython-39.pyc
│  │     │  │  │     ├─ test_magic.cpython-39.pyc
│  │     │  │  │     ├─ test_magic_arguments.cpython-39.pyc
│  │     │  │  │     ├─ test_magic_terminal.cpython-39.pyc
│  │     │  │  │     ├─ test_oinspect.cpython-39.pyc
│  │     │  │  │     ├─ test_page.cpython-39.pyc
│  │     │  │  │     ├─ test_paths.cpython-39.pyc
│  │     │  │  │     ├─ test_prefilter.cpython-39.pyc
│  │     │  │  │     ├─ test_profile.cpython-39.pyc
│  │     │  │  │     ├─ test_prompts.cpython-39.pyc
│  │     │  │  │     ├─ test_pylabtools.cpython-39.pyc
│  │     │  │  │     ├─ test_run.cpython-39.pyc
│  │     │  │  │     ├─ test_shellapp.cpython-39.pyc
│  │     │  │  │     ├─ test_splitinput.cpython-39.pyc
│  │     │  │  │     ├─ test_ultratb.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ ultratb.py
│  │     │  │  ├─ usage.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ alias.cpython-39.pyc
│  │     │  │     ├─ application.cpython-39.pyc
│  │     │  │     ├─ async_helpers.cpython-39.pyc
│  │     │  │     ├─ autocall.cpython-39.pyc
│  │     │  │     ├─ builtin_trap.cpython-39.pyc
│  │     │  │     ├─ compilerop.cpython-39.pyc
│  │     │  │     ├─ completer.cpython-39.pyc
│  │     │  │     ├─ completerlib.cpython-39.pyc
│  │     │  │     ├─ crashhandler.cpython-39.pyc
│  │     │  │     ├─ debugger.cpython-39.pyc
│  │     │  │     ├─ display.cpython-39.pyc
│  │     │  │     ├─ displayhook.cpython-39.pyc
│  │     │  │     ├─ displaypub.cpython-39.pyc
│  │     │  │     ├─ display_functions.cpython-39.pyc
│  │     │  │     ├─ display_trap.cpython-39.pyc
│  │     │  │     ├─ error.cpython-39.pyc
│  │     │  │     ├─ events.cpython-39.pyc
│  │     │  │     ├─ excolors.cpython-39.pyc
│  │     │  │     ├─ extensions.cpython-39.pyc
│  │     │  │     ├─ formatters.cpython-39.pyc
│  │     │  │     ├─ getipython.cpython-39.pyc
│  │     │  │     ├─ guarded_eval.cpython-39.pyc
│  │     │  │     ├─ history.cpython-39.pyc
│  │     │  │     ├─ historyapp.cpython-39.pyc
│  │     │  │     ├─ inputsplitter.cpython-39.pyc
│  │     │  │     ├─ inputtransformer.cpython-39.pyc
│  │     │  │     ├─ inputtransformer2.cpython-39.pyc
│  │     │  │     ├─ interactiveshell.cpython-39.pyc
│  │     │  │     ├─ latex_symbols.cpython-39.pyc
│  │     │  │     ├─ logger.cpython-39.pyc
│  │     │  │     ├─ macro.cpython-39.pyc
│  │     │  │     ├─ magic.cpython-39.pyc
│  │     │  │     ├─ magic_arguments.cpython-39.pyc
│  │     │  │     ├─ oinspect.cpython-39.pyc
│  │     │  │     ├─ page.cpython-39.pyc
│  │     │  │     ├─ payload.cpython-39.pyc
│  │     │  │     ├─ payloadpage.cpython-39.pyc
│  │     │  │     ├─ prefilter.cpython-39.pyc
│  │     │  │     ├─ profileapp.cpython-39.pyc
│  │     │  │     ├─ profiledir.cpython-39.pyc
│  │     │  │     ├─ prompts.cpython-39.pyc
│  │     │  │     ├─ pylabtools.cpython-39.pyc
│  │     │  │     ├─ release.cpython-39.pyc
│  │     │  │     ├─ shellapp.cpython-39.pyc
│  │     │  │     ├─ splitinput.cpython-39.pyc
│  │     │  │     ├─ ultratb.cpython-39.pyc
│  │     │  │     ├─ usage.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ display.py
│  │     │  ├─ extensions
│  │     │  │  ├─ autoreload.py
│  │     │  │  ├─ storemagic.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_autoreload.py
│  │     │  │  │  ├─ test_storemagic.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_autoreload.cpython-39.pyc
│  │     │  │  │     ├─ test_storemagic.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ autoreload.cpython-39.pyc
│  │     │  │     ├─ storemagic.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ external
│  │     │  │  ├─ qt_for_kernel.py
│  │     │  │  ├─ qt_loaders.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_qt_loaders.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_qt_loaders.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ qt_for_kernel.cpython-39.pyc
│  │     │  │     ├─ qt_loaders.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ lib
│  │     │  │  ├─ backgroundjobs.py
│  │     │  │  ├─ clipboard.py
│  │     │  │  ├─ deepreload.py
│  │     │  │  ├─ demo.py
│  │     │  │  ├─ display.py
│  │     │  │  ├─ guisupport.py
│  │     │  │  ├─ latextools.py
│  │     │  │  ├─ lexers.py
│  │     │  │  ├─ pretty.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test.wav
│  │     │  │  │  ├─ test_backgroundjobs.py
│  │     │  │  │  ├─ test_clipboard.py
│  │     │  │  │  ├─ test_deepreload.py
│  │     │  │  │  ├─ test_display.py
│  │     │  │  │  ├─ test_imports.py
│  │     │  │  │  ├─ test_latextools.py
│  │     │  │  │  ├─ test_lexers.py
│  │     │  │  │  ├─ test_pretty.py
│  │     │  │  │  ├─ test_pygments.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_backgroundjobs.cpython-39.pyc
│  │     │  │  │     ├─ test_clipboard.cpython-39.pyc
│  │     │  │  │     ├─ test_deepreload.cpython-39.pyc
│  │     │  │  │     ├─ test_display.cpython-39.pyc
│  │     │  │  │     ├─ test_imports.cpython-39.pyc
│  │     │  │  │     ├─ test_latextools.cpython-39.pyc
│  │     │  │  │     ├─ test_lexers.cpython-39.pyc
│  │     │  │  │     ├─ test_pretty.cpython-39.pyc
│  │     │  │  │     ├─ test_pygments.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ backgroundjobs.cpython-39.pyc
│  │     │  │     ├─ clipboard.cpython-39.pyc
│  │     │  │     ├─ deepreload.cpython-39.pyc
│  │     │  │     ├─ demo.cpython-39.pyc
│  │     │  │     ├─ display.cpython-39.pyc
│  │     │  │     ├─ guisupport.cpython-39.pyc
│  │     │  │     ├─ latextools.cpython-39.pyc
│  │     │  │     ├─ lexers.cpython-39.pyc
│  │     │  │     ├─ pretty.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ paths.py
│  │     │  ├─ py.typed
│  │     │  ├─ sphinxext
│  │     │  │  ├─ custom_doctests.py
│  │     │  │  ├─ ipython_console_highlighting.py
│  │     │  │  ├─ ipython_directive.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ custom_doctests.cpython-39.pyc
│  │     │  │     ├─ ipython_console_highlighting.cpython-39.pyc
│  │     │  │     ├─ ipython_directive.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ terminal
│  │     │  │  ├─ console.py
│  │     │  │  ├─ debugger.py
│  │     │  │  ├─ embed.py
│  │     │  │  ├─ interactiveshell.py
│  │     │  │  ├─ ipapp.py
│  │     │  │  ├─ magics.py
│  │     │  │  ├─ prompts.py
│  │     │  │  ├─ ptutils.py
│  │     │  │  ├─ shortcuts
│  │     │  │  │  ├─ auto_match.py
│  │     │  │  │  ├─ auto_suggest.py
│  │     │  │  │  ├─ filters.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ auto_match.cpython-39.pyc
│  │     │  │  │     ├─ auto_suggest.cpython-39.pyc
│  │     │  │  │     ├─ filters.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_debug_magic.py
│  │     │  │  │  ├─ test_embed.py
│  │     │  │  │  ├─ test_help.py
│  │     │  │  │  ├─ test_interactivshell.py
│  │     │  │  │  ├─ test_shortcuts.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_debug_magic.cpython-39.pyc
│  │     │  │  │     ├─ test_embed.cpython-39.pyc
│  │     │  │  │     ├─ test_help.cpython-39.pyc
│  │     │  │  │     ├─ test_interactivshell.cpython-39.pyc
│  │     │  │  │     ├─ test_shortcuts.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ console.cpython-39.pyc
│  │     │  │     ├─ debugger.cpython-39.pyc
│  │     │  │     ├─ embed.cpython-39.pyc
│  │     │  │     ├─ interactiveshell.cpython-39.pyc
│  │     │  │     ├─ ipapp.cpython-39.pyc
│  │     │  │     ├─ magics.cpython-39.pyc
│  │     │  │     ├─ prompts.cpython-39.pyc
│  │     │  │     ├─ ptutils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ testing
│  │     │  │  ├─ decorators.py
│  │     │  │  ├─ globalipapp.py
│  │     │  │  ├─ ipunittest.py
│  │     │  │  ├─ plugin
│  │     │  │  │  ├─ dtexample.py
│  │     │  │  │  ├─ ipdoctest.py
│  │     │  │  │  ├─ pytest_ipdoctest.py
│  │     │  │  │  ├─ README.txt
│  │     │  │  │  ├─ setup.py
│  │     │  │  │  ├─ simple.py
│  │     │  │  │  ├─ simplevars.py
│  │     │  │  │  ├─ test_combo.txt
│  │     │  │  │  ├─ test_example.txt
│  │     │  │  │  ├─ test_exampleip.txt
│  │     │  │  │  ├─ test_ipdoctest.py
│  │     │  │  │  ├─ test_refs.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ dtexample.cpython-39.pyc
│  │     │  │  │     ├─ ipdoctest.cpython-39.pyc
│  │     │  │  │     ├─ pytest_ipdoctest.cpython-39.pyc
│  │     │  │  │     ├─ setup.cpython-39.pyc
│  │     │  │  │     ├─ simple.cpython-39.pyc
│  │     │  │  │     ├─ simplevars.cpython-39.pyc
│  │     │  │  │     ├─ test_ipdoctest.cpython-39.pyc
│  │     │  │  │     ├─ test_refs.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ skipdoctest.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_decorators.py
│  │     │  │  │  ├─ test_ipunittest.py
│  │     │  │  │  ├─ test_tools.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_decorators.cpython-39.pyc
│  │     │  │  │     ├─ test_ipunittest.cpython-39.pyc
│  │     │  │  │     ├─ test_tools.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ tools.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ decorators.cpython-39.pyc
│  │     │  │     ├─ globalipapp.cpython-39.pyc
│  │     │  │     ├─ ipunittest.cpython-39.pyc
│  │     │  │     ├─ skipdoctest.cpython-39.pyc
│  │     │  │     ├─ tools.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ utils
│  │     │  │  ├─ capture.py
│  │     │  │  ├─ colorable.py
│  │     │  │  ├─ coloransi.py
│  │     │  │  ├─ contexts.py
│  │     │  │  ├─ daemonize.py
│  │     │  │  ├─ data.py
│  │     │  │  ├─ decorators.py
│  │     │  │  ├─ dir2.py
│  │     │  │  ├─ docs.py
│  │     │  │  ├─ encoding.py
│  │     │  │  ├─ eventful.py
│  │     │  │  ├─ frame.py
│  │     │  │  ├─ generics.py
│  │     │  │  ├─ importstring.py
│  │     │  │  ├─ io.py
│  │     │  │  ├─ ipstruct.py
│  │     │  │  ├─ jsonutil.py
│  │     │  │  ├─ localinterfaces.py
│  │     │  │  ├─ log.py
│  │     │  │  ├─ module_paths.py
│  │     │  │  ├─ openpy.py
│  │     │  │  ├─ path.py
│  │     │  │  ├─ process.py
│  │     │  │  ├─ py3compat.py
│  │     │  │  ├─ PyColorize.py
│  │     │  │  ├─ sentinel.py
│  │     │  │  ├─ shimmodule.py
│  │     │  │  ├─ signatures.py
│  │     │  │  ├─ strdispatch.py
│  │     │  │  ├─ sysinfo.py
│  │     │  │  ├─ syspathcontext.py
│  │     │  │  ├─ tempdir.py
│  │     │  │  ├─ terminal.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_capture.py
│  │     │  │  │  ├─ test_decorators.py
│  │     │  │  │  ├─ test_deprecated.py
│  │     │  │  │  ├─ test_dir2.py
│  │     │  │  │  ├─ test_imports.py
│  │     │  │  │  ├─ test_importstring.py
│  │     │  │  │  ├─ test_io.py
│  │     │  │  │  ├─ test_module_paths.py
│  │     │  │  │  ├─ test_openpy.py
│  │     │  │  │  ├─ test_path.py
│  │     │  │  │  ├─ test_process.py
│  │     │  │  │  ├─ test_pycolorize.py
│  │     │  │  │  ├─ test_shimmodule.py
│  │     │  │  │  ├─ test_sysinfo.py
│  │     │  │  │  ├─ test_tempdir.py
│  │     │  │  │  ├─ test_text.py
│  │     │  │  │  ├─ test_tokenutil.py
│  │     │  │  │  ├─ test_wildcard.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_capture.cpython-39.pyc
│  │     │  │  │     ├─ test_decorators.cpython-39.pyc
│  │     │  │  │     ├─ test_deprecated.cpython-39.pyc
│  │     │  │  │     ├─ test_dir2.cpython-39.pyc
│  │     │  │  │     ├─ test_imports.cpython-39.pyc
│  │     │  │  │     ├─ test_importstring.cpython-39.pyc
│  │     │  │  │     ├─ test_io.cpython-39.pyc
│  │     │  │  │     ├─ test_module_paths.cpython-39.pyc
│  │     │  │  │     ├─ test_openpy.cpython-39.pyc
│  │     │  │  │     ├─ test_path.cpython-39.pyc
│  │     │  │  │     ├─ test_process.cpython-39.pyc
│  │     │  │  │     ├─ test_pycolorize.cpython-39.pyc
│  │     │  │  │     ├─ test_shimmodule.cpython-39.pyc
│  │     │  │  │     ├─ test_sysinfo.cpython-39.pyc
│  │     │  │  │     ├─ test_tempdir.cpython-39.pyc
│  │     │  │  │     ├─ test_text.cpython-39.pyc
│  │     │  │  │     ├─ test_tokenutil.cpython-39.pyc
│  │     │  │  │     ├─ test_wildcard.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ text.py
│  │     │  │  ├─ timing.py
│  │     │  │  ├─ tokenutil.py
│  │     │  │  ├─ traitlets.py
│  │     │  │  ├─ tz.py
│  │     │  │  ├─ ulinecache.py
│  │     │  │  ├─ version.py
│  │     │  │  ├─ wildcard.py
│  │     │  │  ├─ _process_cli.py
│  │     │  │  ├─ _process_common.py
│  │     │  │  ├─ _process_posix.py
│  │     │  │  ├─ _process_win32.py
│  │     │  │  ├─ _process_win32_controller.py
│  │     │  │  ├─ _sysinfo.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ capture.cpython-39.pyc
│  │     │  │     ├─ colorable.cpython-39.pyc
│  │     │  │     ├─ coloransi.cpython-39.pyc
│  │     │  │     ├─ contexts.cpython-39.pyc
│  │     │  │     ├─ daemonize.cpython-39.pyc
│  │     │  │     ├─ data.cpython-39.pyc
│  │     │  │     ├─ decorators.cpython-39.pyc
│  │     │  │     ├─ dir2.cpython-39.pyc
│  │     │  │     ├─ docs.cpython-39.pyc
│  │     │  │     ├─ encoding.cpython-39.pyc
│  │     │  │     ├─ eventful.cpython-39.pyc
│  │     │  │     ├─ frame.cpython-39.pyc
│  │     │  │     ├─ generics.cpython-39.pyc
│  │     │  │     ├─ importstring.cpython-39.pyc
│  │     │  │     ├─ io.cpython-39.pyc
│  │     │  │     ├─ ipstruct.cpython-39.pyc
│  │     │  │     ├─ jsonutil.cpython-39.pyc
│  │     │  │     ├─ localinterfaces.cpython-39.pyc
│  │     │  │     ├─ log.cpython-39.pyc
│  │     │  │     ├─ module_paths.cpython-39.pyc
│  │     │  │     ├─ openpy.cpython-39.pyc
│  │     │  │     ├─ path.cpython-39.pyc
│  │     │  │     ├─ process.cpython-39.pyc
│  │     │  │     ├─ py3compat.cpython-39.pyc
│  │     │  │     ├─ PyColorize.cpython-39.pyc
│  │     │  │     ├─ sentinel.cpython-39.pyc
│  │     │  │     ├─ shimmodule.cpython-39.pyc
│  │     │  │     ├─ signatures.cpython-39.pyc
│  │     │  │     ├─ strdispatch.cpython-39.pyc
│  │     │  │     ├─ sysinfo.cpython-39.pyc
│  │     │  │     ├─ syspathcontext.cpython-39.pyc
│  │     │  │     ├─ tempdir.cpython-39.pyc
│  │     │  │     ├─ terminal.cpython-39.pyc
│  │     │  │     ├─ text.cpython-39.pyc
│  │     │  │     ├─ timing.cpython-39.pyc
│  │     │  │     ├─ tokenutil.cpython-39.pyc
│  │     │  │     ├─ traitlets.cpython-39.pyc
│  │     │  │     ├─ tz.cpython-39.pyc
│  │     │  │     ├─ ulinecache.cpython-39.pyc
│  │     │  │     ├─ version.cpython-39.pyc
│  │     │  │     ├─ wildcard.cpython-39.pyc
│  │     │  │     ├─ _process_cli.cpython-39.pyc
│  │     │  │     ├─ _process_common.cpython-39.pyc
│  │     │  │     ├─ _process_posix.cpython-39.pyc
│  │     │  │     ├─ _process_win32.cpython-39.pyc
│  │     │  │     ├─ _process_win32_controller.cpython-39.pyc
│  │     │  │     ├─ _sysinfo.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ conftest.cpython-39.pyc
│  │     │     ├─ consoleapp.cpython-39.pyc
│  │     │     ├─ display.cpython-39.pyc
│  │     │     ├─ paths.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ ipython-8.12.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ isapi
│  │     │  ├─ doc
│  │     │  │  └─ isapi.html
│  │     │  ├─ install.py
│  │     │  ├─ isapicon.py
│  │     │  ├─ PyISAPI_loader.dll
│  │     │  ├─ README.txt
│  │     │  ├─ samples
│  │     │  │  ├─ advanced.py
│  │     │  │  ├─ README.txt
│  │     │  │  ├─ redirector.py
│  │     │  │  ├─ redirector_asynch.py
│  │     │  │  ├─ redirector_with_filter.py
│  │     │  │  ├─ test.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ advanced.cpython-39.pyc
│  │     │  │     ├─ redirector.cpython-39.pyc
│  │     │  │     ├─ redirector_asynch.cpython-39.pyc
│  │     │  │     ├─ redirector_with_filter.cpython-39.pyc
│  │     │  │     └─ test.cpython-39.pyc
│  │     │  ├─ simple.py
│  │     │  ├─ test
│  │     │  │  ├─ extension_simple.py
│  │     │  │  ├─ README.txt
│  │     │  │  └─ __pycache__
│  │     │  │     └─ extension_simple.cpython-39.pyc
│  │     │  ├─ threaded_extension.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ install.cpython-39.pyc
│  │     │     ├─ isapicon.cpython-39.pyc
│  │     │     ├─ simple.cpython-39.pyc
│  │     │     ├─ threaded_extension.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ isort
│  │     │  ├─ api.py
│  │     │  ├─ comments.py
│  │     │  ├─ core.py
│  │     │  ├─ deprecated
│  │     │  │  ├─ finders.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ finders.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ exceptions.py
│  │     │  ├─ files.py
│  │     │  ├─ format.py
│  │     │  ├─ identify.py
│  │     │  ├─ io.py
│  │     │  ├─ literal.py
│  │     │  ├─ logo.py
│  │     │  ├─ main.py
│  │     │  ├─ output.py
│  │     │  ├─ parse.py
│  │     │  ├─ place.py
│  │     │  ├─ profiles.py
│  │     │  ├─ py.typed
│  │     │  ├─ pylama_isort.py
│  │     │  ├─ sections.py
│  │     │  ├─ settings.py
│  │     │  ├─ setuptools_commands.py
│  │     │  ├─ sorting.py
│  │     │  ├─ stdlibs
│  │     │  │  ├─ all.py
│  │     │  │  ├─ py2.py
│  │     │  │  ├─ py27.py
│  │     │  │  ├─ py3.py
│  │     │  │  ├─ py310.py
│  │     │  │  ├─ py311.py
│  │     │  │  ├─ py36.py
│  │     │  │  ├─ py37.py
│  │     │  │  ├─ py38.py
│  │     │  │  ├─ py39.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ all.cpython-39.pyc
│  │     │  │     ├─ py2.cpython-39.pyc
│  │     │  │     ├─ py27.cpython-39.pyc
│  │     │  │     ├─ py3.cpython-39.pyc
│  │     │  │     ├─ py310.cpython-39.pyc
│  │     │  │     ├─ py311.cpython-39.pyc
│  │     │  │     ├─ py36.cpython-39.pyc
│  │     │  │     ├─ py37.cpython-39.pyc
│  │     │  │     ├─ py38.cpython-39.pyc
│  │     │  │     ├─ py39.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ utils.py
│  │     │  ├─ wrap.py
│  │     │  ├─ wrap_modes.py
│  │     │  ├─ _vendored
│  │     │  │  └─ tomli
│  │     │  │     ├─ LICENSE
│  │     │  │     ├─ py.typed
│  │     │  │     ├─ _parser.py
│  │     │  │     ├─ _re.py
│  │     │  │     ├─ __init__.py
│  │     │  │     └─ __pycache__
│  │     │  │        ├─ _parser.cpython-39.pyc
│  │     │  │        ├─ _re.cpython-39.pyc
│  │     │  │        └─ __init__.cpython-39.pyc
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ api.cpython-39.pyc
│  │     │     ├─ comments.cpython-39.pyc
│  │     │     ├─ core.cpython-39.pyc
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ files.cpython-39.pyc
│  │     │     ├─ format.cpython-39.pyc
│  │     │     ├─ identify.cpython-39.pyc
│  │     │     ├─ io.cpython-39.pyc
│  │     │     ├─ literal.cpython-39.pyc
│  │     │     ├─ logo.cpython-39.pyc
│  │     │     ├─ main.cpython-39.pyc
│  │     │     ├─ output.cpython-39.pyc
│  │     │     ├─ parse.cpython-39.pyc
│  │     │     ├─ place.cpython-39.pyc
│  │     │     ├─ profiles.cpython-39.pyc
│  │     │     ├─ pylama_isort.cpython-39.pyc
│  │     │     ├─ sections.cpython-39.pyc
│  │     │     ├─ settings.cpython-39.pyc
│  │     │     ├─ setuptools_commands.cpython-39.pyc
│  │     │     ├─ sorting.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ wrap.cpython-39.pyc
│  │     │     ├─ wrap_modes.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ isort-5.12.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ jedi
│  │     │  ├─ api
│  │     │  │  ├─ classes.py
│  │     │  │  ├─ completion.py
│  │     │  │  ├─ completion_cache.py
│  │     │  │  ├─ environment.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ file_name.py
│  │     │  │  ├─ helpers.py
│  │     │  │  ├─ interpreter.py
│  │     │  │  ├─ keywords.py
│  │     │  │  ├─ project.py
│  │     │  │  ├─ refactoring
│  │     │  │  │  ├─ extract.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ extract.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ replstartup.py
│  │     │  │  ├─ strings.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ classes.cpython-39.pyc
│  │     │  │     ├─ completion.cpython-39.pyc
│  │     │  │     ├─ completion_cache.cpython-39.pyc
│  │     │  │     ├─ environment.cpython-39.pyc
│  │     │  │     ├─ errors.cpython-39.pyc
│  │     │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │     ├─ file_name.cpython-39.pyc
│  │     │  │     ├─ helpers.cpython-39.pyc
│  │     │  │     ├─ interpreter.cpython-39.pyc
│  │     │  │     ├─ keywords.cpython-39.pyc
│  │     │  │     ├─ project.cpython-39.pyc
│  │     │  │     ├─ replstartup.cpython-39.pyc
│  │     │  │     ├─ strings.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ cache.py
│  │     │  ├─ common.py
│  │     │  ├─ debug.py
│  │     │  ├─ file_io.py
│  │     │  ├─ inference
│  │     │  │  ├─ analysis.py
│  │     │  │  ├─ arguments.py
│  │     │  │  ├─ base_value.py
│  │     │  │  ├─ cache.py
│  │     │  │  ├─ compiled
│  │     │  │  │  ├─ access.py
│  │     │  │  │  ├─ getattr_static.py
│  │     │  │  │  ├─ mixed.py
│  │     │  │  │  ├─ subprocess
│  │     │  │  │  │  ├─ functions.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ __main__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ functions.cpython-39.pyc
│  │     │  │  │  │     ├─ __init__.cpython-39.pyc
│  │     │  │  │  │     └─ __main__.cpython-39.pyc
│  │     │  │  │  ├─ value.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ access.cpython-39.pyc
│  │     │  │  │     ├─ getattr_static.cpython-39.pyc
│  │     │  │  │     ├─ mixed.cpython-39.pyc
│  │     │  │  │     ├─ value.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ context.py
│  │     │  │  ├─ docstrings.py
│  │     │  │  ├─ docstring_utils.py
│  │     │  │  ├─ dynamic_params.py
│  │     │  │  ├─ filters.py
│  │     │  │  ├─ finder.py
│  │     │  │  ├─ flow_analysis.py
│  │     │  │  ├─ gradual
│  │     │  │  │  ├─ annotation.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ conversion.py
│  │     │  │  │  ├─ generics.py
│  │     │  │  │  ├─ stub_value.py
│  │     │  │  │  ├─ typeshed.py
│  │     │  │  │  ├─ type_var.py
│  │     │  │  │  ├─ typing.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ annotation.cpython-39.pyc
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ conversion.cpython-39.pyc
│  │     │  │  │     ├─ generics.cpython-39.pyc
│  │     │  │  │     ├─ stub_value.cpython-39.pyc
│  │     │  │  │     ├─ typeshed.cpython-39.pyc
│  │     │  │  │     ├─ type_var.cpython-39.pyc
│  │     │  │  │     ├─ typing.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ helpers.py
│  │     │  │  ├─ imports.py
│  │     │  │  ├─ lazy_value.py
│  │     │  │  ├─ names.py
│  │     │  │  ├─ param.py
│  │     │  │  ├─ parser_cache.py
│  │     │  │  ├─ recursion.py
│  │     │  │  ├─ references.py
│  │     │  │  ├─ signature.py
│  │     │  │  ├─ star_args.py
│  │     │  │  ├─ syntax_tree.py
│  │     │  │  ├─ sys_path.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ value
│  │     │  │  │  ├─ decorator.py
│  │     │  │  │  ├─ dynamic_arrays.py
│  │     │  │  │  ├─ function.py
│  │     │  │  │  ├─ instance.py
│  │     │  │  │  ├─ iterable.py
│  │     │  │  │  ├─ klass.py
│  │     │  │  │  ├─ module.py
│  │     │  │  │  ├─ namespace.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ decorator.cpython-39.pyc
│  │     │  │  │     ├─ dynamic_arrays.cpython-39.pyc
│  │     │  │  │     ├─ function.cpython-39.pyc
│  │     │  │  │     ├─ instance.cpython-39.pyc
│  │     │  │  │     ├─ iterable.cpython-39.pyc
│  │     │  │  │     ├─ klass.cpython-39.pyc
│  │     │  │  │     ├─ module.cpython-39.pyc
│  │     │  │  │     ├─ namespace.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ analysis.cpython-39.pyc
│  │     │  │     ├─ arguments.cpython-39.pyc
│  │     │  │     ├─ base_value.cpython-39.pyc
│  │     │  │     ├─ cache.cpython-39.pyc
│  │     │  │     ├─ context.cpython-39.pyc
│  │     │  │     ├─ docstrings.cpython-39.pyc
│  │     │  │     ├─ docstring_utils.cpython-39.pyc
│  │     │  │     ├─ dynamic_params.cpython-39.pyc
│  │     │  │     ├─ filters.cpython-39.pyc
│  │     │  │     ├─ finder.cpython-39.pyc
│  │     │  │     ├─ flow_analysis.cpython-39.pyc
│  │     │  │     ├─ helpers.cpython-39.pyc
│  │     │  │     ├─ imports.cpython-39.pyc
│  │     │  │     ├─ lazy_value.cpython-39.pyc
│  │     │  │     ├─ names.cpython-39.pyc
│  │     │  │     ├─ param.cpython-39.pyc
│  │     │  │     ├─ parser_cache.cpython-39.pyc
│  │     │  │     ├─ recursion.cpython-39.pyc
│  │     │  │     ├─ references.cpython-39.pyc
│  │     │  │     ├─ signature.cpython-39.pyc
│  │     │  │     ├─ star_args.cpython-39.pyc
│  │     │  │     ├─ syntax_tree.cpython-39.pyc
│  │     │  │     ├─ sys_path.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ parser_utils.py
│  │     │  ├─ plugins
│  │     │  │  ├─ django.py
│  │     │  │  ├─ flask.py
│  │     │  │  ├─ pytest.py
│  │     │  │  ├─ registry.py
│  │     │  │  ├─ stdlib.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ django.cpython-39.pyc
│  │     │  │     ├─ flask.cpython-39.pyc
│  │     │  │     ├─ pytest.cpython-39.pyc
│  │     │  │     ├─ registry.cpython-39.pyc
│  │     │  │     ├─ stdlib.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ settings.py
│  │     │  ├─ third_party
│  │     │  │  ├─ django-stubs
│  │     │  │  │  ├─ django-stubs
│  │     │  │  │  │  ├─ apps
│  │     │  │  │  │  │  ├─ config.pyi
│  │     │  │  │  │  │  ├─ registry.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ conf
│  │     │  │  │  │  │  ├─ global_settings.pyi
│  │     │  │  │  │  │  ├─ locale
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ urls
│  │     │  │  │  │  │  │  ├─ i18n.pyi
│  │     │  │  │  │  │  │  ├─ static.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ contrib
│  │     │  │  │  │  │  ├─ admin
│  │     │  │  │  │  │  │  ├─ actions.pyi
│  │     │  │  │  │  │  │  ├─ apps.pyi
│  │     │  │  │  │  │  │  ├─ checks.pyi
│  │     │  │  │  │  │  │  ├─ decorators.pyi
│  │     │  │  │  │  │  │  ├─ filters.pyi
│  │     │  │  │  │  │  │  ├─ forms.pyi
│  │     │  │  │  │  │  │  ├─ helpers.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  ├─ options.pyi
│  │     │  │  │  │  │  │  ├─ sites.pyi
│  │     │  │  │  │  │  │  ├─ templatetags
│  │     │  │  │  │  │  │  │  ├─ admin_list.pyi
│  │     │  │  │  │  │  │  │  ├─ admin_modify.pyi
│  │     │  │  │  │  │  │  │  ├─ admin_static.pyi
│  │     │  │  │  │  │  │  │  ├─ admin_urls.pyi
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ log.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ tests.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  ├─ views
│  │     │  │  │  │  │  │  │  ├─ autocomplete.pyi
│  │     │  │  │  │  │  │  │  ├─ decorators.pyi
│  │     │  │  │  │  │  │  │  ├─ main.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ widgets.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ admindocs
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ urls.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  ├─ views.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ auth
│  │     │  │  │  │  │  │  ├─ admin.pyi
│  │     │  │  │  │  │  │  ├─ apps.pyi
│  │     │  │  │  │  │  │  ├─ backends.pyi
│  │     │  │  │  │  │  │  ├─ base_user.pyi
│  │     │  │  │  │  │  │  ├─ checks.pyi
│  │     │  │  │  │  │  │  ├─ context_processors.pyi
│  │     │  │  │  │  │  │  ├─ decorators.pyi
│  │     │  │  │  │  │  │  ├─ forms.pyi
│  │     │  │  │  │  │  │  ├─ handlers
│  │     │  │  │  │  │  │  │  ├─ modwsgi.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ hashers.pyi
│  │     │  │  │  │  │  │  ├─ management
│  │     │  │  │  │  │  │  │  ├─ commands
│  │     │  │  │  │  │  │  │  │  ├─ changepassword.pyi
│  │     │  │  │  │  │  │  │  │  ├─ createsuperuser.pyi
│  │     │  │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ mixins.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  ├─ password_validation.pyi
│  │     │  │  │  │  │  │  ├─ signals.pyi
│  │     │  │  │  │  │  │  ├─ tokens.pyi
│  │     │  │  │  │  │  │  ├─ urls.pyi
│  │     │  │  │  │  │  │  ├─ validators.pyi
│  │     │  │  │  │  │  │  ├─ views.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ contenttypes
│  │     │  │  │  │  │  │  ├─ admin.pyi
│  │     │  │  │  │  │  │  ├─ apps.pyi
│  │     │  │  │  │  │  │  ├─ checks.pyi
│  │     │  │  │  │  │  │  ├─ fields.pyi
│  │     │  │  │  │  │  │  ├─ forms.pyi
│  │     │  │  │  │  │  │  ├─ management
│  │     │  │  │  │  │  │  │  ├─ commands
│  │     │  │  │  │  │  │  │  │  ├─ remove_stale_contenttypes.pyi
│  │     │  │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  ├─ views.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ flatpages
│  │     │  │  │  │  │  │  ├─ forms.pyi
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  ├─ sitemaps.pyi
│  │     │  │  │  │  │  │  ├─ templatetags
│  │     │  │  │  │  │  │  │  ├─ flatpages.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ urls.pyi
│  │     │  │  │  │  │  │  ├─ views.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ gis
│  │     │  │  │  │  │  │  ├─ db
│  │     │  │  │  │  │  │  │  ├─ models
│  │     │  │  │  │  │  │  │  │  ├─ fields.pyi
│  │     │  │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ humanize
│  │     │  │  │  │  │  │  ├─ templatetags
│  │     │  │  │  │  │  │  │  ├─ humanize.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ messages
│  │     │  │  │  │  │  │  ├─ api.pyi
│  │     │  │  │  │  │  │  ├─ constants.pyi
│  │     │  │  │  │  │  │  ├─ context_processors.pyi
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ storage
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ cookie.pyi
│  │     │  │  │  │  │  │  │  ├─ fallback.pyi
│  │     │  │  │  │  │  │  │  ├─ session.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  ├─ views.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ postgres
│  │     │  │  │  │  │  │  ├─ aggregates
│  │     │  │  │  │  │  │  │  ├─ general.pyi
│  │     │  │  │  │  │  │  │  ├─ mixins.pyi
│  │     │  │  │  │  │  │  │  ├─ statistics.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ constraints.pyi
│  │     │  │  │  │  │  │  ├─ fields
│  │     │  │  │  │  │  │  │  ├─ array.pyi
│  │     │  │  │  │  │  │  │  ├─ citext.pyi
│  │     │  │  │  │  │  │  │  ├─ hstore.pyi
│  │     │  │  │  │  │  │  │  ├─ jsonb.pyi
│  │     │  │  │  │  │  │  │  ├─ mixins.pyi
│  │     │  │  │  │  │  │  │  ├─ ranges.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ functions.pyi
│  │     │  │  │  │  │  │  ├─ indexes.pyi
│  │     │  │  │  │  │  │  ├─ lookups.pyi
│  │     │  │  │  │  │  │  ├─ operations.pyi
│  │     │  │  │  │  │  │  ├─ search.pyi
│  │     │  │  │  │  │  │  ├─ signals.pyi
│  │     │  │  │  │  │  │  ├─ validators.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ redirects
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ sessions
│  │     │  │  │  │  │  │  ├─ backends
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ cache.pyi
│  │     │  │  │  │  │  │  │  ├─ cached_db.pyi
│  │     │  │  │  │  │  │  │  ├─ db.pyi
│  │     │  │  │  │  │  │  │  ├─ file.pyi
│  │     │  │  │  │  │  │  │  ├─ signed_cookies.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ base_session.pyi
│  │     │  │  │  │  │  │  ├─ exceptions.pyi
│  │     │  │  │  │  │  │  ├─ management
│  │     │  │  │  │  │  │  │  ├─ commands
│  │     │  │  │  │  │  │  │  │  ├─ clearsessions.pyi
│  │     │  │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  ├─ serializers.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ sitemaps
│  │     │  │  │  │  │  │  ├─ management
│  │     │  │  │  │  │  │  │  ├─ commands
│  │     │  │  │  │  │  │  │  │  ├─ ping_google.pyi
│  │     │  │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ views.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ sites
│  │     │  │  │  │  │  │  ├─ apps.pyi
│  │     │  │  │  │  │  │  ├─ management.pyi
│  │     │  │  │  │  │  │  ├─ managers.pyi
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  ├─ requests.pyi
│  │     │  │  │  │  │  │  ├─ shortcuts.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ staticfiles
│  │     │  │  │  │  │  │  ├─ apps.pyi
│  │     │  │  │  │  │  │  ├─ checks.pyi
│  │     │  │  │  │  │  │  ├─ finders.pyi
│  │     │  │  │  │  │  │  ├─ handlers.pyi
│  │     │  │  │  │  │  │  ├─ management
│  │     │  │  │  │  │  │  │  ├─ commands
│  │     │  │  │  │  │  │  │  │  ├─ collectstatic.pyi
│  │     │  │  │  │  │  │  │  │  ├─ findstatic.pyi
│  │     │  │  │  │  │  │  │  │  ├─ runserver.pyi
│  │     │  │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ storage.pyi
│  │     │  │  │  │  │  │  ├─ templatetags
│  │     │  │  │  │  │  │  │  ├─ staticfiles.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ testing.pyi
│  │     │  │  │  │  │  │  ├─ urls.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  ├─ views.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ syndication
│  │     │  │  │  │  │  │  ├─ views.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ core
│  │     │  │  │  │  │  ├─ cache
│  │     │  │  │  │  │  │  ├─ backends
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ db.pyi
│  │     │  │  │  │  │  │  │  ├─ dummy.pyi
│  │     │  │  │  │  │  │  │  ├─ filebased.pyi
│  │     │  │  │  │  │  │  │  ├─ locmem.pyi
│  │     │  │  │  │  │  │  │  ├─ memcached.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ checks
│  │     │  │  │  │  │  │  ├─ caches.pyi
│  │     │  │  │  │  │  │  ├─ database.pyi
│  │     │  │  │  │  │  │  ├─ messages.pyi
│  │     │  │  │  │  │  │  ├─ model_checks.pyi
│  │     │  │  │  │  │  │  ├─ registry.pyi
│  │     │  │  │  │  │  │  ├─ security
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ csrf.pyi
│  │     │  │  │  │  │  │  │  ├─ sessions.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ templates.pyi
│  │     │  │  │  │  │  │  ├─ translation.pyi
│  │     │  │  │  │  │  │  ├─ urls.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ exceptions.pyi
│  │     │  │  │  │  │  ├─ files
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ images.pyi
│  │     │  │  │  │  │  │  ├─ locks.pyi
│  │     │  │  │  │  │  │  ├─ move.pyi
│  │     │  │  │  │  │  │  ├─ storage.pyi
│  │     │  │  │  │  │  │  ├─ temp.pyi
│  │     │  │  │  │  │  │  ├─ uploadedfile.pyi
│  │     │  │  │  │  │  │  ├─ uploadhandler.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ handlers
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ exception.pyi
│  │     │  │  │  │  │  │  ├─ wsgi.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ mail
│  │     │  │  │  │  │  │  ├─ backends
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ console.pyi
│  │     │  │  │  │  │  │  │  ├─ dummy.pyi
│  │     │  │  │  │  │  │  │  ├─ filebased.pyi
│  │     │  │  │  │  │  │  │  ├─ locmem.pyi
│  │     │  │  │  │  │  │  │  ├─ smtp.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ message.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ management
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ color.pyi
│  │     │  │  │  │  │  │  ├─ commands
│  │     │  │  │  │  │  │  │  ├─ dumpdata.pyi
│  │     │  │  │  │  │  │  │  ├─ loaddata.pyi
│  │     │  │  │  │  │  │  │  ├─ makemessages.pyi
│  │     │  │  │  │  │  │  │  ├─ runserver.pyi
│  │     │  │  │  │  │  │  │  ├─ testserver.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ sql.pyi
│  │     │  │  │  │  │  │  ├─ templates.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ paginator.pyi
│  │     │  │  │  │  │  ├─ serializers
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ json.pyi
│  │     │  │  │  │  │  │  ├─ python.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ servers
│  │     │  │  │  │  │  │  ├─ basehttp.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ signals.pyi
│  │     │  │  │  │  │  ├─ signing.pyi
│  │     │  │  │  │  │  ├─ validators.pyi
│  │     │  │  │  │  │  ├─ wsgi.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ db
│  │     │  │  │  │  │  ├─ backends
│  │     │  │  │  │  │  │  ├─ base
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ client.pyi
│  │     │  │  │  │  │  │  │  ├─ creation.pyi
│  │     │  │  │  │  │  │  │  ├─ features.pyi
│  │     │  │  │  │  │  │  │  ├─ introspection.pyi
│  │     │  │  │  │  │  │  │  ├─ operations.pyi
│  │     │  │  │  │  │  │  │  ├─ schema.pyi
│  │     │  │  │  │  │  │  │  ├─ validation.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ ddl_references.pyi
│  │     │  │  │  │  │  │  ├─ dummy
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ mysql
│  │     │  │  │  │  │  │  │  ├─ client.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ postgresql
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ client.pyi
│  │     │  │  │  │  │  │  │  ├─ creation.pyi
│  │     │  │  │  │  │  │  │  ├─ operations.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ signals.pyi
│  │     │  │  │  │  │  │  ├─ sqlite3
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ creation.pyi
│  │     │  │  │  │  │  │  │  ├─ features.pyi
│  │     │  │  │  │  │  │  │  ├─ introspection.pyi
│  │     │  │  │  │  │  │  │  ├─ operations.pyi
│  │     │  │  │  │  │  │  │  ├─ schema.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ migrations
│  │     │  │  │  │  │  │  ├─ autodetector.pyi
│  │     │  │  │  │  │  │  ├─ exceptions.pyi
│  │     │  │  │  │  │  │  ├─ executor.pyi
│  │     │  │  │  │  │  │  ├─ graph.pyi
│  │     │  │  │  │  │  │  ├─ loader.pyi
│  │     │  │  │  │  │  │  ├─ migration.pyi
│  │     │  │  │  │  │  │  ├─ operations
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ fields.pyi
│  │     │  │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  │  ├─ special.pyi
│  │     │  │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ optimizer.pyi
│  │     │  │  │  │  │  │  ├─ questioner.pyi
│  │     │  │  │  │  │  │  ├─ recorder.pyi
│  │     │  │  │  │  │  │  ├─ serializer.pyi
│  │     │  │  │  │  │  │  ├─ state.pyi
│  │     │  │  │  │  │  │  ├─ topological_sort.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  ├─ writer.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ models
│  │     │  │  │  │  │  │  ├─ aggregates.pyi
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ constraints.pyi
│  │     │  │  │  │  │  │  ├─ deletion.pyi
│  │     │  │  │  │  │  │  ├─ enums.pyi
│  │     │  │  │  │  │  │  ├─ expressions.pyi
│  │     │  │  │  │  │  │  ├─ fields
│  │     │  │  │  │  │  │  │  ├─ files.pyi
│  │     │  │  │  │  │  │  │  ├─ mixins.pyi
│  │     │  │  │  │  │  │  │  ├─ proxy.pyi
│  │     │  │  │  │  │  │  │  ├─ related.pyi
│  │     │  │  │  │  │  │  │  ├─ related_descriptors.pyi
│  │     │  │  │  │  │  │  │  ├─ related_lookups.pyi
│  │     │  │  │  │  │  │  │  ├─ reverse_related.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ functions
│  │     │  │  │  │  │  │  │  ├─ comparison.pyi
│  │     │  │  │  │  │  │  │  ├─ datetime.pyi
│  │     │  │  │  │  │  │  │  ├─ math.pyi
│  │     │  │  │  │  │  │  │  ├─ mixins.pyi
│  │     │  │  │  │  │  │  │  ├─ text.pyi
│  │     │  │  │  │  │  │  │  ├─ window.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ indexes.pyi
│  │     │  │  │  │  │  │  ├─ lookups.pyi
│  │     │  │  │  │  │  │  ├─ manager.pyi
│  │     │  │  │  │  │  │  ├─ options.pyi
│  │     │  │  │  │  │  │  ├─ query.pyi
│  │     │  │  │  │  │  │  ├─ query_utils.pyi
│  │     │  │  │  │  │  │  ├─ signals.pyi
│  │     │  │  │  │  │  │  ├─ sql
│  │     │  │  │  │  │  │  │  ├─ compiler.pyi
│  │     │  │  │  │  │  │  │  ├─ constants.pyi
│  │     │  │  │  │  │  │  │  ├─ datastructures.pyi
│  │     │  │  │  │  │  │  │  ├─ query.pyi
│  │     │  │  │  │  │  │  │  ├─ subqueries.pyi
│  │     │  │  │  │  │  │  │  ├─ where.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ transaction.pyi
│  │     │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ dispatch
│  │     │  │  │  │  │  ├─ dispatcher.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ forms
│  │     │  │  │  │  │  ├─ boundfield.pyi
│  │     │  │  │  │  │  ├─ fields.pyi
│  │     │  │  │  │  │  ├─ forms.pyi
│  │     │  │  │  │  │  ├─ formsets.pyi
│  │     │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  ├─ renderers.pyi
│  │     │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  ├─ widgets.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ http
│  │     │  │  │  │  │  ├─ cookie.pyi
│  │     │  │  │  │  │  ├─ multipartparser.pyi
│  │     │  │  │  │  │  ├─ request.pyi
│  │     │  │  │  │  │  ├─ response.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ middleware
│  │     │  │  │  │  │  ├─ cache.pyi
│  │     │  │  │  │  │  ├─ clickjacking.pyi
│  │     │  │  │  │  │  ├─ common.pyi
│  │     │  │  │  │  │  ├─ csrf.pyi
│  │     │  │  │  │  │  ├─ gzip.pyi
│  │     │  │  │  │  │  ├─ http.pyi
│  │     │  │  │  │  │  ├─ locale.pyi
│  │     │  │  │  │  │  ├─ security.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ shortcuts.pyi
│  │     │  │  │  │  ├─ template
│  │     │  │  │  │  │  ├─ backends
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ django.pyi
│  │     │  │  │  │  │  │  ├─ dummy.pyi
│  │     │  │  │  │  │  │  ├─ jinja2.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  ├─ context.pyi
│  │     │  │  │  │  │  ├─ context_processors.pyi
│  │     │  │  │  │  │  ├─ defaultfilters.pyi
│  │     │  │  │  │  │  ├─ defaulttags.pyi
│  │     │  │  │  │  │  ├─ engine.pyi
│  │     │  │  │  │  │  ├─ exceptions.pyi
│  │     │  │  │  │  │  ├─ library.pyi
│  │     │  │  │  │  │  ├─ loader.pyi
│  │     │  │  │  │  │  ├─ loaders
│  │     │  │  │  │  │  │  ├─ app_directories.pyi
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ cached.pyi
│  │     │  │  │  │  │  │  ├─ filesystem.pyi
│  │     │  │  │  │  │  │  ├─ locmem.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ loader_tags.pyi
│  │     │  │  │  │  │  ├─ response.pyi
│  │     │  │  │  │  │  ├─ smartif.pyi
│  │     │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ templatetags
│  │     │  │  │  │  │  ├─ cache.pyi
│  │     │  │  │  │  │  ├─ i18n.pyi
│  │     │  │  │  │  │  ├─ l10n.pyi
│  │     │  │  │  │  │  ├─ static.pyi
│  │     │  │  │  │  │  ├─ tz.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ test
│  │     │  │  │  │  │  ├─ client.pyi
│  │     │  │  │  │  │  ├─ html.pyi
│  │     │  │  │  │  │  ├─ runner.pyi
│  │     │  │  │  │  │  ├─ selenium.pyi
│  │     │  │  │  │  │  ├─ signals.pyi
│  │     │  │  │  │  │  ├─ testcases.pyi
│  │     │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ urls
│  │     │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  ├─ conf.pyi
│  │     │  │  │  │  │  ├─ converters.pyi
│  │     │  │  │  │  │  ├─ exceptions.pyi
│  │     │  │  │  │  │  ├─ resolvers.pyi
│  │     │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ utils
│  │     │  │  │  │  │  ├─ archive.pyi
│  │     │  │  │  │  │  ├─ autoreload.pyi
│  │     │  │  │  │  │  ├─ baseconv.pyi
│  │     │  │  │  │  │  ├─ cache.pyi
│  │     │  │  │  │  │  ├─ crypto.pyi
│  │     │  │  │  │  │  ├─ datastructures.pyi
│  │     │  │  │  │  │  ├─ dateformat.pyi
│  │     │  │  │  │  │  ├─ dateparse.pyi
│  │     │  │  │  │  │  ├─ dates.pyi
│  │     │  │  │  │  │  ├─ datetime_safe.pyi
│  │     │  │  │  │  │  ├─ deconstruct.pyi
│  │     │  │  │  │  │  ├─ decorators.pyi
│  │     │  │  │  │  │  ├─ deprecation.pyi
│  │     │  │  │  │  │  ├─ duration.pyi
│  │     │  │  │  │  │  ├─ encoding.pyi
│  │     │  │  │  │  │  ├─ feedgenerator.pyi
│  │     │  │  │  │  │  ├─ formats.pyi
│  │     │  │  │  │  │  ├─ functional.pyi
│  │     │  │  │  │  │  ├─ hashable.pyi
│  │     │  │  │  │  │  ├─ html.pyi
│  │     │  │  │  │  │  ├─ http.pyi
│  │     │  │  │  │  │  ├─ inspect.pyi
│  │     │  │  │  │  │  ├─ ipv6.pyi
│  │     │  │  │  │  │  ├─ itercompat.pyi
│  │     │  │  │  │  │  ├─ jslex.pyi
│  │     │  │  │  │  │  ├─ log.pyi
│  │     │  │  │  │  │  ├─ lorem_ipsum.pyi
│  │     │  │  │  │  │  ├─ module_loading.pyi
│  │     │  │  │  │  │  ├─ numberformat.pyi
│  │     │  │  │  │  │  ├─ regex_helper.pyi
│  │     │  │  │  │  │  ├─ safestring.pyi
│  │     │  │  │  │  │  ├─ six.pyi
│  │     │  │  │  │  │  ├─ termcolors.pyi
│  │     │  │  │  │  │  ├─ text.pyi
│  │     │  │  │  │  │  ├─ timesince.pyi
│  │     │  │  │  │  │  ├─ timezone.pyi
│  │     │  │  │  │  │  ├─ topological_sort.pyi
│  │     │  │  │  │  │  ├─ translation
│  │     │  │  │  │  │  │  ├─ reloader.pyi
│  │     │  │  │  │  │  │  ├─ template.pyi
│  │     │  │  │  │  │  │  ├─ trans_null.pyi
│  │     │  │  │  │  │  │  ├─ trans_real.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ tree.pyi
│  │     │  │  │  │  │  ├─ version.pyi
│  │     │  │  │  │  │  ├─ xmlutils.pyi
│  │     │  │  │  │  │  ├─ _os.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ views
│  │     │  │  │  │  │  ├─ csrf.pyi
│  │     │  │  │  │  │  ├─ debug.pyi
│  │     │  │  │  │  │  ├─ decorators
│  │     │  │  │  │  │  │  ├─ cache.pyi
│  │     │  │  │  │  │  │  ├─ clickjacking.pyi
│  │     │  │  │  │  │  │  ├─ csrf.pyi
│  │     │  │  │  │  │  │  ├─ debug.pyi
│  │     │  │  │  │  │  │  ├─ gzip.pyi
│  │     │  │  │  │  │  │  ├─ http.pyi
│  │     │  │  │  │  │  │  ├─ vary.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ defaults.pyi
│  │     │  │  │  │  │  ├─ generic
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ dates.pyi
│  │     │  │  │  │  │  │  ├─ detail.pyi
│  │     │  │  │  │  │  │  ├─ edit.pyi
│  │     │  │  │  │  │  │  ├─ list.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ i18n.pyi
│  │     │  │  │  │  │  ├─ static.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  └─ LICENSE.txt
│  │     │  │  └─ typeshed
│  │     │  │     ├─ LICENSE
│  │     │  │     ├─ stdlib
│  │     │  │     │  ├─ 2
│  │     │  │     │  │  ├─ abc.pyi
│  │     │  │     │  │  ├─ ast.pyi
│  │     │  │     │  │  ├─ atexit.pyi
│  │     │  │     │  │  ├─ BaseHTTPServer.pyi
│  │     │  │     │  │  ├─ builtins.pyi
│  │     │  │     │  │  ├─ CGIHTTPServer.pyi
│  │     │  │     │  │  ├─ collections.pyi
│  │     │  │     │  │  ├─ commands.pyi
│  │     │  │     │  │  ├─ compileall.pyi
│  │     │  │     │  │  ├─ ConfigParser.pyi
│  │     │  │     │  │  ├─ Cookie.pyi
│  │     │  │     │  │  ├─ cookielib.pyi
│  │     │  │     │  │  ├─ copy_reg.pyi
│  │     │  │     │  │  ├─ cPickle.pyi
│  │     │  │     │  │  ├─ cStringIO.pyi
│  │     │  │     │  │  ├─ dircache.pyi
│  │     │  │     │  │  ├─ distutils
│  │     │  │     │  │  │  ├─ archive_util.pyi
│  │     │  │     │  │  │  ├─ bcppcompiler.pyi
│  │     │  │     │  │  │  ├─ ccompiler.pyi
│  │     │  │     │  │  │  ├─ cmd.pyi
│  │     │  │     │  │  │  ├─ command
│  │     │  │     │  │  │  │  ├─ bdist.pyi
│  │     │  │     │  │  │  │  ├─ bdist_dumb.pyi
│  │     │  │     │  │  │  │  ├─ bdist_msi.pyi
│  │     │  │     │  │  │  │  ├─ bdist_packager.pyi
│  │     │  │     │  │  │  │  ├─ bdist_rpm.pyi
│  │     │  │     │  │  │  │  ├─ bdist_wininst.pyi
│  │     │  │     │  │  │  │  ├─ build.pyi
│  │     │  │     │  │  │  │  ├─ build_clib.pyi
│  │     │  │     │  │  │  │  ├─ build_ext.pyi
│  │     │  │     │  │  │  │  ├─ build_py.pyi
│  │     │  │     │  │  │  │  ├─ build_scripts.pyi
│  │     │  │     │  │  │  │  ├─ check.pyi
│  │     │  │     │  │  │  │  ├─ clean.pyi
│  │     │  │     │  │  │  │  ├─ config.pyi
│  │     │  │     │  │  │  │  ├─ install.pyi
│  │     │  │     │  │  │  │  ├─ install_data.pyi
│  │     │  │     │  │  │  │  ├─ install_egg_info.pyi
│  │     │  │     │  │  │  │  ├─ install_headers.pyi
│  │     │  │     │  │  │  │  ├─ install_lib.pyi
│  │     │  │     │  │  │  │  ├─ install_scripts.pyi
│  │     │  │     │  │  │  │  ├─ register.pyi
│  │     │  │     │  │  │  │  ├─ sdist.pyi
│  │     │  │     │  │  │  │  ├─ upload.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ config.pyi
│  │     │  │     │  │  │  ├─ core.pyi
│  │     │  │     │  │  │  ├─ cygwinccompiler.pyi
│  │     │  │     │  │  │  ├─ debug.pyi
│  │     │  │     │  │  │  ├─ dep_util.pyi
│  │     │  │     │  │  │  ├─ dir_util.pyi
│  │     │  │     │  │  │  ├─ dist.pyi
│  │     │  │     │  │  │  ├─ emxccompiler.pyi
│  │     │  │     │  │  │  ├─ errors.pyi
│  │     │  │     │  │  │  ├─ extension.pyi
│  │     │  │     │  │  │  ├─ fancy_getopt.pyi
│  │     │  │     │  │  │  ├─ filelist.pyi
│  │     │  │     │  │  │  ├─ file_util.pyi
│  │     │  │     │  │  │  ├─ log.pyi
│  │     │  │     │  │  │  ├─ msvccompiler.pyi
│  │     │  │     │  │  │  ├─ spawn.pyi
│  │     │  │     │  │  │  ├─ sysconfig.pyi
│  │     │  │     │  │  │  ├─ text_file.pyi
│  │     │  │     │  │  │  ├─ unixccompiler.pyi
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  ├─ version.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ dummy_thread.pyi
│  │     │  │     │  │  ├─ email
│  │     │  │     │  │  │  ├─ base64mime.pyi
│  │     │  │     │  │  │  ├─ charset.pyi
│  │     │  │     │  │  │  ├─ encoders.pyi
│  │     │  │     │  │  │  ├─ feedparser.pyi
│  │     │  │     │  │  │  ├─ generator.pyi
│  │     │  │     │  │  │  ├─ header.pyi
│  │     │  │     │  │  │  ├─ iterators.pyi
│  │     │  │     │  │  │  ├─ message.pyi
│  │     │  │     │  │  │  ├─ mime
│  │     │  │     │  │  │  │  ├─ application.pyi
│  │     │  │     │  │  │  │  ├─ audio.pyi
│  │     │  │     │  │  │  │  ├─ base.pyi
│  │     │  │     │  │  │  │  ├─ image.pyi
│  │     │  │     │  │  │  │  ├─ message.pyi
│  │     │  │     │  │  │  │  ├─ multipart.pyi
│  │     │  │     │  │  │  │  ├─ nonmultipart.pyi
│  │     │  │     │  │  │  │  ├─ text.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ MIMEText.pyi
│  │     │  │     │  │  │  ├─ parser.pyi
│  │     │  │     │  │  │  ├─ quoprimime.pyi
│  │     │  │     │  │  │  ├─ utils.pyi
│  │     │  │     │  │  │  ├─ _parseaddr.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ encodings
│  │     │  │     │  │  │  ├─ utf_8.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ exceptions.pyi
│  │     │  │     │  │  ├─ fcntl.pyi
│  │     │  │     │  │  ├─ fnmatch.pyi
│  │     │  │     │  │  ├─ functools.pyi
│  │     │  │     │  │  ├─ future_builtins.pyi
│  │     │  │     │  │  ├─ gc.pyi
│  │     │  │     │  │  ├─ getopt.pyi
│  │     │  │     │  │  ├─ getpass.pyi
│  │     │  │     │  │  ├─ gettext.pyi
│  │     │  │     │  │  ├─ glob.pyi
│  │     │  │     │  │  ├─ gzip.pyi
│  │     │  │     │  │  ├─ hashlib.pyi
│  │     │  │     │  │  ├─ heapq.pyi
│  │     │  │     │  │  ├─ htmlentitydefs.pyi
│  │     │  │     │  │  ├─ HTMLParser.pyi
│  │     │  │     │  │  ├─ httplib.pyi
│  │     │  │     │  │  ├─ imp.pyi
│  │     │  │     │  │  ├─ importlib.pyi
│  │     │  │     │  │  ├─ inspect.pyi
│  │     │  │     │  │  ├─ io.pyi
│  │     │  │     │  │  ├─ itertools.pyi
│  │     │  │     │  │  ├─ json.pyi
│  │     │  │     │  │  ├─ markupbase.pyi
│  │     │  │     │  │  ├─ md5.pyi
│  │     │  │     │  │  ├─ mimetools.pyi
│  │     │  │     │  │  ├─ multiprocessing
│  │     │  │     │  │  │  ├─ dummy
│  │     │  │     │  │  │  │  ├─ connection.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ pool.pyi
│  │     │  │     │  │  │  ├─ process.pyi
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ mutex.pyi
│  │     │  │     │  │  ├─ ntpath.pyi
│  │     │  │     │  │  ├─ nturl2path.pyi
│  │     │  │     │  │  ├─ os
│  │     │  │     │  │  │  ├─ path.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ os2emxpath.pyi
│  │     │  │     │  │  ├─ pipes.pyi
│  │     │  │     │  │  ├─ platform.pyi
│  │     │  │     │  │  ├─ popen2.pyi
│  │     │  │     │  │  ├─ posix.pyi
│  │     │  │     │  │  ├─ posixpath.pyi
│  │     │  │     │  │  ├─ Queue.pyi
│  │     │  │     │  │  ├─ random.pyi
│  │     │  │     │  │  ├─ re.pyi
│  │     │  │     │  │  ├─ repr.pyi
│  │     │  │     │  │  ├─ resource.pyi
│  │     │  │     │  │  ├─ rfc822.pyi
│  │     │  │     │  │  ├─ robotparser.pyi
│  │     │  │     │  │  ├─ runpy.pyi
│  │     │  │     │  │  ├─ sets.pyi
│  │     │  │     │  │  ├─ sha.pyi
│  │     │  │     │  │  ├─ shelve.pyi
│  │     │  │     │  │  ├─ shlex.pyi
│  │     │  │     │  │  ├─ signal.pyi
│  │     │  │     │  │  ├─ SimpleHTTPServer.pyi
│  │     │  │     │  │  ├─ smtplib.pyi
│  │     │  │     │  │  ├─ SocketServer.pyi
│  │     │  │     │  │  ├─ spwd.pyi
│  │     │  │     │  │  ├─ sre_constants.pyi
│  │     │  │     │  │  ├─ sre_parse.pyi
│  │     │  │     │  │  ├─ stat.pyi
│  │     │  │     │  │  ├─ string.pyi
│  │     │  │     │  │  ├─ StringIO.pyi
│  │     │  │     │  │  ├─ stringold.pyi
│  │     │  │     │  │  ├─ strop.pyi
│  │     │  │     │  │  ├─ subprocess.pyi
│  │     │  │     │  │  ├─ symbol.pyi
│  │     │  │     │  │  ├─ sys.pyi
│  │     │  │     │  │  ├─ tempfile.pyi
│  │     │  │     │  │  ├─ textwrap.pyi
│  │     │  │     │  │  ├─ thread.pyi
│  │     │  │     │  │  ├─ toaiff.pyi
│  │     │  │     │  │  ├─ tokenize.pyi
│  │     │  │     │  │  ├─ types.pyi
│  │     │  │     │  │  ├─ typing.pyi
│  │     │  │     │  │  ├─ unittest.pyi
│  │     │  │     │  │  ├─ urllib.pyi
│  │     │  │     │  │  ├─ urllib2.pyi
│  │     │  │     │  │  ├─ urlparse.pyi
│  │     │  │     │  │  ├─ user.pyi
│  │     │  │     │  │  ├─ UserDict.pyi
│  │     │  │     │  │  ├─ UserList.pyi
│  │     │  │     │  │  ├─ UserString.pyi
│  │     │  │     │  │  ├─ whichdb.pyi
│  │     │  │     │  │  ├─ xmlrpclib.pyi
│  │     │  │     │  │  ├─ _ast.pyi
│  │     │  │     │  │  ├─ _collections.pyi
│  │     │  │     │  │  ├─ _functools.pyi
│  │     │  │     │  │  ├─ _hotshot.pyi
│  │     │  │     │  │  ├─ _io.pyi
│  │     │  │     │  │  ├─ _json.pyi
│  │     │  │     │  │  ├─ _md5.pyi
│  │     │  │     │  │  ├─ _sha.pyi
│  │     │  │     │  │  ├─ _sha256.pyi
│  │     │  │     │  │  ├─ _sha512.pyi
│  │     │  │     │  │  ├─ _socket.pyi
│  │     │  │     │  │  ├─ _sre.pyi
│  │     │  │     │  │  ├─ _struct.pyi
│  │     │  │     │  │  ├─ _symtable.pyi
│  │     │  │     │  │  ├─ _threading_local.pyi
│  │     │  │     │  │  ├─ _winreg.pyi
│  │     │  │     │  │  └─ __builtin__.pyi
│  │     │  │     │  ├─ 2and3
│  │     │  │     │  │  ├─ aifc.pyi
│  │     │  │     │  │  ├─ antigravity.pyi
│  │     │  │     │  │  ├─ argparse.pyi
│  │     │  │     │  │  ├─ array.pyi
│  │     │  │     │  │  ├─ asynchat.pyi
│  │     │  │     │  │  ├─ asyncore.pyi
│  │     │  │     │  │  ├─ audioop.pyi
│  │     │  │     │  │  ├─ base64.pyi
│  │     │  │     │  │  ├─ bdb.pyi
│  │     │  │     │  │  ├─ binascii.pyi
│  │     │  │     │  │  ├─ binhex.pyi
│  │     │  │     │  │  ├─ bisect.pyi
│  │     │  │     │  │  ├─ bz2.pyi
│  │     │  │     │  │  ├─ calendar.pyi
│  │     │  │     │  │  ├─ cgi.pyi
│  │     │  │     │  │  ├─ cgitb.pyi
│  │     │  │     │  │  ├─ chunk.pyi
│  │     │  │     │  │  ├─ cmath.pyi
│  │     │  │     │  │  ├─ cmd.pyi
│  │     │  │     │  │  ├─ code.pyi
│  │     │  │     │  │  ├─ codecs.pyi
│  │     │  │     │  │  ├─ codeop.pyi
│  │     │  │     │  │  ├─ colorsys.pyi
│  │     │  │     │  │  ├─ contextlib.pyi
│  │     │  │     │  │  ├─ copy.pyi
│  │     │  │     │  │  ├─ cProfile.pyi
│  │     │  │     │  │  ├─ crypt.pyi
│  │     │  │     │  │  ├─ csv.pyi
│  │     │  │     │  │  ├─ ctypes
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  ├─ wintypes.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ curses
│  │     │  │     │  │  │  ├─ ascii.pyi
│  │     │  │     │  │  │  ├─ panel.pyi
│  │     │  │     │  │  │  ├─ textpad.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ datetime.pyi
│  │     │  │     │  │  ├─ decimal.pyi
│  │     │  │     │  │  ├─ difflib.pyi
│  │     │  │     │  │  ├─ dis.pyi
│  │     │  │     │  │  ├─ doctest.pyi
│  │     │  │     │  │  ├─ dummy_threading.pyi
│  │     │  │     │  │  ├─ ensurepip
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ errno.pyi
│  │     │  │     │  │  ├─ filecmp.pyi
│  │     │  │     │  │  ├─ fileinput.pyi
│  │     │  │     │  │  ├─ formatter.pyi
│  │     │  │     │  │  ├─ fractions.pyi
│  │     │  │     │  │  ├─ ftplib.pyi
│  │     │  │     │  │  ├─ genericpath.pyi
│  │     │  │     │  │  ├─ grp.pyi
│  │     │  │     │  │  ├─ hmac.pyi
│  │     │  │     │  │  ├─ imaplib.pyi
│  │     │  │     │  │  ├─ imghdr.pyi
│  │     │  │     │  │  ├─ keyword.pyi
│  │     │  │     │  │  ├─ lib2to3
│  │     │  │     │  │  │  ├─ pgen2
│  │     │  │     │  │  │  │  ├─ driver.pyi
│  │     │  │     │  │  │  │  ├─ grammar.pyi
│  │     │  │     │  │  │  │  ├─ literals.pyi
│  │     │  │     │  │  │  │  ├─ parse.pyi
│  │     │  │     │  │  │  │  ├─ pgen.pyi
│  │     │  │     │  │  │  │  ├─ token.pyi
│  │     │  │     │  │  │  │  ├─ tokenize.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ pygram.pyi
│  │     │  │     │  │  │  ├─ pytree.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ linecache.pyi
│  │     │  │     │  │  ├─ locale.pyi
│  │     │  │     │  │  ├─ logging
│  │     │  │     │  │  │  ├─ config.pyi
│  │     │  │     │  │  │  ├─ handlers.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ macpath.pyi
│  │     │  │     │  │  ├─ mailbox.pyi
│  │     │  │     │  │  ├─ mailcap.pyi
│  │     │  │     │  │  ├─ marshal.pyi
│  │     │  │     │  │  ├─ math.pyi
│  │     │  │     │  │  ├─ mimetypes.pyi
│  │     │  │     │  │  ├─ mmap.pyi
│  │     │  │     │  │  ├─ modulefinder.pyi
│  │     │  │     │  │  ├─ msilib
│  │     │  │     │  │  │  ├─ schema.pyi
│  │     │  │     │  │  │  ├─ sequence.pyi
│  │     │  │     │  │  │  ├─ text.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ msvcrt.pyi
│  │     │  │     │  │  ├─ netrc.pyi
│  │     │  │     │  │  ├─ nis.pyi
│  │     │  │     │  │  ├─ numbers.pyi
│  │     │  │     │  │  ├─ opcode.pyi
│  │     │  │     │  │  ├─ operator.pyi
│  │     │  │     │  │  ├─ optparse.pyi
│  │     │  │     │  │  ├─ parser.pyi
│  │     │  │     │  │  ├─ pdb.pyi
│  │     │  │     │  │  ├─ pickle.pyi
│  │     │  │     │  │  ├─ pickletools.pyi
│  │     │  │     │  │  ├─ pkgutil.pyi
│  │     │  │     │  │  ├─ plistlib.pyi
│  │     │  │     │  │  ├─ poplib.pyi
│  │     │  │     │  │  ├─ pprint.pyi
│  │     │  │     │  │  ├─ profile.pyi
│  │     │  │     │  │  ├─ pstats.pyi
│  │     │  │     │  │  ├─ pty.pyi
│  │     │  │     │  │  ├─ pwd.pyi
│  │     │  │     │  │  ├─ pyclbr.pyi
│  │     │  │     │  │  ├─ pydoc.pyi
│  │     │  │     │  │  ├─ pydoc_data
│  │     │  │     │  │  │  ├─ topics.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ pyexpat
│  │     │  │     │  │  │  ├─ errors.pyi
│  │     │  │     │  │  │  ├─ model.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ py_compile.pyi
│  │     │  │     │  │  ├─ quopri.pyi
│  │     │  │     │  │  ├─ readline.pyi
│  │     │  │     │  │  ├─ rlcompleter.pyi
│  │     │  │     │  │  ├─ sched.pyi
│  │     │  │     │  │  ├─ select.pyi
│  │     │  │     │  │  ├─ shutil.pyi
│  │     │  │     │  │  ├─ site.pyi
│  │     │  │     │  │  ├─ smtpd.pyi
│  │     │  │     │  │  ├─ sndhdr.pyi
│  │     │  │     │  │  ├─ socket.pyi
│  │     │  │     │  │  ├─ sqlite3
│  │     │  │     │  │  │  ├─ dbapi2.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ sre_compile.pyi
│  │     │  │     │  │  ├─ ssl.pyi
│  │     │  │     │  │  ├─ stringprep.pyi
│  │     │  │     │  │  ├─ struct.pyi
│  │     │  │     │  │  ├─ sunau.pyi
│  │     │  │     │  │  ├─ symtable.pyi
│  │     │  │     │  │  ├─ sysconfig.pyi
│  │     │  │     │  │  ├─ syslog.pyi
│  │     │  │     │  │  ├─ tabnanny.pyi
│  │     │  │     │  │  ├─ tarfile.pyi
│  │     │  │     │  │  ├─ telnetlib.pyi
│  │     │  │     │  │  ├─ termios.pyi
│  │     │  │     │  │  ├─ this.pyi
│  │     │  │     │  │  ├─ threading.pyi
│  │     │  │     │  │  ├─ time.pyi
│  │     │  │     │  │  ├─ timeit.pyi
│  │     │  │     │  │  ├─ token.pyi
│  │     │  │     │  │  ├─ trace.pyi
│  │     │  │     │  │  ├─ traceback.pyi
│  │     │  │     │  │  ├─ tty.pyi
│  │     │  │     │  │  ├─ turtle.pyi
│  │     │  │     │  │  ├─ unicodedata.pyi
│  │     │  │     │  │  ├─ uu.pyi
│  │     │  │     │  │  ├─ uuid.pyi
│  │     │  │     │  │  ├─ warnings.pyi
│  │     │  │     │  │  ├─ wave.pyi
│  │     │  │     │  │  ├─ weakref.pyi
│  │     │  │     │  │  ├─ webbrowser.pyi
│  │     │  │     │  │  ├─ winsound.pyi
│  │     │  │     │  │  ├─ wsgiref
│  │     │  │     │  │  │  ├─ handlers.pyi
│  │     │  │     │  │  │  ├─ headers.pyi
│  │     │  │     │  │  │  ├─ simple_server.pyi
│  │     │  │     │  │  │  ├─ types.pyi
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  ├─ validate.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ xdrlib.pyi
│  │     │  │     │  │  ├─ xml
│  │     │  │     │  │  │  ├─ dom
│  │     │  │     │  │  │  │  ├─ domreg.pyi
│  │     │  │     │  │  │  │  ├─ expatbuilder.pyi
│  │     │  │     │  │  │  │  ├─ minicompat.pyi
│  │     │  │     │  │  │  │  ├─ minidom.pyi
│  │     │  │     │  │  │  │  ├─ NodeFilter.pyi
│  │     │  │     │  │  │  │  ├─ pulldom.pyi
│  │     │  │     │  │  │  │  ├─ xmlbuilder.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ etree
│  │     │  │     │  │  │  │  ├─ cElementTree.pyi
│  │     │  │     │  │  │  │  ├─ ElementInclude.pyi
│  │     │  │     │  │  │  │  ├─ ElementPath.pyi
│  │     │  │     │  │  │  │  ├─ ElementTree.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ parsers
│  │     │  │     │  │  │  │  ├─ expat
│  │     │  │     │  │  │  │  │  ├─ errors.pyi
│  │     │  │     │  │  │  │  │  ├─ model.pyi
│  │     │  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ sax
│  │     │  │     │  │  │  │  ├─ handler.pyi
│  │     │  │     │  │  │  │  ├─ saxutils.pyi
│  │     │  │     │  │  │  │  ├─ xmlreader.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ zipfile.pyi
│  │     │  │     │  │  ├─ zipimport.pyi
│  │     │  │     │  │  ├─ zlib.pyi
│  │     │  │     │  │  ├─ _bisect.pyi
│  │     │  │     │  │  ├─ _codecs.pyi
│  │     │  │     │  │  ├─ _csv.pyi
│  │     │  │     │  │  ├─ _curses.pyi
│  │     │  │     │  │  ├─ _dummy_threading.pyi
│  │     │  │     │  │  ├─ _heapq.pyi
│  │     │  │     │  │  ├─ _msi.pyi
│  │     │  │     │  │  ├─ _random.pyi
│  │     │  │     │  │  ├─ _typeshed
│  │     │  │     │  │  │  ├─ wsgi.pyi
│  │     │  │     │  │  │  ├─ xml.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ _warnings.pyi
│  │     │  │     │  │  ├─ _weakref.pyi
│  │     │  │     │  │  ├─ _weakrefset.pyi
│  │     │  │     │  │  └─ __future__.pyi
│  │     │  │     │  ├─ 3
│  │     │  │     │  │  ├─ abc.pyi
│  │     │  │     │  │  ├─ ast.pyi
│  │     │  │     │  │  ├─ asyncio
│  │     │  │     │  │  │  ├─ base_events.pyi
│  │     │  │     │  │  │  ├─ base_futures.pyi
│  │     │  │     │  │  │  ├─ base_subprocess.pyi
│  │     │  │     │  │  │  ├─ base_tasks.pyi
│  │     │  │     │  │  │  ├─ compat.pyi
│  │     │  │     │  │  │  ├─ constants.pyi
│  │     │  │     │  │  │  ├─ coroutines.pyi
│  │     │  │     │  │  │  ├─ events.pyi
│  │     │  │     │  │  │  ├─ exceptions.pyi
│  │     │  │     │  │  │  ├─ format_helpers.pyi
│  │     │  │     │  │  │  ├─ futures.pyi
│  │     │  │     │  │  │  ├─ locks.pyi
│  │     │  │     │  │  │  ├─ log.pyi
│  │     │  │     │  │  │  ├─ proactor_events.pyi
│  │     │  │     │  │  │  ├─ protocols.pyi
│  │     │  │     │  │  │  ├─ queues.pyi
│  │     │  │     │  │  │  ├─ runners.pyi
│  │     │  │     │  │  │  ├─ selector_events.pyi
│  │     │  │     │  │  │  ├─ sslproto.pyi
│  │     │  │     │  │  │  ├─ staggered.pyi
│  │     │  │     │  │  │  ├─ streams.pyi
│  │     │  │     │  │  │  ├─ subprocess.pyi
│  │     │  │     │  │  │  ├─ tasks.pyi
│  │     │  │     │  │  │  ├─ threads.pyi
│  │     │  │     │  │  │  ├─ transports.pyi
│  │     │  │     │  │  │  ├─ trsock.pyi
│  │     │  │     │  │  │  ├─ unix_events.pyi
│  │     │  │     │  │  │  ├─ windows_events.pyi
│  │     │  │     │  │  │  ├─ windows_utils.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ atexit.pyi
│  │     │  │     │  │  ├─ builtins.pyi
│  │     │  │     │  │  ├─ collections
│  │     │  │     │  │  │  ├─ abc.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ compileall.pyi
│  │     │  │     │  │  ├─ concurrent
│  │     │  │     │  │  │  ├─ futures
│  │     │  │     │  │  │  │  ├─ process.pyi
│  │     │  │     │  │  │  │  ├─ thread.pyi
│  │     │  │     │  │  │  │  ├─ _base.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ configparser.pyi
│  │     │  │     │  │  ├─ copyreg.pyi
│  │     │  │     │  │  ├─ dbm
│  │     │  │     │  │  │  ├─ dumb.pyi
│  │     │  │     │  │  │  ├─ gnu.pyi
│  │     │  │     │  │  │  ├─ ndbm.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ distutils
│  │     │  │     │  │  │  ├─ archive_util.pyi
│  │     │  │     │  │  │  ├─ bcppcompiler.pyi
│  │     │  │     │  │  │  ├─ ccompiler.pyi
│  │     │  │     │  │  │  ├─ cmd.pyi
│  │     │  │     │  │  │  ├─ command
│  │     │  │     │  │  │  │  ├─ bdist.pyi
│  │     │  │     │  │  │  │  ├─ bdist_dumb.pyi
│  │     │  │     │  │  │  │  ├─ bdist_msi.pyi
│  │     │  │     │  │  │  │  ├─ bdist_packager.pyi
│  │     │  │     │  │  │  │  ├─ bdist_rpm.pyi
│  │     │  │     │  │  │  │  ├─ bdist_wininst.pyi
│  │     │  │     │  │  │  │  ├─ build.pyi
│  │     │  │     │  │  │  │  ├─ build_clib.pyi
│  │     │  │     │  │  │  │  ├─ build_ext.pyi
│  │     │  │     │  │  │  │  ├─ build_py.pyi
│  │     │  │     │  │  │  │  ├─ build_scripts.pyi
│  │     │  │     │  │  │  │  ├─ check.pyi
│  │     │  │     │  │  │  │  ├─ clean.pyi
│  │     │  │     │  │  │  │  ├─ config.pyi
│  │     │  │     │  │  │  │  ├─ install.pyi
│  │     │  │     │  │  │  │  ├─ install_data.pyi
│  │     │  │     │  │  │  │  ├─ install_egg_info.pyi
│  │     │  │     │  │  │  │  ├─ install_headers.pyi
│  │     │  │     │  │  │  │  ├─ install_lib.pyi
│  │     │  │     │  │  │  │  ├─ install_scripts.pyi
│  │     │  │     │  │  │  │  ├─ register.pyi
│  │     │  │     │  │  │  │  ├─ sdist.pyi
│  │     │  │     │  │  │  │  ├─ upload.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ config.pyi
│  │     │  │     │  │  │  ├─ core.pyi
│  │     │  │     │  │  │  ├─ cygwinccompiler.pyi
│  │     │  │     │  │  │  ├─ debug.pyi
│  │     │  │     │  │  │  ├─ dep_util.pyi
│  │     │  │     │  │  │  ├─ dir_util.pyi
│  │     │  │     │  │  │  ├─ dist.pyi
│  │     │  │     │  │  │  ├─ errors.pyi
│  │     │  │     │  │  │  ├─ extension.pyi
│  │     │  │     │  │  │  ├─ fancy_getopt.pyi
│  │     │  │     │  │  │  ├─ filelist.pyi
│  │     │  │     │  │  │  ├─ file_util.pyi
│  │     │  │     │  │  │  ├─ log.pyi
│  │     │  │     │  │  │  ├─ msvccompiler.pyi
│  │     │  │     │  │  │  ├─ spawn.pyi
│  │     │  │     │  │  │  ├─ sysconfig.pyi
│  │     │  │     │  │  │  ├─ text_file.pyi
│  │     │  │     │  │  │  ├─ unixccompiler.pyi
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  ├─ version.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ email
│  │     │  │     │  │  │  ├─ charset.pyi
│  │     │  │     │  │  │  ├─ contentmanager.pyi
│  │     │  │     │  │  │  ├─ encoders.pyi
│  │     │  │     │  │  │  ├─ errors.pyi
│  │     │  │     │  │  │  ├─ feedparser.pyi
│  │     │  │     │  │  │  ├─ generator.pyi
│  │     │  │     │  │  │  ├─ header.pyi
│  │     │  │     │  │  │  ├─ headerregistry.pyi
│  │     │  │     │  │  │  ├─ iterators.pyi
│  │     │  │     │  │  │  ├─ message.pyi
│  │     │  │     │  │  │  ├─ mime
│  │     │  │     │  │  │  │  ├─ application.pyi
│  │     │  │     │  │  │  │  ├─ audio.pyi
│  │     │  │     │  │  │  │  ├─ base.pyi
│  │     │  │     │  │  │  │  ├─ image.pyi
│  │     │  │     │  │  │  │  ├─ message.pyi
│  │     │  │     │  │  │  │  ├─ multipart.pyi
│  │     │  │     │  │  │  │  ├─ nonmultipart.pyi
│  │     │  │     │  │  │  │  ├─ text.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ parser.pyi
│  │     │  │     │  │  │  ├─ policy.pyi
│  │     │  │     │  │  │  ├─ utils.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ encodings
│  │     │  │     │  │  │  ├─ utf_8.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ enum.pyi
│  │     │  │     │  │  ├─ faulthandler.pyi
│  │     │  │     │  │  ├─ fcntl.pyi
│  │     │  │     │  │  ├─ fnmatch.pyi
│  │     │  │     │  │  ├─ functools.pyi
│  │     │  │     │  │  ├─ gc.pyi
│  │     │  │     │  │  ├─ getopt.pyi
│  │     │  │     │  │  ├─ getpass.pyi
│  │     │  │     │  │  ├─ gettext.pyi
│  │     │  │     │  │  ├─ glob.pyi
│  │     │  │     │  │  ├─ gzip.pyi
│  │     │  │     │  │  ├─ hashlib.pyi
│  │     │  │     │  │  ├─ heapq.pyi
│  │     │  │     │  │  ├─ html
│  │     │  │     │  │  │  ├─ entities.pyi
│  │     │  │     │  │  │  ├─ parser.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ http
│  │     │  │     │  │  │  ├─ client.pyi
│  │     │  │     │  │  │  ├─ cookiejar.pyi
│  │     │  │     │  │  │  ├─ cookies.pyi
│  │     │  │     │  │  │  ├─ server.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ imp.pyi
│  │     │  │     │  │  ├─ importlib
│  │     │  │     │  │  │  ├─ abc.pyi
│  │     │  │     │  │  │  ├─ machinery.pyi
│  │     │  │     │  │  │  ├─ metadata.pyi
│  │     │  │     │  │  │  ├─ resources.pyi
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ inspect.pyi
│  │     │  │     │  │  ├─ io.pyi
│  │     │  │     │  │  ├─ ipaddress.pyi
│  │     │  │     │  │  ├─ itertools.pyi
│  │     │  │     │  │  ├─ json
│  │     │  │     │  │  │  ├─ decoder.pyi
│  │     │  │     │  │  │  ├─ encoder.pyi
│  │     │  │     │  │  │  ├─ tool.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ lzma.pyi
│  │     │  │     │  │  ├─ macurl2path.pyi
│  │     │  │     │  │  ├─ multiprocessing
│  │     │  │     │  │  │  ├─ connection.pyi
│  │     │  │     │  │  │  ├─ context.pyi
│  │     │  │     │  │  │  ├─ dummy
│  │     │  │     │  │  │  │  ├─ connection.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ managers.pyi
│  │     │  │     │  │  │  ├─ pool.pyi
│  │     │  │     │  │  │  ├─ process.pyi
│  │     │  │     │  │  │  ├─ queues.pyi
│  │     │  │     │  │  │  ├─ sharedctypes.pyi
│  │     │  │     │  │  │  ├─ shared_memory.pyi
│  │     │  │     │  │  │  ├─ spawn.pyi
│  │     │  │     │  │  │  ├─ synchronize.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ nntplib.pyi
│  │     │  │     │  │  ├─ ntpath.pyi
│  │     │  │     │  │  ├─ nturl2path.pyi
│  │     │  │     │  │  ├─ os
│  │     │  │     │  │  │  ├─ path.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ pathlib.pyi
│  │     │  │     │  │  ├─ pipes.pyi
│  │     │  │     │  │  ├─ platform.pyi
│  │     │  │     │  │  ├─ posix.pyi
│  │     │  │     │  │  ├─ posixpath.pyi
│  │     │  │     │  │  ├─ queue.pyi
│  │     │  │     │  │  ├─ random.pyi
│  │     │  │     │  │  ├─ re.pyi
│  │     │  │     │  │  ├─ reprlib.pyi
│  │     │  │     │  │  ├─ resource.pyi
│  │     │  │     │  │  ├─ runpy.pyi
│  │     │  │     │  │  ├─ secrets.pyi
│  │     │  │     │  │  ├─ selectors.pyi
│  │     │  │     │  │  ├─ shelve.pyi
│  │     │  │     │  │  ├─ shlex.pyi
│  │     │  │     │  │  ├─ signal.pyi
│  │     │  │     │  │  ├─ smtplib.pyi
│  │     │  │     │  │  ├─ socketserver.pyi
│  │     │  │     │  │  ├─ spwd.pyi
│  │     │  │     │  │  ├─ sre_constants.pyi
│  │     │  │     │  │  ├─ sre_parse.pyi
│  │     │  │     │  │  ├─ stat.pyi
│  │     │  │     │  │  ├─ statistics.pyi
│  │     │  │     │  │  ├─ string.pyi
│  │     │  │     │  │  ├─ subprocess.pyi
│  │     │  │     │  │  ├─ symbol.pyi
│  │     │  │     │  │  ├─ sys.pyi
│  │     │  │     │  │  ├─ tempfile.pyi
│  │     │  │     │  │  ├─ textwrap.pyi
│  │     │  │     │  │  ├─ tkinter
│  │     │  │     │  │  │  ├─ commondialog.pyi
│  │     │  │     │  │  │  ├─ constants.pyi
│  │     │  │     │  │  │  ├─ dialog.pyi
│  │     │  │     │  │  │  ├─ filedialog.pyi
│  │     │  │     │  │  │  ├─ font.pyi
│  │     │  │     │  │  │  ├─ messagebox.pyi
│  │     │  │     │  │  │  ├─ ttk.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ tokenize.pyi
│  │     │  │     │  │  ├─ tracemalloc.pyi
│  │     │  │     │  │  ├─ types.pyi
│  │     │  │     │  │  ├─ typing.pyi
│  │     │  │     │  │  ├─ unittest
│  │     │  │     │  │  │  ├─ async_case.pyi
│  │     │  │     │  │  │  ├─ case.pyi
│  │     │  │     │  │  │  ├─ loader.pyi
│  │     │  │     │  │  │  ├─ main.pyi
│  │     │  │     │  │  │  ├─ mock.pyi
│  │     │  │     │  │  │  ├─ result.pyi
│  │     │  │     │  │  │  ├─ runner.pyi
│  │     │  │     │  │  │  ├─ signals.pyi
│  │     │  │     │  │  │  ├─ suite.pyi
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ urllib
│  │     │  │     │  │  │  ├─ error.pyi
│  │     │  │     │  │  │  ├─ parse.pyi
│  │     │  │     │  │  │  ├─ request.pyi
│  │     │  │     │  │  │  ├─ response.pyi
│  │     │  │     │  │  │  ├─ robotparser.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ venv
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ winreg.pyi
│  │     │  │     │  │  ├─ xmlrpc
│  │     │  │     │  │  │  ├─ client.pyi
│  │     │  │     │  │  │  ├─ server.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ xxlimited.pyi
│  │     │  │     │  │  ├─ zipapp.pyi
│  │     │  │     │  │  ├─ _ast.pyi
│  │     │  │     │  │  ├─ _bootlocale.pyi
│  │     │  │     │  │  ├─ _compat_pickle.pyi
│  │     │  │     │  │  ├─ _compression.pyi
│  │     │  │     │  │  ├─ _decimal.pyi
│  │     │  │     │  │  ├─ _dummy_thread.pyi
│  │     │  │     │  │  ├─ _imp.pyi
│  │     │  │     │  │  ├─ _importlib_modulespec.pyi
│  │     │  │     │  │  ├─ _json.pyi
│  │     │  │     │  │  ├─ _markupbase.pyi
│  │     │  │     │  │  ├─ _operator.pyi
│  │     │  │     │  │  ├─ _osx_support.pyi
│  │     │  │     │  │  ├─ _posixsubprocess.pyi
│  │     │  │     │  │  ├─ _pydecimal.pyi
│  │     │  │     │  │  ├─ _sitebuiltins.pyi
│  │     │  │     │  │  ├─ _stat.pyi
│  │     │  │     │  │  ├─ _thread.pyi
│  │     │  │     │  │  ├─ _threading_local.pyi
│  │     │  │     │  │  ├─ _tkinter.pyi
│  │     │  │     │  │  ├─ _tracemalloc.pyi
│  │     │  │     │  │  └─ _winapi.pyi
│  │     │  │     │  ├─ 3.7
│  │     │  │     │  │  ├─ contextvars.pyi
│  │     │  │     │  │  ├─ dataclasses.pyi
│  │     │  │     │  │  └─ _py_abc.pyi
│  │     │  │     │  └─ 3.9
│  │     │  │     │     ├─ graphlib.pyi
│  │     │  │     │     └─ zoneinfo
│  │     │  │     │        └─ __init__.pyi
│  │     │  │     └─ third_party
│  │     │  │        ├─ 2
│  │     │  │        │  ├─ concurrent
│  │     │  │        │  │  ├─ futures
│  │     │  │        │  │  │  ├─ process.pyi
│  │     │  │        │  │  │  ├─ thread.pyi
│  │     │  │        │  │  │  ├─ _base.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ enum.pyi
│  │     │  │        │  ├─ fb303
│  │     │  │        │  │  ├─ FacebookService.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ ipaddress.pyi
│  │     │  │        │  ├─ kazoo
│  │     │  │        │  │  ├─ client.pyi
│  │     │  │        │  │  ├─ exceptions.pyi
│  │     │  │        │  │  ├─ recipe
│  │     │  │        │  │  │  ├─ watchers.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ OpenSSL
│  │     │  │        │  │  ├─ crypto.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ pathlib2.pyi
│  │     │  │        │  ├─ pymssql.pyi
│  │     │  │        │  ├─ routes
│  │     │  │        │  │  ├─ mapper.pyi
│  │     │  │        │  │  ├─ util.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ scribe
│  │     │  │        │  │  ├─ scribe.pyi
│  │     │  │        │  │  ├─ ttypes.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ six
│  │     │  │        │  │  ├─ moves
│  │     │  │        │  │  │  ├─ BaseHTTPServer.pyi
│  │     │  │        │  │  │  ├─ CGIHTTPServer.pyi
│  │     │  │        │  │  │  ├─ collections_abc.pyi
│  │     │  │        │  │  │  ├─ configparser.pyi
│  │     │  │        │  │  │  ├─ cPickle.pyi
│  │     │  │        │  │  │  ├─ email_mime_base.pyi
│  │     │  │        │  │  │  ├─ email_mime_multipart.pyi
│  │     │  │        │  │  │  ├─ email_mime_nonmultipart.pyi
│  │     │  │        │  │  │  ├─ email_mime_text.pyi
│  │     │  │        │  │  │  ├─ html_entities.pyi
│  │     │  │        │  │  │  ├─ html_parser.pyi
│  │     │  │        │  │  │  ├─ http_client.pyi
│  │     │  │        │  │  │  ├─ http_cookiejar.pyi
│  │     │  │        │  │  │  ├─ http_cookies.pyi
│  │     │  │        │  │  │  ├─ queue.pyi
│  │     │  │        │  │  │  ├─ reprlib.pyi
│  │     │  │        │  │  │  ├─ SimpleHTTPServer.pyi
│  │     │  │        │  │  │  ├─ socketserver.pyi
│  │     │  │        │  │  │  ├─ urllib
│  │     │  │        │  │  │  │  ├─ error.pyi
│  │     │  │        │  │  │  │  ├─ parse.pyi
│  │     │  │        │  │  │  │  ├─ request.pyi
│  │     │  │        │  │  │  │  ├─ response.pyi
│  │     │  │        │  │  │  │  ├─ robotparser.pyi
│  │     │  │        │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  ├─ urllib_error.pyi
│  │     │  │        │  │  │  ├─ urllib_parse.pyi
│  │     │  │        │  │  │  ├─ urllib_request.pyi
│  │     │  │        │  │  │  ├─ urllib_response.pyi
│  │     │  │        │  │  │  ├─ urllib_robotparser.pyi
│  │     │  │        │  │  │  ├─ xmlrpc_client.pyi
│  │     │  │        │  │  │  ├─ _dummy_thread.pyi
│  │     │  │        │  │  │  ├─ _thread.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  └─ tornado
│  │     │  │        │     ├─ concurrent.pyi
│  │     │  │        │     ├─ gen.pyi
│  │     │  │        │     ├─ httpclient.pyi
│  │     │  │        │     ├─ httpserver.pyi
│  │     │  │        │     ├─ httputil.pyi
│  │     │  │        │     ├─ ioloop.pyi
│  │     │  │        │     ├─ locks.pyi
│  │     │  │        │     ├─ netutil.pyi
│  │     │  │        │     ├─ process.pyi
│  │     │  │        │     ├─ tcpserver.pyi
│  │     │  │        │     ├─ testing.pyi
│  │     │  │        │     ├─ util.pyi
│  │     │  │        │     ├─ web.pyi
│  │     │  │        │     └─ __init__.pyi
│  │     │  │        ├─ 2and3
│  │     │  │        │  ├─ atomicwrites
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ attr
│  │     │  │        │  │  ├─ converters.pyi
│  │     │  │        │  │  ├─ exceptions.pyi
│  │     │  │        │  │  ├─ filters.pyi
│  │     │  │        │  │  ├─ validators.pyi
│  │     │  │        │  │  ├─ _version_info.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ backports
│  │     │  │        │  │  ├─ ssl_match_hostname.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ backports_abc.pyi
│  │     │  │        │  ├─ bleach
│  │     │  │        │  │  ├─ callbacks.pyi
│  │     │  │        │  │  ├─ linkifier.pyi
│  │     │  │        │  │  ├─ sanitizer.pyi
│  │     │  │        │  │  ├─ utils.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ boto
│  │     │  │        │  │  ├─ auth.pyi
│  │     │  │        │  │  ├─ auth_handler.pyi
│  │     │  │        │  │  ├─ compat.pyi
│  │     │  │        │  │  ├─ connection.pyi
│  │     │  │        │  │  ├─ ec2
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ elb
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ exception.pyi
│  │     │  │        │  │  ├─ kms
│  │     │  │        │  │  │  ├─ exceptions.pyi
│  │     │  │        │  │  │  ├─ layer1.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ plugin.pyi
│  │     │  │        │  │  ├─ regioninfo.pyi
│  │     │  │        │  │  ├─ s3
│  │     │  │        │  │  │  ├─ acl.pyi
│  │     │  │        │  │  │  ├─ bucket.pyi
│  │     │  │        │  │  │  ├─ bucketlistresultset.pyi
│  │     │  │        │  │  │  ├─ bucketlogging.pyi
│  │     │  │        │  │  │  ├─ connection.pyi
│  │     │  │        │  │  │  ├─ cors.pyi
│  │     │  │        │  │  │  ├─ deletemarker.pyi
│  │     │  │        │  │  │  ├─ key.pyi
│  │     │  │        │  │  │  ├─ keyfile.pyi
│  │     │  │        │  │  │  ├─ lifecycle.pyi
│  │     │  │        │  │  │  ├─ multidelete.pyi
│  │     │  │        │  │  │  ├─ multipart.pyi
│  │     │  │        │  │  │  ├─ prefix.pyi
│  │     │  │        │  │  │  ├─ tagging.pyi
│  │     │  │        │  │  │  ├─ user.pyi
│  │     │  │        │  │  │  ├─ website.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ utils.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ cachetools
│  │     │  │        │  │  ├─ abc.pyi
│  │     │  │        │  │  ├─ cache.pyi
│  │     │  │        │  │  ├─ decorators.pyi
│  │     │  │        │  │  ├─ func.pyi
│  │     │  │        │  │  ├─ lfu.pyi
│  │     │  │        │  │  ├─ lru.pyi
│  │     │  │        │  │  ├─ rr.pyi
│  │     │  │        │  │  ├─ ttl.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ certifi.pyi
│  │     │  │        │  ├─ characteristic
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ chardet
│  │     │  │        │  │  ├─ enums.pyi
│  │     │  │        │  │  ├─ langbulgarianmodel.pyi
│  │     │  │        │  │  ├─ langcyrillicmodel.pyi
│  │     │  │        │  │  ├─ langgreekmodel.pyi
│  │     │  │        │  │  ├─ langhebrewmodel.pyi
│  │     │  │        │  │  ├─ langhungarianmodel.pyi
│  │     │  │        │  │  ├─ langthaimodel.pyi
│  │     │  │        │  │  ├─ langturkishmodel.pyi
│  │     │  │        │  │  ├─ universaldetector.pyi
│  │     │  │        │  │  ├─ version.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ click
│  │     │  │        │  │  ├─ core.pyi
│  │     │  │        │  │  ├─ decorators.pyi
│  │     │  │        │  │  ├─ exceptions.pyi
│  │     │  │        │  │  ├─ formatting.pyi
│  │     │  │        │  │  ├─ globals.pyi
│  │     │  │        │  │  ├─ parser.pyi
│  │     │  │        │  │  ├─ termui.pyi
│  │     │  │        │  │  ├─ testing.pyi
│  │     │  │        │  │  ├─ types.pyi
│  │     │  │        │  │  ├─ utils.pyi
│  │     │  │        │  │  ├─ _termui_impl.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ croniter.pyi
│  │     │  │        │  ├─ cryptography
│  │     │  │        │  │  ├─ exceptions.pyi
│  │     │  │        │  │  ├─ fernet.pyi
│  │     │  │        │  │  ├─ hazmat
│  │     │  │        │  │  │  ├─ backends
│  │     │  │        │  │  │  │  ├─ interfaces.pyi
│  │     │  │        │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  ├─ bindings
│  │     │  │        │  │  │  │  ├─ openssl
│  │     │  │        │  │  │  │  │  ├─ binding.pyi
│  │     │  │        │  │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  ├─ primitives
│  │     │  │        │  │  │  │  ├─ asymmetric
│  │     │  │        │  │  │  │  │  ├─ dh.pyi
│  │     │  │        │  │  │  │  │  ├─ dsa.pyi
│  │     │  │        │  │  │  │  │  ├─ ec.pyi
│  │     │  │        │  │  │  │  │  ├─ ed25519.pyi
│  │     │  │        │  │  │  │  │  ├─ ed448.pyi
│  │     │  │        │  │  │  │  │  ├─ padding.pyi
│  │     │  │        │  │  │  │  │  ├─ rsa.pyi
│  │     │  │        │  │  │  │  │  ├─ utils.pyi
│  │     │  │        │  │  │  │  │  ├─ x25519.pyi
│  │     │  │        │  │  │  │  │  ├─ x448.pyi
│  │     │  │        │  │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  │  ├─ ciphers
│  │     │  │        │  │  │  │  │  ├─ aead.pyi
│  │     │  │        │  │  │  │  │  ├─ algorithms.pyi
│  │     │  │        │  │  │  │  │  ├─ modes.pyi
│  │     │  │        │  │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  │  ├─ cmac.pyi
│  │     │  │        │  │  │  │  ├─ constant_time.pyi
│  │     │  │        │  │  │  │  ├─ hashes.pyi
│  │     │  │        │  │  │  │  ├─ hmac.pyi
│  │     │  │        │  │  │  │  ├─ kdf
│  │     │  │        │  │  │  │  │  ├─ concatkdf.pyi
│  │     │  │        │  │  │  │  │  ├─ hkdf.pyi
│  │     │  │        │  │  │  │  │  ├─ kbkdf.pyi
│  │     │  │        │  │  │  │  │  ├─ pbkdf2.pyi
│  │     │  │        │  │  │  │  │  ├─ scrypt.pyi
│  │     │  │        │  │  │  │  │  ├─ x963kdf.pyi
│  │     │  │        │  │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  │  ├─ keywrap.pyi
│  │     │  │        │  │  │  │  ├─ padding.pyi
│  │     │  │        │  │  │  │  ├─ poly1305.pyi
│  │     │  │        │  │  │  │  ├─ serialization
│  │     │  │        │  │  │  │  │  ├─ pkcs12.pyi
│  │     │  │        │  │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  │  ├─ twofactor
│  │     │  │        │  │  │  │  │  ├─ hotp.pyi
│  │     │  │        │  │  │  │  │  ├─ totp.pyi
│  │     │  │        │  │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ x509
│  │     │  │        │  │  │  ├─ extensions.pyi
│  │     │  │        │  │  │  ├─ oid.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ dateparser.pyi
│  │     │  │        │  ├─ datetimerange
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ dateutil
│  │     │  │        │  │  ├─ easter.pyi
│  │     │  │        │  │  ├─ parser.pyi
│  │     │  │        │  │  ├─ relativedelta.pyi
│  │     │  │        │  │  ├─ rrule.pyi
│  │     │  │        │  │  ├─ tz
│  │     │  │        │  │  │  ├─ tz.pyi
│  │     │  │        │  │  │  ├─ _common.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ utils.pyi
│  │     │  │        │  │  ├─ _common.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ decorator.pyi
│  │     │  │        │  ├─ deprecated
│  │     │  │        │  │  ├─ classic.pyi
│  │     │  │        │  │  ├─ sphinx.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ emoji
│  │     │  │        │  │  ├─ core.pyi
│  │     │  │        │  │  ├─ unicode_codes.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ first.pyi
│  │     │  │        │  ├─ flask
│  │     │  │        │  │  ├─ app.pyi
│  │     │  │        │  │  ├─ blueprints.pyi
│  │     │  │        │  │  ├─ cli.pyi
│  │     │  │        │  │  ├─ config.pyi
│  │     │  │        │  │  ├─ ctx.pyi
│  │     │  │        │  │  ├─ debughelpers.pyi
│  │     │  │        │  │  ├─ globals.pyi
│  │     │  │        │  │  ├─ helpers.pyi
│  │     │  │        │  │  ├─ json
│  │     │  │        │  │  │  ├─ tag.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ logging.pyi
│  │     │  │        │  │  ├─ sessions.pyi
│  │     │  │        │  │  ├─ signals.pyi
│  │     │  │        │  │  ├─ templating.pyi
│  │     │  │        │  │  ├─ testing.pyi
│  │     │  │        │  │  ├─ views.pyi
│  │     │  │        │  │  ├─ wrappers.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ geoip2
│  │     │  │        │  │  ├─ database.pyi
│  │     │  │        │  │  ├─ errors.pyi
│  │     │  │        │  │  ├─ mixins.pyi
│  │     │  │        │  │  ├─ models.pyi
│  │     │  │        │  │  ├─ records.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ gflags.pyi
│  │     │  │        │  ├─ google
│  │     │  │        │  │  ├─ protobuf
│  │     │  │        │  │  │  ├─ any_pb2.pyi
│  │     │  │        │  │  │  ├─ api_pb2.pyi
│  │     │  │        │  │  │  ├─ compiler
│  │     │  │        │  │  │  │  ├─ plugin_pb2.pyi
│  │     │  │        │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  ├─ descriptor.pyi
│  │     │  │        │  │  │  ├─ descriptor_pb2.pyi
│  │     │  │        │  │  │  ├─ descriptor_pool.pyi
│  │     │  │        │  │  │  ├─ duration_pb2.pyi
│  │     │  │        │  │  │  ├─ empty_pb2.pyi
│  │     │  │        │  │  │  ├─ field_mask_pb2.pyi
│  │     │  │        │  │  │  ├─ internal
│  │     │  │        │  │  │  │  ├─ containers.pyi
│  │     │  │        │  │  │  │  ├─ decoder.pyi
│  │     │  │        │  │  │  │  ├─ encoder.pyi
│  │     │  │        │  │  │  │  ├─ enum_type_wrapper.pyi
│  │     │  │        │  │  │  │  ├─ extension_dict.pyi
│  │     │  │        │  │  │  │  ├─ message_listener.pyi
│  │     │  │        │  │  │  │  ├─ python_message.pyi
│  │     │  │        │  │  │  │  ├─ well_known_types.pyi
│  │     │  │        │  │  │  │  ├─ wire_format.pyi
│  │     │  │        │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  ├─ json_format.pyi
│  │     │  │        │  │  │  ├─ message.pyi
│  │     │  │        │  │  │  ├─ message_factory.pyi
│  │     │  │        │  │  │  ├─ reflection.pyi
│  │     │  │        │  │  │  ├─ service.pyi
│  │     │  │        │  │  │  ├─ source_context_pb2.pyi
│  │     │  │        │  │  │  ├─ struct_pb2.pyi
│  │     │  │        │  │  │  ├─ symbol_database.pyi
│  │     │  │        │  │  │  ├─ timestamp_pb2.pyi
│  │     │  │        │  │  │  ├─ type_pb2.pyi
│  │     │  │        │  │  │  ├─ util
│  │     │  │        │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  ├─ wrappers_pb2.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ itsdangerous.pyi
│  │     │  │        │  ├─ jinja2
│  │     │  │        │  │  ├─ bccache.pyi
│  │     │  │        │  │  ├─ compiler.pyi
│  │     │  │        │  │  ├─ constants.pyi
│  │     │  │        │  │  ├─ debug.pyi
│  │     │  │        │  │  ├─ defaults.pyi
│  │     │  │        │  │  ├─ environment.pyi
│  │     │  │        │  │  ├─ exceptions.pyi
│  │     │  │        │  │  ├─ ext.pyi
│  │     │  │        │  │  ├─ filters.pyi
│  │     │  │        │  │  ├─ lexer.pyi
│  │     │  │        │  │  ├─ loaders.pyi
│  │     │  │        │  │  ├─ meta.pyi
│  │     │  │        │  │  ├─ nodes.pyi
│  │     │  │        │  │  ├─ optimizer.pyi
│  │     │  │        │  │  ├─ parser.pyi
│  │     │  │        │  │  ├─ runtime.pyi
│  │     │  │        │  │  ├─ sandbox.pyi
│  │     │  │        │  │  ├─ tests.pyi
│  │     │  │        │  │  ├─ utils.pyi
│  │     │  │        │  │  ├─ visitor.pyi
│  │     │  │        │  │  ├─ _compat.pyi
│  │     │  │        │  │  ├─ _stringdefs.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ markdown
│  │     │  │        │  │  ├─ blockparser.pyi
│  │     │  │        │  │  ├─ blockprocessors.pyi
│  │     │  │        │  │  ├─ core.pyi
│  │     │  │        │  │  ├─ extensions
│  │     │  │        │  │  │  ├─ abbr.pyi
│  │     │  │        │  │  │  ├─ admonition.pyi
│  │     │  │        │  │  │  ├─ attr_list.pyi
│  │     │  │        │  │  │  ├─ codehilite.pyi
│  │     │  │        │  │  │  ├─ def_list.pyi
│  │     │  │        │  │  │  ├─ extra.pyi
│  │     │  │        │  │  │  ├─ fenced_code.pyi
│  │     │  │        │  │  │  ├─ footnotes.pyi
│  │     │  │        │  │  │  ├─ legacy_attrs.pyi
│  │     │  │        │  │  │  ├─ legacy_em.pyi
│  │     │  │        │  │  │  ├─ md_in_html.pyi
│  │     │  │        │  │  │  ├─ meta.pyi
│  │     │  │        │  │  │  ├─ nl2br.pyi
│  │     │  │        │  │  │  ├─ sane_lists.pyi
│  │     │  │        │  │  │  ├─ smarty.pyi
│  │     │  │        │  │  │  ├─ tables.pyi
│  │     │  │        │  │  │  ├─ toc.pyi
│  │     │  │        │  │  │  ├─ wikilinks.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ inlinepatterns.pyi
│  │     │  │        │  │  ├─ pep562.pyi
│  │     │  │        │  │  ├─ postprocessors.pyi
│  │     │  │        │  │  ├─ preprocessors.pyi
│  │     │  │        │  │  ├─ serializers.pyi
│  │     │  │        │  │  ├─ treeprocessors.pyi
│  │     │  │        │  │  ├─ util.pyi
│  │     │  │        │  │  ├─ __init__.pyi
│  │     │  │        │  │  └─ __meta__.pyi
│  │     │  │        │  ├─ markupsafe
│  │     │  │        │  │  ├─ _compat.pyi
│  │     │  │        │  │  ├─ _constants.pyi
│  │     │  │        │  │  ├─ _native.pyi
│  │     │  │        │  │  ├─ _speedups.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ maxminddb
│  │     │  │        │  │  ├─ compat.pyi
│  │     │  │        │  │  ├─ const.pyi
│  │     │  │        │  │  ├─ decoder.pyi
│  │     │  │        │  │  ├─ errors.pyi
│  │     │  │        │  │  ├─ extension.pyi
│  │     │  │        │  │  ├─ reader.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ mock.pyi
│  │     │  │        │  ├─ mypy_extensions.pyi
│  │     │  │        │  ├─ nmap
│  │     │  │        │  │  ├─ nmap.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ paramiko
│  │     │  │        │  │  ├─ agent.pyi
│  │     │  │        │  │  ├─ auth_handler.pyi
│  │     │  │        │  │  ├─ ber.pyi
│  │     │  │        │  │  ├─ buffered_pipe.pyi
│  │     │  │        │  │  ├─ channel.pyi
│  │     │  │        │  │  ├─ client.pyi
│  │     │  │        │  │  ├─ common.pyi
│  │     │  │        │  │  ├─ compress.pyi
│  │     │  │        │  │  ├─ config.pyi
│  │     │  │        │  │  ├─ dsskey.pyi
│  │     │  │        │  │  ├─ ecdsakey.pyi
│  │     │  │        │  │  ├─ ed25519key.pyi
│  │     │  │        │  │  ├─ file.pyi
│  │     │  │        │  │  ├─ hostkeys.pyi
│  │     │  │        │  │  ├─ kex_curve25519.pyi
│  │     │  │        │  │  ├─ kex_ecdh_nist.pyi
│  │     │  │        │  │  ├─ kex_gex.pyi
│  │     │  │        │  │  ├─ kex_group1.pyi
│  │     │  │        │  │  ├─ kex_group14.pyi
│  │     │  │        │  │  ├─ kex_group16.pyi
│  │     │  │        │  │  ├─ kex_gss.pyi
│  │     │  │        │  │  ├─ message.pyi
│  │     │  │        │  │  ├─ packet.pyi
│  │     │  │        │  │  ├─ pipe.pyi
│  │     │  │        │  │  ├─ pkey.pyi
│  │     │  │        │  │  ├─ primes.pyi
│  │     │  │        │  │  ├─ proxy.pyi
│  │     │  │        │  │  ├─ py3compat.pyi
│  │     │  │        │  │  ├─ rsakey.pyi
│  │     │  │        │  │  ├─ server.pyi
│  │     │  │        │  │  ├─ sftp.pyi
│  │     │  │        │  │  ├─ sftp_attr.pyi
│  │     │  │        │  │  ├─ sftp_client.pyi
│  │     │  │        │  │  ├─ sftp_file.pyi
│  │     │  │        │  │  ├─ sftp_handle.pyi
│  │     │  │        │  │  ├─ sftp_server.pyi
│  │     │  │        │  │  ├─ sftp_si.pyi
│  │     │  │        │  │  ├─ ssh_exception.pyi
│  │     │  │        │  │  ├─ ssh_gss.pyi
│  │     │  │        │  │  ├─ transport.pyi
│  │     │  │        │  │  ├─ util.pyi
│  │     │  │        │  │  ├─ win_pageant.pyi
│  │     │  │        │  │  ├─ _version.pyi
│  │     │  │        │  │  ├─ _winapi.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ polib.pyi
│  │     │  │        │  ├─ pycurl.pyi
│  │     │  │        │  ├─ pymysql
│  │     │  │        │  │  ├─ charset.pyi
│  │     │  │        │  │  ├─ connections.pyi
│  │     │  │        │  │  ├─ constants
│  │     │  │        │  │  │  ├─ CLIENT.pyi
│  │     │  │        │  │  │  ├─ COMMAND.pyi
│  │     │  │        │  │  │  ├─ ER.pyi
│  │     │  │        │  │  │  ├─ FIELD_TYPE.pyi
│  │     │  │        │  │  │  ├─ FLAG.pyi
│  │     │  │        │  │  │  ├─ SERVER_STATUS.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ converters.pyi
│  │     │  │        │  │  ├─ cursors.pyi
│  │     │  │        │  │  ├─ err.pyi
│  │     │  │        │  │  ├─ times.pyi
│  │     │  │        │  │  ├─ util.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ pynamodb
│  │     │  │        │  │  ├─ attributes.pyi
│  │     │  │        │  │  ├─ connection
│  │     │  │        │  │  │  ├─ base.pyi
│  │     │  │        │  │  │  ├─ table.pyi
│  │     │  │        │  │  │  ├─ util.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ constants.pyi
│  │     │  │        │  │  ├─ exceptions.pyi
│  │     │  │        │  │  ├─ indexes.pyi
│  │     │  │        │  │  ├─ models.pyi
│  │     │  │        │  │  ├─ settings.pyi
│  │     │  │        │  │  ├─ throttle.pyi
│  │     │  │        │  │  ├─ types.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ pyre_extensions.pyi
│  │     │  │        │  ├─ pytz
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ pyVmomi
│  │     │  │        │  │  ├─ vim
│  │     │  │        │  │  │  ├─ event.pyi
│  │     │  │        │  │  │  ├─ fault.pyi
│  │     │  │        │  │  │  ├─ option.pyi
│  │     │  │        │  │  │  ├─ view.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ vmodl
│  │     │  │        │  │  │  ├─ fault.pyi
│  │     │  │        │  │  │  ├─ query.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ redis
│  │     │  │        │  │  ├─ client.pyi
│  │     │  │        │  │  ├─ connection.pyi
│  │     │  │        │  │  ├─ exceptions.pyi
│  │     │  │        │  │  ├─ utils.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ requests
│  │     │  │        │  │  ├─ adapters.pyi
│  │     │  │        │  │  ├─ api.pyi
│  │     │  │        │  │  ├─ auth.pyi
│  │     │  │        │  │  ├─ compat.pyi
│  │     │  │        │  │  ├─ cookies.pyi
│  │     │  │        │  │  ├─ exceptions.pyi
│  │     │  │        │  │  ├─ models.pyi
│  │     │  │        │  │  ├─ packages
│  │     │  │        │  │  │  ├─ urllib3
│  │     │  │        │  │  │  │  ├─ connection.pyi
│  │     │  │        │  │  │  │  ├─ connectionpool.pyi
│  │     │  │        │  │  │  │  ├─ contrib
│  │     │  │        │  │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  │  ├─ exceptions.pyi
│  │     │  │        │  │  │  │  ├─ fields.pyi
│  │     │  │        │  │  │  │  ├─ filepost.pyi
│  │     │  │        │  │  │  │  ├─ packages
│  │     │  │        │  │  │  │  │  ├─ ssl_match_hostname
│  │     │  │        │  │  │  │  │  │  ├─ _implementation.pyi
│  │     │  │        │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  │  ├─ poolmanager.pyi
│  │     │  │        │  │  │  │  ├─ request.pyi
│  │     │  │        │  │  │  │  ├─ response.pyi
│  │     │  │        │  │  │  │  ├─ util
│  │     │  │        │  │  │  │  │  ├─ connection.pyi
│  │     │  │        │  │  │  │  │  ├─ request.pyi
│  │     │  │        │  │  │  │  │  ├─ response.pyi
│  │     │  │        │  │  │  │  │  ├─ retry.pyi
│  │     │  │        │  │  │  │  │  ├─ ssl_.pyi
│  │     │  │        │  │  │  │  │  ├─ timeout.pyi
│  │     │  │        │  │  │  │  │  ├─ url.pyi
│  │     │  │        │  │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  │  ├─ _collections.pyi
│  │     │  │        │  │  │  │  └─ __init__.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ sessions.pyi
│  │     │  │        │  │  ├─ status_codes.pyi
│  │     │  │        │  │  ├─ structures.pyi
│  │     │  │        │  │  ├─ utils.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ retry
│  │     │  │        │  │  ├─ api.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ simplejson
│  │     │  │        │  │  ├─ decoder.pyi
│  │     │  │        │  │  ├─ encoder.pyi
│  │     │  │        │  │  ├─ scanner.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ singledispatch.pyi
│  │     │  │        │  ├─ slugify
│  │     │  │        │  │  ├─ slugify.pyi
│  │     │  │        │  │  ├─ special.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ tabulate.pyi
│  │     │  │        │  ├─ termcolor.pyi
│  │     │  │        │  ├─ toml.pyi
│  │     │  │        │  ├─ typing_extensions.pyi
│  │     │  │        │  ├─ tzlocal
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  ├─ ujson.pyi
│  │     │  │        │  ├─ werkzeug
│  │     │  │        │  │  ├─ contrib
│  │     │  │        │  │  │  ├─ atom.pyi
│  │     │  │        │  │  │  ├─ cache.pyi
│  │     │  │        │  │  │  ├─ fixers.pyi
│  │     │  │        │  │  │  ├─ iterio.pyi
│  │     │  │        │  │  │  ├─ jsrouting.pyi
│  │     │  │        │  │  │  ├─ limiter.pyi
│  │     │  │        │  │  │  ├─ lint.pyi
│  │     │  │        │  │  │  ├─ profiler.pyi
│  │     │  │        │  │  │  ├─ securecookie.pyi
│  │     │  │        │  │  │  ├─ sessions.pyi
│  │     │  │        │  │  │  ├─ testtools.pyi
│  │     │  │        │  │  │  ├─ wrappers.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ datastructures.pyi
│  │     │  │        │  │  ├─ debug
│  │     │  │        │  │  │  ├─ console.pyi
│  │     │  │        │  │  │  ├─ repr.pyi
│  │     │  │        │  │  │  ├─ tbtools.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ exceptions.pyi
│  │     │  │        │  │  ├─ filesystem.pyi
│  │     │  │        │  │  ├─ formparser.pyi
│  │     │  │        │  │  ├─ http.pyi
│  │     │  │        │  │  ├─ local.pyi
│  │     │  │        │  │  ├─ middleware
│  │     │  │        │  │  │  ├─ dispatcher.pyi
│  │     │  │        │  │  │  ├─ http_proxy.pyi
│  │     │  │        │  │  │  ├─ lint.pyi
│  │     │  │        │  │  │  ├─ profiler.pyi
│  │     │  │        │  │  │  ├─ proxy_fix.pyi
│  │     │  │        │  │  │  ├─ shared_data.pyi
│  │     │  │        │  │  │  └─ __init__.pyi
│  │     │  │        │  │  ├─ posixemulation.pyi
│  │     │  │        │  │  ├─ routing.pyi
│  │     │  │        │  │  ├─ script.pyi
│  │     │  │        │  │  ├─ security.pyi
│  │     │  │        │  │  ├─ serving.pyi
│  │     │  │        │  │  ├─ test.pyi
│  │     │  │        │  │  ├─ testapp.pyi
│  │     │  │        │  │  ├─ urls.pyi
│  │     │  │        │  │  ├─ useragents.pyi
│  │     │  │        │  │  ├─ utils.pyi
│  │     │  │        │  │  ├─ wrappers.pyi
│  │     │  │        │  │  ├─ wsgi.pyi
│  │     │  │        │  │  ├─ _compat.pyi
│  │     │  │        │  │  ├─ _internal.pyi
│  │     │  │        │  │  ├─ _reloader.pyi
│  │     │  │        │  │  └─ __init__.pyi
│  │     │  │        │  └─ yaml
│  │     │  │        │     ├─ composer.pyi
│  │     │  │        │     ├─ constructor.pyi
│  │     │  │        │     ├─ cyaml.pyi
│  │     │  │        │     ├─ dumper.pyi
│  │     │  │        │     ├─ emitter.pyi
│  │     │  │        │     ├─ error.pyi
│  │     │  │        │     ├─ events.pyi
│  │     │  │        │     ├─ loader.pyi
│  │     │  │        │     ├─ nodes.pyi
│  │     │  │        │     ├─ parser.pyi
│  │     │  │        │     ├─ reader.pyi
│  │     │  │        │     ├─ representer.pyi
│  │     │  │        │     ├─ resolver.pyi
│  │     │  │        │     ├─ scanner.pyi
│  │     │  │        │     ├─ serializer.pyi
│  │     │  │        │     ├─ tokens.pyi
│  │     │  │        │     └─ __init__.pyi
│  │     │  │        └─ 3
│  │     │  │           ├─ aiofiles
│  │     │  │           │  ├─ base.pyi
│  │     │  │           │  ├─ os.pyi
│  │     │  │           │  ├─ threadpool
│  │     │  │           │  │  ├─ binary.pyi
│  │     │  │           │  │  ├─ text.pyi
│  │     │  │           │  │  └─ __init__.pyi
│  │     │  │           │  └─ __init__.pyi
│  │     │  │           ├─ contextvars.pyi
│  │     │  │           ├─ dataclasses.pyi
│  │     │  │           ├─ docutils
│  │     │  │           │  ├─ examples.pyi
│  │     │  │           │  ├─ nodes.pyi
│  │     │  │           │  ├─ parsers
│  │     │  │           │  │  ├─ rst
│  │     │  │           │  │  │  ├─ nodes.pyi
│  │     │  │           │  │  │  ├─ roles.pyi
│  │     │  │           │  │  │  ├─ states.pyi
│  │     │  │           │  │  │  └─ __init__.pyi
│  │     │  │           │  │  └─ __init__.pyi
│  │     │  │           │  └─ __init__.pyi
│  │     │  │           ├─ filelock
│  │     │  │           │  └─ __init__.pyi
│  │     │  │           ├─ freezegun
│  │     │  │           │  ├─ api.pyi
│  │     │  │           │  └─ __init__.pyi
│  │     │  │           ├─ frozendict.pyi
│  │     │  │           ├─ jwt
│  │     │  │           │  ├─ algorithms.pyi
│  │     │  │           │  ├─ contrib
│  │     │  │           │  │  ├─ algorithms
│  │     │  │           │  │  │  ├─ pycrypto.pyi
│  │     │  │           │  │  │  ├─ py_ecdsa.pyi
│  │     │  │           │  │  │  └─ __init__.pyi
│  │     │  │           │  │  └─ __init__.pyi
│  │     │  │           │  └─ __init__.pyi
│  │     │  │           ├─ orjson.pyi
│  │     │  │           ├─ pkg_resources
│  │     │  │           │  ├─ py31compat.pyi
│  │     │  │           │  └─ __init__.pyi
│  │     │  │           ├─ pyrfc3339
│  │     │  │           │  ├─ generator.pyi
│  │     │  │           │  ├─ parser.pyi
│  │     │  │           │  ├─ utils.pyi
│  │     │  │           │  └─ __init__.pyi
│  │     │  │           ├─ six
│  │     │  │           │  ├─ moves
│  │     │  │           │  │  ├─ BaseHTTPServer.pyi
│  │     │  │           │  │  ├─ builtins.pyi
│  │     │  │           │  │  ├─ CGIHTTPServer.pyi
│  │     │  │           │  │  ├─ collections_abc.pyi
│  │     │  │           │  │  ├─ configparser.pyi
│  │     │  │           │  │  ├─ cPickle.pyi
│  │     │  │           │  │  ├─ email_mime_base.pyi
│  │     │  │           │  │  ├─ email_mime_multipart.pyi
│  │     │  │           │  │  ├─ email_mime_nonmultipart.pyi
│  │     │  │           │  │  ├─ email_mime_text.pyi
│  │     │  │           │  │  ├─ html_entities.pyi
│  │     │  │           │  │  ├─ html_parser.pyi
│  │     │  │           │  │  ├─ http_client.pyi
│  │     │  │           │  │  ├─ http_cookiejar.pyi
│  │     │  │           │  │  ├─ http_cookies.pyi
│  │     │  │           │  │  ├─ queue.pyi
│  │     │  │           │  │  ├─ reprlib.pyi
│  │     │  │           │  │  ├─ SimpleHTTPServer.pyi
│  │     │  │           │  │  ├─ socketserver.pyi
│  │     │  │           │  │  ├─ tkinter.pyi
│  │     │  │           │  │  ├─ tkinter_commondialog.pyi
│  │     │  │           │  │  ├─ tkinter_constants.pyi
│  │     │  │           │  │  ├─ tkinter_dialog.pyi
│  │     │  │           │  │  ├─ tkinter_filedialog.pyi
│  │     │  │           │  │  ├─ tkinter_tkfiledialog.pyi
│  │     │  │           │  │  ├─ tkinter_ttk.pyi
│  │     │  │           │  │  ├─ urllib
│  │     │  │           │  │  │  ├─ error.pyi
│  │     │  │           │  │  │  ├─ parse.pyi
│  │     │  │           │  │  │  ├─ request.pyi
│  │     │  │           │  │  │  ├─ response.pyi
│  │     │  │           │  │  │  ├─ robotparser.pyi
│  │     │  │           │  │  │  └─ __init__.pyi
│  │     │  │           │  │  ├─ urllib_error.pyi
│  │     │  │           │  │  ├─ urllib_parse.pyi
│  │     │  │           │  │  ├─ urllib_request.pyi
│  │     │  │           │  │  ├─ urllib_response.pyi
│  │     │  │           │  │  ├─ urllib_robotparser.pyi
│  │     │  │           │  │  ├─ _dummy_thread.pyi
│  │     │  │           │  │  ├─ _thread.pyi
│  │     │  │           │  │  └─ __init__.pyi
│  │     │  │           │  └─ __init__.pyi
│  │     │  │           ├─ typed_ast
│  │     │  │           │  ├─ ast27.pyi
│  │     │  │           │  ├─ ast3.pyi
│  │     │  │           │  ├─ conversions.pyi
│  │     │  │           │  └─ __init__.pyi
│  │     │  │           └─ waitress
│  │     │  │              ├─ adjustments.pyi
│  │     │  │              ├─ buffers.pyi
│  │     │  │              ├─ channel.pyi
│  │     │  │              ├─ compat.pyi
│  │     │  │              ├─ parser.pyi
│  │     │  │              ├─ proxy_headers.pyi
│  │     │  │              ├─ receiver.pyi
│  │     │  │              ├─ rfc7230.pyi
│  │     │  │              ├─ runner.pyi
│  │     │  │              ├─ server.pyi
│  │     │  │              ├─ task.pyi
│  │     │  │              ├─ trigger.pyi
│  │     │  │              ├─ utilities.pyi
│  │     │  │              ├─ wasyncore.pyi
│  │     │  │              └─ __init__.pyi
│  │     │  ├─ utils.py
│  │     │  ├─ _compatibility.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ cache.cpython-39.pyc
│  │     │     ├─ common.cpython-39.pyc
│  │     │     ├─ debug.cpython-39.pyc
│  │     │     ├─ file_io.cpython-39.pyc
│  │     │     ├─ parser_utils.cpython-39.pyc
│  │     │     ├─ settings.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ _compatibility.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ jedi-0.18.2.dist-info
│  │     │  ├─ AUTHORS.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ jinja2
│  │     │  ├─ async_utils.py
│  │     │  ├─ bccache.py
│  │     │  ├─ compiler.py
│  │     │  ├─ constants.py
│  │     │  ├─ debug.py
│  │     │  ├─ defaults.py
│  │     │  ├─ environment.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ ext.py
│  │     │  ├─ filters.py
│  │     │  ├─ idtracking.py
│  │     │  ├─ lexer.py
│  │     │  ├─ loaders.py
│  │     │  ├─ meta.py
│  │     │  ├─ nativetypes.py
│  │     │  ├─ nodes.py
│  │     │  ├─ optimizer.py
│  │     │  ├─ parser.py
│  │     │  ├─ py.typed
│  │     │  ├─ runtime.py
│  │     │  ├─ sandbox.py
│  │     │  ├─ tests.py
│  │     │  ├─ utils.py
│  │     │  ├─ visitor.py
│  │     │  ├─ _identifier.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ async_utils.cpython-39.pyc
│  │     │     ├─ bccache.cpython-39.pyc
│  │     │     ├─ compiler.cpython-39.pyc
│  │     │     ├─ constants.cpython-39.pyc
│  │     │     ├─ debug.cpython-39.pyc
│  │     │     ├─ defaults.cpython-39.pyc
│  │     │     ├─ environment.cpython-39.pyc
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ ext.cpython-39.pyc
│  │     │     ├─ filters.cpython-39.pyc
│  │     │     ├─ idtracking.cpython-39.pyc
│  │     │     ├─ lexer.cpython-39.pyc
│  │     │     ├─ loaders.cpython-39.pyc
│  │     │     ├─ meta.cpython-39.pyc
│  │     │     ├─ nativetypes.cpython-39.pyc
│  │     │     ├─ nodes.cpython-39.pyc
│  │     │     ├─ optimizer.cpython-39.pyc
│  │     │     ├─ parser.cpython-39.pyc
│  │     │     ├─ runtime.cpython-39.pyc
│  │     │     ├─ sandbox.cpython-39.pyc
│  │     │     ├─ tests.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ visitor.cpython-39.pyc
│  │     │     ├─ _identifier.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ Jinja2-3.1.2.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.rst
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ joblib
│  │     │  ├─ backports.py
│  │     │  ├─ compressor.py
│  │     │  ├─ disk.py
│  │     │  ├─ executor.py
│  │     │  ├─ externals
│  │     │  │  ├─ cloudpickle
│  │     │  │  │  ├─ cloudpickle.py
│  │     │  │  │  ├─ cloudpickle_fast.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cloudpickle.cpython-39.pyc
│  │     │  │  │     ├─ cloudpickle_fast.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ loky
│  │     │  │  │  ├─ backend
│  │     │  │  │  │  ├─ context.py
│  │     │  │  │  │  ├─ fork_exec.py
│  │     │  │  │  │  ├─ popen_loky_posix.py
│  │     │  │  │  │  ├─ popen_loky_win32.py
│  │     │  │  │  │  ├─ process.py
│  │     │  │  │  │  ├─ queues.py
│  │     │  │  │  │  ├─ reduction.py
│  │     │  │  │  │  ├─ resource_tracker.py
│  │     │  │  │  │  ├─ spawn.py
│  │     │  │  │  │  ├─ synchronize.py
│  │     │  │  │  │  ├─ utils.py
│  │     │  │  │  │  ├─ _posix_reduction.py
│  │     │  │  │  │  ├─ _win_reduction.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ context.cpython-39.pyc
│  │     │  │  │  │     ├─ fork_exec.cpython-39.pyc
│  │     │  │  │  │     ├─ popen_loky_posix.cpython-39.pyc
│  │     │  │  │  │     ├─ popen_loky_win32.cpython-39.pyc
│  │     │  │  │  │     ├─ process.cpython-39.pyc
│  │     │  │  │  │     ├─ queues.cpython-39.pyc
│  │     │  │  │  │     ├─ reduction.cpython-39.pyc
│  │     │  │  │  │     ├─ resource_tracker.cpython-39.pyc
│  │     │  │  │  │     ├─ spawn.cpython-39.pyc
│  │     │  │  │  │     ├─ synchronize.cpython-39.pyc
│  │     │  │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │  │     ├─ _posix_reduction.cpython-39.pyc
│  │     │  │  │  │     ├─ _win_reduction.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ cloudpickle_wrapper.py
│  │     │  │  │  ├─ initializers.py
│  │     │  │  │  ├─ process_executor.py
│  │     │  │  │  ├─ reusable_executor.py
│  │     │  │  │  ├─ _base.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cloudpickle_wrapper.cpython-39.pyc
│  │     │  │  │     ├─ initializers.cpython-39.pyc
│  │     │  │  │     ├─ process_executor.cpython-39.pyc
│  │     │  │  │     ├─ reusable_executor.cpython-39.pyc
│  │     │  │  │     ├─ _base.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ format_stack.py
│  │     │  ├─ func_inspect.py
│  │     │  ├─ hashing.py
│  │     │  ├─ logger.py
│  │     │  ├─ memory.py
│  │     │  ├─ my_exceptions.py
│  │     │  ├─ numpy_pickle.py
│  │     │  ├─ numpy_pickle_compat.py
│  │     │  ├─ numpy_pickle_utils.py
│  │     │  ├─ parallel.py
│  │     │  ├─ pool.py
│  │     │  ├─ test
│  │     │  │  ├─ common.py
│  │     │  │  ├─ data
│  │     │  │  │  ├─ create_numpy_pickle.py
│  │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py27_np16.gz
│  │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py27_np17.gz
│  │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py33_np18.gz
│  │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py34_np19.gz
│  │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py35_np19.gz
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.bz2
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.gzip
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.lzma
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.xz
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.bz2
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.gzip
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.lzma
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.xz
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.bz2
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.gzip
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.lzma
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.xz
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.bz2
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.gzip
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.lzma
│  │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.xz
│  │     │  │  │  ├─ joblib_0.11.0_compressed_pickle_py36_np111.gz
│  │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl
│  │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.bz2
│  │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.gzip
│  │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.lzma
│  │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.xz
│  │     │  │  │  ├─ joblib_0.8.4_compressed_pickle_py27_np17.gz
│  │     │  │  │  ├─ joblib_0.9.2_compressed_pickle_py27_np16.gz
│  │     │  │  │  ├─ joblib_0.9.2_compressed_pickle_py27_np17.gz
│  │     │  │  │  ├─ joblib_0.9.2_compressed_pickle_py34_np19.gz
│  │     │  │  │  ├─ joblib_0.9.2_compressed_pickle_py35_np19.gz
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_01.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_02.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_03.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_04.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_01.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_02.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_03.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_04.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_01.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_02.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_03.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_04.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_01.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_02.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_03.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_04.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_01.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_02.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_03.npy
│  │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_04.npy
│  │     │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz
│  │     │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_01.npy.z
│  │     │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_02.npy.z
│  │     │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_03.npy.z
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ create_numpy_pickle.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ testutils.py
│  │     │  │  ├─ test_backports.py
│  │     │  │  ├─ test_cloudpickle_wrapper.py
│  │     │  │  ├─ test_dask.py
│  │     │  │  ├─ test_deprecated_objects.py
│  │     │  │  ├─ test_disk.py
│  │     │  │  ├─ test_format_stack.py
│  │     │  │  ├─ test_func_inspect.py
│  │     │  │  ├─ test_func_inspect_special_encoding.py
│  │     │  │  ├─ test_hashing.py
│  │     │  │  ├─ test_init.py
│  │     │  │  ├─ test_logger.py
│  │     │  │  ├─ test_memmapping.py
│  │     │  │  ├─ test_memory.py
│  │     │  │  ├─ test_missing_multiprocessing.py
│  │     │  │  ├─ test_module.py
│  │     │  │  ├─ test_my_exceptions.py
│  │     │  │  ├─ test_numpy_pickle.py
│  │     │  │  ├─ test_numpy_pickle_compat.py
│  │     │  │  ├─ test_numpy_pickle_utils.py
│  │     │  │  ├─ test_parallel.py
│  │     │  │  ├─ test_store_backends.py
│  │     │  │  ├─ test_testing.py
│  │     │  │  ├─ test_utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ common.cpython-39.pyc
│  │     │  │     ├─ testutils.cpython-39.pyc
│  │     │  │     ├─ test_backports.cpython-39.pyc
│  │     │  │     ├─ test_cloudpickle_wrapper.cpython-39.pyc
│  │     │  │     ├─ test_dask.cpython-39.pyc
│  │     │  │     ├─ test_deprecated_objects.cpython-39.pyc
│  │     │  │     ├─ test_disk.cpython-39.pyc
│  │     │  │     ├─ test_format_stack.cpython-39.pyc
│  │     │  │     ├─ test_func_inspect.cpython-39.pyc
│  │     │  │     ├─ test_func_inspect_special_encoding.cpython-39.pyc
│  │     │  │     ├─ test_hashing.cpython-39.pyc
│  │     │  │     ├─ test_init.cpython-39.pyc
│  │     │  │     ├─ test_logger.cpython-39.pyc
│  │     │  │     ├─ test_memmapping.cpython-39.pyc
│  │     │  │     ├─ test_memory.cpython-39.pyc
│  │     │  │     ├─ test_missing_multiprocessing.cpython-39.pyc
│  │     │  │     ├─ test_module.cpython-39.pyc
│  │     │  │     ├─ test_my_exceptions.cpython-39.pyc
│  │     │  │     ├─ test_numpy_pickle.cpython-39.pyc
│  │     │  │     ├─ test_numpy_pickle_compat.cpython-39.pyc
│  │     │  │     ├─ test_numpy_pickle_utils.cpython-39.pyc
│  │     │  │     ├─ test_parallel.cpython-39.pyc
│  │     │  │     ├─ test_store_backends.cpython-39.pyc
│  │     │  │     ├─ test_testing.cpython-39.pyc
│  │     │  │     ├─ test_utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ testing.py
│  │     │  ├─ _cloudpickle_wrapper.py
│  │     │  ├─ _dask.py
│  │     │  ├─ _deprecated_format_stack.py
│  │     │  ├─ _deprecated_my_exceptions.py
│  │     │  ├─ _memmapping_reducer.py
│  │     │  ├─ _multiprocessing_helpers.py
│  │     │  ├─ _parallel_backends.py
│  │     │  ├─ _store_backends.py
│  │     │  ├─ _utils.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ backports.cpython-39.pyc
│  │     │     ├─ compressor.cpython-39.pyc
│  │     │     ├─ disk.cpython-39.pyc
│  │     │     ├─ executor.cpython-39.pyc
│  │     │     ├─ format_stack.cpython-39.pyc
│  │     │     ├─ func_inspect.cpython-39.pyc
│  │     │     ├─ hashing.cpython-39.pyc
│  │     │     ├─ logger.cpython-39.pyc
│  │     │     ├─ memory.cpython-39.pyc
│  │     │     ├─ my_exceptions.cpython-39.pyc
│  │     │     ├─ numpy_pickle.cpython-39.pyc
│  │     │     ├─ numpy_pickle_compat.cpython-39.pyc
│  │     │     ├─ numpy_pickle_utils.cpython-39.pyc
│  │     │     ├─ parallel.cpython-39.pyc
│  │     │     ├─ pool.cpython-39.pyc
│  │     │     ├─ testing.cpython-39.pyc
│  │     │     ├─ _cloudpickle_wrapper.cpython-39.pyc
│  │     │     ├─ _dask.cpython-39.pyc
│  │     │     ├─ _deprecated_format_stack.cpython-39.pyc
│  │     │     ├─ _deprecated_my_exceptions.cpython-39.pyc
│  │     │     ├─ _memmapping_reducer.cpython-39.pyc
│  │     │     ├─ _multiprocessing_helpers.cpython-39.pyc
│  │     │     ├─ _parallel_backends.cpython-39.pyc
│  │     │     ├─ _store_backends.cpython-39.pyc
│  │     │     ├─ _utils.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ joblib-1.2.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ jsonschema
│  │     │  ├─ benchmarks
│  │     │  │  ├─ issue232
│  │     │  │  │  └─ issue.json
│  │     │  │  ├─ issue232.py
│  │     │  │  ├─ json_schema_test_suite.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ issue232.cpython-39.pyc
│  │     │  │     ├─ json_schema_test_suite.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ cli.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ protocols.py
│  │     │  ├─ schemas
│  │     │  │  ├─ draft2019-09.json
│  │     │  │  ├─ draft2020-12.json
│  │     │  │  ├─ draft3.json
│  │     │  │  ├─ draft4.json
│  │     │  │  ├─ draft6.json
│  │     │  │  ├─ draft7.json
│  │     │  │  └─ vocabularies
│  │     │  │     ├─ draft2019-09
│  │     │  │     │  ├─ applicator
│  │     │  │     │  ├─ content
│  │     │  │     │  ├─ core
│  │     │  │     │  ├─ meta-data
│  │     │  │     │  └─ validation
│  │     │  │     └─ draft2020-12
│  │     │  │        ├─ applicator
│  │     │  │        ├─ content
│  │     │  │        ├─ core
│  │     │  │        ├─ format
│  │     │  │        ├─ format-annotation
│  │     │  │        ├─ format-assertion
│  │     │  │        ├─ meta-data
│  │     │  │        ├─ unevaluated
│  │     │  │        └─ validation
│  │     │  ├─ tests
│  │     │  │  ├─ fuzz_validate.py
│  │     │  │  ├─ test_cli.py
│  │     │  │  ├─ test_deprecations.py
│  │     │  │  ├─ test_exceptions.py
│  │     │  │  ├─ test_format.py
│  │     │  │  ├─ test_jsonschema_test_suite.py
│  │     │  │  ├─ test_types.py
│  │     │  │  ├─ test_utils.py
│  │     │  │  ├─ test_validators.py
│  │     │  │  ├─ _helpers.py
│  │     │  │  ├─ _suite.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ fuzz_validate.cpython-39.pyc
│  │     │  │     ├─ test_cli.cpython-39.pyc
│  │     │  │     ├─ test_deprecations.cpython-39.pyc
│  │     │  │     ├─ test_exceptions.cpython-39.pyc
│  │     │  │     ├─ test_format.cpython-39.pyc
│  │     │  │     ├─ test_jsonschema_test_suite.cpython-39.pyc
│  │     │  │     ├─ test_types.cpython-39.pyc
│  │     │  │     ├─ test_utils.cpython-39.pyc
│  │     │  │     ├─ test_validators.cpython-39.pyc
│  │     │  │     ├─ _helpers.cpython-39.pyc
│  │     │  │     ├─ _suite.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ validators.py
│  │     │  ├─ _format.py
│  │     │  ├─ _legacy_validators.py
│  │     │  ├─ _types.py
│  │     │  ├─ _utils.py
│  │     │  ├─ _validators.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ cli.cpython-39.pyc
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ protocols.cpython-39.pyc
│  │     │     ├─ validators.cpython-39.pyc
│  │     │     ├─ _format.cpython-39.pyc
│  │     │     ├─ _legacy_validators.cpython-39.pyc
│  │     │     ├─ _types.cpython-39.pyc
│  │     │     ├─ _utils.cpython-39.pyc
│  │     │     ├─ _validators.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ jsonschema-4.17.3.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ COPYING
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ jsonschema_spec
│  │     │  ├─ accessors.py
│  │     │  ├─ handlers
│  │     │  │  ├─ file.py
│  │     │  │  ├─ protocols.py
│  │     │  │  ├─ requests.py
│  │     │  │  ├─ urllib.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ file.cpython-39.pyc
│  │     │  │     ├─ protocols.cpython-39.pyc
│  │     │  │     ├─ requests.cpython-39.pyc
│  │     │  │     ├─ urllib.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ loaders.py
│  │     │  ├─ paths.py
│  │     │  ├─ py.typed
│  │     │  ├─ readers.py
│  │     │  ├─ utils.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ accessors.cpython-39.pyc
│  │     │     ├─ loaders.cpython-39.pyc
│  │     │     ├─ paths.cpython-39.pyc
│  │     │     ├─ readers.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ jsonschema_spec-0.1.4.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ jupyter.py
│  │     ├─ jupyter_client
│  │     │  ├─ adapter.py
│  │     │  ├─ asynchronous
│  │     │  │  ├─ client.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ client.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ blocking
│  │     │  │  ├─ client.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ client.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ channels.py
│  │     │  ├─ channelsabc.py
│  │     │  ├─ client.py
│  │     │  ├─ clientabc.py
│  │     │  ├─ connect.py
│  │     │  ├─ consoleapp.py
│  │     │  ├─ ioloop
│  │     │  │  ├─ manager.py
│  │     │  │  ├─ restarter.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ manager.cpython-39.pyc
│  │     │  │     ├─ restarter.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ jsonutil.py
│  │     │  ├─ kernelapp.py
│  │     │  ├─ kernelspec.py
│  │     │  ├─ kernelspecapp.py
│  │     │  ├─ launcher.py
│  │     │  ├─ localinterfaces.py
│  │     │  ├─ manager.py
│  │     │  ├─ managerabc.py
│  │     │  ├─ multikernelmanager.py
│  │     │  ├─ provisioning
│  │     │  │  ├─ factory.py
│  │     │  │  ├─ local_provisioner.py
│  │     │  │  ├─ provisioner_base.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ factory.cpython-39.pyc
│  │     │  │     ├─ local_provisioner.cpython-39.pyc
│  │     │  │     ├─ provisioner_base.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ restarter.py
│  │     │  ├─ runapp.py
│  │     │  ├─ session.py
│  │     │  ├─ ssh
│  │     │  │  ├─ forward.py
│  │     │  │  ├─ tunnel.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ forward.cpython-39.pyc
│  │     │  │     ├─ tunnel.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ threaded.py
│  │     │  ├─ utils.py
│  │     │  ├─ win_interrupt.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ adapter.cpython-39.pyc
│  │     │     ├─ channels.cpython-39.pyc
│  │     │     ├─ channelsabc.cpython-39.pyc
│  │     │     ├─ client.cpython-39.pyc
│  │     │     ├─ clientabc.cpython-39.pyc
│  │     │     ├─ connect.cpython-39.pyc
│  │     │     ├─ consoleapp.cpython-39.pyc
│  │     │     ├─ jsonutil.cpython-39.pyc
│  │     │     ├─ kernelapp.cpython-39.pyc
│  │     │     ├─ kernelspec.cpython-39.pyc
│  │     │     ├─ kernelspecapp.cpython-39.pyc
│  │     │     ├─ launcher.cpython-39.pyc
│  │     │     ├─ localinterfaces.cpython-39.pyc
│  │     │     ├─ manager.cpython-39.pyc
│  │     │     ├─ managerabc.cpython-39.pyc
│  │     │     ├─ multikernelmanager.cpython-39.pyc
│  │     │     ├─ restarter.cpython-39.pyc
│  │     │     ├─ runapp.cpython-39.pyc
│  │     │     ├─ session.cpython-39.pyc
│  │     │     ├─ threaded.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ win_interrupt.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ jupyter_client-8.2.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ jupyter_core
│  │     │  ├─ application.py
│  │     │  ├─ command.py
│  │     │  ├─ migrate.py
│  │     │  ├─ paths.py
│  │     │  ├─ py.typed
│  │     │  ├─ tests
│  │     │  │  ├─ dotipython
│  │     │  │  │  ├─ nbextensions
│  │     │  │  │  │  └─ myext.js
│  │     │  │  │  └─ profile_default
│  │     │  │  │     ├─ ipython_config.py
│  │     │  │  │     ├─ ipython_console_config.py
│  │     │  │  │     ├─ ipython_kernel_config.py
│  │     │  │  │     ├─ ipython_nbconvert_config.py
│  │     │  │  │     ├─ ipython_notebook_config.py
│  │     │  │  │     ├─ static
│  │     │  │  │     │  └─ custom
│  │     │  │  │     │     ├─ custom.css
│  │     │  │  │     │     └─ custom.js
│  │     │  │  │     └─ __pycache__
│  │     │  │  │        ├─ ipython_config.cpython-39.pyc
│  │     │  │  │        ├─ ipython_console_config.cpython-39.pyc
│  │     │  │  │        ├─ ipython_kernel_config.cpython-39.pyc
│  │     │  │  │        ├─ ipython_nbconvert_config.cpython-39.pyc
│  │     │  │  │        └─ ipython_notebook_config.cpython-39.pyc
│  │     │  │  ├─ dotipython_empty
│  │     │  │  │  └─ profile_default
│  │     │  │  │     ├─ ipython_config.py
│  │     │  │  │     ├─ ipython_console_config.py
│  │     │  │  │     ├─ ipython_kernel_config.py
│  │     │  │  │     ├─ ipython_nbconvert_config.py
│  │     │  │  │     ├─ ipython_notebook_config.py
│  │     │  │  │     ├─ static
│  │     │  │  │     │  └─ custom
│  │     │  │  │     │     ├─ custom.css
│  │     │  │  │     │     └─ custom.js
│  │     │  │  │     └─ __pycache__
│  │     │  │  │        ├─ ipython_config.cpython-39.pyc
│  │     │  │  │        ├─ ipython_console_config.cpython-39.pyc
│  │     │  │  │        ├─ ipython_kernel_config.cpython-39.pyc
│  │     │  │  │        ├─ ipython_nbconvert_config.cpython-39.pyc
│  │     │  │  │        └─ ipython_notebook_config.cpython-39.pyc
│  │     │  │  ├─ mocking.py
│  │     │  │  ├─ test_application.py
│  │     │  │  ├─ test_async.py
│  │     │  │  ├─ test_command.py
│  │     │  │  ├─ test_migrate.py
│  │     │  │  ├─ test_paths.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ mocking.cpython-39.pyc
│  │     │  │     ├─ test_application.cpython-39.pyc
│  │     │  │     ├─ test_async.cpython-39.pyc
│  │     │  │     ├─ test_command.cpython-39.pyc
│  │     │  │     ├─ test_migrate.cpython-39.pyc
│  │     │  │     ├─ test_paths.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ troubleshoot.py
│  │     │  ├─ utils
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ application.cpython-39.pyc
│  │     │     ├─ command.cpython-39.pyc
│  │     │     ├─ migrate.cpython-39.pyc
│  │     │     ├─ paths.cpython-39.pyc
│  │     │     ├─ troubleshoot.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ jupyter_core-5.3.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ kiwisolver
│  │     │  ├─ py.typed
│  │     │  ├─ _cext.cp39-win_amd64.pyd
│  │     │  ├─ _cext.pyi
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ kiwisolver-1.4.4.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ lazy_object_proxy
│  │     │  ├─ cext.cp39-win_amd64.pyd
│  │     │  ├─ compat.py
│  │     │  ├─ simple.py
│  │     │  ├─ slots.py
│  │     │  ├─ utils.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ compat.cpython-39.pyc
│  │     │     ├─ simple.cpython-39.pyc
│  │     │     ├─ slots.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ lazy_object_proxy-1.9.0.dist-info
│  │     │  ├─ AUTHORS.rst
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ markupsafe
│  │     │  ├─ py.typed
│  │     │  ├─ _native.py
│  │     │  ├─ _speedups.c
│  │     │  ├─ _speedups.cp39-win_amd64.pyd
│  │     │  ├─ _speedups.pyi
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ _native.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ MarkupSafe-2.1.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.rst
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ matplotlib
│  │     │  ├─ afm.py
│  │     │  ├─ animation.py
│  │     │  ├─ artist.py
│  │     │  ├─ axes
│  │     │  │  ├─ _axes.py
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _secondary_axes.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _axes.cpython-39.pyc
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _secondary_axes.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ axis.py
│  │     │  ├─ backends
│  │     │  │  ├─ backend_agg.py
│  │     │  │  ├─ backend_cairo.py
│  │     │  │  ├─ backend_gtk3.py
│  │     │  │  ├─ backend_gtk3agg.py
│  │     │  │  ├─ backend_gtk3cairo.py
│  │     │  │  ├─ backend_gtk4.py
│  │     │  │  ├─ backend_gtk4agg.py
│  │     │  │  ├─ backend_gtk4cairo.py
│  │     │  │  ├─ backend_macosx.py
│  │     │  │  ├─ backend_mixed.py
│  │     │  │  ├─ backend_nbagg.py
│  │     │  │  ├─ backend_pdf.py
│  │     │  │  ├─ backend_pgf.py
│  │     │  │  ├─ backend_ps.py
│  │     │  │  ├─ backend_qt.py
│  │     │  │  ├─ backend_qt5.py
│  │     │  │  ├─ backend_qt5agg.py
│  │     │  │  ├─ backend_qt5cairo.py
│  │     │  │  ├─ backend_qtagg.py
│  │     │  │  ├─ backend_qtcairo.py
│  │     │  │  ├─ backend_svg.py
│  │     │  │  ├─ backend_template.py
│  │     │  │  ├─ backend_tkagg.py
│  │     │  │  ├─ backend_tkcairo.py
│  │     │  │  ├─ backend_webagg.py
│  │     │  │  ├─ backend_webagg_core.py
│  │     │  │  ├─ backend_wx.py
│  │     │  │  ├─ backend_wxagg.py
│  │     │  │  ├─ backend_wxcairo.py
│  │     │  │  ├─ qt_compat.py
│  │     │  │  ├─ qt_editor
│  │     │  │  │  ├─ figureoptions.py
│  │     │  │  │  ├─ _formlayout.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ figureoptions.cpython-39.pyc
│  │     │  │  │     ├─ _formlayout.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ web_backend
│  │     │  │  │  ├─ .eslintrc.js
│  │     │  │  │  ├─ .prettierignore
│  │     │  │  │  ├─ .prettierrc
│  │     │  │  │  ├─ all_figures.html
│  │     │  │  │  ├─ css
│  │     │  │  │  │  ├─ boilerplate.css
│  │     │  │  │  │  ├─ fbm.css
│  │     │  │  │  │  ├─ mpl.css
│  │     │  │  │  │  └─ page.css
│  │     │  │  │  ├─ ipython_inline_figure.html
│  │     │  │  │  ├─ js
│  │     │  │  │  │  ├─ mpl.js
│  │     │  │  │  │  ├─ mpl_tornado.js
│  │     │  │  │  │  └─ nbagg_mpl.js
│  │     │  │  │  ├─ nbagg_uat.ipynb
│  │     │  │  │  ├─ package.json
│  │     │  │  │  └─ single_figure.html
│  │     │  │  ├─ _backend_agg.cp39-win_amd64.pyd
│  │     │  │  ├─ _backend_gtk.py
│  │     │  │  ├─ _backend_pdf_ps.py
│  │     │  │  ├─ _backend_tk.py
│  │     │  │  ├─ _tkagg.cp39-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ backend_agg.cpython-39.pyc
│  │     │  │     ├─ backend_cairo.cpython-39.pyc
│  │     │  │     ├─ backend_gtk3.cpython-39.pyc
│  │     │  │     ├─ backend_gtk3agg.cpython-39.pyc
│  │     │  │     ├─ backend_gtk3cairo.cpython-39.pyc
│  │     │  │     ├─ backend_gtk4.cpython-39.pyc
│  │     │  │     ├─ backend_gtk4agg.cpython-39.pyc
│  │     │  │     ├─ backend_gtk4cairo.cpython-39.pyc
│  │     │  │     ├─ backend_macosx.cpython-39.pyc
│  │     │  │     ├─ backend_mixed.cpython-39.pyc
│  │     │  │     ├─ backend_nbagg.cpython-39.pyc
│  │     │  │     ├─ backend_pdf.cpython-39.pyc
│  │     │  │     ├─ backend_pgf.cpython-39.pyc
│  │     │  │     ├─ backend_ps.cpython-39.pyc
│  │     │  │     ├─ backend_qt.cpython-39.pyc
│  │     │  │     ├─ backend_qt5.cpython-39.pyc
│  │     │  │     ├─ backend_qt5agg.cpython-39.pyc
│  │     │  │     ├─ backend_qt5cairo.cpython-39.pyc
│  │     │  │     ├─ backend_qtagg.cpython-39.pyc
│  │     │  │     ├─ backend_qtcairo.cpython-39.pyc
│  │     │  │     ├─ backend_svg.cpython-39.pyc
│  │     │  │     ├─ backend_template.cpython-39.pyc
│  │     │  │     ├─ backend_tkagg.cpython-39.pyc
│  │     │  │     ├─ backend_tkcairo.cpython-39.pyc
│  │     │  │     ├─ backend_webagg.cpython-39.pyc
│  │     │  │     ├─ backend_webagg_core.cpython-39.pyc
│  │     │  │     ├─ backend_wx.cpython-39.pyc
│  │     │  │     ├─ backend_wxagg.cpython-39.pyc
│  │     │  │     ├─ backend_wxcairo.cpython-39.pyc
│  │     │  │     ├─ qt_compat.cpython-39.pyc
│  │     │  │     ├─ _backend_gtk.cpython-39.pyc
│  │     │  │     ├─ _backend_pdf_ps.cpython-39.pyc
│  │     │  │     ├─ _backend_tk.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ backend_bases.py
│  │     │  ├─ backend_managers.py
│  │     │  ├─ backend_tools.py
│  │     │  ├─ bezier.py
│  │     │  ├─ category.py
│  │     │  ├─ cbook
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ cm.py
│  │     │  ├─ collections.py
│  │     │  ├─ colorbar.py
│  │     │  ├─ colors.py
│  │     │  ├─ container.py
│  │     │  ├─ contour.py
│  │     │  ├─ dates.py
│  │     │  ├─ docstring.py
│  │     │  ├─ dviread.py
│  │     │  ├─ figure.py
│  │     │  ├─ fontconfig_pattern.py
│  │     │  ├─ font_manager.py
│  │     │  ├─ ft2font.cp39-win_amd64.pyd
│  │     │  ├─ gridspec.py
│  │     │  ├─ hatch.py
│  │     │  ├─ image.py
│  │     │  ├─ layout_engine.py
│  │     │  ├─ legend.py
│  │     │  ├─ legend_handler.py
│  │     │  ├─ lines.py
│  │     │  ├─ markers.py
│  │     │  ├─ mathtext.py
│  │     │  ├─ mlab.py
│  │     │  ├─ mpl-data
│  │     │  │  ├─ fonts
│  │     │  │  │  ├─ afm
│  │     │  │  │  │  ├─ cmex10.afm
│  │     │  │  │  │  ├─ cmmi10.afm
│  │     │  │  │  │  ├─ cmr10.afm
│  │     │  │  │  │  ├─ cmsy10.afm
│  │     │  │  │  │  ├─ cmtt10.afm
│  │     │  │  │  │  ├─ pagd8a.afm
│  │     │  │  │  │  ├─ pagdo8a.afm
│  │     │  │  │  │  ├─ pagk8a.afm
│  │     │  │  │  │  ├─ pagko8a.afm
│  │     │  │  │  │  ├─ pbkd8a.afm
│  │     │  │  │  │  ├─ pbkdi8a.afm
│  │     │  │  │  │  ├─ pbkl8a.afm
│  │     │  │  │  │  ├─ pbkli8a.afm
│  │     │  │  │  │  ├─ pcrb8a.afm
│  │     │  │  │  │  ├─ pcrbo8a.afm
│  │     │  │  │  │  ├─ pcrr8a.afm
│  │     │  │  │  │  ├─ pcrro8a.afm
│  │     │  │  │  │  ├─ phvb8a.afm
│  │     │  │  │  │  ├─ phvb8an.afm
│  │     │  │  │  │  ├─ phvbo8a.afm
│  │     │  │  │  │  ├─ phvbo8an.afm
│  │     │  │  │  │  ├─ phvl8a.afm
│  │     │  │  │  │  ├─ phvlo8a.afm
│  │     │  │  │  │  ├─ phvr8a.afm
│  │     │  │  │  │  ├─ phvr8an.afm
│  │     │  │  │  │  ├─ phvro8a.afm
│  │     │  │  │  │  ├─ phvro8an.afm
│  │     │  │  │  │  ├─ pncb8a.afm
│  │     │  │  │  │  ├─ pncbi8a.afm
│  │     │  │  │  │  ├─ pncr8a.afm
│  │     │  │  │  │  ├─ pncri8a.afm
│  │     │  │  │  │  ├─ pplb8a.afm
│  │     │  │  │  │  ├─ pplbi8a.afm
│  │     │  │  │  │  ├─ pplr8a.afm
│  │     │  │  │  │  ├─ pplri8a.afm
│  │     │  │  │  │  ├─ psyr.afm
│  │     │  │  │  │  ├─ ptmb8a.afm
│  │     │  │  │  │  ├─ ptmbi8a.afm
│  │     │  │  │  │  ├─ ptmr8a.afm
│  │     │  │  │  │  ├─ ptmri8a.afm
│  │     │  │  │  │  ├─ putb8a.afm
│  │     │  │  │  │  ├─ putbi8a.afm
│  │     │  │  │  │  ├─ putr8a.afm
│  │     │  │  │  │  ├─ putri8a.afm
│  │     │  │  │  │  ├─ pzcmi8a.afm
│  │     │  │  │  │  └─ pzdr.afm
│  │     │  │  │  ├─ pdfcorefonts
│  │     │  │  │  │  ├─ Courier-Bold.afm
│  │     │  │  │  │  ├─ Courier-BoldOblique.afm
│  │     │  │  │  │  ├─ Courier-Oblique.afm
│  │     │  │  │  │  ├─ Courier.afm
│  │     │  │  │  │  ├─ Helvetica-Bold.afm
│  │     │  │  │  │  ├─ Helvetica-BoldOblique.afm
│  │     │  │  │  │  ├─ Helvetica-Oblique.afm
│  │     │  │  │  │  ├─ Helvetica.afm
│  │     │  │  │  │  ├─ readme.txt
│  │     │  │  │  │  ├─ Symbol.afm
│  │     │  │  │  │  ├─ Times-Bold.afm
│  │     │  │  │  │  ├─ Times-BoldItalic.afm
│  │     │  │  │  │  ├─ Times-Italic.afm
│  │     │  │  │  │  ├─ Times-Roman.afm
│  │     │  │  │  │  └─ ZapfDingbats.afm
│  │     │  │  │  └─ ttf
│  │     │  │  │     ├─ cmb10.ttf
│  │     │  │  │     ├─ cmex10.ttf
│  │     │  │  │     ├─ cmmi10.ttf
│  │     │  │  │     ├─ cmr10.ttf
│  │     │  │  │     ├─ cmss10.ttf
│  │     │  │  │     ├─ cmsy10.ttf
│  │     │  │  │     ├─ cmtt10.ttf
│  │     │  │  │     ├─ DejaVuSans-Bold.ttf
│  │     │  │  │     ├─ DejaVuSans-BoldOblique.ttf
│  │     │  │  │     ├─ DejaVuSans-Oblique.ttf
│  │     │  │  │     ├─ DejaVuSans.ttf
│  │     │  │  │     ├─ DejaVuSansDisplay.ttf
│  │     │  │  │     ├─ DejaVuSansMono-Bold.ttf
│  │     │  │  │     ├─ DejaVuSansMono-BoldOblique.ttf
│  │     │  │  │     ├─ DejaVuSansMono-Oblique.ttf
│  │     │  │  │     ├─ DejaVuSansMono.ttf
│  │     │  │  │     ├─ DejaVuSerif-Bold.ttf
│  │     │  │  │     ├─ DejaVuSerif-BoldItalic.ttf
│  │     │  │  │     ├─ DejaVuSerif-Italic.ttf
│  │     │  │  │     ├─ DejaVuSerif.ttf
│  │     │  │  │     ├─ DejaVuSerifDisplay.ttf
│  │     │  │  │     ├─ LICENSE_DEJAVU
│  │     │  │  │     ├─ LICENSE_STIX
│  │     │  │  │     ├─ STIXGeneral.ttf
│  │     │  │  │     ├─ STIXGeneralBol.ttf
│  │     │  │  │     ├─ STIXGeneralBolIta.ttf
│  │     │  │  │     ├─ STIXGeneralItalic.ttf
│  │     │  │  │     ├─ STIXNonUni.ttf
│  │     │  │  │     ├─ STIXNonUniBol.ttf
│  │     │  │  │     ├─ STIXNonUniBolIta.ttf
│  │     │  │  │     ├─ STIXNonUniIta.ttf
│  │     │  │  │     ├─ STIXSizFiveSymReg.ttf
│  │     │  │  │     ├─ STIXSizFourSymBol.ttf
│  │     │  │  │     ├─ STIXSizFourSymReg.ttf
│  │     │  │  │     ├─ STIXSizOneSymBol.ttf
│  │     │  │  │     ├─ STIXSizOneSymReg.ttf
│  │     │  │  │     ├─ STIXSizThreeSymBol.ttf
│  │     │  │  │     ├─ STIXSizThreeSymReg.ttf
│  │     │  │  │     ├─ STIXSizTwoSymBol.ttf
│  │     │  │  │     └─ STIXSizTwoSymReg.ttf
│  │     │  │  ├─ images
│  │     │  │  │  ├─ back-symbolic.svg
│  │     │  │  │  ├─ back.pdf
│  │     │  │  │  ├─ back.png
│  │     │  │  │  ├─ back.svg
│  │     │  │  │  ├─ back_large.png
│  │     │  │  │  ├─ filesave-symbolic.svg
│  │     │  │  │  ├─ filesave.pdf
│  │     │  │  │  ├─ filesave.png
│  │     │  │  │  ├─ filesave.svg
│  │     │  │  │  ├─ filesave_large.png
│  │     │  │  │  ├─ forward-symbolic.svg
│  │     │  │  │  ├─ forward.pdf
│  │     │  │  │  ├─ forward.png
│  │     │  │  │  ├─ forward.svg
│  │     │  │  │  ├─ forward_large.png
│  │     │  │  │  ├─ hand.pdf
│  │     │  │  │  ├─ hand.png
│  │     │  │  │  ├─ hand.svg
│  │     │  │  │  ├─ help-symbolic.svg
│  │     │  │  │  ├─ help.pdf
│  │     │  │  │  ├─ help.png
│  │     │  │  │  ├─ help.svg
│  │     │  │  │  ├─ help_large.png
│  │     │  │  │  ├─ home-symbolic.svg
│  │     │  │  │  ├─ home.pdf
│  │     │  │  │  ├─ home.png
│  │     │  │  │  ├─ home.svg
│  │     │  │  │  ├─ home_large.png
│  │     │  │  │  ├─ matplotlib.pdf
│  │     │  │  │  ├─ matplotlib.png
│  │     │  │  │  ├─ matplotlib.svg
│  │     │  │  │  ├─ matplotlib_large.png
│  │     │  │  │  ├─ move-symbolic.svg
│  │     │  │  │  ├─ move.pdf
│  │     │  │  │  ├─ move.png
│  │     │  │  │  ├─ move.svg
│  │     │  │  │  ├─ move_large.png
│  │     │  │  │  ├─ qt4_editor_options.pdf
│  │     │  │  │  ├─ qt4_editor_options.png
│  │     │  │  │  ├─ qt4_editor_options.svg
│  │     │  │  │  ├─ qt4_editor_options_large.png
│  │     │  │  │  ├─ subplots-symbolic.svg
│  │     │  │  │  ├─ subplots.pdf
│  │     │  │  │  ├─ subplots.png
│  │     │  │  │  ├─ subplots.svg
│  │     │  │  │  ├─ subplots_large.png
│  │     │  │  │  ├─ zoom_to_rect-symbolic.svg
│  │     │  │  │  ├─ zoom_to_rect.pdf
│  │     │  │  │  ├─ zoom_to_rect.png
│  │     │  │  │  ├─ zoom_to_rect.svg
│  │     │  │  │  └─ zoom_to_rect_large.png
│  │     │  │  ├─ kpsewhich.lua
│  │     │  │  ├─ matplotlibrc
│  │     │  │  ├─ plot_directive
│  │     │  │  │  └─ plot_directive.css
│  │     │  │  ├─ sample_data
│  │     │  │  │  ├─ axes_grid
│  │     │  │  │  │  └─ bivariate_normal.npy
│  │     │  │  │  ├─ data_x_x2_x3.csv
│  │     │  │  │  ├─ eeg.dat
│  │     │  │  │  ├─ embedding_in_wx3.xrc
│  │     │  │  │  ├─ goog.npz
│  │     │  │  │  ├─ grace_hopper.jpg
│  │     │  │  │  ├─ jacksboro_fault_dem.npz
│  │     │  │  │  ├─ logo2.png
│  │     │  │  │  ├─ membrane.dat
│  │     │  │  │  ├─ Minduka_Present_Blue_Pack.png
│  │     │  │  │  ├─ msft.csv
│  │     │  │  │  ├─ percent_bachelors_degrees_women_usa.csv
│  │     │  │  │  ├─ README.txt
│  │     │  │  │  ├─ s1045.ima.gz
│  │     │  │  │  ├─ Stocks.csv
│  │     │  │  │  └─ topobathy.npz
│  │     │  │  └─ stylelib
│  │     │  │     ├─ bmh.mplstyle
│  │     │  │     ├─ classic.mplstyle
│  │     │  │     ├─ dark_background.mplstyle
│  │     │  │     ├─ fast.mplstyle
│  │     │  │     ├─ fivethirtyeight.mplstyle
│  │     │  │     ├─ ggplot.mplstyle
│  │     │  │     ├─ grayscale.mplstyle
│  │     │  │     ├─ seaborn-v0_8-bright.mplstyle
│  │     │  │     ├─ seaborn-v0_8-colorblind.mplstyle
│  │     │  │     ├─ seaborn-v0_8-dark-palette.mplstyle
│  │     │  │     ├─ seaborn-v0_8-dark.mplstyle
│  │     │  │     ├─ seaborn-v0_8-darkgrid.mplstyle
│  │     │  │     ├─ seaborn-v0_8-deep.mplstyle
│  │     │  │     ├─ seaborn-v0_8-muted.mplstyle
│  │     │  │     ├─ seaborn-v0_8-notebook.mplstyle
│  │     │  │     ├─ seaborn-v0_8-paper.mplstyle
│  │     │  │     ├─ seaborn-v0_8-pastel.mplstyle
│  │     │  │     ├─ seaborn-v0_8-poster.mplstyle
│  │     │  │     ├─ seaborn-v0_8-talk.mplstyle
│  │     │  │     ├─ seaborn-v0_8-ticks.mplstyle
│  │     │  │     ├─ seaborn-v0_8-white.mplstyle
│  │     │  │     ├─ seaborn-v0_8-whitegrid.mplstyle
│  │     │  │     ├─ seaborn-v0_8.mplstyle
│  │     │  │     ├─ Solarize_Light2.mplstyle
│  │     │  │     ├─ tableau-colorblind10.mplstyle
│  │     │  │     ├─ _classic_test_patch.mplstyle
│  │     │  │     ├─ _mpl-gallery-nogrid.mplstyle
│  │     │  │     └─ _mpl-gallery.mplstyle
│  │     │  ├─ offsetbox.py
│  │     │  ├─ patches.py
│  │     │  ├─ path.py
│  │     │  ├─ patheffects.py
│  │     │  ├─ projections
│  │     │  │  ├─ geo.py
│  │     │  │  ├─ polar.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ geo.cpython-39.pyc
│  │     │  │     ├─ polar.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ pylab.py
│  │     │  ├─ pyplot.py
│  │     │  ├─ quiver.py
│  │     │  ├─ rcsetup.py
│  │     │  ├─ sankey.py
│  │     │  ├─ scale.py
│  │     │  ├─ sphinxext
│  │     │  │  ├─ mathmpl.py
│  │     │  │  ├─ plot_directive.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ mathmpl.cpython-39.pyc
│  │     │  │     ├─ plot_directive.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ spines.py
│  │     │  ├─ stackplot.py
│  │     │  ├─ streamplot.py
│  │     │  ├─ style
│  │     │  │  ├─ core.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ core.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ table.py
│  │     │  ├─ testing
│  │     │  │  ├─ compare.py
│  │     │  │  ├─ conftest.py
│  │     │  │  ├─ decorators.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ jpl_units
│  │     │  │  │  ├─ Duration.py
│  │     │  │  │  ├─ Epoch.py
│  │     │  │  │  ├─ EpochConverter.py
│  │     │  │  │  ├─ StrConverter.py
│  │     │  │  │  ├─ UnitDbl.py
│  │     │  │  │  ├─ UnitDblConverter.py
│  │     │  │  │  ├─ UnitDblFormatter.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ Duration.cpython-39.pyc
│  │     │  │  │     ├─ Epoch.cpython-39.pyc
│  │     │  │  │     ├─ EpochConverter.cpython-39.pyc
│  │     │  │  │     ├─ StrConverter.cpython-39.pyc
│  │     │  │  │     ├─ UnitDbl.cpython-39.pyc
│  │     │  │  │     ├─ UnitDblConverter.cpython-39.pyc
│  │     │  │  │     ├─ UnitDblFormatter.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ widgets.py
│  │     │  │  ├─ _markers.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ compare.cpython-39.pyc
│  │     │  │     ├─ conftest.cpython-39.pyc
│  │     │  │     ├─ decorators.cpython-39.pyc
│  │     │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │     ├─ widgets.cpython-39.pyc
│  │     │  │     ├─ _markers.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ tests
│  │     │  │  ├─ conftest.py
│  │     │  │  ├─ test_afm.py
│  │     │  │  ├─ test_agg.py
│  │     │  │  ├─ test_agg_filter.py
│  │     │  │  ├─ test_animation.py
│  │     │  │  ├─ test_api.py
│  │     │  │  ├─ test_arrow_patches.py
│  │     │  │  ├─ test_artist.py
│  │     │  │  ├─ test_axes.py
│  │     │  │  ├─ test_backends_interactive.py
│  │     │  │  ├─ test_backend_bases.py
│  │     │  │  ├─ test_backend_cairo.py
│  │     │  │  ├─ test_backend_gtk3.py
│  │     │  │  ├─ test_backend_macosx.py
│  │     │  │  ├─ test_backend_nbagg.py
│  │     │  │  ├─ test_backend_pdf.py
│  │     │  │  ├─ test_backend_pgf.py
│  │     │  │  ├─ test_backend_ps.py
│  │     │  │  ├─ test_backend_qt.py
│  │     │  │  ├─ test_backend_svg.py
│  │     │  │  ├─ test_backend_template.py
│  │     │  │  ├─ test_backend_tk.py
│  │     │  │  ├─ test_backend_tools.py
│  │     │  │  ├─ test_backend_webagg.py
│  │     │  │  ├─ test_basic.py
│  │     │  │  ├─ test_bbox_tight.py
│  │     │  │  ├─ test_category.py
│  │     │  │  ├─ test_cbook.py
│  │     │  │  ├─ test_collections.py
│  │     │  │  ├─ test_colorbar.py
│  │     │  │  ├─ test_colors.py
│  │     │  │  ├─ test_compare_images.py
│  │     │  │  ├─ test_constrainedlayout.py
│  │     │  │  ├─ test_container.py
│  │     │  │  ├─ test_contour.py
│  │     │  │  ├─ test_cycles.py
│  │     │  │  ├─ test_dates.py
│  │     │  │  ├─ test_determinism.py
│  │     │  │  ├─ test_doc.py
│  │     │  │  ├─ test_dviread.py
│  │     │  │  ├─ test_figure.py
│  │     │  │  ├─ test_fontconfig_pattern.py
│  │     │  │  ├─ test_font_manager.py
│  │     │  │  ├─ test_ft2font.py
│  │     │  │  ├─ test_getattr.py
│  │     │  │  ├─ test_gridspec.py
│  │     │  │  ├─ test_image.py
│  │     │  │  ├─ test_legend.py
│  │     │  │  ├─ test_lines.py
│  │     │  │  ├─ test_marker.py
│  │     │  │  ├─ test_mathtext.py
│  │     │  │  ├─ test_matplotlib.py
│  │     │  │  ├─ test_mlab.py
│  │     │  │  ├─ test_offsetbox.py
│  │     │  │  ├─ test_patches.py
│  │     │  │  ├─ test_path.py
│  │     │  │  ├─ test_patheffects.py
│  │     │  │  ├─ test_pickle.py
│  │     │  │  ├─ test_png.py
│  │     │  │  ├─ test_polar.py
│  │     │  │  ├─ test_preprocess_data.py
│  │     │  │  ├─ test_pyplot.py
│  │     │  │  ├─ test_quiver.py
│  │     │  │  ├─ test_rcparams.py
│  │     │  │  ├─ test_sankey.py
│  │     │  │  ├─ test_scale.py
│  │     │  │  ├─ test_simplification.py
│  │     │  │  ├─ test_skew.py
│  │     │  │  ├─ test_sphinxext.py
│  │     │  │  ├─ test_spines.py
│  │     │  │  ├─ test_streamplot.py
│  │     │  │  ├─ test_style.py
│  │     │  │  ├─ test_subplots.py
│  │     │  │  ├─ test_table.py
│  │     │  │  ├─ test_testing.py
│  │     │  │  ├─ test_texmanager.py
│  │     │  │  ├─ test_text.py
│  │     │  │  ├─ test_textpath.py
│  │     │  │  ├─ test_ticker.py
│  │     │  │  ├─ test_tightlayout.py
│  │     │  │  ├─ test_transforms.py
│  │     │  │  ├─ test_triangulation.py
│  │     │  │  ├─ test_ttconv.py
│  │     │  │  ├─ test_type1font.py
│  │     │  │  ├─ test_units.py
│  │     │  │  ├─ test_usetex.py
│  │     │  │  ├─ test_widgets.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ conftest.cpython-39.pyc
│  │     │  │     ├─ test_afm.cpython-39.pyc
│  │     │  │     ├─ test_agg.cpython-39.pyc
│  │     │  │     ├─ test_agg_filter.cpython-39.pyc
│  │     │  │     ├─ test_animation.cpython-39.pyc
│  │     │  │     ├─ test_api.cpython-39.pyc
│  │     │  │     ├─ test_arrow_patches.cpython-39.pyc
│  │     │  │     ├─ test_artist.cpython-39.pyc
│  │     │  │     ├─ test_axes.cpython-39.pyc
│  │     │  │     ├─ test_backends_interactive.cpython-39.pyc
│  │     │  │     ├─ test_backend_bases.cpython-39.pyc
│  │     │  │     ├─ test_backend_cairo.cpython-39.pyc
│  │     │  │     ├─ test_backend_gtk3.cpython-39.pyc
│  │     │  │     ├─ test_backend_macosx.cpython-39.pyc
│  │     │  │     ├─ test_backend_nbagg.cpython-39.pyc
│  │     │  │     ├─ test_backend_pdf.cpython-39.pyc
│  │     │  │     ├─ test_backend_pgf.cpython-39.pyc
│  │     │  │     ├─ test_backend_ps.cpython-39.pyc
│  │     │  │     ├─ test_backend_qt.cpython-39.pyc
│  │     │  │     ├─ test_backend_svg.cpython-39.pyc
│  │     │  │     ├─ test_backend_template.cpython-39.pyc
│  │     │  │     ├─ test_backend_tk.cpython-39.pyc
│  │     │  │     ├─ test_backend_tools.cpython-39.pyc
│  │     │  │     ├─ test_backend_webagg.cpython-39.pyc
│  │     │  │     ├─ test_basic.cpython-39.pyc
│  │     │  │     ├─ test_bbox_tight.cpython-39.pyc
│  │     │  │     ├─ test_category.cpython-39.pyc
│  │     │  │     ├─ test_cbook.cpython-39.pyc
│  │     │  │     ├─ test_collections.cpython-39.pyc
│  │     │  │     ├─ test_colorbar.cpython-39.pyc
│  │     │  │     ├─ test_colors.cpython-39.pyc
│  │     │  │     ├─ test_compare_images.cpython-39.pyc
│  │     │  │     ├─ test_constrainedlayout.cpython-39.pyc
│  │     │  │     ├─ test_container.cpython-39.pyc
│  │     │  │     ├─ test_contour.cpython-39.pyc
│  │     │  │     ├─ test_cycles.cpython-39.pyc
│  │     │  │     ├─ test_dates.cpython-39.pyc
│  │     │  │     ├─ test_determinism.cpython-39.pyc
│  │     │  │     ├─ test_doc.cpython-39.pyc
│  │     │  │     ├─ test_dviread.cpython-39.pyc
│  │     │  │     ├─ test_figure.cpython-39.pyc
│  │     │  │     ├─ test_fontconfig_pattern.cpython-39.pyc
│  │     │  │     ├─ test_font_manager.cpython-39.pyc
│  │     │  │     ├─ test_ft2font.cpython-39.pyc
│  │     │  │     ├─ test_getattr.cpython-39.pyc
│  │     │  │     ├─ test_gridspec.cpython-39.pyc
│  │     │  │     ├─ test_image.cpython-39.pyc
│  │     │  │     ├─ test_legend.cpython-39.pyc
│  │     │  │     ├─ test_lines.cpython-39.pyc
│  │     │  │     ├─ test_marker.cpython-39.pyc
│  │     │  │     ├─ test_mathtext.cpython-39.pyc
│  │     │  │     ├─ test_matplotlib.cpython-39.pyc
│  │     │  │     ├─ test_mlab.cpython-39.pyc
│  │     │  │     ├─ test_offsetbox.cpython-39.pyc
│  │     │  │     ├─ test_patches.cpython-39.pyc
│  │     │  │     ├─ test_path.cpython-39.pyc
│  │     │  │     ├─ test_patheffects.cpython-39.pyc
│  │     │  │     ├─ test_pickle.cpython-39.pyc
│  │     │  │     ├─ test_png.cpython-39.pyc
│  │     │  │     ├─ test_polar.cpython-39.pyc
│  │     │  │     ├─ test_preprocess_data.cpython-39.pyc
│  │     │  │     ├─ test_pyplot.cpython-39.pyc
│  │     │  │     ├─ test_quiver.cpython-39.pyc
│  │     │  │     ├─ test_rcparams.cpython-39.pyc
│  │     │  │     ├─ test_sankey.cpython-39.pyc
│  │     │  │     ├─ test_scale.cpython-39.pyc
│  │     │  │     ├─ test_simplification.cpython-39.pyc
│  │     │  │     ├─ test_skew.cpython-39.pyc
│  │     │  │     ├─ test_sphinxext.cpython-39.pyc
│  │     │  │     ├─ test_spines.cpython-39.pyc
│  │     │  │     ├─ test_streamplot.cpython-39.pyc
│  │     │  │     ├─ test_style.cpython-39.pyc
│  │     │  │     ├─ test_subplots.cpython-39.pyc
│  │     │  │     ├─ test_table.cpython-39.pyc
│  │     │  │     ├─ test_testing.cpython-39.pyc
│  │     │  │     ├─ test_texmanager.cpython-39.pyc
│  │     │  │     ├─ test_text.cpython-39.pyc
│  │     │  │     ├─ test_textpath.cpython-39.pyc
│  │     │  │     ├─ test_ticker.cpython-39.pyc
│  │     │  │     ├─ test_tightlayout.cpython-39.pyc
│  │     │  │     ├─ test_transforms.cpython-39.pyc
│  │     │  │     ├─ test_triangulation.cpython-39.pyc
│  │     │  │     ├─ test_ttconv.cpython-39.pyc
│  │     │  │     ├─ test_type1font.cpython-39.pyc
│  │     │  │     ├─ test_units.cpython-39.pyc
│  │     │  │     ├─ test_usetex.cpython-39.pyc
│  │     │  │     ├─ test_widgets.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ texmanager.py
│  │     │  ├─ text.py
│  │     │  ├─ textpath.py
│  │     │  ├─ ticker.py
│  │     │  ├─ tight_bbox.py
│  │     │  ├─ tight_layout.py
│  │     │  ├─ transforms.py
│  │     │  ├─ tri
│  │     │  │  ├─ triangulation.py
│  │     │  │  ├─ tricontour.py
│  │     │  │  ├─ trifinder.py
│  │     │  │  ├─ triinterpolate.py
│  │     │  │  ├─ tripcolor.py
│  │     │  │  ├─ triplot.py
│  │     │  │  ├─ trirefine.py
│  │     │  │  ├─ tritools.py
│  │     │  │  ├─ _triangulation.py
│  │     │  │  ├─ _tricontour.py
│  │     │  │  ├─ _trifinder.py
│  │     │  │  ├─ _triinterpolate.py
│  │     │  │  ├─ _tripcolor.py
│  │     │  │  ├─ _triplot.py
│  │     │  │  ├─ _trirefine.py
│  │     │  │  ├─ _tritools.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ triangulation.cpython-39.pyc
│  │     │  │     ├─ tricontour.cpython-39.pyc
│  │     │  │     ├─ trifinder.cpython-39.pyc
│  │     │  │     ├─ triinterpolate.cpython-39.pyc
│  │     │  │     ├─ tripcolor.cpython-39.pyc
│  │     │  │     ├─ triplot.cpython-39.pyc
│  │     │  │     ├─ trirefine.cpython-39.pyc
│  │     │  │     ├─ tritools.cpython-39.pyc
│  │     │  │     ├─ _triangulation.cpython-39.pyc
│  │     │  │     ├─ _tricontour.cpython-39.pyc
│  │     │  │     ├─ _trifinder.cpython-39.pyc
│  │     │  │     ├─ _triinterpolate.cpython-39.pyc
│  │     │  │     ├─ _tripcolor.cpython-39.pyc
│  │     │  │     ├─ _triplot.cpython-39.pyc
│  │     │  │     ├─ _trirefine.cpython-39.pyc
│  │     │  │     ├─ _tritools.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ type1font.py
│  │     │  ├─ units.py
│  │     │  ├─ widgets.py
│  │     │  ├─ _afm.py
│  │     │  ├─ _animation_data.py
│  │     │  ├─ _api
│  │     │  │  ├─ deprecation.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ deprecation.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _blocking_input.py
│  │     │  ├─ _cm.py
│  │     │  ├─ _cm_listed.py
│  │     │  ├─ _color_data.py
│  │     │  ├─ _constrained_layout.py
│  │     │  ├─ _c_internal_utils.cp39-win_amd64.pyd
│  │     │  ├─ _docstring.py
│  │     │  ├─ _enums.py
│  │     │  ├─ _fontconfig_pattern.py
│  │     │  ├─ _image.cp39-win_amd64.pyd
│  │     │  ├─ _internal_utils.py
│  │     │  ├─ _layoutgrid.py
│  │     │  ├─ _mathtext.py
│  │     │  ├─ _mathtext_data.py
│  │     │  ├─ _path.cp39-win_amd64.pyd
│  │     │  ├─ _pylab_helpers.py
│  │     │  ├─ _qhull.cp39-win_amd64.pyd
│  │     │  ├─ _text_helpers.py
│  │     │  ├─ _tight_bbox.py
│  │     │  ├─ _tight_layout.py
│  │     │  ├─ _tri.cp39-win_amd64.pyd
│  │     │  ├─ _ttconv.cp39-win_amd64.pyd
│  │     │  ├─ _type1font.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ afm.cpython-39.pyc
│  │     │     ├─ animation.cpython-39.pyc
│  │     │     ├─ artist.cpython-39.pyc
│  │     │     ├─ axis.cpython-39.pyc
│  │     │     ├─ backend_bases.cpython-39.pyc
│  │     │     ├─ backend_managers.cpython-39.pyc
│  │     │     ├─ backend_tools.cpython-39.pyc
│  │     │     ├─ bezier.cpython-39.pyc
│  │     │     ├─ category.cpython-39.pyc
│  │     │     ├─ cm.cpython-39.pyc
│  │     │     ├─ collections.cpython-39.pyc
│  │     │     ├─ colorbar.cpython-39.pyc
│  │     │     ├─ colors.cpython-39.pyc
│  │     │     ├─ container.cpython-39.pyc
│  │     │     ├─ contour.cpython-39.pyc
│  │     │     ├─ dates.cpython-39.pyc
│  │     │     ├─ docstring.cpython-39.pyc
│  │     │     ├─ dviread.cpython-39.pyc
│  │     │     ├─ figure.cpython-39.pyc
│  │     │     ├─ fontconfig_pattern.cpython-39.pyc
│  │     │     ├─ font_manager.cpython-39.pyc
│  │     │     ├─ gridspec.cpython-39.pyc
│  │     │     ├─ hatch.cpython-39.pyc
│  │     │     ├─ image.cpython-39.pyc
│  │     │     ├─ layout_engine.cpython-39.pyc
│  │     │     ├─ legend.cpython-39.pyc
│  │     │     ├─ legend_handler.cpython-39.pyc
│  │     │     ├─ lines.cpython-39.pyc
│  │     │     ├─ markers.cpython-39.pyc
│  │     │     ├─ mathtext.cpython-39.pyc
│  │     │     ├─ mlab.cpython-39.pyc
│  │     │     ├─ offsetbox.cpython-39.pyc
│  │     │     ├─ patches.cpython-39.pyc
│  │     │     ├─ path.cpython-39.pyc
│  │     │     ├─ patheffects.cpython-39.pyc
│  │     │     ├─ pylab.cpython-39.pyc
│  │     │     ├─ pyplot.cpython-39.pyc
│  │     │     ├─ quiver.cpython-39.pyc
│  │     │     ├─ rcsetup.cpython-39.pyc
│  │     │     ├─ sankey.cpython-39.pyc
│  │     │     ├─ scale.cpython-39.pyc
│  │     │     ├─ spines.cpython-39.pyc
│  │     │     ├─ stackplot.cpython-39.pyc
│  │     │     ├─ streamplot.cpython-39.pyc
│  │     │     ├─ table.cpython-39.pyc
│  │     │     ├─ texmanager.cpython-39.pyc
│  │     │     ├─ text.cpython-39.pyc
│  │     │     ├─ textpath.cpython-39.pyc
│  │     │     ├─ ticker.cpython-39.pyc
│  │     │     ├─ tight_bbox.cpython-39.pyc
│  │     │     ├─ tight_layout.cpython-39.pyc
│  │     │     ├─ transforms.cpython-39.pyc
│  │     │     ├─ type1font.cpython-39.pyc
│  │     │     ├─ units.cpython-39.pyc
│  │     │     ├─ widgets.cpython-39.pyc
│  │     │     ├─ _afm.cpython-39.pyc
│  │     │     ├─ _animation_data.cpython-39.pyc
│  │     │     ├─ _blocking_input.cpython-39.pyc
│  │     │     ├─ _cm.cpython-39.pyc
│  │     │     ├─ _cm_listed.cpython-39.pyc
│  │     │     ├─ _color_data.cpython-39.pyc
│  │     │     ├─ _constrained_layout.cpython-39.pyc
│  │     │     ├─ _docstring.cpython-39.pyc
│  │     │     ├─ _enums.cpython-39.pyc
│  │     │     ├─ _fontconfig_pattern.cpython-39.pyc
│  │     │     ├─ _internal_utils.cpython-39.pyc
│  │     │     ├─ _layoutgrid.cpython-39.pyc
│  │     │     ├─ _mathtext.cpython-39.pyc
│  │     │     ├─ _mathtext_data.cpython-39.pyc
│  │     │     ├─ _pylab_helpers.cpython-39.pyc
│  │     │     ├─ _text_helpers.cpython-39.pyc
│  │     │     ├─ _tight_bbox.cpython-39.pyc
│  │     │     ├─ _tight_layout.cpython-39.pyc
│  │     │     ├─ _type1font.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ matplotlib-3.7.1-py3.9-nspkg.pth
│  │     ├─ matplotlib-3.7.1.dist-info
│  │     │  ├─ DELVEWHEEL
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ LICENSE_AMSFONTS
│  │     │  ├─ LICENSE_BAKOMA
│  │     │  ├─ LICENSE_CARLOGO
│  │     │  ├─ LICENSE_COLORBREWER
│  │     │  ├─ LICENSE_COURIERTEN
│  │     │  ├─ LICENSE_JSXTOOLS_RESIZE_OBSERVER
│  │     │  ├─ LICENSE_QHULL
│  │     │  ├─ LICENSE_QT4_EDITOR
│  │     │  ├─ LICENSE_SOLARIZED
│  │     │  ├─ LICENSE_STIX
│  │     │  ├─ LICENSE_YORICK
│  │     │  ├─ METADATA
│  │     │  ├─ namespace_packages.txt
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ matplotlib.libs
│  │     │  ├─ .load-order-matplotlib-3.7.1
│  │     │  ├─ concrt140-926cbd79f0b5f4b2e35c5425ae9a58fd.dll
│  │     │  └─ msvcp140-e78ebc24b6ffa690be9375aacad743a7.dll
│  │     ├─ matplotlib_inline
│  │     │  ├─ backend_inline.py
│  │     │  ├─ config.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ backend_inline.cpython-39.pyc
│  │     │     ├─ config.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ matplotlib_inline-0.1.6.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ missingno
│  │     │  ├─ missingno.py
│  │     │  ├─ utils.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ missingno.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ missingno-0.5.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ mpl_toolkits
│  │     │  ├─ axes_grid1
│  │     │  │  ├─ anchored_artists.py
│  │     │  │  ├─ axes_divider.py
│  │     │  │  ├─ axes_grid.py
│  │     │  │  ├─ axes_rgb.py
│  │     │  │  ├─ axes_size.py
│  │     │  │  ├─ inset_locator.py
│  │     │  │  ├─ mpl_axes.py
│  │     │  │  ├─ parasite_axes.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_axes_grid1.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_axes_grid1.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ anchored_artists.cpython-39.pyc
│  │     │  │     ├─ axes_divider.cpython-39.pyc
│  │     │  │     ├─ axes_grid.cpython-39.pyc
│  │     │  │     ├─ axes_rgb.cpython-39.pyc
│  │     │  │     ├─ axes_size.cpython-39.pyc
│  │     │  │     ├─ inset_locator.cpython-39.pyc
│  │     │  │     ├─ mpl_axes.cpython-39.pyc
│  │     │  │     ├─ parasite_axes.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ axisartist
│  │     │  │  ├─ angle_helper.py
│  │     │  │  ├─ axes_divider.py
│  │     │  │  ├─ axes_grid.py
│  │     │  │  ├─ axes_rgb.py
│  │     │  │  ├─ axislines.py
│  │     │  │  ├─ axisline_style.py
│  │     │  │  ├─ axis_artist.py
│  │     │  │  ├─ floating_axes.py
│  │     │  │  ├─ grid_finder.py
│  │     │  │  ├─ grid_helper_curvelinear.py
│  │     │  │  ├─ parasite_axes.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_angle_helper.py
│  │     │  │  │  ├─ test_axislines.py
│  │     │  │  │  ├─ test_axis_artist.py
│  │     │  │  │  ├─ test_floating_axes.py
│  │     │  │  │  ├─ test_grid_finder.py
│  │     │  │  │  ├─ test_grid_helper_curvelinear.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_angle_helper.cpython-39.pyc
│  │     │  │  │     ├─ test_axislines.cpython-39.pyc
│  │     │  │  │     ├─ test_axis_artist.cpython-39.pyc
│  │     │  │  │     ├─ test_floating_axes.cpython-39.pyc
│  │     │  │  │     ├─ test_grid_finder.cpython-39.pyc
│  │     │  │  │     ├─ test_grid_helper_curvelinear.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ angle_helper.cpython-39.pyc
│  │     │  │     ├─ axes_divider.cpython-39.pyc
│  │     │  │     ├─ axes_grid.cpython-39.pyc
│  │     │  │     ├─ axes_rgb.cpython-39.pyc
│  │     │  │     ├─ axislines.cpython-39.pyc
│  │     │  │     ├─ axisline_style.cpython-39.pyc
│  │     │  │     ├─ axis_artist.cpython-39.pyc
│  │     │  │     ├─ floating_axes.cpython-39.pyc
│  │     │  │     ├─ grid_finder.cpython-39.pyc
│  │     │  │     ├─ grid_helper_curvelinear.cpython-39.pyc
│  │     │  │     ├─ parasite_axes.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ mplot3d
│  │     │  │  ├─ art3d.py
│  │     │  │  ├─ axes3d.py
│  │     │  │  ├─ axis3d.py
│  │     │  │  ├─ proj3d.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_art3d.py
│  │     │  │  │  ├─ test_axes3d.py
│  │     │  │  │  ├─ test_legend3d.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_art3d.cpython-39.pyc
│  │     │  │  │     ├─ test_axes3d.cpython-39.pyc
│  │     │  │  │     ├─ test_legend3d.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ art3d.cpython-39.pyc
│  │     │  │     ├─ axes3d.cpython-39.pyc
│  │     │  │     ├─ axis3d.cpython-39.pyc
│  │     │  │     ├─ proj3d.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ mypy_extensions-1.0.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ mypy_extensions.py
│  │     ├─ nest_asyncio-1.5.6.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ nest_asyncio.py
│  │     ├─ numpy
│  │     │  ├─ .libs
│  │     │  │  └─ libopenblas64__v0.3.21-gcc_10_3_0.dll
│  │     │  ├─ array_api
│  │     │  │  ├─ linalg.py
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_array_object.py
│  │     │  │  │  ├─ test_creation_functions.py
│  │     │  │  │  ├─ test_data_type_functions.py
│  │     │  │  │  ├─ test_elementwise_functions.py
│  │     │  │  │  ├─ test_set_functions.py
│  │     │  │  │  ├─ test_sorting_functions.py
│  │     │  │  │  ├─ test_validation.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_array_object.cpython-39.pyc
│  │     │  │  │     ├─ test_creation_functions.cpython-39.pyc
│  │     │  │  │     ├─ test_data_type_functions.cpython-39.pyc
│  │     │  │  │     ├─ test_elementwise_functions.cpython-39.pyc
│  │     │  │  │     ├─ test_set_functions.cpython-39.pyc
│  │     │  │  │     ├─ test_sorting_functions.cpython-39.pyc
│  │     │  │  │     ├─ test_validation.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _array_object.py
│  │     │  │  ├─ _constants.py
│  │     │  │  ├─ _creation_functions.py
│  │     │  │  ├─ _data_type_functions.py
│  │     │  │  ├─ _dtypes.py
│  │     │  │  ├─ _elementwise_functions.py
│  │     │  │  ├─ _manipulation_functions.py
│  │     │  │  ├─ _searching_functions.py
│  │     │  │  ├─ _set_functions.py
│  │     │  │  ├─ _sorting_functions.py
│  │     │  │  ├─ _statistical_functions.py
│  │     │  │  ├─ _typing.py
│  │     │  │  ├─ _utility_functions.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ linalg.cpython-39.pyc
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     ├─ _array_object.cpython-39.pyc
│  │     │  │     ├─ _constants.cpython-39.pyc
│  │     │  │     ├─ _creation_functions.cpython-39.pyc
│  │     │  │     ├─ _data_type_functions.cpython-39.pyc
│  │     │  │     ├─ _dtypes.cpython-39.pyc
│  │     │  │     ├─ _elementwise_functions.cpython-39.pyc
│  │     │  │     ├─ _manipulation_functions.cpython-39.pyc
│  │     │  │     ├─ _searching_functions.cpython-39.pyc
│  │     │  │     ├─ _set_functions.cpython-39.pyc
│  │     │  │     ├─ _sorting_functions.cpython-39.pyc
│  │     │  │     ├─ _statistical_functions.cpython-39.pyc
│  │     │  │     ├─ _typing.cpython-39.pyc
│  │     │  │     ├─ _utility_functions.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ compat
│  │     │  │  ├─ py3k.py
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_compat.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_compat.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _inspect.py
│  │     │  │  ├─ _pep440.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ py3k.cpython-39.pyc
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     ├─ _inspect.cpython-39.pyc
│  │     │  │     ├─ _pep440.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ conftest.py
│  │     │  ├─ core
│  │     │  │  ├─ arrayprint.py
│  │     │  │  ├─ arrayprint.pyi
│  │     │  │  ├─ cversions.py
│  │     │  │  ├─ defchararray.py
│  │     │  │  ├─ defchararray.pyi
│  │     │  │  ├─ einsumfunc.py
│  │     │  │  ├─ einsumfunc.pyi
│  │     │  │  ├─ fromnumeric.py
│  │     │  │  ├─ fromnumeric.pyi
│  │     │  │  ├─ function_base.py
│  │     │  │  ├─ function_base.pyi
│  │     │  │  ├─ generate_numpy_api.py
│  │     │  │  ├─ getlimits.py
│  │     │  │  ├─ getlimits.pyi
│  │     │  │  ├─ include
│  │     │  │  │  └─ numpy
│  │     │  │  │     ├─ .doxyfile
│  │     │  │  │     ├─ arrayobject.h
│  │     │  │  │     ├─ arrayscalars.h
│  │     │  │  │     ├─ experimental_dtype_api.h
│  │     │  │  │     ├─ halffloat.h
│  │     │  │  │     ├─ libdivide
│  │     │  │  │     │  ├─ libdivide.h
│  │     │  │  │     │  └─ LICENSE.txt
│  │     │  │  │     ├─ multiarray_api.txt
│  │     │  │  │     ├─ ndarrayobject.h
│  │     │  │  │     ├─ ndarraytypes.h
│  │     │  │  │     ├─ noprefix.h
│  │     │  │  │     ├─ npy_1_7_deprecated_api.h
│  │     │  │  │     ├─ npy_3kcompat.h
│  │     │  │  │     ├─ npy_common.h
│  │     │  │  │     ├─ npy_cpu.h
│  │     │  │  │     ├─ npy_endian.h
│  │     │  │  │     ├─ npy_interrupt.h
│  │     │  │  │     ├─ npy_math.h
│  │     │  │  │     ├─ npy_no_deprecated_api.h
│  │     │  │  │     ├─ npy_os.h
│  │     │  │  │     ├─ numpyconfig.h
│  │     │  │  │     ├─ oldnumeric.h
│  │     │  │  │     ├─ old_defines.h
│  │     │  │  │     ├─ random
│  │     │  │  │     │  ├─ bitgen.h
│  │     │  │  │     │  └─ distributions.h
│  │     │  │  │     ├─ ufuncobject.h
│  │     │  │  │     ├─ ufunc_api.txt
│  │     │  │  │     ├─ utils.h
│  │     │  │  │     ├─ _neighborhood_iterator_imp.h
│  │     │  │  │     ├─ _numpyconfig.h
│  │     │  │  │     ├─ __multiarray_api.h
│  │     │  │  │     └─ __ufunc_api.h
│  │     │  │  ├─ lib
│  │     │  │  │  ├─ npy-pkg-config
│  │     │  │  │  │  ├─ mlib.ini
│  │     │  │  │  │  └─ npymath.ini
│  │     │  │  │  └─ npymath.lib
│  │     │  │  ├─ memmap.py
│  │     │  │  ├─ memmap.pyi
│  │     │  │  ├─ multiarray.py
│  │     │  │  ├─ multiarray.pyi
│  │     │  │  ├─ numeric.py
│  │     │  │  ├─ numeric.pyi
│  │     │  │  ├─ numerictypes.py
│  │     │  │  ├─ numerictypes.pyi
│  │     │  │  ├─ overrides.py
│  │     │  │  ├─ records.py
│  │     │  │  ├─ records.pyi
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ setup_common.py
│  │     │  │  ├─ shape_base.py
│  │     │  │  ├─ shape_base.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ astype_copy.pkl
│  │     │  │  │  │  ├─ generate_umath_validation_data.cpp
│  │     │  │  │  │  ├─ recarray_from_file.fits
│  │     │  │  │  │  ├─ umath-validation-set-arccos.csv
│  │     │  │  │  │  ├─ umath-validation-set-arccosh.csv
│  │     │  │  │  │  ├─ umath-validation-set-arcsin.csv
│  │     │  │  │  │  ├─ umath-validation-set-arcsinh.csv
│  │     │  │  │  │  ├─ umath-validation-set-arctan.csv
│  │     │  │  │  │  ├─ umath-validation-set-arctanh.csv
│  │     │  │  │  │  ├─ umath-validation-set-cbrt.csv
│  │     │  │  │  │  ├─ umath-validation-set-cos.csv
│  │     │  │  │  │  ├─ umath-validation-set-cosh.csv
│  │     │  │  │  │  ├─ umath-validation-set-exp.csv
│  │     │  │  │  │  ├─ umath-validation-set-exp2.csv
│  │     │  │  │  │  ├─ umath-validation-set-expm1.csv
│  │     │  │  │  │  ├─ umath-validation-set-log.csv
│  │     │  │  │  │  ├─ umath-validation-set-log10.csv
│  │     │  │  │  │  ├─ umath-validation-set-log1p.csv
│  │     │  │  │  │  ├─ umath-validation-set-log2.csv
│  │     │  │  │  │  ├─ umath-validation-set-README.txt
│  │     │  │  │  │  ├─ umath-validation-set-sin.csv
│  │     │  │  │  │  ├─ umath-validation-set-sinh.csv
│  │     │  │  │  │  ├─ umath-validation-set-tan.csv
│  │     │  │  │  │  └─ umath-validation-set-tanh.csv
│  │     │  │  │  ├─ examples
│  │     │  │  │  │  ├─ cython
│  │     │  │  │  │  │  ├─ checks.pyx
│  │     │  │  │  │  │  ├─ setup.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     └─ setup.cpython-39.pyc
│  │     │  │  │  │  └─ limited_api
│  │     │  │  │  │     ├─ limited_api.c
│  │     │  │  │  │     ├─ setup.py
│  │     │  │  │  │     └─ __pycache__
│  │     │  │  │  │        └─ setup.cpython-39.pyc
│  │     │  │  │  ├─ test_abc.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_argparse.py
│  │     │  │  │  ├─ test_arraymethod.py
│  │     │  │  │  ├─ test_arrayprint.py
│  │     │  │  │  ├─ test_array_coercion.py
│  │     │  │  │  ├─ test_array_interface.py
│  │     │  │  │  ├─ test_casting_floatingpoint_errors.py
│  │     │  │  │  ├─ test_casting_unittests.py
│  │     │  │  │  ├─ test_conversion_utils.py
│  │     │  │  │  ├─ test_cpu_dispatcher.py
│  │     │  │  │  ├─ test_cpu_features.py
│  │     │  │  │  ├─ test_custom_dtypes.py
│  │     │  │  │  ├─ test_cython.py
│  │     │  │  │  ├─ test_datetime.py
│  │     │  │  │  ├─ test_defchararray.py
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_dlpack.py
│  │     │  │  │  ├─ test_dtype.py
│  │     │  │  │  ├─ test_einsum.py
│  │     │  │  │  ├─ test_errstate.py
│  │     │  │  │  ├─ test_extint128.py
│  │     │  │  │  ├─ test_function_base.py
│  │     │  │  │  ├─ test_getlimits.py
│  │     │  │  │  ├─ test_half.py
│  │     │  │  │  ├─ test_hashtable.py
│  │     │  │  │  ├─ test_indexerrors.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_item_selection.py
│  │     │  │  │  ├─ test_limited_api.py
│  │     │  │  │  ├─ test_longdouble.py
│  │     │  │  │  ├─ test_machar.py
│  │     │  │  │  ├─ test_memmap.py
│  │     │  │  │  ├─ test_mem_overlap.py
│  │     │  │  │  ├─ test_mem_policy.py
│  │     │  │  │  ├─ test_multiarray.py
│  │     │  │  │  ├─ test_nditer.py
│  │     │  │  │  ├─ test_nep50_promotions.py
│  │     │  │  │  ├─ test_numeric.py
│  │     │  │  │  ├─ test_numerictypes.py
│  │     │  │  │  ├─ test_overrides.py
│  │     │  │  │  ├─ test_print.py
│  │     │  │  │  ├─ test_protocols.py
│  │     │  │  │  ├─ test_records.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_scalarbuffer.py
│  │     │  │  │  ├─ test_scalarinherit.py
│  │     │  │  │  ├─ test_scalarmath.py
│  │     │  │  │  ├─ test_scalarprint.py
│  │     │  │  │  ├─ test_scalar_ctors.py
│  │     │  │  │  ├─ test_scalar_methods.py
│  │     │  │  │  ├─ test_shape_base.py
│  │     │  │  │  ├─ test_simd.py
│  │     │  │  │  ├─ test_simd_module.py
│  │     │  │  │  ├─ test_strings.py
│  │     │  │  │  ├─ test_ufunc.py
│  │     │  │  │  ├─ test_umath.py
│  │     │  │  │  ├─ test_umath_accuracy.py
│  │     │  │  │  ├─ test_umath_complex.py
│  │     │  │  │  ├─ test_unicode.py
│  │     │  │  │  ├─ test__exceptions.py
│  │     │  │  │  ├─ _locales.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_abc.cpython-39.pyc
│  │     │  │  │     ├─ test_api.cpython-39.pyc
│  │     │  │  │     ├─ test_argparse.cpython-39.pyc
│  │     │  │  │     ├─ test_arraymethod.cpython-39.pyc
│  │     │  │  │     ├─ test_arrayprint.cpython-39.pyc
│  │     │  │  │     ├─ test_array_coercion.cpython-39.pyc
│  │     │  │  │     ├─ test_array_interface.cpython-39.pyc
│  │     │  │  │     ├─ test_casting_floatingpoint_errors.cpython-39.pyc
│  │     │  │  │     ├─ test_casting_unittests.cpython-39.pyc
│  │     │  │  │     ├─ test_conversion_utils.cpython-39.pyc
│  │     │  │  │     ├─ test_cpu_dispatcher.cpython-39.pyc
│  │     │  │  │     ├─ test_cpu_features.cpython-39.pyc
│  │     │  │  │     ├─ test_custom_dtypes.cpython-39.pyc
│  │     │  │  │     ├─ test_cython.cpython-39.pyc
│  │     │  │  │     ├─ test_datetime.cpython-39.pyc
│  │     │  │  │     ├─ test_defchararray.cpython-39.pyc
│  │     │  │  │     ├─ test_deprecations.cpython-39.pyc
│  │     │  │  │     ├─ test_dlpack.cpython-39.pyc
│  │     │  │  │     ├─ test_dtype.cpython-39.pyc
│  │     │  │  │     ├─ test_einsum.cpython-39.pyc
│  │     │  │  │     ├─ test_errstate.cpython-39.pyc
│  │     │  │  │     ├─ test_extint128.cpython-39.pyc
│  │     │  │  │     ├─ test_function_base.cpython-39.pyc
│  │     │  │  │     ├─ test_getlimits.cpython-39.pyc
│  │     │  │  │     ├─ test_half.cpython-39.pyc
│  │     │  │  │     ├─ test_hashtable.cpython-39.pyc
│  │     │  │  │     ├─ test_indexerrors.cpython-39.pyc
│  │     │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │     ├─ test_item_selection.cpython-39.pyc
│  │     │  │  │     ├─ test_limited_api.cpython-39.pyc
│  │     │  │  │     ├─ test_longdouble.cpython-39.pyc
│  │     │  │  │     ├─ test_machar.cpython-39.pyc
│  │     │  │  │     ├─ test_memmap.cpython-39.pyc
│  │     │  │  │     ├─ test_mem_overlap.cpython-39.pyc
│  │     │  │  │     ├─ test_mem_policy.cpython-39.pyc
│  │     │  │  │     ├─ test_multiarray.cpython-39.pyc
│  │     │  │  │     ├─ test_nditer.cpython-39.pyc
│  │     │  │  │     ├─ test_nep50_promotions.cpython-39.pyc
│  │     │  │  │     ├─ test_numeric.cpython-39.pyc
│  │     │  │  │     ├─ test_numerictypes.cpython-39.pyc
│  │     │  │  │     ├─ test_overrides.cpython-39.pyc
│  │     │  │  │     ├─ test_print.cpython-39.pyc
│  │     │  │  │     ├─ test_protocols.cpython-39.pyc
│  │     │  │  │     ├─ test_records.cpython-39.pyc
│  │     │  │  │     ├─ test_regression.cpython-39.pyc
│  │     │  │  │     ├─ test_scalarbuffer.cpython-39.pyc
│  │     │  │  │     ├─ test_scalarinherit.cpython-39.pyc
│  │     │  │  │     ├─ test_scalarmath.cpython-39.pyc
│  │     │  │  │     ├─ test_scalarprint.cpython-39.pyc
│  │     │  │  │     ├─ test_scalar_ctors.cpython-39.pyc
│  │     │  │  │     ├─ test_scalar_methods.cpython-39.pyc
│  │     │  │  │     ├─ test_shape_base.cpython-39.pyc
│  │     │  │  │     ├─ test_simd.cpython-39.pyc
│  │     │  │  │     ├─ test_simd_module.cpython-39.pyc
│  │     │  │  │     ├─ test_strings.cpython-39.pyc
│  │     │  │  │     ├─ test_ufunc.cpython-39.pyc
│  │     │  │  │     ├─ test_umath.cpython-39.pyc
│  │     │  │  │     ├─ test_umath_accuracy.cpython-39.pyc
│  │     │  │  │     ├─ test_umath_complex.cpython-39.pyc
│  │     │  │  │     ├─ test_unicode.cpython-39.pyc
│  │     │  │  │     ├─ test__exceptions.cpython-39.pyc
│  │     │  │  │     ├─ _locales.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ umath.py
│  │     │  │  ├─ umath_tests.py
│  │     │  │  ├─ _add_newdocs.py
│  │     │  │  ├─ _add_newdocs_scalars.py
│  │     │  │  ├─ _asarray.py
│  │     │  │  ├─ _asarray.pyi
│  │     │  │  ├─ _dtype.py
│  │     │  │  ├─ _dtype_ctypes.py
│  │     │  │  ├─ _exceptions.py
│  │     │  │  ├─ _internal.py
│  │     │  │  ├─ _internal.pyi
│  │     │  │  ├─ _machar.py
│  │     │  │  ├─ _methods.py
│  │     │  │  ├─ _multiarray_tests.cp39-win_amd64.pyd
│  │     │  │  ├─ _multiarray_umath.cp39-win_amd64.pyd
│  │     │  │  ├─ _operand_flag_tests.cp39-win_amd64.pyd
│  │     │  │  ├─ _rational_tests.cp39-win_amd64.pyd
│  │     │  │  ├─ _simd.cp39-win_amd64.pyd
│  │     │  │  ├─ _string_helpers.py
│  │     │  │  ├─ _struct_ufunc_tests.cp39-win_amd64.pyd
│  │     │  │  ├─ _type_aliases.py
│  │     │  │  ├─ _type_aliases.pyi
│  │     │  │  ├─ _ufunc_config.py
│  │     │  │  ├─ _ufunc_config.pyi
│  │     │  │  ├─ _umath_tests.cp39-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ arrayprint.cpython-39.pyc
│  │     │  │     ├─ cversions.cpython-39.pyc
│  │     │  │     ├─ defchararray.cpython-39.pyc
│  │     │  │     ├─ einsumfunc.cpython-39.pyc
│  │     │  │     ├─ fromnumeric.cpython-39.pyc
│  │     │  │     ├─ function_base.cpython-39.pyc
│  │     │  │     ├─ generate_numpy_api.cpython-39.pyc
│  │     │  │     ├─ getlimits.cpython-39.pyc
│  │     │  │     ├─ memmap.cpython-39.pyc
│  │     │  │     ├─ multiarray.cpython-39.pyc
│  │     │  │     ├─ numeric.cpython-39.pyc
│  │     │  │     ├─ numerictypes.cpython-39.pyc
│  │     │  │     ├─ overrides.cpython-39.pyc
│  │     │  │     ├─ records.cpython-39.pyc
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     ├─ setup_common.cpython-39.pyc
│  │     │  │     ├─ shape_base.cpython-39.pyc
│  │     │  │     ├─ umath.cpython-39.pyc
│  │     │  │     ├─ umath_tests.cpython-39.pyc
│  │     │  │     ├─ _add_newdocs.cpython-39.pyc
│  │     │  │     ├─ _add_newdocs_scalars.cpython-39.pyc
│  │     │  │     ├─ _asarray.cpython-39.pyc
│  │     │  │     ├─ _dtype.cpython-39.pyc
│  │     │  │     ├─ _dtype_ctypes.cpython-39.pyc
│  │     │  │     ├─ _exceptions.cpython-39.pyc
│  │     │  │     ├─ _internal.cpython-39.pyc
│  │     │  │     ├─ _machar.cpython-39.pyc
│  │     │  │     ├─ _methods.cpython-39.pyc
│  │     │  │     ├─ _string_helpers.cpython-39.pyc
│  │     │  │     ├─ _type_aliases.cpython-39.pyc
│  │     │  │     ├─ _ufunc_config.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ ctypeslib.py
│  │     │  ├─ ctypeslib.pyi
│  │     │  ├─ distutils
│  │     │  │  ├─ armccompiler.py
│  │     │  │  ├─ ccompiler.py
│  │     │  │  ├─ ccompiler_opt.py
│  │     │  │  ├─ checks
│  │     │  │  │  ├─ cpu_asimd.c
│  │     │  │  │  ├─ cpu_asimddp.c
│  │     │  │  │  ├─ cpu_asimdfhm.c
│  │     │  │  │  ├─ cpu_asimdhp.c
│  │     │  │  │  ├─ cpu_avx.c
│  │     │  │  │  ├─ cpu_avx2.c
│  │     │  │  │  ├─ cpu_avx512cd.c
│  │     │  │  │  ├─ cpu_avx512f.c
│  │     │  │  │  ├─ cpu_avx512_clx.c
│  │     │  │  │  ├─ cpu_avx512_cnl.c
│  │     │  │  │  ├─ cpu_avx512_icl.c
│  │     │  │  │  ├─ cpu_avx512_knl.c
│  │     │  │  │  ├─ cpu_avx512_knm.c
│  │     │  │  │  ├─ cpu_avx512_skx.c
│  │     │  │  │  ├─ cpu_f16c.c
│  │     │  │  │  ├─ cpu_fma3.c
│  │     │  │  │  ├─ cpu_fma4.c
│  │     │  │  │  ├─ cpu_neon.c
│  │     │  │  │  ├─ cpu_neon_fp16.c
│  │     │  │  │  ├─ cpu_neon_vfpv4.c
│  │     │  │  │  ├─ cpu_popcnt.c
│  │     │  │  │  ├─ cpu_sse.c
│  │     │  │  │  ├─ cpu_sse2.c
│  │     │  │  │  ├─ cpu_sse3.c
│  │     │  │  │  ├─ cpu_sse41.c
│  │     │  │  │  ├─ cpu_sse42.c
│  │     │  │  │  ├─ cpu_ssse3.c
│  │     │  │  │  ├─ cpu_vsx.c
│  │     │  │  │  ├─ cpu_vsx2.c
│  │     │  │  │  ├─ cpu_vsx3.c
│  │     │  │  │  ├─ cpu_vsx4.c
│  │     │  │  │  ├─ cpu_vx.c
│  │     │  │  │  ├─ cpu_vxe.c
│  │     │  │  │  ├─ cpu_vxe2.c
│  │     │  │  │  ├─ cpu_xop.c
│  │     │  │  │  ├─ extra_avx512bw_mask.c
│  │     │  │  │  ├─ extra_avx512dq_mask.c
│  │     │  │  │  ├─ extra_avx512f_reduce.c
│  │     │  │  │  ├─ extra_vsx4_mma.c
│  │     │  │  │  ├─ extra_vsx_asm.c
│  │     │  │  │  └─ test_flags.c
│  │     │  │  ├─ command
│  │     │  │  │  ├─ autodist.py
│  │     │  │  │  ├─ bdist_rpm.py
│  │     │  │  │  ├─ build.py
│  │     │  │  │  ├─ build_clib.py
│  │     │  │  │  ├─ build_ext.py
│  │     │  │  │  ├─ build_py.py
│  │     │  │  │  ├─ build_scripts.py
│  │     │  │  │  ├─ build_src.py
│  │     │  │  │  ├─ config.py
│  │     │  │  │  ├─ config_compiler.py
│  │     │  │  │  ├─ develop.py
│  │     │  │  │  ├─ egg_info.py
│  │     │  │  │  ├─ install.py
│  │     │  │  │  ├─ install_clib.py
│  │     │  │  │  ├─ install_data.py
│  │     │  │  │  ├─ install_headers.py
│  │     │  │  │  ├─ sdist.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ autodist.cpython-39.pyc
│  │     │  │  │     ├─ bdist_rpm.cpython-39.pyc
│  │     │  │  │     ├─ build.cpython-39.pyc
│  │     │  │  │     ├─ build_clib.cpython-39.pyc
│  │     │  │  │     ├─ build_ext.cpython-39.pyc
│  │     │  │  │     ├─ build_py.cpython-39.pyc
│  │     │  │  │     ├─ build_scripts.cpython-39.pyc
│  │     │  │  │     ├─ build_src.cpython-39.pyc
│  │     │  │  │     ├─ config.cpython-39.pyc
│  │     │  │  │     ├─ config_compiler.cpython-39.pyc
│  │     │  │  │     ├─ develop.cpython-39.pyc
│  │     │  │  │     ├─ egg_info.cpython-39.pyc
│  │     │  │  │     ├─ install.cpython-39.pyc
│  │     │  │  │     ├─ install_clib.cpython-39.pyc
│  │     │  │  │     ├─ install_data.cpython-39.pyc
│  │     │  │  │     ├─ install_headers.cpython-39.pyc
│  │     │  │  │     ├─ sdist.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ conv_template.py
│  │     │  │  ├─ core.py
│  │     │  │  ├─ cpuinfo.py
│  │     │  │  ├─ exec_command.py
│  │     │  │  ├─ extension.py
│  │     │  │  ├─ fcompiler
│  │     │  │  │  ├─ absoft.py
│  │     │  │  │  ├─ arm.py
│  │     │  │  │  ├─ compaq.py
│  │     │  │  │  ├─ environment.py
│  │     │  │  │  ├─ fujitsu.py
│  │     │  │  │  ├─ g95.py
│  │     │  │  │  ├─ gnu.py
│  │     │  │  │  ├─ hpux.py
│  │     │  │  │  ├─ ibm.py
│  │     │  │  │  ├─ intel.py
│  │     │  │  │  ├─ lahey.py
│  │     │  │  │  ├─ mips.py
│  │     │  │  │  ├─ nag.py
│  │     │  │  │  ├─ none.py
│  │     │  │  │  ├─ nv.py
│  │     │  │  │  ├─ pathf95.py
│  │     │  │  │  ├─ pg.py
│  │     │  │  │  ├─ sun.py
│  │     │  │  │  ├─ vast.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ absoft.cpython-39.pyc
│  │     │  │  │     ├─ arm.cpython-39.pyc
│  │     │  │  │     ├─ compaq.cpython-39.pyc
│  │     │  │  │     ├─ environment.cpython-39.pyc
│  │     │  │  │     ├─ fujitsu.cpython-39.pyc
│  │     │  │  │     ├─ g95.cpython-39.pyc
│  │     │  │  │     ├─ gnu.cpython-39.pyc
│  │     │  │  │     ├─ hpux.cpython-39.pyc
│  │     │  │  │     ├─ ibm.cpython-39.pyc
│  │     │  │  │     ├─ intel.cpython-39.pyc
│  │     │  │  │     ├─ lahey.cpython-39.pyc
│  │     │  │  │     ├─ mips.cpython-39.pyc
│  │     │  │  │     ├─ nag.cpython-39.pyc
│  │     │  │  │     ├─ none.cpython-39.pyc
│  │     │  │  │     ├─ nv.cpython-39.pyc
│  │     │  │  │     ├─ pathf95.cpython-39.pyc
│  │     │  │  │     ├─ pg.cpython-39.pyc
│  │     │  │  │     ├─ sun.cpython-39.pyc
│  │     │  │  │     ├─ vast.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ from_template.py
│  │     │  │  ├─ intelccompiler.py
│  │     │  │  ├─ lib2def.py
│  │     │  │  ├─ line_endings.py
│  │     │  │  ├─ log.py
│  │     │  │  ├─ mingw
│  │     │  │  │  └─ gfortran_vs2003_hack.c
│  │     │  │  ├─ mingw32ccompiler.py
│  │     │  │  ├─ misc_util.py
│  │     │  │  ├─ msvc9compiler.py
│  │     │  │  ├─ msvccompiler.py
│  │     │  │  ├─ npy_pkg_config.py
│  │     │  │  ├─ numpy_distribution.py
│  │     │  │  ├─ pathccompiler.py
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ system_info.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_build_ext.py
│  │     │  │  │  ├─ test_ccompiler_opt.py
│  │     │  │  │  ├─ test_ccompiler_opt_conf.py
│  │     │  │  │  ├─ test_exec_command.py
│  │     │  │  │  ├─ test_fcompiler.py
│  │     │  │  │  ├─ test_fcompiler_gnu.py
│  │     │  │  │  ├─ test_fcompiler_intel.py
│  │     │  │  │  ├─ test_fcompiler_nagfor.py
│  │     │  │  │  ├─ test_from_template.py
│  │     │  │  │  ├─ test_log.py
│  │     │  │  │  ├─ test_mingw32ccompiler.py
│  │     │  │  │  ├─ test_misc_util.py
│  │     │  │  │  ├─ test_npy_pkg_config.py
│  │     │  │  │  ├─ test_shell_utils.py
│  │     │  │  │  ├─ test_system_info.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_build_ext.cpython-39.pyc
│  │     │  │  │     ├─ test_ccompiler_opt.cpython-39.pyc
│  │     │  │  │     ├─ test_ccompiler_opt_conf.cpython-39.pyc
│  │     │  │  │     ├─ test_exec_command.cpython-39.pyc
│  │     │  │  │     ├─ test_fcompiler.cpython-39.pyc
│  │     │  │  │     ├─ test_fcompiler_gnu.cpython-39.pyc
│  │     │  │  │     ├─ test_fcompiler_intel.cpython-39.pyc
│  │     │  │  │     ├─ test_fcompiler_nagfor.cpython-39.pyc
│  │     │  │  │     ├─ test_from_template.cpython-39.pyc
│  │     │  │  │     ├─ test_log.cpython-39.pyc
│  │     │  │  │     ├─ test_mingw32ccompiler.cpython-39.pyc
│  │     │  │  │     ├─ test_misc_util.cpython-39.pyc
│  │     │  │  │     ├─ test_npy_pkg_config.cpython-39.pyc
│  │     │  │  │     ├─ test_shell_utils.cpython-39.pyc
│  │     │  │  │     ├─ test_system_info.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ unixccompiler.py
│  │     │  │  ├─ _shell_utils.py
│  │     │  │  ├─ __config__.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ armccompiler.cpython-39.pyc
│  │     │  │     ├─ ccompiler.cpython-39.pyc
│  │     │  │     ├─ ccompiler_opt.cpython-39.pyc
│  │     │  │     ├─ conv_template.cpython-39.pyc
│  │     │  │     ├─ core.cpython-39.pyc
│  │     │  │     ├─ cpuinfo.cpython-39.pyc
│  │     │  │     ├─ exec_command.cpython-39.pyc
│  │     │  │     ├─ extension.cpython-39.pyc
│  │     │  │     ├─ from_template.cpython-39.pyc
│  │     │  │     ├─ intelccompiler.cpython-39.pyc
│  │     │  │     ├─ lib2def.cpython-39.pyc
│  │     │  │     ├─ line_endings.cpython-39.pyc
│  │     │  │     ├─ log.cpython-39.pyc
│  │     │  │     ├─ mingw32ccompiler.cpython-39.pyc
│  │     │  │     ├─ misc_util.cpython-39.pyc
│  │     │  │     ├─ msvc9compiler.cpython-39.pyc
│  │     │  │     ├─ msvccompiler.cpython-39.pyc
│  │     │  │     ├─ npy_pkg_config.cpython-39.pyc
│  │     │  │     ├─ numpy_distribution.cpython-39.pyc
│  │     │  │     ├─ pathccompiler.cpython-39.pyc
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     ├─ system_info.cpython-39.pyc
│  │     │  │     ├─ unixccompiler.cpython-39.pyc
│  │     │  │     ├─ _shell_utils.cpython-39.pyc
│  │     │  │     ├─ __config__.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ doc
│  │     │  │  ├─ constants.py
│  │     │  │  ├─ ufuncs.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ constants.cpython-39.pyc
│  │     │  │     ├─ ufuncs.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ dual.py
│  │     │  ├─ f2py
│  │     │  │  ├─ auxfuncs.py
│  │     │  │  ├─ capi_maps.py
│  │     │  │  ├─ cb_rules.py
│  │     │  │  ├─ cfuncs.py
│  │     │  │  ├─ common_rules.py
│  │     │  │  ├─ crackfortran.py
│  │     │  │  ├─ diagnose.py
│  │     │  │  ├─ f2py2e.py
│  │     │  │  ├─ f90mod_rules.py
│  │     │  │  ├─ func2subr.py
│  │     │  │  ├─ rules.py
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ src
│  │     │  │  │  ├─ fortranobject.c
│  │     │  │  │  └─ fortranobject.h
│  │     │  │  ├─ symbolic.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ src
│  │     │  │  │  │  ├─ abstract_interface
│  │     │  │  │  │  │  ├─ foo.f90
│  │     │  │  │  │  │  └─ gh18403_mod.f90
│  │     │  │  │  │  ├─ array_from_pyobj
│  │     │  │  │  │  │  └─ wrapmodule.c
│  │     │  │  │  │  ├─ assumed_shape
│  │     │  │  │  │  │  ├─ .f2py_f2cmap
│  │     │  │  │  │  │  ├─ foo_free.f90
│  │     │  │  │  │  │  ├─ foo_mod.f90
│  │     │  │  │  │  │  ├─ foo_use.f90
│  │     │  │  │  │  │  └─ precision.f90
│  │     │  │  │  │  ├─ block_docstring
│  │     │  │  │  │  │  └─ foo.f
│  │     │  │  │  │  ├─ callback
│  │     │  │  │  │  │  ├─ foo.f
│  │     │  │  │  │  │  ├─ gh17797.f90
│  │     │  │  │  │  │  └─ gh18335.f90
│  │     │  │  │  │  ├─ cli
│  │     │  │  │  │  │  ├─ hi77.f
│  │     │  │  │  │  │  └─ hiworld.f90
│  │     │  │  │  │  ├─ common
│  │     │  │  │  │  │  └─ block.f
│  │     │  │  │  │  ├─ crackfortran
│  │     │  │  │  │  │  ├─ accesstype.f90
│  │     │  │  │  │  │  ├─ foo_deps.f90
│  │     │  │  │  │  │  ├─ gh15035.f
│  │     │  │  │  │  │  ├─ gh17859.f
│  │     │  │  │  │  │  ├─ gh2848.f90
│  │     │  │  │  │  │  ├─ operators.f90
│  │     │  │  │  │  │  ├─ privatemod.f90
│  │     │  │  │  │  │  ├─ publicmod.f90
│  │     │  │  │  │  │  ├─ pubprivmod.f90
│  │     │  │  │  │  │  └─ unicode_comment.f90
│  │     │  │  │  │  ├─ f2cmap
│  │     │  │  │  │  │  ├─ .f2py_f2cmap
│  │     │  │  │  │  │  └─ isoFortranEnvMap.f90
│  │     │  │  │  │  ├─ kind
│  │     │  │  │  │  │  └─ foo.f90
│  │     │  │  │  │  ├─ mixed
│  │     │  │  │  │  │  ├─ foo.f
│  │     │  │  │  │  │  ├─ foo_fixed.f90
│  │     │  │  │  │  │  └─ foo_free.f90
│  │     │  │  │  │  ├─ module_data
│  │     │  │  │  │  │  ├─ mod.mod
│  │     │  │  │  │  │  └─ module_data_docstring.f90
│  │     │  │  │  │  ├─ negative_bounds
│  │     │  │  │  │  │  └─ issue_20853.f90
│  │     │  │  │  │  ├─ parameter
│  │     │  │  │  │  │  ├─ constant_both.f90
│  │     │  │  │  │  │  ├─ constant_compound.f90
│  │     │  │  │  │  │  ├─ constant_integer.f90
│  │     │  │  │  │  │  ├─ constant_non_compound.f90
│  │     │  │  │  │  │  └─ constant_real.f90
│  │     │  │  │  │  ├─ quoted_character
│  │     │  │  │  │  │  └─ foo.f
│  │     │  │  │  │  ├─ regression
│  │     │  │  │  │  │  └─ inout.f90
│  │     │  │  │  │  ├─ return_character
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_complex
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_integer
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_logical
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_real
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ size
│  │     │  │  │  │  │  └─ foo.f90
│  │     │  │  │  │  ├─ string
│  │     │  │  │  │  │  ├─ char.f90
│  │     │  │  │  │  │  ├─ fixed_string.f90
│  │     │  │  │  │  │  └─ string.f
│  │     │  │  │  │  └─ value_attrspec
│  │     │  │  │  │     └─ gh21665.f90
│  │     │  │  │  ├─ test_abstract_interface.py
│  │     │  │  │  ├─ test_array_from_pyobj.py
│  │     │  │  │  ├─ test_assumed_shape.py
│  │     │  │  │  ├─ test_block_docstring.py
│  │     │  │  │  ├─ test_callback.py
│  │     │  │  │  ├─ test_character.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_compile_function.py
│  │     │  │  │  ├─ test_crackfortran.py
│  │     │  │  │  ├─ test_docs.py
│  │     │  │  │  ├─ test_f2cmap.py
│  │     │  │  │  ├─ test_f2py2e.py
│  │     │  │  │  ├─ test_kind.py
│  │     │  │  │  ├─ test_mixed.py
│  │     │  │  │  ├─ test_module_doc.py
│  │     │  │  │  ├─ test_parameter.py
│  │     │  │  │  ├─ test_quoted_character.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_return_character.py
│  │     │  │  │  ├─ test_return_complex.py
│  │     │  │  │  ├─ test_return_integer.py
│  │     │  │  │  ├─ test_return_logical.py
│  │     │  │  │  ├─ test_return_real.py
│  │     │  │  │  ├─ test_semicolon_split.py
│  │     │  │  │  ├─ test_size.py
│  │     │  │  │  ├─ test_string.py
│  │     │  │  │  ├─ test_symbolic.py
│  │     │  │  │  ├─ test_value_attrspec.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_abstract_interface.cpython-39.pyc
│  │     │  │  │     ├─ test_array_from_pyobj.cpython-39.pyc
│  │     │  │  │     ├─ test_assumed_shape.cpython-39.pyc
│  │     │  │  │     ├─ test_block_docstring.cpython-39.pyc
│  │     │  │  │     ├─ test_callback.cpython-39.pyc
│  │     │  │  │     ├─ test_character.cpython-39.pyc
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_compile_function.cpython-39.pyc
│  │     │  │  │     ├─ test_crackfortran.cpython-39.pyc
│  │     │  │  │     ├─ test_docs.cpython-39.pyc
│  │     │  │  │     ├─ test_f2cmap.cpython-39.pyc
│  │     │  │  │     ├─ test_f2py2e.cpython-39.pyc
│  │     │  │  │     ├─ test_kind.cpython-39.pyc
│  │     │  │  │     ├─ test_mixed.cpython-39.pyc
│  │     │  │  │     ├─ test_module_doc.cpython-39.pyc
│  │     │  │  │     ├─ test_parameter.cpython-39.pyc
│  │     │  │  │     ├─ test_quoted_character.cpython-39.pyc
│  │     │  │  │     ├─ test_regression.cpython-39.pyc
│  │     │  │  │     ├─ test_return_character.cpython-39.pyc
│  │     │  │  │     ├─ test_return_complex.cpython-39.pyc
│  │     │  │  │     ├─ test_return_integer.cpython-39.pyc
│  │     │  │  │     ├─ test_return_logical.cpython-39.pyc
│  │     │  │  │     ├─ test_return_real.cpython-39.pyc
│  │     │  │  │     ├─ test_semicolon_split.cpython-39.pyc
│  │     │  │  │     ├─ test_size.cpython-39.pyc
│  │     │  │  │     ├─ test_string.cpython-39.pyc
│  │     │  │  │     ├─ test_symbolic.cpython-39.pyc
│  │     │  │  │     ├─ test_value_attrspec.cpython-39.pyc
│  │     │  │  │     ├─ util.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ use_rules.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ __pycache__
│  │     │  │  │  ├─ auxfuncs.cpython-39.pyc
│  │     │  │  │  ├─ capi_maps.cpython-39.pyc
│  │     │  │  │  ├─ cb_rules.cpython-39.pyc
│  │     │  │  │  ├─ cfuncs.cpython-39.pyc
│  │     │  │  │  ├─ common_rules.cpython-39.pyc
│  │     │  │  │  ├─ crackfortran.cpython-39.pyc
│  │     │  │  │  ├─ diagnose.cpython-39.pyc
│  │     │  │  │  ├─ f2py2e.cpython-39.pyc
│  │     │  │  │  ├─ f90mod_rules.cpython-39.pyc
│  │     │  │  │  ├─ func2subr.cpython-39.pyc
│  │     │  │  │  ├─ rules.cpython-39.pyc
│  │     │  │  │  ├─ setup.cpython-39.pyc
│  │     │  │  │  ├─ symbolic.cpython-39.pyc
│  │     │  │  │  ├─ use_rules.cpython-39.pyc
│  │     │  │  │  ├─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __main__.cpython-39.pyc
│  │     │  │  │  └─ __version__.cpython-39.pyc
│  │     │  │  └─ __version__.py
│  │     │  ├─ fft
│  │     │  │  ├─ helper.py
│  │     │  │  ├─ helper.pyi
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_helper.py
│  │     │  │  │  ├─ test_pocketfft.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_helper.cpython-39.pyc
│  │     │  │  │     ├─ test_pocketfft.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _pocketfft.py
│  │     │  │  ├─ _pocketfft.pyi
│  │     │  │  ├─ _pocketfft_internal.cp39-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ helper.cpython-39.pyc
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     ├─ _pocketfft.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ lib
│  │     │  │  ├─ arraypad.py
│  │     │  │  ├─ arraypad.pyi
│  │     │  │  ├─ arraysetops.py
│  │     │  │  ├─ arraysetops.pyi
│  │     │  │  ├─ arrayterator.py
│  │     │  │  ├─ arrayterator.pyi
│  │     │  │  ├─ format.py
│  │     │  │  ├─ format.pyi
│  │     │  │  ├─ function_base.py
│  │     │  │  ├─ function_base.pyi
│  │     │  │  ├─ histograms.py
│  │     │  │  ├─ histograms.pyi
│  │     │  │  ├─ index_tricks.py
│  │     │  │  ├─ index_tricks.pyi
│  │     │  │  ├─ mixins.py
│  │     │  │  ├─ mixins.pyi
│  │     │  │  ├─ nanfunctions.py
│  │     │  │  ├─ nanfunctions.pyi
│  │     │  │  ├─ npyio.py
│  │     │  │  ├─ npyio.pyi
│  │     │  │  ├─ polynomial.py
│  │     │  │  ├─ polynomial.pyi
│  │     │  │  ├─ recfunctions.py
│  │     │  │  ├─ scimath.py
│  │     │  │  ├─ scimath.pyi
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ shape_base.py
│  │     │  │  ├─ shape_base.pyi
│  │     │  │  ├─ stride_tricks.py
│  │     │  │  ├─ stride_tricks.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ py2-objarr.npy
│  │     │  │  │  │  ├─ py2-objarr.npz
│  │     │  │  │  │  ├─ py3-objarr.npy
│  │     │  │  │  │  ├─ py3-objarr.npz
│  │     │  │  │  │  ├─ python3.npy
│  │     │  │  │  │  └─ win64python2.npy
│  │     │  │  │  ├─ test_arraypad.py
│  │     │  │  │  ├─ test_arraysetops.py
│  │     │  │  │  ├─ test_arrayterator.py
│  │     │  │  │  ├─ test_financial_expired.py
│  │     │  │  │  ├─ test_format.py
│  │     │  │  │  ├─ test_function_base.py
│  │     │  │  │  ├─ test_histograms.py
│  │     │  │  │  ├─ test_index_tricks.py
│  │     │  │  │  ├─ test_io.py
│  │     │  │  │  ├─ test_loadtxt.py
│  │     │  │  │  ├─ test_mixins.py
│  │     │  │  │  ├─ test_nanfunctions.py
│  │     │  │  │  ├─ test_packbits.py
│  │     │  │  │  ├─ test_polynomial.py
│  │     │  │  │  ├─ test_recfunctions.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_shape_base.py
│  │     │  │  │  ├─ test_stride_tricks.py
│  │     │  │  │  ├─ test_twodim_base.py
│  │     │  │  │  ├─ test_type_check.py
│  │     │  │  │  ├─ test_ufunclike.py
│  │     │  │  │  ├─ test_utils.py
│  │     │  │  │  ├─ test__datasource.py
│  │     │  │  │  ├─ test__iotools.py
│  │     │  │  │  ├─ test__version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_arraypad.cpython-39.pyc
│  │     │  │  │     ├─ test_arraysetops.cpython-39.pyc
│  │     │  │  │     ├─ test_arrayterator.cpython-39.pyc
│  │     │  │  │     ├─ test_financial_expired.cpython-39.pyc
│  │     │  │  │     ├─ test_format.cpython-39.pyc
│  │     │  │  │     ├─ test_function_base.cpython-39.pyc
│  │     │  │  │     ├─ test_histograms.cpython-39.pyc
│  │     │  │  │     ├─ test_index_tricks.cpython-39.pyc
│  │     │  │  │     ├─ test_io.cpython-39.pyc
│  │     │  │  │     ├─ test_loadtxt.cpython-39.pyc
│  │     │  │  │     ├─ test_mixins.cpython-39.pyc
│  │     │  │  │     ├─ test_nanfunctions.cpython-39.pyc
│  │     │  │  │     ├─ test_packbits.cpython-39.pyc
│  │     │  │  │     ├─ test_polynomial.cpython-39.pyc
│  │     │  │  │     ├─ test_recfunctions.cpython-39.pyc
│  │     │  │  │     ├─ test_regression.cpython-39.pyc
│  │     │  │  │     ├─ test_shape_base.cpython-39.pyc
│  │     │  │  │     ├─ test_stride_tricks.cpython-39.pyc
│  │     │  │  │     ├─ test_twodim_base.cpython-39.pyc
│  │     │  │  │     ├─ test_type_check.cpython-39.pyc
│  │     │  │  │     ├─ test_ufunclike.cpython-39.pyc
│  │     │  │  │     ├─ test_utils.cpython-39.pyc
│  │     │  │  │     ├─ test__datasource.cpython-39.pyc
│  │     │  │  │     ├─ test__iotools.cpython-39.pyc
│  │     │  │  │     ├─ test__version.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ twodim_base.py
│  │     │  │  ├─ twodim_base.pyi
│  │     │  │  ├─ type_check.py
│  │     │  │  ├─ type_check.pyi
│  │     │  │  ├─ ufunclike.py
│  │     │  │  ├─ ufunclike.pyi
│  │     │  │  ├─ user_array.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ utils.pyi
│  │     │  │  ├─ _datasource.py
│  │     │  │  ├─ _iotools.py
│  │     │  │  ├─ _version.py
│  │     │  │  ├─ _version.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ arraypad.cpython-39.pyc
│  │     │  │     ├─ arraysetops.cpython-39.pyc
│  │     │  │     ├─ arrayterator.cpython-39.pyc
│  │     │  │     ├─ format.cpython-39.pyc
│  │     │  │     ├─ function_base.cpython-39.pyc
│  │     │  │     ├─ histograms.cpython-39.pyc
│  │     │  │     ├─ index_tricks.cpython-39.pyc
│  │     │  │     ├─ mixins.cpython-39.pyc
│  │     │  │     ├─ nanfunctions.cpython-39.pyc
│  │     │  │     ├─ npyio.cpython-39.pyc
│  │     │  │     ├─ polynomial.cpython-39.pyc
│  │     │  │     ├─ recfunctions.cpython-39.pyc
│  │     │  │     ├─ scimath.cpython-39.pyc
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     ├─ shape_base.cpython-39.pyc
│  │     │  │     ├─ stride_tricks.cpython-39.pyc
│  │     │  │     ├─ twodim_base.cpython-39.pyc
│  │     │  │     ├─ type_check.cpython-39.pyc
│  │     │  │     ├─ ufunclike.cpython-39.pyc
│  │     │  │     ├─ user_array.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     ├─ _datasource.cpython-39.pyc
│  │     │  │     ├─ _iotools.cpython-39.pyc
│  │     │  │     ├─ _version.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ linalg
│  │     │  │  ├─ lapack_lite.cp39-win_amd64.pyd
│  │     │  │  ├─ linalg.py
│  │     │  │  ├─ linalg.pyi
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_linalg.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_deprecations.cpython-39.pyc
│  │     │  │  │     ├─ test_linalg.cpython-39.pyc
│  │     │  │  │     ├─ test_regression.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _umath_linalg.cp39-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ linalg.cpython-39.pyc
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ ma
│  │     │  │  ├─ bench.py
│  │     │  │  ├─ core.py
│  │     │  │  ├─ core.pyi
│  │     │  │  ├─ extras.py
│  │     │  │  ├─ extras.pyi
│  │     │  │  ├─ mrecords.py
│  │     │  │  ├─ mrecords.pyi
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_core.py
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_extras.py
│  │     │  │  │  ├─ test_mrecords.py
│  │     │  │  │  ├─ test_old_ma.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_subclassing.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_core.cpython-39.pyc
│  │     │  │  │     ├─ test_deprecations.cpython-39.pyc
│  │     │  │  │     ├─ test_extras.cpython-39.pyc
│  │     │  │  │     ├─ test_mrecords.cpython-39.pyc
│  │     │  │  │     ├─ test_old_ma.cpython-39.pyc
│  │     │  │  │     ├─ test_regression.cpython-39.pyc
│  │     │  │  │     ├─ test_subclassing.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ testutils.py
│  │     │  │  ├─ timer_comparison.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ bench.cpython-39.pyc
│  │     │  │     ├─ core.cpython-39.pyc
│  │     │  │     ├─ extras.cpython-39.pyc
│  │     │  │     ├─ mrecords.cpython-39.pyc
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     ├─ testutils.cpython-39.pyc
│  │     │  │     ├─ timer_comparison.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ matlib.py
│  │     │  ├─ matrixlib
│  │     │  │  ├─ defmatrix.py
│  │     │  │  ├─ defmatrix.pyi
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_defmatrix.py
│  │     │  │  │  ├─ test_interaction.py
│  │     │  │  │  ├─ test_masked_matrix.py
│  │     │  │  │  ├─ test_matrix_linalg.py
│  │     │  │  │  ├─ test_multiarray.py
│  │     │  │  │  ├─ test_numeric.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_defmatrix.cpython-39.pyc
│  │     │  │  │     ├─ test_interaction.cpython-39.pyc
│  │     │  │  │     ├─ test_masked_matrix.cpython-39.pyc
│  │     │  │  │     ├─ test_matrix_linalg.cpython-39.pyc
│  │     │  │  │     ├─ test_multiarray.cpython-39.pyc
│  │     │  │  │     ├─ test_numeric.cpython-39.pyc
│  │     │  │  │     ├─ test_regression.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ defmatrix.cpython-39.pyc
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ polynomial
│  │     │  │  ├─ chebyshev.py
│  │     │  │  ├─ chebyshev.pyi
│  │     │  │  ├─ hermite.py
│  │     │  │  ├─ hermite.pyi
│  │     │  │  ├─ hermite_e.py
│  │     │  │  ├─ hermite_e.pyi
│  │     │  │  ├─ laguerre.py
│  │     │  │  ├─ laguerre.pyi
│  │     │  │  ├─ legendre.py
│  │     │  │  ├─ legendre.pyi
│  │     │  │  ├─ polynomial.py
│  │     │  │  ├─ polynomial.pyi
│  │     │  │  ├─ polyutils.py
│  │     │  │  ├─ polyutils.pyi
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_chebyshev.py
│  │     │  │  │  ├─ test_classes.py
│  │     │  │  │  ├─ test_hermite.py
│  │     │  │  │  ├─ test_hermite_e.py
│  │     │  │  │  ├─ test_laguerre.py
│  │     │  │  │  ├─ test_legendre.py
│  │     │  │  │  ├─ test_polynomial.py
│  │     │  │  │  ├─ test_polyutils.py
│  │     │  │  │  ├─ test_printing.py
│  │     │  │  │  ├─ test_symbol.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_chebyshev.cpython-39.pyc
│  │     │  │  │     ├─ test_classes.cpython-39.pyc
│  │     │  │  │     ├─ test_hermite.cpython-39.pyc
│  │     │  │  │     ├─ test_hermite_e.cpython-39.pyc
│  │     │  │  │     ├─ test_laguerre.cpython-39.pyc
│  │     │  │  │     ├─ test_legendre.cpython-39.pyc
│  │     │  │  │     ├─ test_polynomial.cpython-39.pyc
│  │     │  │  │     ├─ test_polyutils.cpython-39.pyc
│  │     │  │  │     ├─ test_printing.cpython-39.pyc
│  │     │  │  │     ├─ test_symbol.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _polybase.py
│  │     │  │  ├─ _polybase.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ chebyshev.cpython-39.pyc
│  │     │  │     ├─ hermite.cpython-39.pyc
│  │     │  │     ├─ hermite_e.cpython-39.pyc
│  │     │  │     ├─ laguerre.cpython-39.pyc
│  │     │  │     ├─ legendre.cpython-39.pyc
│  │     │  │     ├─ polynomial.cpython-39.pyc
│  │     │  │     ├─ polyutils.cpython-39.pyc
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     ├─ _polybase.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ random
│  │     │  │  ├─ bit_generator.cp39-win_amd64.pyd
│  │     │  │  ├─ bit_generator.pxd
│  │     │  │  ├─ bit_generator.pyi
│  │     │  │  ├─ c_distributions.pxd
│  │     │  │  ├─ lib
│  │     │  │  │  └─ npyrandom.lib
│  │     │  │  ├─ mtrand.cp39-win_amd64.pyd
│  │     │  │  ├─ mtrand.pyi
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ mt19937-testset-1.csv
│  │     │  │  │  │  ├─ mt19937-testset-2.csv
│  │     │  │  │  │  ├─ pcg64-testset-1.csv
│  │     │  │  │  │  ├─ pcg64-testset-2.csv
│  │     │  │  │  │  ├─ pcg64dxsm-testset-1.csv
│  │     │  │  │  │  ├─ pcg64dxsm-testset-2.csv
│  │     │  │  │  │  ├─ philox-testset-1.csv
│  │     │  │  │  │  ├─ philox-testset-2.csv
│  │     │  │  │  │  ├─ sfc64-testset-1.csv
│  │     │  │  │  │  ├─ sfc64-testset-2.csv
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_direct.py
│  │     │  │  │  ├─ test_extending.py
│  │     │  │  │  ├─ test_generator_mt19937.py
│  │     │  │  │  ├─ test_generator_mt19937_regressions.py
│  │     │  │  │  ├─ test_random.py
│  │     │  │  │  ├─ test_randomstate.py
│  │     │  │  │  ├─ test_randomstate_regression.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_seed_sequence.py
│  │     │  │  │  ├─ test_smoke.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_direct.cpython-39.pyc
│  │     │  │  │     ├─ test_extending.cpython-39.pyc
│  │     │  │  │     ├─ test_generator_mt19937.cpython-39.pyc
│  │     │  │  │     ├─ test_generator_mt19937_regressions.cpython-39.pyc
│  │     │  │  │     ├─ test_random.cpython-39.pyc
│  │     │  │  │     ├─ test_randomstate.cpython-39.pyc
│  │     │  │  │     ├─ test_randomstate_regression.cpython-39.pyc
│  │     │  │  │     ├─ test_regression.cpython-39.pyc
│  │     │  │  │     ├─ test_seed_sequence.cpython-39.pyc
│  │     │  │  │     ├─ test_smoke.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _bounded_integers.cp39-win_amd64.pyd
│  │     │  │  ├─ _bounded_integers.pxd
│  │     │  │  ├─ _common.cp39-win_amd64.pyd
│  │     │  │  ├─ _common.pxd
│  │     │  │  ├─ _examples
│  │     │  │  │  ├─ cffi
│  │     │  │  │  │  ├─ extending.py
│  │     │  │  │  │  ├─ parse.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ extending.cpython-39.pyc
│  │     │  │  │  │     └─ parse.cpython-39.pyc
│  │     │  │  │  ├─ cython
│  │     │  │  │  │  ├─ extending.pyx
│  │     │  │  │  │  ├─ extending_distributions.pyx
│  │     │  │  │  │  ├─ setup.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ setup.cpython-39.pyc
│  │     │  │  │  └─ numba
│  │     │  │  │     ├─ extending.py
│  │     │  │  │     ├─ extending_distributions.py
│  │     │  │  │     └─ __pycache__
│  │     │  │  │        ├─ extending.cpython-39.pyc
│  │     │  │  │        └─ extending_distributions.cpython-39.pyc
│  │     │  │  ├─ _generator.cp39-win_amd64.pyd
│  │     │  │  ├─ _generator.pyi
│  │     │  │  ├─ _mt19937.cp39-win_amd64.pyd
│  │     │  │  ├─ _mt19937.pyi
│  │     │  │  ├─ _pcg64.cp39-win_amd64.pyd
│  │     │  │  ├─ _pcg64.pyi
│  │     │  │  ├─ _philox.cp39-win_amd64.pyd
│  │     │  │  ├─ _philox.pyi
│  │     │  │  ├─ _pickle.py
│  │     │  │  ├─ _sfc64.cp39-win_amd64.pyd
│  │     │  │  ├─ _sfc64.pyi
│  │     │  │  ├─ __init__.pxd
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     ├─ _pickle.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ setup.py
│  │     │  ├─ testing
│  │     │  │  ├─ print_coercion_tables.py
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_doctesting.py
│  │     │  │  │  ├─ test_utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_doctesting.cpython-39.pyc
│  │     │  │  │     ├─ test_utils.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ _private
│  │     │  │  │  ├─ decorators.py
│  │     │  │  │  ├─ extbuild.py
│  │     │  │  │  ├─ noseclasses.py
│  │     │  │  │  ├─ nosetester.py
│  │     │  │  │  ├─ parameterized.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ utils.pyi
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ decorators.cpython-39.pyc
│  │     │  │  │     ├─ extbuild.cpython-39.pyc
│  │     │  │  │     ├─ noseclasses.cpython-39.pyc
│  │     │  │  │     ├─ nosetester.cpython-39.pyc
│  │     │  │  │     ├─ parameterized.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ print_coercion_tables.cpython-39.pyc
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ tests
│  │     │  │  ├─ test_ctypeslib.py
│  │     │  │  ├─ test_lazyloading.py
│  │     │  │  ├─ test_matlib.py
│  │     │  │  ├─ test_numpy_version.py
│  │     │  │  ├─ test_public_api.py
│  │     │  │  ├─ test_reloading.py
│  │     │  │  ├─ test_scripts.py
│  │     │  │  ├─ test_warnings.py
│  │     │  │  ├─ test__all__.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ test_ctypeslib.cpython-39.pyc
│  │     │  │     ├─ test_lazyloading.cpython-39.pyc
│  │     │  │     ├─ test_matlib.cpython-39.pyc
│  │     │  │     ├─ test_numpy_version.cpython-39.pyc
│  │     │  │     ├─ test_public_api.cpython-39.pyc
│  │     │  │     ├─ test_reloading.cpython-39.pyc
│  │     │  │     ├─ test_scripts.cpython-39.pyc
│  │     │  │     ├─ test_warnings.cpython-39.pyc
│  │     │  │     ├─ test__all__.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ typing
│  │     │  │  ├─ mypy_plugin.py
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ fail
│  │     │  │  │  │  │  ├─ arithmetic.pyi
│  │     │  │  │  │  │  ├─ arrayprint.pyi
│  │     │  │  │  │  │  ├─ arrayterator.pyi
│  │     │  │  │  │  │  ├─ array_constructors.pyi
│  │     │  │  │  │  │  ├─ array_like.pyi
│  │     │  │  │  │  │  ├─ array_pad.pyi
│  │     │  │  │  │  │  ├─ bitwise_ops.pyi
│  │     │  │  │  │  │  ├─ char.pyi
│  │     │  │  │  │  │  ├─ chararray.pyi
│  │     │  │  │  │  │  ├─ comparisons.pyi
│  │     │  │  │  │  │  ├─ constants.pyi
│  │     │  │  │  │  │  ├─ datasource.pyi
│  │     │  │  │  │  │  ├─ dtype.pyi
│  │     │  │  │  │  │  ├─ einsumfunc.pyi
│  │     │  │  │  │  │  ├─ false_positives.pyi
│  │     │  │  │  │  │  ├─ flatiter.pyi
│  │     │  │  │  │  │  ├─ fromnumeric.pyi
│  │     │  │  │  │  │  ├─ histograms.pyi
│  │     │  │  │  │  │  ├─ index_tricks.pyi
│  │     │  │  │  │  │  ├─ lib_function_base.pyi
│  │     │  │  │  │  │  ├─ lib_polynomial.pyi
│  │     │  │  │  │  │  ├─ lib_utils.pyi
│  │     │  │  │  │  │  ├─ lib_version.pyi
│  │     │  │  │  │  │  ├─ linalg.pyi
│  │     │  │  │  │  │  ├─ memmap.pyi
│  │     │  │  │  │  │  ├─ modules.pyi
│  │     │  │  │  │  │  ├─ multiarray.pyi
│  │     │  │  │  │  │  ├─ ndarray.pyi
│  │     │  │  │  │  │  ├─ ndarray_misc.pyi
│  │     │  │  │  │  │  ├─ nditer.pyi
│  │     │  │  │  │  │  ├─ nested_sequence.pyi
│  │     │  │  │  │  │  ├─ npyio.pyi
│  │     │  │  │  │  │  ├─ numerictypes.pyi
│  │     │  │  │  │  │  ├─ random.pyi
│  │     │  │  │  │  │  ├─ rec.pyi
│  │     │  │  │  │  │  ├─ scalars.pyi
│  │     │  │  │  │  │  ├─ shape_base.pyi
│  │     │  │  │  │  │  ├─ stride_tricks.pyi
│  │     │  │  │  │  │  ├─ testing.pyi
│  │     │  │  │  │  │  ├─ twodim_base.pyi
│  │     │  │  │  │  │  ├─ type_check.pyi
│  │     │  │  │  │  │  ├─ ufunclike.pyi
│  │     │  │  │  │  │  ├─ ufuncs.pyi
│  │     │  │  │  │  │  ├─ ufunc_config.pyi
│  │     │  │  │  │  │  └─ warnings_and_errors.pyi
│  │     │  │  │  │  ├─ misc
│  │     │  │  │  │  │  └─ extended_precision.pyi
│  │     │  │  │  │  ├─ mypy.ini
│  │     │  │  │  │  ├─ pass
│  │     │  │  │  │  │  ├─ arithmetic.py
│  │     │  │  │  │  │  ├─ arrayprint.py
│  │     │  │  │  │  │  ├─ arrayterator.py
│  │     │  │  │  │  │  ├─ array_constructors.py
│  │     │  │  │  │  │  ├─ array_like.py
│  │     │  │  │  │  │  ├─ bitwise_ops.py
│  │     │  │  │  │  │  ├─ comparisons.py
│  │     │  │  │  │  │  ├─ dtype.py
│  │     │  │  │  │  │  ├─ einsumfunc.py
│  │     │  │  │  │  │  ├─ flatiter.py
│  │     │  │  │  │  │  ├─ fromnumeric.py
│  │     │  │  │  │  │  ├─ index_tricks.py
│  │     │  │  │  │  │  ├─ lib_utils.py
│  │     │  │  │  │  │  ├─ lib_version.py
│  │     │  │  │  │  │  ├─ literal.py
│  │     │  │  │  │  │  ├─ mod.py
│  │     │  │  │  │  │  ├─ modules.py
│  │     │  │  │  │  │  ├─ multiarray.py
│  │     │  │  │  │  │  ├─ ndarray_conversion.py
│  │     │  │  │  │  │  ├─ ndarray_misc.py
│  │     │  │  │  │  │  ├─ ndarray_shape_manipulation.py
│  │     │  │  │  │  │  ├─ numeric.py
│  │     │  │  │  │  │  ├─ numerictypes.py
│  │     │  │  │  │  │  ├─ random.py
│  │     │  │  │  │  │  ├─ scalars.py
│  │     │  │  │  │  │  ├─ simple.py
│  │     │  │  │  │  │  ├─ simple_py3.py
│  │     │  │  │  │  │  ├─ ufunclike.py
│  │     │  │  │  │  │  ├─ ufuncs.py
│  │     │  │  │  │  │  ├─ ufunc_config.py
│  │     │  │  │  │  │  ├─ warnings_and_errors.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ arithmetic.cpython-39.pyc
│  │     │  │  │  │  │     ├─ arrayprint.cpython-39.pyc
│  │     │  │  │  │  │     ├─ arrayterator.cpython-39.pyc
│  │     │  │  │  │  │     ├─ array_constructors.cpython-39.pyc
│  │     │  │  │  │  │     ├─ array_like.cpython-39.pyc
│  │     │  │  │  │  │     ├─ bitwise_ops.cpython-39.pyc
│  │     │  │  │  │  │     ├─ comparisons.cpython-39.pyc
│  │     │  │  │  │  │     ├─ dtype.cpython-39.pyc
│  │     │  │  │  │  │     ├─ einsumfunc.cpython-39.pyc
│  │     │  │  │  │  │     ├─ flatiter.cpython-39.pyc
│  │     │  │  │  │  │     ├─ fromnumeric.cpython-39.pyc
│  │     │  │  │  │  │     ├─ index_tricks.cpython-39.pyc
│  │     │  │  │  │  │     ├─ lib_utils.cpython-39.pyc
│  │     │  │  │  │  │     ├─ lib_version.cpython-39.pyc
│  │     │  │  │  │  │     ├─ literal.cpython-39.pyc
│  │     │  │  │  │  │     ├─ mod.cpython-39.pyc
│  │     │  │  │  │  │     ├─ modules.cpython-39.pyc
│  │     │  │  │  │  │     ├─ multiarray.cpython-39.pyc
│  │     │  │  │  │  │     ├─ ndarray_conversion.cpython-39.pyc
│  │     │  │  │  │  │     ├─ ndarray_misc.cpython-39.pyc
│  │     │  │  │  │  │     ├─ ndarray_shape_manipulation.cpython-39.pyc
│  │     │  │  │  │  │     ├─ numeric.cpython-39.pyc
│  │     │  │  │  │  │     ├─ numerictypes.cpython-39.pyc
│  │     │  │  │  │  │     ├─ random.cpython-39.pyc
│  │     │  │  │  │  │     ├─ scalars.cpython-39.pyc
│  │     │  │  │  │  │     ├─ simple.cpython-39.pyc
│  │     │  │  │  │  │     ├─ simple_py3.cpython-39.pyc
│  │     │  │  │  │  │     ├─ ufunclike.cpython-39.pyc
│  │     │  │  │  │  │     ├─ ufuncs.cpython-39.pyc
│  │     │  │  │  │  │     ├─ ufunc_config.cpython-39.pyc
│  │     │  │  │  │  │     └─ warnings_and_errors.cpython-39.pyc
│  │     │  │  │  │  └─ reveal
│  │     │  │  │  │     ├─ arithmetic.pyi
│  │     │  │  │  │     ├─ arraypad.pyi
│  │     │  │  │  │     ├─ arrayprint.pyi
│  │     │  │  │  │     ├─ arraysetops.pyi
│  │     │  │  │  │     ├─ arrayterator.pyi
│  │     │  │  │  │     ├─ array_constructors.pyi
│  │     │  │  │  │     ├─ bitwise_ops.pyi
│  │     │  │  │  │     ├─ char.pyi
│  │     │  │  │  │     ├─ chararray.pyi
│  │     │  │  │  │     ├─ comparisons.pyi
│  │     │  │  │  │     ├─ constants.pyi
│  │     │  │  │  │     ├─ ctypeslib.pyi
│  │     │  │  │  │     ├─ datasource.pyi
│  │     │  │  │  │     ├─ dtype.pyi
│  │     │  │  │  │     ├─ einsumfunc.pyi
│  │     │  │  │  │     ├─ emath.pyi
│  │     │  │  │  │     ├─ false_positives.pyi
│  │     │  │  │  │     ├─ fft.pyi
│  │     │  │  │  │     ├─ flatiter.pyi
│  │     │  │  │  │     ├─ fromnumeric.pyi
│  │     │  │  │  │     ├─ getlimits.pyi
│  │     │  │  │  │     ├─ histograms.pyi
│  │     │  │  │  │     ├─ index_tricks.pyi
│  │     │  │  │  │     ├─ lib_function_base.pyi
│  │     │  │  │  │     ├─ lib_polynomial.pyi
│  │     │  │  │  │     ├─ lib_utils.pyi
│  │     │  │  │  │     ├─ lib_version.pyi
│  │     │  │  │  │     ├─ linalg.pyi
│  │     │  │  │  │     ├─ matrix.pyi
│  │     │  │  │  │     ├─ memmap.pyi
│  │     │  │  │  │     ├─ mod.pyi
│  │     │  │  │  │     ├─ modules.pyi
│  │     │  │  │  │     ├─ multiarray.pyi
│  │     │  │  │  │     ├─ nbit_base_example.pyi
│  │     │  │  │  │     ├─ ndarray_conversion.pyi
│  │     │  │  │  │     ├─ ndarray_misc.pyi
│  │     │  │  │  │     ├─ ndarray_shape_manipulation.pyi
│  │     │  │  │  │     ├─ nditer.pyi
│  │     │  │  │  │     ├─ nested_sequence.pyi
│  │     │  │  │  │     ├─ npyio.pyi
│  │     │  │  │  │     ├─ numeric.pyi
│  │     │  │  │  │     ├─ numerictypes.pyi
│  │     │  │  │  │     ├─ random.pyi
│  │     │  │  │  │     ├─ rec.pyi
│  │     │  │  │  │     ├─ scalars.pyi
│  │     │  │  │  │     ├─ shape_base.pyi
│  │     │  │  │  │     ├─ stride_tricks.pyi
│  │     │  │  │  │     ├─ testing.pyi
│  │     │  │  │  │     ├─ twodim_base.pyi
│  │     │  │  │  │     ├─ type_check.pyi
│  │     │  │  │  │     ├─ ufunclike.pyi
│  │     │  │  │  │     ├─ ufuncs.pyi
│  │     │  │  │  │     ├─ ufunc_config.pyi
│  │     │  │  │  │     ├─ version.pyi
│  │     │  │  │  │     └─ warnings_and_errors.pyi
│  │     │  │  │  ├─ test_generic_alias.py
│  │     │  │  │  ├─ test_isfile.py
│  │     │  │  │  ├─ test_runtime.py
│  │     │  │  │  ├─ test_typing.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_generic_alias.cpython-39.pyc
│  │     │  │  │     ├─ test_isfile.cpython-39.pyc
│  │     │  │  │     ├─ test_runtime.cpython-39.pyc
│  │     │  │  │     ├─ test_typing.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ mypy_plugin.cpython-39.pyc
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ version.py
│  │     │  ├─ _distributor_init.py
│  │     │  ├─ _globals.py
│  │     │  ├─ _pyinstaller
│  │     │  │  ├─ hook-numpy.py
│  │     │  │  ├─ pyinstaller-smoke.py
│  │     │  │  ├─ test_pyinstaller.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ hook-numpy.cpython-39.pyc
│  │     │  │     ├─ pyinstaller-smoke.cpython-39.pyc
│  │     │  │     ├─ test_pyinstaller.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _pytesttester.py
│  │     │  ├─ _pytesttester.pyi
│  │     │  ├─ _typing
│  │     │  │  ├─ setup.py
│  │     │  │  ├─ _add_docstring.py
│  │     │  │  ├─ _array_like.py
│  │     │  │  ├─ _callable.pyi
│  │     │  │  ├─ _char_codes.py
│  │     │  │  ├─ _dtype_like.py
│  │     │  │  ├─ _extended_precision.py
│  │     │  │  ├─ _generic_alias.py
│  │     │  │  ├─ _nbit.py
│  │     │  │  ├─ _nested_sequence.py
│  │     │  │  ├─ _scalars.py
│  │     │  │  ├─ _shape.py
│  │     │  │  ├─ _ufunc.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ setup.cpython-39.pyc
│  │     │  │     ├─ _add_docstring.cpython-39.pyc
│  │     │  │     ├─ _array_like.cpython-39.pyc
│  │     │  │     ├─ _char_codes.cpython-39.pyc
│  │     │  │     ├─ _dtype_like.cpython-39.pyc
│  │     │  │     ├─ _extended_precision.cpython-39.pyc
│  │     │  │     ├─ _generic_alias.cpython-39.pyc
│  │     │  │     ├─ _nbit.cpython-39.pyc
│  │     │  │     ├─ _nested_sequence.cpython-39.pyc
│  │     │  │     ├─ _scalars.cpython-39.pyc
│  │     │  │     ├─ _shape.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _version.py
│  │     │  ├─ __config__.py
│  │     │  ├─ __init__.cython-30.pxd
│  │     │  ├─ __init__.pxd
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  └─ __pycache__
│  │     │     ├─ conftest.cpython-39.pyc
│  │     │     ├─ ctypeslib.cpython-39.pyc
│  │     │     ├─ dual.cpython-39.pyc
│  │     │     ├─ matlib.cpython-39.pyc
│  │     │     ├─ setup.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     ├─ _distributor_init.cpython-39.pyc
│  │     │     ├─ _globals.cpython-39.pyc
│  │     │     ├─ _pytesttester.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     ├─ __config__.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ numpy-1.24.2.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ LICENSES_bundled.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ openapi_schema_validator
│  │     │  ├─ py.typed
│  │     │  ├─ shortcuts.py
│  │     │  ├─ validators.py
│  │     │  ├─ _format.py
│  │     │  ├─ _types.py
│  │     │  ├─ _validators.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ shortcuts.cpython-39.pyc
│  │     │     ├─ validators.cpython-39.pyc
│  │     │     ├─ _format.cpython-39.pyc
│  │     │     ├─ _types.cpython-39.pyc
│  │     │     ├─ _validators.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ openapi_schema_validator-0.3.4.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ openapi_spec_validator
│  │     │  ├─ exceptions.py
│  │     │  ├─ py.typed
│  │     │  ├─ readers.py
│  │     │  ├─ resources
│  │     │  │  └─ schemas
│  │     │  │     ├─ v2.0
│  │     │  │     │  └─ schema.json
│  │     │  │     ├─ v3.0
│  │     │  │     │  └─ schema.json
│  │     │  │     ├─ v3.0.0
│  │     │  │     │  └─ schema.json
│  │     │  │     └─ v3.1
│  │     │  │        └─ schema.json
│  │     │  ├─ schemas
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ shortcuts.py
│  │     │  ├─ validation
│  │     │  │  ├─ decorators.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ protocols.py
│  │     │  │  ├─ proxies.py
│  │     │  │  ├─ validators.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ decorators.cpython-39.pyc
│  │     │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │     ├─ protocols.cpython-39.pyc
│  │     │  │     ├─ proxies.cpython-39.pyc
│  │     │  │     ├─ validators.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ readers.cpython-39.pyc
│  │     │     ├─ shortcuts.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ openapi_spec_validator-0.5.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ packaging
│  │     │  ├─ markers.py
│  │     │  ├─ metadata.py
│  │     │  ├─ py.typed
│  │     │  ├─ requirements.py
│  │     │  ├─ specifiers.py
│  │     │  ├─ tags.py
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ _elffile.py
│  │     │  ├─ _manylinux.py
│  │     │  ├─ _musllinux.py
│  │     │  ├─ _parser.py
│  │     │  ├─ _structures.py
│  │     │  ├─ _tokenizer.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ markers.cpython-39.pyc
│  │     │     ├─ metadata.cpython-39.pyc
│  │     │     ├─ requirements.cpython-39.pyc
│  │     │     ├─ specifiers.cpython-39.pyc
│  │     │     ├─ tags.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     ├─ _elffile.cpython-39.pyc
│  │     │     ├─ _manylinux.cpython-39.pyc
│  │     │     ├─ _musllinux.cpython-39.pyc
│  │     │     ├─ _parser.cpython-39.pyc
│  │     │     ├─ _structures.cpython-39.pyc
│  │     │     ├─ _tokenizer.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ packaging-23.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ LICENSE.APACHE
│  │     │  ├─ LICENSE.BSD
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pandas
│  │     │  ├─ api
│  │     │  │  ├─ extensions
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ indexers
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ interchange
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ types
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ arrays
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ compat
│  │     │  │  ├─ chainmap.py
│  │     │  │  ├─ numpy
│  │     │  │  │  ├─ function.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ function.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pickle_compat.py
│  │     │  │  ├─ pyarrow.py
│  │     │  │  ├─ _optional.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ chainmap.cpython-39.pyc
│  │     │  │     ├─ pickle_compat.cpython-39.pyc
│  │     │  │     ├─ pyarrow.cpython-39.pyc
│  │     │  │     ├─ _optional.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ conftest.py
│  │     │  ├─ core
│  │     │  │  ├─ accessor.py
│  │     │  │  ├─ algorithms.py
│  │     │  │  ├─ api.py
│  │     │  │  ├─ apply.py
│  │     │  │  ├─ arraylike.py
│  │     │  │  ├─ arrays
│  │     │  │  │  ├─ arrow
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ dtype.py
│  │     │  │  │  │  ├─ extension_types.py
│  │     │  │  │  │  ├─ _arrow_utils.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ array.cpython-39.pyc
│  │     │  │  │  │     ├─ dtype.cpython-39.pyc
│  │     │  │  │  │     ├─ extension_types.cpython-39.pyc
│  │     │  │  │  │     ├─ _arrow_utils.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ boolean.py
│  │     │  │  │  ├─ categorical.py
│  │     │  │  │  ├─ datetimelike.py
│  │     │  │  │  ├─ datetimes.py
│  │     │  │  │  ├─ floating.py
│  │     │  │  │  ├─ integer.py
│  │     │  │  │  ├─ interval.py
│  │     │  │  │  ├─ masked.py
│  │     │  │  │  ├─ numeric.py
│  │     │  │  │  ├─ numpy_.py
│  │     │  │  │  ├─ period.py
│  │     │  │  │  ├─ sparse
│  │     │  │  │  │  ├─ accessor.py
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ dtype.py
│  │     │  │  │  │  ├─ scipy_sparse.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ accessor.cpython-39.pyc
│  │     │  │  │  │     ├─ array.cpython-39.pyc
│  │     │  │  │  │     ├─ dtype.cpython-39.pyc
│  │     │  │  │  │     ├─ scipy_sparse.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ string_.py
│  │     │  │  │  ├─ string_arrow.py
│  │     │  │  │  ├─ timedeltas.py
│  │     │  │  │  ├─ _mixins.py
│  │     │  │  │  ├─ _ranges.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ boolean.cpython-39.pyc
│  │     │  │  │     ├─ categorical.cpython-39.pyc
│  │     │  │  │     ├─ datetimelike.cpython-39.pyc
│  │     │  │  │     ├─ datetimes.cpython-39.pyc
│  │     │  │  │     ├─ floating.cpython-39.pyc
│  │     │  │  │     ├─ integer.cpython-39.pyc
│  │     │  │  │     ├─ interval.cpython-39.pyc
│  │     │  │  │     ├─ masked.cpython-39.pyc
│  │     │  │  │     ├─ numeric.cpython-39.pyc
│  │     │  │  │     ├─ numpy_.cpython-39.pyc
│  │     │  │  │     ├─ period.cpython-39.pyc
│  │     │  │  │     ├─ string_.cpython-39.pyc
│  │     │  │  │     ├─ string_arrow.cpython-39.pyc
│  │     │  │  │     ├─ timedeltas.cpython-39.pyc
│  │     │  │  │     ├─ _mixins.cpython-39.pyc
│  │     │  │  │     ├─ _ranges.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ array_algos
│  │     │  │  │  ├─ masked_reductions.py
│  │     │  │  │  ├─ putmask.py
│  │     │  │  │  ├─ quantile.py
│  │     │  │  │  ├─ replace.py
│  │     │  │  │  ├─ take.py
│  │     │  │  │  ├─ transforms.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ masked_reductions.cpython-39.pyc
│  │     │  │  │     ├─ putmask.cpython-39.pyc
│  │     │  │  │     ├─ quantile.cpython-39.pyc
│  │     │  │  │     ├─ replace.cpython-39.pyc
│  │     │  │  │     ├─ take.cpython-39.pyc
│  │     │  │  │     ├─ transforms.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ base.py
│  │     │  │  ├─ common.py
│  │     │  │  ├─ computation
│  │     │  │  │  ├─ align.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ engines.py
│  │     │  │  │  ├─ eval.py
│  │     │  │  │  ├─ expr.py
│  │     │  │  │  ├─ expressions.py
│  │     │  │  │  ├─ ops.py
│  │     │  │  │  ├─ parsing.py
│  │     │  │  │  ├─ pytables.py
│  │     │  │  │  ├─ scope.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ align.cpython-39.pyc
│  │     │  │  │     ├─ api.cpython-39.pyc
│  │     │  │  │     ├─ check.cpython-39.pyc
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ engines.cpython-39.pyc
│  │     │  │  │     ├─ eval.cpython-39.pyc
│  │     │  │  │     ├─ expr.cpython-39.pyc
│  │     │  │  │     ├─ expressions.cpython-39.pyc
│  │     │  │  │     ├─ ops.cpython-39.pyc
│  │     │  │  │     ├─ parsing.cpython-39.pyc
│  │     │  │  │     ├─ pytables.cpython-39.pyc
│  │     │  │  │     ├─ scope.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ config_init.py
│  │     │  │  ├─ construction.py
│  │     │  │  ├─ describe.py
│  │     │  │  ├─ dtypes
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ astype.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ cast.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ concat.py
│  │     │  │  │  ├─ dtypes.py
│  │     │  │  │  ├─ generic.py
│  │     │  │  │  ├─ inference.py
│  │     │  │  │  ├─ missing.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ api.cpython-39.pyc
│  │     │  │  │     ├─ astype.cpython-39.pyc
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ cast.cpython-39.pyc
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ concat.cpython-39.pyc
│  │     │  │  │     ├─ dtypes.cpython-39.pyc
│  │     │  │  │     ├─ generic.cpython-39.pyc
│  │     │  │  │     ├─ inference.cpython-39.pyc
│  │     │  │  │     ├─ missing.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ flags.py
│  │     │  │  ├─ frame.py
│  │     │  │  ├─ generic.py
│  │     │  │  ├─ groupby
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ categorical.py
│  │     │  │  │  ├─ generic.py
│  │     │  │  │  ├─ groupby.py
│  │     │  │  │  ├─ grouper.py
│  │     │  │  │  ├─ indexing.py
│  │     │  │  │  ├─ numba_.py
│  │     │  │  │  ├─ ops.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ categorical.cpython-39.pyc
│  │     │  │  │     ├─ generic.cpython-39.pyc
│  │     │  │  │     ├─ groupby.cpython-39.pyc
│  │     │  │  │     ├─ grouper.cpython-39.pyc
│  │     │  │  │     ├─ indexing.cpython-39.pyc
│  │     │  │  │     ├─ numba_.cpython-39.pyc
│  │     │  │  │     ├─ ops.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ index.py
│  │     │  │  ├─ indexers
│  │     │  │  │  ├─ objects.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ objects.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ indexes
│  │     │  │  │  ├─ accessors.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ category.py
│  │     │  │  │  ├─ datetimelike.py
│  │     │  │  │  ├─ datetimes.py
│  │     │  │  │  ├─ extension.py
│  │     │  │  │  ├─ frozen.py
│  │     │  │  │  ├─ interval.py
│  │     │  │  │  ├─ multi.py
│  │     │  │  │  ├─ numeric.py
│  │     │  │  │  ├─ period.py
│  │     │  │  │  ├─ range.py
│  │     │  │  │  ├─ timedeltas.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ accessors.cpython-39.pyc
│  │     │  │  │     ├─ api.cpython-39.pyc
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ category.cpython-39.pyc
│  │     │  │  │     ├─ datetimelike.cpython-39.pyc
│  │     │  │  │     ├─ datetimes.cpython-39.pyc
│  │     │  │  │     ├─ extension.cpython-39.pyc
│  │     │  │  │     ├─ frozen.cpython-39.pyc
│  │     │  │  │     ├─ interval.cpython-39.pyc
│  │     │  │  │     ├─ multi.cpython-39.pyc
│  │     │  │  │     ├─ numeric.cpython-39.pyc
│  │     │  │  │     ├─ period.cpython-39.pyc
│  │     │  │  │     ├─ range.cpython-39.pyc
│  │     │  │  │     ├─ timedeltas.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ indexing.py
│  │     │  │  ├─ interchange
│  │     │  │  │  ├─ buffer.py
│  │     │  │  │  ├─ column.py
│  │     │  │  │  ├─ dataframe.py
│  │     │  │  │  ├─ dataframe_protocol.py
│  │     │  │  │  ├─ from_dataframe.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ buffer.cpython-39.pyc
│  │     │  │  │     ├─ column.cpython-39.pyc
│  │     │  │  │     ├─ dataframe.cpython-39.pyc
│  │     │  │  │     ├─ dataframe_protocol.cpython-39.pyc
│  │     │  │  │     ├─ from_dataframe.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ internals
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ array_manager.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ blocks.py
│  │     │  │  │  ├─ concat.py
│  │     │  │  │  ├─ construction.py
│  │     │  │  │  ├─ managers.py
│  │     │  │  │  ├─ ops.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ api.cpython-39.pyc
│  │     │  │  │     ├─ array_manager.cpython-39.pyc
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ blocks.cpython-39.pyc
│  │     │  │  │     ├─ concat.cpython-39.pyc
│  │     │  │  │     ├─ construction.cpython-39.pyc
│  │     │  │  │     ├─ managers.cpython-39.pyc
│  │     │  │  │     ├─ ops.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ missing.py
│  │     │  │  ├─ nanops.py
│  │     │  │  ├─ ops
│  │     │  │  │  ├─ array_ops.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ dispatch.py
│  │     │  │  │  ├─ docstrings.py
│  │     │  │  │  ├─ invalid.py
│  │     │  │  │  ├─ mask_ops.py
│  │     │  │  │  ├─ methods.py
│  │     │  │  │  ├─ missing.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ array_ops.cpython-39.pyc
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ dispatch.cpython-39.pyc
│  │     │  │  │     ├─ docstrings.cpython-39.pyc
│  │     │  │  │     ├─ invalid.cpython-39.pyc
│  │     │  │  │     ├─ mask_ops.cpython-39.pyc
│  │     │  │  │     ├─ methods.cpython-39.pyc
│  │     │  │  │     ├─ missing.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ resample.py
│  │     │  │  ├─ reshape
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ concat.py
│  │     │  │  │  ├─ encoding.py
│  │     │  │  │  ├─ melt.py
│  │     │  │  │  ├─ merge.py
│  │     │  │  │  ├─ pivot.py
│  │     │  │  │  ├─ reshape.py
│  │     │  │  │  ├─ tile.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ api.cpython-39.pyc
│  │     │  │  │     ├─ concat.cpython-39.pyc
│  │     │  │  │     ├─ encoding.cpython-39.pyc
│  │     │  │  │     ├─ melt.cpython-39.pyc
│  │     │  │  │     ├─ merge.cpython-39.pyc
│  │     │  │  │     ├─ pivot.cpython-39.pyc
│  │     │  │  │     ├─ reshape.cpython-39.pyc
│  │     │  │  │     ├─ tile.cpython-39.pyc
│  │     │  │  │     ├─ util.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ roperator.py
│  │     │  │  ├─ sample.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ shared_docs.py
│  │     │  │  ├─ sorting.py
│  │     │  │  ├─ sparse
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ api.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ strings
│  │     │  │  │  ├─ accessor.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ object_array.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ accessor.cpython-39.pyc
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ object_array.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ tools
│  │     │  │  │  ├─ datetimes.py
│  │     │  │  │  ├─ numeric.py
│  │     │  │  │  ├─ timedeltas.py
│  │     │  │  │  ├─ times.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ datetimes.cpython-39.pyc
│  │     │  │  │     ├─ numeric.cpython-39.pyc
│  │     │  │  │     ├─ timedeltas.cpython-39.pyc
│  │     │  │  │     ├─ times.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ util
│  │     │  │  │  ├─ hashing.py
│  │     │  │  │  ├─ numba_.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ hashing.cpython-39.pyc
│  │     │  │  │     ├─ numba_.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ window
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ doc.py
│  │     │  │  │  ├─ ewm.py
│  │     │  │  │  ├─ expanding.py
│  │     │  │  │  ├─ numba_.py
│  │     │  │  │  ├─ online.py
│  │     │  │  │  ├─ rolling.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ doc.cpython-39.pyc
│  │     │  │  │     ├─ ewm.cpython-39.pyc
│  │     │  │  │     ├─ expanding.cpython-39.pyc
│  │     │  │  │     ├─ numba_.cpython-39.pyc
│  │     │  │  │     ├─ online.cpython-39.pyc
│  │     │  │  │     ├─ rolling.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _numba
│  │     │  │  │  ├─ executor.py
│  │     │  │  │  ├─ kernels
│  │     │  │  │  │  ├─ mean_.py
│  │     │  │  │  │  ├─ min_max_.py
│  │     │  │  │  │  ├─ shared.py
│  │     │  │  │  │  ├─ sum_.py
│  │     │  │  │  │  ├─ var_.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ mean_.cpython-39.pyc
│  │     │  │  │  │     ├─ min_max_.cpython-39.pyc
│  │     │  │  │  │     ├─ shared.cpython-39.pyc
│  │     │  │  │  │     ├─ sum_.cpython-39.pyc
│  │     │  │  │  │     ├─ var_.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ executor.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ accessor.cpython-39.pyc
│  │     │  │     ├─ algorithms.cpython-39.pyc
│  │     │  │     ├─ api.cpython-39.pyc
│  │     │  │     ├─ apply.cpython-39.pyc
│  │     │  │     ├─ arraylike.cpython-39.pyc
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ common.cpython-39.pyc
│  │     │  │     ├─ config_init.cpython-39.pyc
│  │     │  │     ├─ construction.cpython-39.pyc
│  │     │  │     ├─ describe.cpython-39.pyc
│  │     │  │     ├─ flags.cpython-39.pyc
│  │     │  │     ├─ frame.cpython-39.pyc
│  │     │  │     ├─ generic.cpython-39.pyc
│  │     │  │     ├─ index.cpython-39.pyc
│  │     │  │     ├─ indexing.cpython-39.pyc
│  │     │  │     ├─ missing.cpython-39.pyc
│  │     │  │     ├─ nanops.cpython-39.pyc
│  │     │  │     ├─ resample.cpython-39.pyc
│  │     │  │     ├─ roperator.cpython-39.pyc
│  │     │  │     ├─ sample.cpython-39.pyc
│  │     │  │     ├─ series.cpython-39.pyc
│  │     │  │     ├─ shared_docs.cpython-39.pyc
│  │     │  │     ├─ sorting.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ errors
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ io
│  │     │  │  ├─ api.py
│  │     │  │  ├─ clipboard
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ clipboards.py
│  │     │  │  ├─ common.py
│  │     │  │  ├─ date_converters.py
│  │     │  │  ├─ excel
│  │     │  │  │  ├─ _base.py
│  │     │  │  │  ├─ _odfreader.py
│  │     │  │  │  ├─ _odswriter.py
│  │     │  │  │  ├─ _openpyxl.py
│  │     │  │  │  ├─ _pyxlsb.py
│  │     │  │  │  ├─ _util.py
│  │     │  │  │  ├─ _xlrd.py
│  │     │  │  │  ├─ _xlsxwriter.py
│  │     │  │  │  ├─ _xlwt.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _base.cpython-39.pyc
│  │     │  │  │     ├─ _odfreader.cpython-39.pyc
│  │     │  │  │     ├─ _odswriter.cpython-39.pyc
│  │     │  │  │     ├─ _openpyxl.cpython-39.pyc
│  │     │  │  │     ├─ _pyxlsb.cpython-39.pyc
│  │     │  │  │     ├─ _util.cpython-39.pyc
│  │     │  │  │     ├─ _xlrd.cpython-39.pyc
│  │     │  │  │     ├─ _xlsxwriter.cpython-39.pyc
│  │     │  │  │     ├─ _xlwt.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ feather_format.py
│  │     │  │  ├─ formats
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ css.py
│  │     │  │  │  ├─ csvs.py
│  │     │  │  │  ├─ excel.py
│  │     │  │  │  ├─ format.py
│  │     │  │  │  ├─ html.py
│  │     │  │  │  ├─ info.py
│  │     │  │  │  ├─ latex.py
│  │     │  │  │  ├─ printing.py
│  │     │  │  │  ├─ string.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ style_render.py
│  │     │  │  │  ├─ templates
│  │     │  │  │  │  ├─ html.tpl
│  │     │  │  │  │  ├─ html_style.tpl
│  │     │  │  │  │  ├─ html_table.tpl
│  │     │  │  │  │  ├─ latex.tpl
│  │     │  │  │  │  ├─ latex_longtable.tpl
│  │     │  │  │  │  ├─ latex_table.tpl
│  │     │  │  │  │  └─ string.tpl
│  │     │  │  │  ├─ xml.py
│  │     │  │  │  ├─ _color_data.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ console.cpython-39.pyc
│  │     │  │  │     ├─ css.cpython-39.pyc
│  │     │  │  │     ├─ csvs.cpython-39.pyc
│  │     │  │  │     ├─ excel.cpython-39.pyc
│  │     │  │  │     ├─ format.cpython-39.pyc
│  │     │  │  │     ├─ html.cpython-39.pyc
│  │     │  │  │     ├─ info.cpython-39.pyc
│  │     │  │  │     ├─ latex.cpython-39.pyc
│  │     │  │  │     ├─ printing.cpython-39.pyc
│  │     │  │  │     ├─ string.cpython-39.pyc
│  │     │  │  │     ├─ style.cpython-39.pyc
│  │     │  │  │     ├─ style_render.cpython-39.pyc
│  │     │  │  │     ├─ xml.cpython-39.pyc
│  │     │  │  │     ├─ _color_data.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ gbq.py
│  │     │  │  ├─ html.py
│  │     │  │  ├─ json
│  │     │  │  │  ├─ _json.py
│  │     │  │  │  ├─ _normalize.py
│  │     │  │  │  ├─ _table_schema.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _json.cpython-39.pyc
│  │     │  │  │     ├─ _normalize.cpython-39.pyc
│  │     │  │  │     ├─ _table_schema.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ orc.py
│  │     │  │  ├─ parquet.py
│  │     │  │  ├─ parsers
│  │     │  │  │  ├─ arrow_parser_wrapper.py
│  │     │  │  │  ├─ base_parser.py
│  │     │  │  │  ├─ c_parser_wrapper.py
│  │     │  │  │  ├─ python_parser.py
│  │     │  │  │  ├─ readers.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ arrow_parser_wrapper.cpython-39.pyc
│  │     │  │  │     ├─ base_parser.cpython-39.pyc
│  │     │  │  │     ├─ c_parser_wrapper.cpython-39.pyc
│  │     │  │  │     ├─ python_parser.cpython-39.pyc
│  │     │  │  │     ├─ readers.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pickle.py
│  │     │  │  ├─ pytables.py
│  │     │  │  ├─ sas
│  │     │  │  │  ├─ sas.pyx
│  │     │  │  │  ├─ sas7bdat.py
│  │     │  │  │  ├─ sasreader.py
│  │     │  │  │  ├─ sas_constants.py
│  │     │  │  │  ├─ sas_xport.py
│  │     │  │  │  ├─ _sas.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _sas.pyi
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ sas7bdat.cpython-39.pyc
│  │     │  │  │     ├─ sasreader.cpython-39.pyc
│  │     │  │  │     ├─ sas_constants.cpython-39.pyc
│  │     │  │  │     ├─ sas_xport.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ spss.py
│  │     │  │  ├─ sql.py
│  │     │  │  ├─ stata.py
│  │     │  │  ├─ xml.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ api.cpython-39.pyc
│  │     │  │     ├─ clipboards.cpython-39.pyc
│  │     │  │     ├─ common.cpython-39.pyc
│  │     │  │     ├─ date_converters.cpython-39.pyc
│  │     │  │     ├─ feather_format.cpython-39.pyc
│  │     │  │     ├─ gbq.cpython-39.pyc
│  │     │  │     ├─ html.cpython-39.pyc
│  │     │  │     ├─ orc.cpython-39.pyc
│  │     │  │     ├─ parquet.cpython-39.pyc
│  │     │  │     ├─ pickle.cpython-39.pyc
│  │     │  │     ├─ pytables.cpython-39.pyc
│  │     │  │     ├─ spss.cpython-39.pyc
│  │     │  │     ├─ sql.cpython-39.pyc
│  │     │  │     ├─ stata.cpython-39.pyc
│  │     │  │     ├─ xml.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ plotting
│  │     │  │  ├─ _core.py
│  │     │  │  ├─ _matplotlib
│  │     │  │  │  ├─ boxplot.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ converter.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ groupby.py
│  │     │  │  │  ├─ hist.py
│  │     │  │  │  ├─ misc.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ timeseries.py
│  │     │  │  │  ├─ tools.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ boxplot.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ converter.cpython-39.pyc
│  │     │  │  │     ├─ core.cpython-39.pyc
│  │     │  │  │     ├─ groupby.cpython-39.pyc
│  │     │  │  │     ├─ hist.cpython-39.pyc
│  │     │  │  │     ├─ misc.cpython-39.pyc
│  │     │  │  │     ├─ style.cpython-39.pyc
│  │     │  │  │     ├─ timeseries.cpython-39.pyc
│  │     │  │  │     ├─ tools.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _misc.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _core.cpython-39.pyc
│  │     │  │     ├─ _misc.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ testing.py
│  │     │  ├─ tests
│  │     │  │  ├─ api
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_types.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_api.cpython-39.pyc
│  │     │  │  │     ├─ test_types.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ apply
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_frame_apply.py
│  │     │  │  │  ├─ test_frame_apply_relabeling.py
│  │     │  │  │  ├─ test_frame_transform.py
│  │     │  │  │  ├─ test_invalid_arg.py
│  │     │  │  │  ├─ test_series_apply.py
│  │     │  │  │  ├─ test_series_apply_relabeling.py
│  │     │  │  │  ├─ test_series_transform.py
│  │     │  │  │  ├─ test_str.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_frame_apply.cpython-39.pyc
│  │     │  │  │     ├─ test_frame_apply_relabeling.cpython-39.pyc
│  │     │  │  │     ├─ test_frame_transform.cpython-39.pyc
│  │     │  │  │     ├─ test_invalid_arg.cpython-39.pyc
│  │     │  │  │     ├─ test_series_apply.cpython-39.pyc
│  │     │  │  │     ├─ test_series_apply_relabeling.cpython-39.pyc
│  │     │  │  │     ├─ test_series_transform.cpython-39.pyc
│  │     │  │  │     ├─ test_str.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ arithmetic
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_array_ops.py
│  │     │  │  │  ├─ test_categorical.py
│  │     │  │  │  ├─ test_datetime64.py
│  │     │  │  │  ├─ test_interval.py
│  │     │  │  │  ├─ test_numeric.py
│  │     │  │  │  ├─ test_object.py
│  │     │  │  │  ├─ test_period.py
│  │     │  │  │  ├─ test_timedelta64.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_array_ops.cpython-39.pyc
│  │     │  │  │     ├─ test_categorical.cpython-39.pyc
│  │     │  │  │     ├─ test_datetime64.cpython-39.pyc
│  │     │  │  │     ├─ test_interval.cpython-39.pyc
│  │     │  │  │     ├─ test_numeric.cpython-39.pyc
│  │     │  │  │     ├─ test_object.cpython-39.pyc
│  │     │  │  │     ├─ test_period.cpython-39.pyc
│  │     │  │  │     ├─ test_timedelta64.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ arrays
│  │     │  │  │  ├─ boolean
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_comparison.py
│  │     │  │  │  │  ├─ test_construction.py
│  │     │  │  │  │  ├─ test_function.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_logical.py
│  │     │  │  │  │  ├─ test_ops.py
│  │     │  │  │  │  ├─ test_reduction.py
│  │     │  │  │  │  ├─ test_repr.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_arithmetic.cpython-39.pyc
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_comparison.cpython-39.pyc
│  │     │  │  │  │     ├─ test_construction.cpython-39.pyc
│  │     │  │  │  │     ├─ test_function.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_logical.cpython-39.pyc
│  │     │  │  │  │     ├─ test_ops.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reduction.cpython-39.pyc
│  │     │  │  │  │     ├─ test_repr.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ categorical
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_algos.py
│  │     │  │  │  │  ├─ test_analytics.py
│  │     │  │  │  │  ├─ test_api.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_dtypes.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_missing.py
│  │     │  │  │  │  ├─ test_operators.py
│  │     │  │  │  │  ├─ test_replace.py
│  │     │  │  │  │  ├─ test_repr.py
│  │     │  │  │  │  ├─ test_sorting.py
│  │     │  │  │  │  ├─ test_subclass.py
│  │     │  │  │  │  ├─ test_take.py
│  │     │  │  │  │  ├─ test_warnings.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_algos.cpython-39.pyc
│  │     │  │  │  │     ├─ test_analytics.cpython-39.pyc
│  │     │  │  │  │     ├─ test_api.cpython-39.pyc
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dtypes.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_missing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_operators.cpython-39.pyc
│  │     │  │  │  │     ├─ test_replace.cpython-39.pyc
│  │     │  │  │  │     ├─ test_repr.cpython-39.pyc
│  │     │  │  │  │     ├─ test_sorting.cpython-39.pyc
│  │     │  │  │  │     ├─ test_subclass.cpython-39.pyc
│  │     │  │  │  │     ├─ test_take.cpython-39.pyc
│  │     │  │  │  │     ├─ test_warnings.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ datetimes
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_reductions.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reductions.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ floating
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_comparison.py
│  │     │  │  │  │  ├─ test_concat.py
│  │     │  │  │  │  ├─ test_construction.py
│  │     │  │  │  │  ├─ test_function.py
│  │     │  │  │  │  ├─ test_repr.py
│  │     │  │  │  │  ├─ test_to_numpy.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_arithmetic.cpython-39.pyc
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_comparison.cpython-39.pyc
│  │     │  │  │  │     ├─ test_concat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_construction.cpython-39.pyc
│  │     │  │  │  │     ├─ test_function.cpython-39.pyc
│  │     │  │  │  │     ├─ test_repr.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_numpy.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ integer
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_comparison.py
│  │     │  │  │  │  ├─ test_concat.py
│  │     │  │  │  │  ├─ test_construction.py
│  │     │  │  │  │  ├─ test_dtypes.py
│  │     │  │  │  │  ├─ test_function.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_repr.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_arithmetic.cpython-39.pyc
│  │     │  │  │  │     ├─ test_comparison.cpython-39.pyc
│  │     │  │  │  │     ├─ test_concat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_construction.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dtypes.cpython-39.pyc
│  │     │  │  │  │     ├─ test_function.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_repr.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ interval
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_interval.py
│  │     │  │  │  │  ├─ test_ops.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_interval.cpython-39.pyc
│  │     │  │  │  │     ├─ test_ops.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ masked
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_arrow_compat.py
│  │     │  │  │  │  ├─ test_function.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_arithmetic.cpython-39.pyc
│  │     │  │  │  │     ├─ test_arrow_compat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_function.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ masked_shared.py
│  │     │  │  │  ├─ numpy_
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_numpy.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_numpy.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ period
│  │     │  │  │  │  ├─ test_arrow_compat.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_reductions.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_arrow_compat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reductions.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ sparse
│  │     │  │  │  │  ├─ test_accessor.py
│  │     │  │  │  │  ├─ test_arithmetics.py
│  │     │  │  │  │  ├─ test_array.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_combine_concat.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_dtype.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_libsparse.py
│  │     │  │  │  │  ├─ test_reductions.py
│  │     │  │  │  │  ├─ test_unary.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_accessor.cpython-39.pyc
│  │     │  │  │  │     ├─ test_arithmetics.cpython-39.pyc
│  │     │  │  │  │     ├─ test_array.cpython-39.pyc
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_combine_concat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dtype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_libsparse.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reductions.cpython-39.pyc
│  │     │  │  │  │     ├─ test_unary.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ string_
│  │     │  │  │  │  ├─ test_string.py
│  │     │  │  │  │  ├─ test_string_arrow.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_string.cpython-39.pyc
│  │     │  │  │  │     ├─ test_string_arrow.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_array.py
│  │     │  │  │  ├─ test_datetimelike.py
│  │     │  │  │  ├─ test_datetimes.py
│  │     │  │  │  ├─ test_ndarray_backed.py
│  │     │  │  │  ├─ test_period.py
│  │     │  │  │  ├─ test_timedeltas.py
│  │     │  │  │  ├─ timedeltas
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_reductions.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reductions.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ masked_shared.cpython-39.pyc
│  │     │  │  │     ├─ test_array.cpython-39.pyc
│  │     │  │  │     ├─ test_datetimelike.cpython-39.pyc
│  │     │  │  │     ├─ test_datetimes.cpython-39.pyc
│  │     │  │  │     ├─ test_ndarray_backed.cpython-39.pyc
│  │     │  │  │     ├─ test_period.cpython-39.pyc
│  │     │  │  │     ├─ test_timedeltas.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ base
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ test_constructors.py
│  │     │  │  │  ├─ test_conversion.py
│  │     │  │  │  ├─ test_fillna.py
│  │     │  │  │  ├─ test_misc.py
│  │     │  │  │  ├─ test_transpose.py
│  │     │  │  │  ├─ test_unique.py
│  │     │  │  │  ├─ test_value_counts.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │     ├─ test_conversion.cpython-39.pyc
│  │     │  │  │     ├─ test_fillna.cpython-39.pyc
│  │     │  │  │     ├─ test_misc.cpython-39.pyc
│  │     │  │  │     ├─ test_transpose.cpython-39.pyc
│  │     │  │  │     ├─ test_unique.cpython-39.pyc
│  │     │  │  │     ├─ test_value_counts.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ computation
│  │     │  │  │  ├─ test_compat.py
│  │     │  │  │  ├─ test_eval.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_compat.cpython-39.pyc
│  │     │  │  │     ├─ test_eval.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ config
│  │     │  │  │  ├─ test_config.py
│  │     │  │  │  ├─ test_localization.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_config.cpython-39.pyc
│  │     │  │  │     ├─ test_localization.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ construction
│  │     │  │  │  ├─ test_extract_array.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_extract_array.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ copy_view
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_internals.py
│  │     │  │  │  ├─ test_methods.py
│  │     │  │  │  ├─ test_setitem.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │     ├─ test_internals.cpython-39.pyc
│  │     │  │  │     ├─ test_methods.cpython-39.pyc
│  │     │  │  │     ├─ test_setitem.cpython-39.pyc
│  │     │  │  │     ├─ util.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ dtypes
│  │     │  │  │  ├─ cast
│  │     │  │  │  │  ├─ test_can_hold_element.py
│  │     │  │  │  │  ├─ test_construct_from_scalar.py
│  │     │  │  │  │  ├─ test_construct_ndarray.py
│  │     │  │  │  │  ├─ test_construct_object_arr.py
│  │     │  │  │  │  ├─ test_dict_compat.py
│  │     │  │  │  │  ├─ test_downcast.py
│  │     │  │  │  │  ├─ test_find_common_type.py
│  │     │  │  │  │  ├─ test_infer_datetimelike.py
│  │     │  │  │  │  ├─ test_infer_dtype.py
│  │     │  │  │  │  ├─ test_maybe_box_native.py
│  │     │  │  │  │  ├─ test_promote.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_can_hold_element.cpython-39.pyc
│  │     │  │  │  │     ├─ test_construct_from_scalar.cpython-39.pyc
│  │     │  │  │  │     ├─ test_construct_ndarray.cpython-39.pyc
│  │     │  │  │  │     ├─ test_construct_object_arr.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dict_compat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_downcast.cpython-39.pyc
│  │     │  │  │  │     ├─ test_find_common_type.cpython-39.pyc
│  │     │  │  │  │     ├─ test_infer_datetimelike.cpython-39.pyc
│  │     │  │  │  │     ├─ test_infer_dtype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_maybe_box_native.cpython-39.pyc
│  │     │  │  │  │     ├─ test_promote.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_concat.py
│  │     │  │  │  ├─ test_dtypes.py
│  │     │  │  │  ├─ test_generic.py
│  │     │  │  │  ├─ test_inference.py
│  │     │  │  │  ├─ test_missing.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_concat.cpython-39.pyc
│  │     │  │  │     ├─ test_dtypes.cpython-39.pyc
│  │     │  │  │     ├─ test_generic.cpython-39.pyc
│  │     │  │  │     ├─ test_inference.cpython-39.pyc
│  │     │  │  │     ├─ test_missing.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ extension
│  │     │  │  │  ├─ array_with_attr
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ test_array_with_attr.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ array.cpython-39.pyc
│  │     │  │  │  │     ├─ test_array_with_attr.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ arrow
│  │     │  │  │  │  ├─ arrays.py
│  │     │  │  │  │  ├─ test_bool.py
│  │     │  │  │  │  ├─ test_string.py
│  │     │  │  │  │  ├─ test_timestamp.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ arrays.cpython-39.pyc
│  │     │  │  │  │     ├─ test_bool.cpython-39.pyc
│  │     │  │  │  │     ├─ test_string.cpython-39.pyc
│  │     │  │  │  │     ├─ test_timestamp.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ base
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ casting.py
│  │     │  │  │  │  ├─ constructors.py
│  │     │  │  │  │  ├─ dim2.py
│  │     │  │  │  │  ├─ dtype.py
│  │     │  │  │  │  ├─ getitem.py
│  │     │  │  │  │  ├─ groupby.py
│  │     │  │  │  │  ├─ index.py
│  │     │  │  │  │  ├─ interface.py
│  │     │  │  │  │  ├─ io.py
│  │     │  │  │  │  ├─ methods.py
│  │     │  │  │  │  ├─ missing.py
│  │     │  │  │  │  ├─ ops.py
│  │     │  │  │  │  ├─ printing.py
│  │     │  │  │  │  ├─ reduce.py
│  │     │  │  │  │  ├─ reshaping.py
│  │     │  │  │  │  ├─ setitem.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │  │     ├─ casting.cpython-39.pyc
│  │     │  │  │  │     ├─ constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ dim2.cpython-39.pyc
│  │     │  │  │  │     ├─ dtype.cpython-39.pyc
│  │     │  │  │  │     ├─ getitem.cpython-39.pyc
│  │     │  │  │  │     ├─ groupby.cpython-39.pyc
│  │     │  │  │  │     ├─ index.cpython-39.pyc
│  │     │  │  │  │     ├─ interface.cpython-39.pyc
│  │     │  │  │  │     ├─ io.cpython-39.pyc
│  │     │  │  │  │     ├─ methods.cpython-39.pyc
│  │     │  │  │  │     ├─ missing.cpython-39.pyc
│  │     │  │  │  │     ├─ ops.cpython-39.pyc
│  │     │  │  │  │     ├─ printing.cpython-39.pyc
│  │     │  │  │  │     ├─ reduce.cpython-39.pyc
│  │     │  │  │  │     ├─ reshaping.cpython-39.pyc
│  │     │  │  │  │     ├─ setitem.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ date
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ array.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ decimal
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ test_decimal.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ array.cpython-39.pyc
│  │     │  │  │  │     ├─ test_decimal.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ json
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ test_json.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ array.cpython-39.pyc
│  │     │  │  │  │     ├─ test_json.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ list
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ test_list.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ array.cpython-39.pyc
│  │     │  │  │  │     ├─ test_list.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_arrow.py
│  │     │  │  │  ├─ test_boolean.py
│  │     │  │  │  ├─ test_categorical.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_datetime.py
│  │     │  │  │  ├─ test_extension.py
│  │     │  │  │  ├─ test_external_block.py
│  │     │  │  │  ├─ test_floating.py
│  │     │  │  │  ├─ test_integer.py
│  │     │  │  │  ├─ test_interval.py
│  │     │  │  │  ├─ test_numpy.py
│  │     │  │  │  ├─ test_period.py
│  │     │  │  │  ├─ test_sparse.py
│  │     │  │  │  ├─ test_string.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_arrow.cpython-39.pyc
│  │     │  │  │     ├─ test_boolean.cpython-39.pyc
│  │     │  │  │     ├─ test_categorical.cpython-39.pyc
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_datetime.cpython-39.pyc
│  │     │  │  │     ├─ test_extension.cpython-39.pyc
│  │     │  │  │     ├─ test_external_block.cpython-39.pyc
│  │     │  │  │     ├─ test_floating.cpython-39.pyc
│  │     │  │  │     ├─ test_integer.cpython-39.pyc
│  │     │  │  │     ├─ test_interval.cpython-39.pyc
│  │     │  │  │     ├─ test_numpy.cpython-39.pyc
│  │     │  │  │     ├─ test_period.cpython-39.pyc
│  │     │  │  │     ├─ test_sparse.cpython-39.pyc
│  │     │  │  │     ├─ test_string.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ frame
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ constructors
│  │     │  │  │  │  ├─ test_from_dict.py
│  │     │  │  │  │  ├─ test_from_records.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_from_dict.cpython-39.pyc
│  │     │  │  │  │     ├─ test_from_records.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ indexing
│  │     │  │  │  │  ├─ test_coercion.py
│  │     │  │  │  │  ├─ test_delitem.py
│  │     │  │  │  │  ├─ test_get.py
│  │     │  │  │  │  ├─ test_getitem.py
│  │     │  │  │  │  ├─ test_get_value.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_insert.py
│  │     │  │  │  │  ├─ test_lookup.py
│  │     │  │  │  │  ├─ test_mask.py
│  │     │  │  │  │  ├─ test_setitem.py
│  │     │  │  │  │  ├─ test_set_value.py
│  │     │  │  │  │  ├─ test_take.py
│  │     │  │  │  │  ├─ test_where.py
│  │     │  │  │  │  ├─ test_xs.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_coercion.cpython-39.pyc
│  │     │  │  │  │     ├─ test_delitem.cpython-39.pyc
│  │     │  │  │  │     ├─ test_get.cpython-39.pyc
│  │     │  │  │  │     ├─ test_getitem.cpython-39.pyc
│  │     │  │  │  │     ├─ test_get_value.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_insert.cpython-39.pyc
│  │     │  │  │  │     ├─ test_lookup.cpython-39.pyc
│  │     │  │  │  │     ├─ test_mask.cpython-39.pyc
│  │     │  │  │  │     ├─ test_setitem.cpython-39.pyc
│  │     │  │  │  │     ├─ test_set_value.cpython-39.pyc
│  │     │  │  │  │     ├─ test_take.cpython-39.pyc
│  │     │  │  │  │     ├─ test_where.cpython-39.pyc
│  │     │  │  │  │     ├─ test_xs.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ methods
│  │     │  │  │  │  ├─ test_add_prefix_suffix.py
│  │     │  │  │  │  ├─ test_align.py
│  │     │  │  │  │  ├─ test_append.py
│  │     │  │  │  │  ├─ test_asfreq.py
│  │     │  │  │  │  ├─ test_asof.py
│  │     │  │  │  │  ├─ test_assign.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_at_time.py
│  │     │  │  │  │  ├─ test_between_time.py
│  │     │  │  │  │  ├─ test_clip.py
│  │     │  │  │  │  ├─ test_combine.py
│  │     │  │  │  │  ├─ test_combine_first.py
│  │     │  │  │  │  ├─ test_compare.py
│  │     │  │  │  │  ├─ test_convert.py
│  │     │  │  │  │  ├─ test_convert_dtypes.py
│  │     │  │  │  │  ├─ test_copy.py
│  │     │  │  │  │  ├─ test_count.py
│  │     │  │  │  │  ├─ test_count_with_level_deprecated.py
│  │     │  │  │  │  ├─ test_cov_corr.py
│  │     │  │  │  │  ├─ test_describe.py
│  │     │  │  │  │  ├─ test_diff.py
│  │     │  │  │  │  ├─ test_dot.py
│  │     │  │  │  │  ├─ test_drop.py
│  │     │  │  │  │  ├─ test_droplevel.py
│  │     │  │  │  │  ├─ test_dropna.py
│  │     │  │  │  │  ├─ test_drop_duplicates.py
│  │     │  │  │  │  ├─ test_dtypes.py
│  │     │  │  │  │  ├─ test_duplicated.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_explode.py
│  │     │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  ├─ test_filter.py
│  │     │  │  │  │  ├─ test_first_and_last.py
│  │     │  │  │  │  ├─ test_first_valid_index.py
│  │     │  │  │  │  ├─ test_get_numeric_data.py
│  │     │  │  │  │  ├─ test_head_tail.py
│  │     │  │  │  │  ├─ test_infer_objects.py
│  │     │  │  │  │  ├─ test_interpolate.py
│  │     │  │  │  │  ├─ test_isin.py
│  │     │  │  │  │  ├─ test_is_homogeneous_dtype.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_matmul.py
│  │     │  │  │  │  ├─ test_nlargest.py
│  │     │  │  │  │  ├─ test_pct_change.py
│  │     │  │  │  │  ├─ test_pipe.py
│  │     │  │  │  │  ├─ test_pop.py
│  │     │  │  │  │  ├─ test_quantile.py
│  │     │  │  │  │  ├─ test_rank.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_reindex_like.py
│  │     │  │  │  │  ├─ test_rename.py
│  │     │  │  │  │  ├─ test_rename_axis.py
│  │     │  │  │  │  ├─ test_reorder_levels.py
│  │     │  │  │  │  ├─ test_replace.py
│  │     │  │  │  │  ├─ test_reset_index.py
│  │     │  │  │  │  ├─ test_round.py
│  │     │  │  │  │  ├─ test_sample.py
│  │     │  │  │  │  ├─ test_select_dtypes.py
│  │     │  │  │  │  ├─ test_set_axis.py
│  │     │  │  │  │  ├─ test_set_index.py
│  │     │  │  │  │  ├─ test_shift.py
│  │     │  │  │  │  ├─ test_sort_index.py
│  │     │  │  │  │  ├─ test_sort_values.py
│  │     │  │  │  │  ├─ test_swapaxes.py
│  │     │  │  │  │  ├─ test_swaplevel.py
│  │     │  │  │  │  ├─ test_to_csv.py
│  │     │  │  │  │  ├─ test_to_dict.py
│  │     │  │  │  │  ├─ test_to_dict_of_blocks.py
│  │     │  │  │  │  ├─ test_to_numpy.py
│  │     │  │  │  │  ├─ test_to_period.py
│  │     │  │  │  │  ├─ test_to_records.py
│  │     │  │  │  │  ├─ test_to_timestamp.py
│  │     │  │  │  │  ├─ test_transpose.py
│  │     │  │  │  │  ├─ test_truncate.py
│  │     │  │  │  │  ├─ test_tz_convert.py
│  │     │  │  │  │  ├─ test_tz_localize.py
│  │     │  │  │  │  ├─ test_update.py
│  │     │  │  │  │  ├─ test_values.py
│  │     │  │  │  │  ├─ test_value_counts.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_add_prefix_suffix.cpython-39.pyc
│  │     │  │  │  │     ├─ test_align.cpython-39.pyc
│  │     │  │  │  │     ├─ test_append.cpython-39.pyc
│  │     │  │  │  │     ├─ test_asfreq.cpython-39.pyc
│  │     │  │  │  │     ├─ test_asof.cpython-39.pyc
│  │     │  │  │  │     ├─ test_assign.cpython-39.pyc
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_at_time.cpython-39.pyc
│  │     │  │  │  │     ├─ test_between_time.cpython-39.pyc
│  │     │  │  │  │     ├─ test_clip.cpython-39.pyc
│  │     │  │  │  │     ├─ test_combine.cpython-39.pyc
│  │     │  │  │  │     ├─ test_combine_first.cpython-39.pyc
│  │     │  │  │  │     ├─ test_compare.cpython-39.pyc
│  │     │  │  │  │     ├─ test_convert.cpython-39.pyc
│  │     │  │  │  │     ├─ test_convert_dtypes.cpython-39.pyc
│  │     │  │  │  │     ├─ test_copy.cpython-39.pyc
│  │     │  │  │  │     ├─ test_count.cpython-39.pyc
│  │     │  │  │  │     ├─ test_count_with_level_deprecated.cpython-39.pyc
│  │     │  │  │  │     ├─ test_cov_corr.cpython-39.pyc
│  │     │  │  │  │     ├─ test_describe.cpython-39.pyc
│  │     │  │  │  │     ├─ test_diff.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dot.cpython-39.pyc
│  │     │  │  │  │     ├─ test_drop.cpython-39.pyc
│  │     │  │  │  │     ├─ test_droplevel.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dropna.cpython-39.pyc
│  │     │  │  │  │     ├─ test_drop_duplicates.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dtypes.cpython-39.pyc
│  │     │  │  │  │     ├─ test_duplicated.cpython-39.pyc
│  │     │  │  │  │     ├─ test_equals.cpython-39.pyc
│  │     │  │  │  │     ├─ test_explode.cpython-39.pyc
│  │     │  │  │  │     ├─ test_fillna.cpython-39.pyc
│  │     │  │  │  │     ├─ test_filter.cpython-39.pyc
│  │     │  │  │  │     ├─ test_first_and_last.cpython-39.pyc
│  │     │  │  │  │     ├─ test_first_valid_index.cpython-39.pyc
│  │     │  │  │  │     ├─ test_get_numeric_data.cpython-39.pyc
│  │     │  │  │  │     ├─ test_head_tail.cpython-39.pyc
│  │     │  │  │  │     ├─ test_infer_objects.cpython-39.pyc
│  │     │  │  │  │     ├─ test_interpolate.cpython-39.pyc
│  │     │  │  │  │     ├─ test_isin.cpython-39.pyc
│  │     │  │  │  │     ├─ test_is_homogeneous_dtype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_join.cpython-39.pyc
│  │     │  │  │  │     ├─ test_matmul.cpython-39.pyc
│  │     │  │  │  │     ├─ test_nlargest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pct_change.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pipe.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pop.cpython-39.pyc
│  │     │  │  │  │     ├─ test_quantile.cpython-39.pyc
│  │     │  │  │  │     ├─ test_rank.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reindex.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reindex_like.cpython-39.pyc
│  │     │  │  │  │     ├─ test_rename.cpython-39.pyc
│  │     │  │  │  │     ├─ test_rename_axis.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reorder_levels.cpython-39.pyc
│  │     │  │  │  │     ├─ test_replace.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reset_index.cpython-39.pyc
│  │     │  │  │  │     ├─ test_round.cpython-39.pyc
│  │     │  │  │  │     ├─ test_sample.cpython-39.pyc
│  │     │  │  │  │     ├─ test_select_dtypes.cpython-39.pyc
│  │     │  │  │  │     ├─ test_set_axis.cpython-39.pyc
│  │     │  │  │  │     ├─ test_set_index.cpython-39.pyc
│  │     │  │  │  │     ├─ test_shift.cpython-39.pyc
│  │     │  │  │  │     ├─ test_sort_index.cpython-39.pyc
│  │     │  │  │  │     ├─ test_sort_values.cpython-39.pyc
│  │     │  │  │  │     ├─ test_swapaxes.cpython-39.pyc
│  │     │  │  │  │     ├─ test_swaplevel.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_csv.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_dict.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_dict_of_blocks.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_numpy.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_period.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_records.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_timestamp.cpython-39.pyc
│  │     │  │  │  │     ├─ test_transpose.cpython-39.pyc
│  │     │  │  │  │     ├─ test_truncate.cpython-39.pyc
│  │     │  │  │  │     ├─ test_tz_convert.cpython-39.pyc
│  │     │  │  │  │     ├─ test_tz_localize.cpython-39.pyc
│  │     │  │  │  │     ├─ test_update.cpython-39.pyc
│  │     │  │  │  │     ├─ test_values.cpython-39.pyc
│  │     │  │  │  │     ├─ test_value_counts.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_alter_axes.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  ├─ test_block_internals.py
│  │     │  │  │  ├─ test_constructors.py
│  │     │  │  │  ├─ test_cumulative.py
│  │     │  │  │  ├─ test_iteration.py
│  │     │  │  │  ├─ test_logical_ops.py
│  │     │  │  │  ├─ test_nonunique_indexes.py
│  │     │  │  │  ├─ test_npfuncs.py
│  │     │  │  │  ├─ test_query_eval.py
│  │     │  │  │  ├─ test_reductions.py
│  │     │  │  │  ├─ test_repr_info.py
│  │     │  │  │  ├─ test_stack_unstack.py
│  │     │  │  │  ├─ test_subclass.py
│  │     │  │  │  ├─ test_ufunc.py
│  │     │  │  │  ├─ test_unary.py
│  │     │  │  │  ├─ test_validate.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_alter_axes.cpython-39.pyc
│  │     │  │  │     ├─ test_api.cpython-39.pyc
│  │     │  │  │     ├─ test_arithmetic.cpython-39.pyc
│  │     │  │  │     ├─ test_block_internals.cpython-39.pyc
│  │     │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │     ├─ test_cumulative.cpython-39.pyc
│  │     │  │  │     ├─ test_iteration.cpython-39.pyc
│  │     │  │  │     ├─ test_logical_ops.cpython-39.pyc
│  │     │  │  │     ├─ test_nonunique_indexes.cpython-39.pyc
│  │     │  │  │     ├─ test_npfuncs.cpython-39.pyc
│  │     │  │  │     ├─ test_query_eval.cpython-39.pyc
│  │     │  │  │     ├─ test_reductions.cpython-39.pyc
│  │     │  │  │     ├─ test_repr_info.cpython-39.pyc
│  │     │  │  │     ├─ test_stack_unstack.cpython-39.pyc
│  │     │  │  │     ├─ test_subclass.cpython-39.pyc
│  │     │  │  │     ├─ test_ufunc.cpython-39.pyc
│  │     │  │  │     ├─ test_unary.cpython-39.pyc
│  │     │  │  │     ├─ test_validate.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ generic
│  │     │  │  │  ├─ test_duplicate_labels.py
│  │     │  │  │  ├─ test_finalize.py
│  │     │  │  │  ├─ test_frame.py
│  │     │  │  │  ├─ test_generic.py
│  │     │  │  │  ├─ test_label_or_level_utils.py
│  │     │  │  │  ├─ test_series.py
│  │     │  │  │  ├─ test_to_xarray.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_duplicate_labels.cpython-39.pyc
│  │     │  │  │     ├─ test_finalize.cpython-39.pyc
│  │     │  │  │     ├─ test_frame.cpython-39.pyc
│  │     │  │  │     ├─ test_generic.cpython-39.pyc
│  │     │  │  │     ├─ test_label_or_level_utils.cpython-39.pyc
│  │     │  │  │     ├─ test_series.cpython-39.pyc
│  │     │  │  │     ├─ test_to_xarray.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ groupby
│  │     │  │  │  ├─ aggregate
│  │     │  │  │  │  ├─ test_aggregate.py
│  │     │  │  │  │  ├─ test_cython.py
│  │     │  │  │  │  ├─ test_numba.py
│  │     │  │  │  │  ├─ test_other.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_aggregate.cpython-39.pyc
│  │     │  │  │  │     ├─ test_cython.cpython-39.pyc
│  │     │  │  │  │     ├─ test_numba.cpython-39.pyc
│  │     │  │  │  │     ├─ test_other.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_allowlist.py
│  │     │  │  │  ├─ test_any_all.py
│  │     │  │  │  ├─ test_apply.py
│  │     │  │  │  ├─ test_apply_mutate.py
│  │     │  │  │  ├─ test_bin_groupby.py
│  │     │  │  │  ├─ test_categorical.py
│  │     │  │  │  ├─ test_counting.py
│  │     │  │  │  ├─ test_filters.py
│  │     │  │  │  ├─ test_frame_value_counts.py
│  │     │  │  │  ├─ test_function.py
│  │     │  │  │  ├─ test_groupby.py
│  │     │  │  │  ├─ test_groupby_dropna.py
│  │     │  │  │  ├─ test_groupby_shift_diff.py
│  │     │  │  │  ├─ test_groupby_subclass.py
│  │     │  │  │  ├─ test_grouping.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_index_as_string.py
│  │     │  │  │  ├─ test_libgroupby.py
│  │     │  │  │  ├─ test_min_max.py
│  │     │  │  │  ├─ test_missing.py
│  │     │  │  │  ├─ test_nth.py
│  │     │  │  │  ├─ test_numba.py
│  │     │  │  │  ├─ test_nunique.py
│  │     │  │  │  ├─ test_pipe.py
│  │     │  │  │  ├─ test_quantile.py
│  │     │  │  │  ├─ test_rank.py
│  │     │  │  │  ├─ test_sample.py
│  │     │  │  │  ├─ test_size.py
│  │     │  │  │  ├─ test_timegrouper.py
│  │     │  │  │  ├─ test_value_counts.py
│  │     │  │  │  ├─ transform
│  │     │  │  │  │  ├─ test_numba.py
│  │     │  │  │  │  ├─ test_transform.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_numba.cpython-39.pyc
│  │     │  │  │  │     ├─ test_transform.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_allowlist.cpython-39.pyc
│  │     │  │  │     ├─ test_any_all.cpython-39.pyc
│  │     │  │  │     ├─ test_apply.cpython-39.pyc
│  │     │  │  │     ├─ test_apply_mutate.cpython-39.pyc
│  │     │  │  │     ├─ test_bin_groupby.cpython-39.pyc
│  │     │  │  │     ├─ test_categorical.cpython-39.pyc
│  │     │  │  │     ├─ test_counting.cpython-39.pyc
│  │     │  │  │     ├─ test_filters.cpython-39.pyc
│  │     │  │  │     ├─ test_frame_value_counts.cpython-39.pyc
│  │     │  │  │     ├─ test_function.cpython-39.pyc
│  │     │  │  │     ├─ test_groupby.cpython-39.pyc
│  │     │  │  │     ├─ test_groupby_dropna.cpython-39.pyc
│  │     │  │  │     ├─ test_groupby_shift_diff.cpython-39.pyc
│  │     │  │  │     ├─ test_groupby_subclass.cpython-39.pyc
│  │     │  │  │     ├─ test_grouping.cpython-39.pyc
│  │     │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │     ├─ test_index_as_string.cpython-39.pyc
│  │     │  │  │     ├─ test_libgroupby.cpython-39.pyc
│  │     │  │  │     ├─ test_min_max.cpython-39.pyc
│  │     │  │  │     ├─ test_missing.cpython-39.pyc
│  │     │  │  │     ├─ test_nth.cpython-39.pyc
│  │     │  │  │     ├─ test_numba.cpython-39.pyc
│  │     │  │  │     ├─ test_nunique.cpython-39.pyc
│  │     │  │  │     ├─ test_pipe.cpython-39.pyc
│  │     │  │  │     ├─ test_quantile.cpython-39.pyc
│  │     │  │  │     ├─ test_rank.cpython-39.pyc
│  │     │  │  │     ├─ test_sample.cpython-39.pyc
│  │     │  │  │     ├─ test_size.cpython-39.pyc
│  │     │  │  │     ├─ test_timegrouper.cpython-39.pyc
│  │     │  │  │     ├─ test_value_counts.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ indexes
│  │     │  │  │  ├─ base_class
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_reshape.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ test_where.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_formats.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pickle.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reshape.cpython-39.pyc
│  │     │  │  │  │     ├─ test_setops.cpython-39.pyc
│  │     │  │  │  │     ├─ test_where.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ categorical
│  │     │  │  │  │  ├─ test_append.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_category.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_map.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_append.cpython-39.pyc
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_category.cpython-39.pyc
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_equals.cpython-39.pyc
│  │     │  │  │  │     ├─ test_fillna.cpython-39.pyc
│  │     │  │  │  │     ├─ test_formats.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_map.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reindex.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ datetimelike.py
│  │     │  │  │  ├─ datetimelike_
│  │     │  │  │  │  ├─ test_drop_duplicates.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_is_monotonic.py
│  │     │  │  │  │  ├─ test_nat.py
│  │     │  │  │  │  ├─ test_sort_values.py
│  │     │  │  │  │  ├─ test_value_counts.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_drop_duplicates.cpython-39.pyc
│  │     │  │  │  │     ├─ test_equals.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_is_monotonic.cpython-39.pyc
│  │     │  │  │  │     ├─ test_nat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_sort_values.cpython-39.pyc
│  │     │  │  │  │     ├─ test_value_counts.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ datetimes
│  │     │  │  │  │  ├─ methods
│  │     │  │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  │  ├─ test_factorize.py
│  │     │  │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  │  ├─ test_insert.py
│  │     │  │  │  │  │  ├─ test_isocalendar.py
│  │     │  │  │  │  │  ├─ test_repeat.py
│  │     │  │  │  │  │  ├─ test_shift.py
│  │     │  │  │  │  │  ├─ test_snap.py
│  │     │  │  │  │  │  ├─ test_to_frame.py
│  │     │  │  │  │  │  ├─ test_to_period.py
│  │     │  │  │  │  │  ├─ test_to_series.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_factorize.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_fillna.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_insert.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_isocalendar.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_repeat.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_shift.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_snap.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_to_frame.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_to_period.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_to_series.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ test_asof.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_datetime.py
│  │     │  │  │  │  ├─ test_datetimelike.py
│  │     │  │  │  │  ├─ test_date_range.py
│  │     │  │  │  │  ├─ test_delete.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_freq_attr.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_map.py
│  │     │  │  │  │  ├─ test_misc.py
│  │     │  │  │  │  ├─ test_npfuncs.py
│  │     │  │  │  │  ├─ test_ops.py
│  │     │  │  │  │  ├─ test_partial_slicing.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_scalar_compat.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ test_timezones.py
│  │     │  │  │  │  ├─ test_unique.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_asof.cpython-39.pyc
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_datetime.cpython-39.pyc
│  │     │  │  │  │     ├─ test_datetimelike.cpython-39.pyc
│  │     │  │  │  │     ├─ test_date_range.cpython-39.pyc
│  │     │  │  │  │     ├─ test_delete.cpython-39.pyc
│  │     │  │  │  │     ├─ test_formats.cpython-39.pyc
│  │     │  │  │  │     ├─ test_freq_attr.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_join.cpython-39.pyc
│  │     │  │  │  │     ├─ test_map.cpython-39.pyc
│  │     │  │  │  │     ├─ test_misc.cpython-39.pyc
│  │     │  │  │  │     ├─ test_npfuncs.cpython-39.pyc
│  │     │  │  │  │     ├─ test_ops.cpython-39.pyc
│  │     │  │  │  │     ├─ test_partial_slicing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pickle.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reindex.cpython-39.pyc
│  │     │  │  │  │     ├─ test_scalar_compat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_setops.cpython-39.pyc
│  │     │  │  │  │     ├─ test_timezones.cpython-39.pyc
│  │     │  │  │  │     ├─ test_unique.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ interval
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_base.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_interval.py
│  │     │  │  │  │  ├─ test_interval_range.py
│  │     │  │  │  │  ├─ test_interval_tree.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_base.cpython-39.pyc
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_equals.cpython-39.pyc
│  │     │  │  │  │     ├─ test_formats.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_interval.cpython-39.pyc
│  │     │  │  │  │     ├─ test_interval_range.cpython-39.pyc
│  │     │  │  │  │     ├─ test_interval_tree.cpython-39.pyc
│  │     │  │  │  │     ├─ test_join.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pickle.cpython-39.pyc
│  │     │  │  │  │     ├─ test_setops.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ multi
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_analytics.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_compat.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_conversion.py
│  │     │  │  │  │  ├─ test_copy.py
│  │     │  │  │  │  ├─ test_drop.py
│  │     │  │  │  │  ├─ test_duplicates.py
│  │     │  │  │  │  ├─ test_equivalence.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_get_level_values.py
│  │     │  │  │  │  ├─ test_get_set.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_integrity.py
│  │     │  │  │  │  ├─ test_isin.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_lexsort.py
│  │     │  │  │  │  ├─ test_missing.py
│  │     │  │  │  │  ├─ test_monotonic.py
│  │     │  │  │  │  ├─ test_names.py
│  │     │  │  │  │  ├─ test_partial_indexing.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_reshape.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ test_sorting.py
│  │     │  │  │  │  ├─ test_take.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_analytics.cpython-39.pyc
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_compat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_conversion.cpython-39.pyc
│  │     │  │  │  │     ├─ test_copy.cpython-39.pyc
│  │     │  │  │  │     ├─ test_drop.cpython-39.pyc
│  │     │  │  │  │     ├─ test_duplicates.cpython-39.pyc
│  │     │  │  │  │     ├─ test_equivalence.cpython-39.pyc
│  │     │  │  │  │     ├─ test_formats.cpython-39.pyc
│  │     │  │  │  │     ├─ test_get_level_values.cpython-39.pyc
│  │     │  │  │  │     ├─ test_get_set.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_integrity.cpython-39.pyc
│  │     │  │  │  │     ├─ test_isin.cpython-39.pyc
│  │     │  │  │  │     ├─ test_join.cpython-39.pyc
│  │     │  │  │  │     ├─ test_lexsort.cpython-39.pyc
│  │     │  │  │  │     ├─ test_missing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_monotonic.cpython-39.pyc
│  │     │  │  │  │     ├─ test_names.cpython-39.pyc
│  │     │  │  │  │     ├─ test_partial_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pickle.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reindex.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reshape.cpython-39.pyc
│  │     │  │  │  │     ├─ test_setops.cpython-39.pyc
│  │     │  │  │  │     ├─ test_sorting.cpython-39.pyc
│  │     │  │  │  │     ├─ test_take.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ numeric
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_numeric.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_join.cpython-39.pyc
│  │     │  │  │  │     ├─ test_numeric.cpython-39.pyc
│  │     │  │  │  │     ├─ test_setops.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ object
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ period
│  │     │  │  │  │  ├─ methods
│  │     │  │  │  │  │  ├─ test_asfreq.py
│  │     │  │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  │  ├─ test_factorize.py
│  │     │  │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  │  ├─ test_insert.py
│  │     │  │  │  │  │  ├─ test_is_full.py
│  │     │  │  │  │  │  ├─ test_repeat.py
│  │     │  │  │  │  │  ├─ test_shift.py
│  │     │  │  │  │  │  ├─ test_to_timestamp.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ test_asfreq.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_factorize.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_fillna.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_insert.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_is_full.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_repeat.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_shift.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_to_timestamp.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_freq_attr.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_monotonic.py
│  │     │  │  │  │  ├─ test_partial_slicing.py
│  │     │  │  │  │  ├─ test_period.py
│  │     │  │  │  │  ├─ test_period_range.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_resolution.py
│  │     │  │  │  │  ├─ test_scalar_compat.py
│  │     │  │  │  │  ├─ test_searchsorted.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ test_tools.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_formats.cpython-39.pyc
│  │     │  │  │  │     ├─ test_freq_attr.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_join.cpython-39.pyc
│  │     │  │  │  │     ├─ test_monotonic.cpython-39.pyc
│  │     │  │  │  │     ├─ test_partial_slicing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_period.cpython-39.pyc
│  │     │  │  │  │     ├─ test_period_range.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pickle.cpython-39.pyc
│  │     │  │  │  │     ├─ test_resolution.cpython-39.pyc
│  │     │  │  │  │     ├─ test_scalar_compat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_searchsorted.cpython-39.pyc
│  │     │  │  │  │     ├─ test_setops.cpython-39.pyc
│  │     │  │  │  │     ├─ test_tools.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ ranges
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_range.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_join.cpython-39.pyc
│  │     │  │  │  │     ├─ test_range.cpython-39.pyc
│  │     │  │  │  │     ├─ test_setops.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_any_index.py
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_engines.py
│  │     │  │  │  ├─ test_frozen.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_index_new.py
│  │     │  │  │  ├─ test_numpy_compat.py
│  │     │  │  │  ├─ test_setops.py
│  │     │  │  │  ├─ test_subclass.py
│  │     │  │  │  ├─ timedeltas
│  │     │  │  │  │  ├─ methods
│  │     │  │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  │  ├─ test_factorize.py
│  │     │  │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  │  ├─ test_insert.py
│  │     │  │  │  │  │  ├─ test_repeat.py
│  │     │  │  │  │  │  ├─ test_shift.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_factorize.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_fillna.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_insert.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_repeat.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_shift.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_delete.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_freq_attr.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_ops.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_scalar_compat.py
│  │     │  │  │  │  ├─ test_searchsorted.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ test_timedelta.py
│  │     │  │  │  │  ├─ test_timedelta_range.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_delete.cpython-39.pyc
│  │     │  │  │  │     ├─ test_formats.cpython-39.pyc
│  │     │  │  │  │     ├─ test_freq_attr.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_join.cpython-39.pyc
│  │     │  │  │  │     ├─ test_ops.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pickle.cpython-39.pyc
│  │     │  │  │  │     ├─ test_scalar_compat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_searchsorted.cpython-39.pyc
│  │     │  │  │  │     ├─ test_setops.cpython-39.pyc
│  │     │  │  │  │     ├─ test_timedelta.cpython-39.pyc
│  │     │  │  │  │     ├─ test_timedelta_range.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ datetimelike.cpython-39.pyc
│  │     │  │  │     ├─ test_any_index.cpython-39.pyc
│  │     │  │  │     ├─ test_base.cpython-39.pyc
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_engines.cpython-39.pyc
│  │     │  │  │     ├─ test_frozen.cpython-39.pyc
│  │     │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │     ├─ test_index_new.cpython-39.pyc
│  │     │  │  │     ├─ test_numpy_compat.cpython-39.pyc
│  │     │  │  │     ├─ test_setops.cpython-39.pyc
│  │     │  │  │     ├─ test_subclass.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ indexing
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ interval
│  │     │  │  │  │  ├─ test_interval.py
│  │     │  │  │  │  ├─ test_interval_new.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_interval.cpython-39.pyc
│  │     │  │  │  │     ├─ test_interval_new.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ multiindex
│  │     │  │  │  │  ├─ test_chaining_and_caching.py
│  │     │  │  │  │  ├─ test_datetime.py
│  │     │  │  │  │  ├─ test_getitem.py
│  │     │  │  │  │  ├─ test_iloc.py
│  │     │  │  │  │  ├─ test_indexing_slow.py
│  │     │  │  │  │  ├─ test_loc.py
│  │     │  │  │  │  ├─ test_multiindex.py
│  │     │  │  │  │  ├─ test_partial.py
│  │     │  │  │  │  ├─ test_setitem.py
│  │     │  │  │  │  ├─ test_slice.py
│  │     │  │  │  │  ├─ test_sorted.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_chaining_and_caching.cpython-39.pyc
│  │     │  │  │  │     ├─ test_datetime.cpython-39.pyc
│  │     │  │  │  │     ├─ test_getitem.cpython-39.pyc
│  │     │  │  │  │     ├─ test_iloc.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing_slow.cpython-39.pyc
│  │     │  │  │  │     ├─ test_loc.cpython-39.pyc
│  │     │  │  │  │     ├─ test_multiindex.cpython-39.pyc
│  │     │  │  │  │     ├─ test_partial.cpython-39.pyc
│  │     │  │  │  │     ├─ test_setitem.cpython-39.pyc
│  │     │  │  │  │     ├─ test_slice.cpython-39.pyc
│  │     │  │  │  │     ├─ test_sorted.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_at.py
│  │     │  │  │  ├─ test_categorical.py
│  │     │  │  │  ├─ test_chaining_and_caching.py
│  │     │  │  │  ├─ test_check_indexer.py
│  │     │  │  │  ├─ test_coercion.py
│  │     │  │  │  ├─ test_datetime.py
│  │     │  │  │  ├─ test_floats.py
│  │     │  │  │  ├─ test_iat.py
│  │     │  │  │  ├─ test_iloc.py
│  │     │  │  │  ├─ test_indexers.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_loc.py
│  │     │  │  │  ├─ test_na_indexing.py
│  │     │  │  │  ├─ test_partial.py
│  │     │  │  │  ├─ test_scalar.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ test_at.cpython-39.pyc
│  │     │  │  │     ├─ test_categorical.cpython-39.pyc
│  │     │  │  │     ├─ test_chaining_and_caching.cpython-39.pyc
│  │     │  │  │     ├─ test_check_indexer.cpython-39.pyc
│  │     │  │  │     ├─ test_coercion.cpython-39.pyc
│  │     │  │  │     ├─ test_datetime.cpython-39.pyc
│  │     │  │  │     ├─ test_floats.cpython-39.pyc
│  │     │  │  │     ├─ test_iat.cpython-39.pyc
│  │     │  │  │     ├─ test_iloc.cpython-39.pyc
│  │     │  │  │     ├─ test_indexers.cpython-39.pyc
│  │     │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │     ├─ test_loc.cpython-39.pyc
│  │     │  │  │     ├─ test_na_indexing.cpython-39.pyc
│  │     │  │  │     ├─ test_partial.cpython-39.pyc
│  │     │  │  │     ├─ test_scalar.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ interchange
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_impl.py
│  │     │  │  │  ├─ test_spec_conformance.py
│  │     │  │  │  ├─ test_utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_impl.cpython-39.pyc
│  │     │  │  │     ├─ test_spec_conformance.cpython-39.pyc
│  │     │  │  │     ├─ test_utils.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ internals
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_internals.py
│  │     │  │  │  ├─ test_managers.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_api.cpython-39.pyc
│  │     │  │  │     ├─ test_internals.cpython-39.pyc
│  │     │  │  │     ├─ test_managers.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ io
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ fixed_width
│  │     │  │  │  │  │  └─ fixed_width_format.txt
│  │     │  │  │  │  ├─ gbq_fake_job.txt
│  │     │  │  │  │  ├─ legacy_pickle
│  │     │  │  │  │  │  └─ 1.2.4
│  │     │  │  │  │  │     └─ empty_frame_v1_2_4-GH#42345.pkl
│  │     │  │  │  │  ├─ parquet
│  │     │  │  │  │  │  └─ simple.parquet
│  │     │  │  │  │  ├─ pickle
│  │     │  │  │  │  │  ├─ test_mi_py27.pkl
│  │     │  │  │  │  │  └─ test_py27.pkl
│  │     │  │  │  │  └─ xml
│  │     │  │  │  │     ├─ baby_names.xml
│  │     │  │  │  │     ├─ books.xml
│  │     │  │  │  │     ├─ cta_rail_lines.kml
│  │     │  │  │  │     ├─ doc_ch_utf.xml
│  │     │  │  │  │     ├─ flatten_doc.xsl
│  │     │  │  │  │     └─ row_field_output.xsl
│  │     │  │  │  ├─ excel
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_odf.py
│  │     │  │  │  │  ├─ test_odswriter.py
│  │     │  │  │  │  ├─ test_openpyxl.py
│  │     │  │  │  │  ├─ test_readers.py
│  │     │  │  │  │  ├─ test_style.py
│  │     │  │  │  │  ├─ test_writers.py
│  │     │  │  │  │  ├─ test_xlrd.py
│  │     │  │  │  │  ├─ test_xlsxwriter.py
│  │     │  │  │  │  ├─ test_xlwt.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_odf.cpython-39.pyc
│  │     │  │  │  │     ├─ test_odswriter.cpython-39.pyc
│  │     │  │  │  │     ├─ test_openpyxl.cpython-39.pyc
│  │     │  │  │  │     ├─ test_readers.cpython-39.pyc
│  │     │  │  │  │     ├─ test_style.cpython-39.pyc
│  │     │  │  │  │     ├─ test_writers.cpython-39.pyc
│  │     │  │  │  │     ├─ test_xlrd.cpython-39.pyc
│  │     │  │  │  │     ├─ test_xlsxwriter.cpython-39.pyc
│  │     │  │  │  │     ├─ test_xlwt.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ formats
│  │     │  │  │  │  ├─ style
│  │     │  │  │  │  │  ├─ test_bar.py
│  │     │  │  │  │  │  ├─ test_deprecated.py
│  │     │  │  │  │  │  ├─ test_exceptions.py
│  │     │  │  │  │  │  ├─ test_format.py
│  │     │  │  │  │  │  ├─ test_highlight.py
│  │     │  │  │  │  │  ├─ test_html.py
│  │     │  │  │  │  │  ├─ test_matplotlib.py
│  │     │  │  │  │  │  ├─ test_non_unique.py
│  │     │  │  │  │  │  ├─ test_style.py
│  │     │  │  │  │  │  ├─ test_tooltip.py
│  │     │  │  │  │  │  ├─ test_to_latex.py
│  │     │  │  │  │  │  ├─ test_to_string.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ test_bar.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_deprecated.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_exceptions.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_format.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_highlight.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_html.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_matplotlib.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_non_unique.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_style.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_tooltip.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_to_latex.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_to_string.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ test_console.py
│  │     │  │  │  │  ├─ test_css.py
│  │     │  │  │  │  ├─ test_eng_formatting.py
│  │     │  │  │  │  ├─ test_format.py
│  │     │  │  │  │  ├─ test_info.py
│  │     │  │  │  │  ├─ test_printing.py
│  │     │  │  │  │  ├─ test_series_info.py
│  │     │  │  │  │  ├─ test_to_csv.py
│  │     │  │  │  │  ├─ test_to_excel.py
│  │     │  │  │  │  ├─ test_to_html.py
│  │     │  │  │  │  ├─ test_to_latex.py
│  │     │  │  │  │  ├─ test_to_markdown.py
│  │     │  │  │  │  ├─ test_to_string.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_console.cpython-39.pyc
│  │     │  │  │  │     ├─ test_css.cpython-39.pyc
│  │     │  │  │  │     ├─ test_eng_formatting.cpython-39.pyc
│  │     │  │  │  │     ├─ test_format.cpython-39.pyc
│  │     │  │  │  │     ├─ test_info.cpython-39.pyc
│  │     │  │  │  │     ├─ test_printing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_series_info.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_csv.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_excel.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_html.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_latex.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_markdown.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_string.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ generate_legacy_storage_files.py
│  │     │  │  │  ├─ json
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_compression.py
│  │     │  │  │  │  ├─ test_deprecated_kwargs.py
│  │     │  │  │  │  ├─ test_json_table_schema.py
│  │     │  │  │  │  ├─ test_json_table_schema_ext_dtype.py
│  │     │  │  │  │  ├─ test_normalize.py
│  │     │  │  │  │  ├─ test_pandas.py
│  │     │  │  │  │  ├─ test_readlines.py
│  │     │  │  │  │  ├─ test_ujson.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_compression.cpython-39.pyc
│  │     │  │  │  │     ├─ test_deprecated_kwargs.cpython-39.pyc
│  │     │  │  │  │     ├─ test_json_table_schema.cpython-39.pyc
│  │     │  │  │  │     ├─ test_json_table_schema_ext_dtype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_normalize.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pandas.cpython-39.pyc
│  │     │  │  │  │     ├─ test_readlines.cpython-39.pyc
│  │     │  │  │  │     ├─ test_ujson.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ parser
│  │     │  │  │  │  ├─ common
│  │     │  │  │  │  │  ├─ test_chunksize.py
│  │     │  │  │  │  │  ├─ test_common_basic.py
│  │     │  │  │  │  │  ├─ test_data_list.py
│  │     │  │  │  │  │  ├─ test_decimal.py
│  │     │  │  │  │  │  ├─ test_file_buffer_url.py
│  │     │  │  │  │  │  ├─ test_float.py
│  │     │  │  │  │  │  ├─ test_index.py
│  │     │  │  │  │  │  ├─ test_inf.py
│  │     │  │  │  │  │  ├─ test_ints.py
│  │     │  │  │  │  │  ├─ test_iterator.py
│  │     │  │  │  │  │  ├─ test_read_errors.py
│  │     │  │  │  │  │  ├─ test_verbose.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ test_chunksize.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_common_basic.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_data_list.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_decimal.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_file_buffer_url.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_float.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_index.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_inf.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_ints.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_iterator.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_read_errors.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_verbose.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ dtypes
│  │     │  │  │  │  │  ├─ test_categorical.py
│  │     │  │  │  │  │  ├─ test_dtypes_basic.py
│  │     │  │  │  │  │  ├─ test_empty.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ test_categorical.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_dtypes_basic.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_empty.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ test_comment.py
│  │     │  │  │  │  ├─ test_compression.py
│  │     │  │  │  │  ├─ test_converters.py
│  │     │  │  │  │  ├─ test_c_parser_only.py
│  │     │  │  │  │  ├─ test_dialect.py
│  │     │  │  │  │  ├─ test_encoding.py
│  │     │  │  │  │  ├─ test_header.py
│  │     │  │  │  │  ├─ test_index_col.py
│  │     │  │  │  │  ├─ test_mangle_dupes.py
│  │     │  │  │  │  ├─ test_multi_thread.py
│  │     │  │  │  │  ├─ test_na_values.py
│  │     │  │  │  │  ├─ test_network.py
│  │     │  │  │  │  ├─ test_parse_dates.py
│  │     │  │  │  │  ├─ test_python_parser_only.py
│  │     │  │  │  │  ├─ test_quoting.py
│  │     │  │  │  │  ├─ test_read_fwf.py
│  │     │  │  │  │  ├─ test_skiprows.py
│  │     │  │  │  │  ├─ test_textreader.py
│  │     │  │  │  │  ├─ test_unsupported.py
│  │     │  │  │  │  ├─ usecols
│  │     │  │  │  │  │  ├─ test_parse_dates.py
│  │     │  │  │  │  │  ├─ test_strings.py
│  │     │  │  │  │  │  ├─ test_usecols_basic.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ test_parse_dates.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_strings.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_usecols_basic.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_comment.cpython-39.pyc
│  │     │  │  │  │     ├─ test_compression.cpython-39.pyc
│  │     │  │  │  │     ├─ test_converters.cpython-39.pyc
│  │     │  │  │  │     ├─ test_c_parser_only.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dialect.cpython-39.pyc
│  │     │  │  │  │     ├─ test_encoding.cpython-39.pyc
│  │     │  │  │  │     ├─ test_header.cpython-39.pyc
│  │     │  │  │  │     ├─ test_index_col.cpython-39.pyc
│  │     │  │  │  │     ├─ test_mangle_dupes.cpython-39.pyc
│  │     │  │  │  │     ├─ test_multi_thread.cpython-39.pyc
│  │     │  │  │  │     ├─ test_na_values.cpython-39.pyc
│  │     │  │  │  │     ├─ test_network.cpython-39.pyc
│  │     │  │  │  │     ├─ test_parse_dates.cpython-39.pyc
│  │     │  │  │  │     ├─ test_python_parser_only.cpython-39.pyc
│  │     │  │  │  │     ├─ test_quoting.cpython-39.pyc
│  │     │  │  │  │     ├─ test_read_fwf.cpython-39.pyc
│  │     │  │  │  │     ├─ test_skiprows.cpython-39.pyc
│  │     │  │  │  │     ├─ test_textreader.cpython-39.pyc
│  │     │  │  │  │     ├─ test_unsupported.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ pytables
│  │     │  │  │  │  ├─ common.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_append.py
│  │     │  │  │  │  ├─ test_categorical.py
│  │     │  │  │  │  ├─ test_compat.py
│  │     │  │  │  │  ├─ test_complex.py
│  │     │  │  │  │  ├─ test_errors.py
│  │     │  │  │  │  ├─ test_file_handling.py
│  │     │  │  │  │  ├─ test_keys.py
│  │     │  │  │  │  ├─ test_put.py
│  │     │  │  │  │  ├─ test_pytables_missing.py
│  │     │  │  │  │  ├─ test_read.py
│  │     │  │  │  │  ├─ test_retain_attributes.py
│  │     │  │  │  │  ├─ test_round_trip.py
│  │     │  │  │  │  ├─ test_select.py
│  │     │  │  │  │  ├─ test_store.py
│  │     │  │  │  │  ├─ test_subclass.py
│  │     │  │  │  │  ├─ test_timezones.py
│  │     │  │  │  │  ├─ test_time_series.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_append.cpython-39.pyc
│  │     │  │  │  │     ├─ test_categorical.cpython-39.pyc
│  │     │  │  │  │     ├─ test_compat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_complex.cpython-39.pyc
│  │     │  │  │  │     ├─ test_errors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_file_handling.cpython-39.pyc
│  │     │  │  │  │     ├─ test_keys.cpython-39.pyc
│  │     │  │  │  │     ├─ test_put.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pytables_missing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_read.cpython-39.pyc
│  │     │  │  │  │     ├─ test_retain_attributes.cpython-39.pyc
│  │     │  │  │  │     ├─ test_round_trip.cpython-39.pyc
│  │     │  │  │  │     ├─ test_select.cpython-39.pyc
│  │     │  │  │  │     ├─ test_store.cpython-39.pyc
│  │     │  │  │  │     ├─ test_subclass.cpython-39.pyc
│  │     │  │  │  │     ├─ test_timezones.cpython-39.pyc
│  │     │  │  │  │     ├─ test_time_series.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ sas
│  │     │  │  │  │  ├─ test_sas.py
│  │     │  │  │  │  ├─ test_sas7bdat.py
│  │     │  │  │  │  ├─ test_xport.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_sas.cpython-39.pyc
│  │     │  │  │  │     ├─ test_sas7bdat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_xport.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_clipboard.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_compression.py
│  │     │  │  │  ├─ test_date_converters.py
│  │     │  │  │  ├─ test_feather.py
│  │     │  │  │  ├─ test_fsspec.py
│  │     │  │  │  ├─ test_gcs.py
│  │     │  │  │  ├─ test_html.py
│  │     │  │  │  ├─ test_orc.py
│  │     │  │  │  ├─ test_parquet.py
│  │     │  │  │  ├─ test_pickle.py
│  │     │  │  │  ├─ test_s3.py
│  │     │  │  │  ├─ test_spss.py
│  │     │  │  │  ├─ test_sql.py
│  │     │  │  │  ├─ test_stata.py
│  │     │  │  │  ├─ test_user_agent.py
│  │     │  │  │  ├─ xml
│  │     │  │  │  │  ├─ test_to_xml.py
│  │     │  │  │  │  ├─ test_xml.py
│  │     │  │  │  │  ├─ test_xml_dtypes.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_to_xml.cpython-39.pyc
│  │     │  │  │  │     ├─ test_xml.cpython-39.pyc
│  │     │  │  │  │     ├─ test_xml_dtypes.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ generate_legacy_storage_files.cpython-39.pyc
│  │     │  │  │     ├─ test_clipboard.cpython-39.pyc
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_compression.cpython-39.pyc
│  │     │  │  │     ├─ test_date_converters.cpython-39.pyc
│  │     │  │  │     ├─ test_feather.cpython-39.pyc
│  │     │  │  │     ├─ test_fsspec.cpython-39.pyc
│  │     │  │  │     ├─ test_gcs.cpython-39.pyc
│  │     │  │  │     ├─ test_html.cpython-39.pyc
│  │     │  │  │     ├─ test_orc.cpython-39.pyc
│  │     │  │  │     ├─ test_parquet.cpython-39.pyc
│  │     │  │  │     ├─ test_pickle.cpython-39.pyc
│  │     │  │  │     ├─ test_s3.cpython-39.pyc
│  │     │  │  │     ├─ test_spss.cpython-39.pyc
│  │     │  │  │     ├─ test_sql.cpython-39.pyc
│  │     │  │  │     ├─ test_stata.cpython-39.pyc
│  │     │  │  │     ├─ test_user_agent.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ libs
│  │     │  │  │  ├─ test_hashtable.py
│  │     │  │  │  ├─ test_join.py
│  │     │  │  │  ├─ test_lib.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_hashtable.cpython-39.pyc
│  │     │  │  │     ├─ test_join.cpython-39.pyc
│  │     │  │  │     ├─ test_lib.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ plotting
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ frame
│  │     │  │  │  │  ├─ test_frame.py
│  │     │  │  │  │  ├─ test_frame_color.py
│  │     │  │  │  │  ├─ test_frame_groupby.py
│  │     │  │  │  │  ├─ test_frame_legend.py
│  │     │  │  │  │  ├─ test_frame_subplots.py
│  │     │  │  │  │  ├─ test_hist_box_by.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_frame.cpython-39.pyc
│  │     │  │  │  │     ├─ test_frame_color.cpython-39.pyc
│  │     │  │  │  │     ├─ test_frame_groupby.cpython-39.pyc
│  │     │  │  │  │     ├─ test_frame_legend.cpython-39.pyc
│  │     │  │  │  │     ├─ test_frame_subplots.cpython-39.pyc
│  │     │  │  │  │     ├─ test_hist_box_by.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_backend.py
│  │     │  │  │  ├─ test_boxplot_method.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_converter.py
│  │     │  │  │  ├─ test_datetimelike.py
│  │     │  │  │  ├─ test_groupby.py
│  │     │  │  │  ├─ test_hist_method.py
│  │     │  │  │  ├─ test_misc.py
│  │     │  │  │  ├─ test_series.py
│  │     │  │  │  ├─ test_style.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_backend.cpython-39.pyc
│  │     │  │  │     ├─ test_boxplot_method.cpython-39.pyc
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_converter.cpython-39.pyc
│  │     │  │  │     ├─ test_datetimelike.cpython-39.pyc
│  │     │  │  │     ├─ test_groupby.cpython-39.pyc
│  │     │  │  │     ├─ test_hist_method.cpython-39.pyc
│  │     │  │  │     ├─ test_misc.cpython-39.pyc
│  │     │  │  │     ├─ test_series.cpython-39.pyc
│  │     │  │  │     ├─ test_style.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ reductions
│  │     │  │  │  ├─ test_reductions.py
│  │     │  │  │  ├─ test_stat_reductions.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_reductions.cpython-39.pyc
│  │     │  │  │     ├─ test_stat_reductions.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ resample
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_datetime_index.py
│  │     │  │  │  ├─ test_deprecated.py
│  │     │  │  │  ├─ test_period_index.py
│  │     │  │  │  ├─ test_resampler_grouper.py
│  │     │  │  │  ├─ test_resample_api.py
│  │     │  │  │  ├─ test_timedelta.py
│  │     │  │  │  ├─ test_time_grouper.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_base.cpython-39.pyc
│  │     │  │  │     ├─ test_datetime_index.cpython-39.pyc
│  │     │  │  │     ├─ test_deprecated.cpython-39.pyc
│  │     │  │  │     ├─ test_period_index.cpython-39.pyc
│  │     │  │  │     ├─ test_resampler_grouper.cpython-39.pyc
│  │     │  │  │     ├─ test_resample_api.cpython-39.pyc
│  │     │  │  │     ├─ test_timedelta.cpython-39.pyc
│  │     │  │  │     ├─ test_time_grouper.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ reshape
│  │     │  │  │  ├─ concat
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_append.py
│  │     │  │  │  │  ├─ test_append_common.py
│  │     │  │  │  │  ├─ test_categorical.py
│  │     │  │  │  │  ├─ test_concat.py
│  │     │  │  │  │  ├─ test_dataframe.py
│  │     │  │  │  │  ├─ test_datetimes.py
│  │     │  │  │  │  ├─ test_empty.py
│  │     │  │  │  │  ├─ test_index.py
│  │     │  │  │  │  ├─ test_invalid.py
│  │     │  │  │  │  ├─ test_series.py
│  │     │  │  │  │  ├─ test_sort.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_append.cpython-39.pyc
│  │     │  │  │  │     ├─ test_append_common.cpython-39.pyc
│  │     │  │  │  │     ├─ test_categorical.cpython-39.pyc
│  │     │  │  │  │     ├─ test_concat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dataframe.cpython-39.pyc
│  │     │  │  │  │     ├─ test_datetimes.cpython-39.pyc
│  │     │  │  │  │     ├─ test_empty.cpython-39.pyc
│  │     │  │  │  │     ├─ test_index.cpython-39.pyc
│  │     │  │  │  │     ├─ test_invalid.cpython-39.pyc
│  │     │  │  │  │     ├─ test_series.cpython-39.pyc
│  │     │  │  │  │     ├─ test_sort.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ merge
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_merge.py
│  │     │  │  │  │  ├─ test_merge_asof.py
│  │     │  │  │  │  ├─ test_merge_cross.py
│  │     │  │  │  │  ├─ test_merge_index_as_string.py
│  │     │  │  │  │  ├─ test_merge_ordered.py
│  │     │  │  │  │  ├─ test_multi.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_join.cpython-39.pyc
│  │     │  │  │  │     ├─ test_merge.cpython-39.pyc
│  │     │  │  │  │     ├─ test_merge_asof.cpython-39.pyc
│  │     │  │  │  │     ├─ test_merge_cross.cpython-39.pyc
│  │     │  │  │  │     ├─ test_merge_index_as_string.cpython-39.pyc
│  │     │  │  │  │     ├─ test_merge_ordered.cpython-39.pyc
│  │     │  │  │  │     ├─ test_multi.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_crosstab.py
│  │     │  │  │  ├─ test_cut.py
│  │     │  │  │  ├─ test_from_dummies.py
│  │     │  │  │  ├─ test_get_dummies.py
│  │     │  │  │  ├─ test_melt.py
│  │     │  │  │  ├─ test_pivot.py
│  │     │  │  │  ├─ test_pivot_multilevel.py
│  │     │  │  │  ├─ test_qcut.py
│  │     │  │  │  ├─ test_union_categoricals.py
│  │     │  │  │  ├─ test_util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_crosstab.cpython-39.pyc
│  │     │  │  │     ├─ test_cut.cpython-39.pyc
│  │     │  │  │     ├─ test_from_dummies.cpython-39.pyc
│  │     │  │  │     ├─ test_get_dummies.cpython-39.pyc
│  │     │  │  │     ├─ test_melt.cpython-39.pyc
│  │     │  │  │     ├─ test_pivot.cpython-39.pyc
│  │     │  │  │     ├─ test_pivot_multilevel.cpython-39.pyc
│  │     │  │  │     ├─ test_qcut.cpython-39.pyc
│  │     │  │  │     ├─ test_union_categoricals.cpython-39.pyc
│  │     │  │  │     ├─ test_util.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ scalar
│  │     │  │  │  ├─ interval
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_interval.py
│  │     │  │  │  │  ├─ test_ops.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_arithmetic.cpython-39.pyc
│  │     │  │  │  │     ├─ test_interval.cpython-39.pyc
│  │     │  │  │  │     ├─ test_ops.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ period
│  │     │  │  │  │  ├─ test_asfreq.py
│  │     │  │  │  │  ├─ test_period.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_asfreq.cpython-39.pyc
│  │     │  │  │  │     ├─ test_period.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_nat.py
│  │     │  │  │  ├─ test_na_scalar.py
│  │     │  │  │  ├─ timedelta
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_timedelta.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_arithmetic.cpython-39.pyc
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_formats.cpython-39.pyc
│  │     │  │  │  │     ├─ test_timedelta.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ timestamp
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_comparisons.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_rendering.py
│  │     │  │  │  │  ├─ test_timestamp.py
│  │     │  │  │  │  ├─ test_timezones.py
│  │     │  │  │  │  ├─ test_unary_ops.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_arithmetic.cpython-39.pyc
│  │     │  │  │  │     ├─ test_comparisons.cpython-39.pyc
│  │     │  │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │  │     ├─ test_formats.cpython-39.pyc
│  │     │  │  │  │     ├─ test_rendering.cpython-39.pyc
│  │     │  │  │  │     ├─ test_timestamp.cpython-39.pyc
│  │     │  │  │  │     ├─ test_timezones.cpython-39.pyc
│  │     │  │  │  │     ├─ test_unary_ops.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_nat.cpython-39.pyc
│  │     │  │  │     ├─ test_na_scalar.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ series
│  │     │  │  │  ├─ accessors
│  │     │  │  │  │  ├─ test_cat_accessor.py
│  │     │  │  │  │  ├─ test_dt_accessor.py
│  │     │  │  │  │  ├─ test_sparse_accessor.py
│  │     │  │  │  │  ├─ test_str_accessor.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_cat_accessor.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dt_accessor.cpython-39.pyc
│  │     │  │  │  │     ├─ test_sparse_accessor.cpython-39.pyc
│  │     │  │  │  │     ├─ test_str_accessor.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ indexing
│  │     │  │  │  │  ├─ test_datetime.py
│  │     │  │  │  │  ├─ test_delitem.py
│  │     │  │  │  │  ├─ test_get.py
│  │     │  │  │  │  ├─ test_getitem.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_mask.py
│  │     │  │  │  │  ├─ test_setitem.py
│  │     │  │  │  │  ├─ test_set_value.py
│  │     │  │  │  │  ├─ test_take.py
│  │     │  │  │  │  ├─ test_where.py
│  │     │  │  │  │  ├─ test_xs.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_datetime.cpython-39.pyc
│  │     │  │  │  │     ├─ test_delitem.cpython-39.pyc
│  │     │  │  │  │     ├─ test_get.cpython-39.pyc
│  │     │  │  │  │     ├─ test_getitem.cpython-39.pyc
│  │     │  │  │  │     ├─ test_indexing.cpython-39.pyc
│  │     │  │  │  │     ├─ test_mask.cpython-39.pyc
│  │     │  │  │  │     ├─ test_setitem.cpython-39.pyc
│  │     │  │  │  │     ├─ test_set_value.cpython-39.pyc
│  │     │  │  │  │     ├─ test_take.cpython-39.pyc
│  │     │  │  │  │     ├─ test_where.cpython-39.pyc
│  │     │  │  │  │     ├─ test_xs.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ methods
│  │     │  │  │  │  ├─ test_align.py
│  │     │  │  │  │  ├─ test_append.py
│  │     │  │  │  │  ├─ test_argsort.py
│  │     │  │  │  │  ├─ test_asof.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_autocorr.py
│  │     │  │  │  │  ├─ test_between.py
│  │     │  │  │  │  ├─ test_clip.py
│  │     │  │  │  │  ├─ test_combine.py
│  │     │  │  │  │  ├─ test_combine_first.py
│  │     │  │  │  │  ├─ test_compare.py
│  │     │  │  │  │  ├─ test_convert.py
│  │     │  │  │  │  ├─ test_convert_dtypes.py
│  │     │  │  │  │  ├─ test_copy.py
│  │     │  │  │  │  ├─ test_count.py
│  │     │  │  │  │  ├─ test_cov_corr.py
│  │     │  │  │  │  ├─ test_describe.py
│  │     │  │  │  │  ├─ test_diff.py
│  │     │  │  │  │  ├─ test_drop.py
│  │     │  │  │  │  ├─ test_dropna.py
│  │     │  │  │  │  ├─ test_drop_duplicates.py
│  │     │  │  │  │  ├─ test_dtypes.py
│  │     │  │  │  │  ├─ test_duplicated.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_explode.py
│  │     │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  ├─ test_get_numeric_data.py
│  │     │  │  │  │  ├─ test_head_tail.py
│  │     │  │  │  │  ├─ test_infer_objects.py
│  │     │  │  │  │  ├─ test_interpolate.py
│  │     │  │  │  │  ├─ test_isin.py
│  │     │  │  │  │  ├─ test_isna.py
│  │     │  │  │  │  ├─ test_is_monotonic.py
│  │     │  │  │  │  ├─ test_is_unique.py
│  │     │  │  │  │  ├─ test_item.py
│  │     │  │  │  │  ├─ test_matmul.py
│  │     │  │  │  │  ├─ test_nlargest.py
│  │     │  │  │  │  ├─ test_nunique.py
│  │     │  │  │  │  ├─ test_pct_change.py
│  │     │  │  │  │  ├─ test_pop.py
│  │     │  │  │  │  ├─ test_quantile.py
│  │     │  │  │  │  ├─ test_rank.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_reindex_like.py
│  │     │  │  │  │  ├─ test_rename.py
│  │     │  │  │  │  ├─ test_rename_axis.py
│  │     │  │  │  │  ├─ test_repeat.py
│  │     │  │  │  │  ├─ test_replace.py
│  │     │  │  │  │  ├─ test_reset_index.py
│  │     │  │  │  │  ├─ test_round.py
│  │     │  │  │  │  ├─ test_searchsorted.py
│  │     │  │  │  │  ├─ test_set_name.py
│  │     │  │  │  │  ├─ test_sort_index.py
│  │     │  │  │  │  ├─ test_sort_values.py
│  │     │  │  │  │  ├─ test_to_csv.py
│  │     │  │  │  │  ├─ test_to_dict.py
│  │     │  │  │  │  ├─ test_to_frame.py
│  │     │  │  │  │  ├─ test_truncate.py
│  │     │  │  │  │  ├─ test_tz_localize.py
│  │     │  │  │  │  ├─ test_unique.py
│  │     │  │  │  │  ├─ test_unstack.py
│  │     │  │  │  │  ├─ test_update.py
│  │     │  │  │  │  ├─ test_values.py
│  │     │  │  │  │  ├─ test_value_counts.py
│  │     │  │  │  │  ├─ test_view.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_align.cpython-39.pyc
│  │     │  │  │  │     ├─ test_append.cpython-39.pyc
│  │     │  │  │  │     ├─ test_argsort.cpython-39.pyc
│  │     │  │  │  │     ├─ test_asof.cpython-39.pyc
│  │     │  │  │  │     ├─ test_astype.cpython-39.pyc
│  │     │  │  │  │     ├─ test_autocorr.cpython-39.pyc
│  │     │  │  │  │     ├─ test_between.cpython-39.pyc
│  │     │  │  │  │     ├─ test_clip.cpython-39.pyc
│  │     │  │  │  │     ├─ test_combine.cpython-39.pyc
│  │     │  │  │  │     ├─ test_combine_first.cpython-39.pyc
│  │     │  │  │  │     ├─ test_compare.cpython-39.pyc
│  │     │  │  │  │     ├─ test_convert.cpython-39.pyc
│  │     │  │  │  │     ├─ test_convert_dtypes.cpython-39.pyc
│  │     │  │  │  │     ├─ test_copy.cpython-39.pyc
│  │     │  │  │  │     ├─ test_count.cpython-39.pyc
│  │     │  │  │  │     ├─ test_cov_corr.cpython-39.pyc
│  │     │  │  │  │     ├─ test_describe.cpython-39.pyc
│  │     │  │  │  │     ├─ test_diff.cpython-39.pyc
│  │     │  │  │  │     ├─ test_drop.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dropna.cpython-39.pyc
│  │     │  │  │  │     ├─ test_drop_duplicates.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dtypes.cpython-39.pyc
│  │     │  │  │  │     ├─ test_duplicated.cpython-39.pyc
│  │     │  │  │  │     ├─ test_equals.cpython-39.pyc
│  │     │  │  │  │     ├─ test_explode.cpython-39.pyc
│  │     │  │  │  │     ├─ test_fillna.cpython-39.pyc
│  │     │  │  │  │     ├─ test_get_numeric_data.cpython-39.pyc
│  │     │  │  │  │     ├─ test_head_tail.cpython-39.pyc
│  │     │  │  │  │     ├─ test_infer_objects.cpython-39.pyc
│  │     │  │  │  │     ├─ test_interpolate.cpython-39.pyc
│  │     │  │  │  │     ├─ test_isin.cpython-39.pyc
│  │     │  │  │  │     ├─ test_isna.cpython-39.pyc
│  │     │  │  │  │     ├─ test_is_monotonic.cpython-39.pyc
│  │     │  │  │  │     ├─ test_is_unique.cpython-39.pyc
│  │     │  │  │  │     ├─ test_item.cpython-39.pyc
│  │     │  │  │  │     ├─ test_matmul.cpython-39.pyc
│  │     │  │  │  │     ├─ test_nlargest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_nunique.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pct_change.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pop.cpython-39.pyc
│  │     │  │  │  │     ├─ test_quantile.cpython-39.pyc
│  │     │  │  │  │     ├─ test_rank.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reindex.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reindex_like.cpython-39.pyc
│  │     │  │  │  │     ├─ test_rename.cpython-39.pyc
│  │     │  │  │  │     ├─ test_rename_axis.cpython-39.pyc
│  │     │  │  │  │     ├─ test_repeat.cpython-39.pyc
│  │     │  │  │  │     ├─ test_replace.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reset_index.cpython-39.pyc
│  │     │  │  │  │     ├─ test_round.cpython-39.pyc
│  │     │  │  │  │     ├─ test_searchsorted.cpython-39.pyc
│  │     │  │  │  │     ├─ test_set_name.cpython-39.pyc
│  │     │  │  │  │     ├─ test_sort_index.cpython-39.pyc
│  │     │  │  │  │     ├─ test_sort_values.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_csv.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_dict.cpython-39.pyc
│  │     │  │  │  │     ├─ test_to_frame.cpython-39.pyc
│  │     │  │  │  │     ├─ test_truncate.cpython-39.pyc
│  │     │  │  │  │     ├─ test_tz_localize.cpython-39.pyc
│  │     │  │  │  │     ├─ test_unique.cpython-39.pyc
│  │     │  │  │  │     ├─ test_unstack.cpython-39.pyc
│  │     │  │  │  │     ├─ test_update.cpython-39.pyc
│  │     │  │  │  │     ├─ test_values.cpython-39.pyc
│  │     │  │  │  │     ├─ test_value_counts.cpython-39.pyc
│  │     │  │  │  │     ├─ test_view.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  ├─ test_constructors.py
│  │     │  │  │  ├─ test_cumulative.py
│  │     │  │  │  ├─ test_iteration.py
│  │     │  │  │  ├─ test_logical_ops.py
│  │     │  │  │  ├─ test_missing.py
│  │     │  │  │  ├─ test_npfuncs.py
│  │     │  │  │  ├─ test_reductions.py
│  │     │  │  │  ├─ test_repr.py
│  │     │  │  │  ├─ test_subclass.py
│  │     │  │  │  ├─ test_ufunc.py
│  │     │  │  │  ├─ test_unary.py
│  │     │  │  │  ├─ test_validate.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_api.cpython-39.pyc
│  │     │  │  │     ├─ test_arithmetic.cpython-39.pyc
│  │     │  │  │     ├─ test_constructors.cpython-39.pyc
│  │     │  │  │     ├─ test_cumulative.cpython-39.pyc
│  │     │  │  │     ├─ test_iteration.cpython-39.pyc
│  │     │  │  │     ├─ test_logical_ops.cpython-39.pyc
│  │     │  │  │     ├─ test_missing.cpython-39.pyc
│  │     │  │  │     ├─ test_npfuncs.cpython-39.pyc
│  │     │  │  │     ├─ test_reductions.cpython-39.pyc
│  │     │  │  │     ├─ test_repr.cpython-39.pyc
│  │     │  │  │     ├─ test_subclass.cpython-39.pyc
│  │     │  │  │     ├─ test_ufunc.cpython-39.pyc
│  │     │  │  │     ├─ test_unary.cpython-39.pyc
│  │     │  │  │     ├─ test_validate.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ strings
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_case_justify.py
│  │     │  │  │  ├─ test_cat.py
│  │     │  │  │  ├─ test_extract.py
│  │     │  │  │  ├─ test_find_replace.py
│  │     │  │  │  ├─ test_get_dummies.py
│  │     │  │  │  ├─ test_split_partition.py
│  │     │  │  │  ├─ test_strings.py
│  │     │  │  │  ├─ test_string_array.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_api.cpython-39.pyc
│  │     │  │  │     ├─ test_case_justify.cpython-39.pyc
│  │     │  │  │     ├─ test_cat.cpython-39.pyc
│  │     │  │  │     ├─ test_extract.cpython-39.pyc
│  │     │  │  │     ├─ test_find_replace.cpython-39.pyc
│  │     │  │  │     ├─ test_get_dummies.cpython-39.pyc
│  │     │  │  │     ├─ test_split_partition.cpython-39.pyc
│  │     │  │  │     ├─ test_strings.cpython-39.pyc
│  │     │  │  │     ├─ test_string_array.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ test_aggregation.py
│  │     │  │  ├─ test_algos.py
│  │     │  │  ├─ test_common.py
│  │     │  │  ├─ test_downstream.py
│  │     │  │  ├─ test_errors.py
│  │     │  │  ├─ test_expressions.py
│  │     │  │  ├─ test_flags.py
│  │     │  │  ├─ test_multilevel.py
│  │     │  │  ├─ test_nanops.py
│  │     │  │  ├─ test_optional_dependency.py
│  │     │  │  ├─ test_register_accessor.py
│  │     │  │  ├─ test_sorting.py
│  │     │  │  ├─ test_take.py
│  │     │  │  ├─ tools
│  │     │  │  │  ├─ test_to_datetime.py
│  │     │  │  │  ├─ test_to_numeric.py
│  │     │  │  │  ├─ test_to_time.py
│  │     │  │  │  ├─ test_to_timedelta.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_to_datetime.cpython-39.pyc
│  │     │  │  │     ├─ test_to_numeric.cpython-39.pyc
│  │     │  │  │     ├─ test_to_time.cpython-39.pyc
│  │     │  │  │     ├─ test_to_timedelta.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ tseries
│  │     │  │  │  ├─ frequencies
│  │     │  │  │  │  ├─ test_frequencies.py
│  │     │  │  │  │  ├─ test_freq_code.py
│  │     │  │  │  │  ├─ test_inference.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_frequencies.cpython-39.pyc
│  │     │  │  │  │     ├─ test_freq_code.cpython-39.pyc
│  │     │  │  │  │     ├─ test_inference.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ holiday
│  │     │  │  │  │  ├─ test_calendar.py
│  │     │  │  │  │  ├─ test_federal.py
│  │     │  │  │  │  ├─ test_holiday.py
│  │     │  │  │  │  ├─ test_observance.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_calendar.cpython-39.pyc
│  │     │  │  │  │     ├─ test_federal.cpython-39.pyc
│  │     │  │  │  │     ├─ test_holiday.cpython-39.pyc
│  │     │  │  │  │     ├─ test_observance.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ offsets
│  │     │  │  │  │  ├─ common.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_business_day.py
│  │     │  │  │  │  ├─ test_business_hour.py
│  │     │  │  │  │  ├─ test_business_month.py
│  │     │  │  │  │  ├─ test_business_quarter.py
│  │     │  │  │  │  ├─ test_business_year.py
│  │     │  │  │  │  ├─ test_custom_business_day.py
│  │     │  │  │  │  ├─ test_custom_business_hour.py
│  │     │  │  │  │  ├─ test_custom_business_month.py
│  │     │  │  │  │  ├─ test_dst.py
│  │     │  │  │  │  ├─ test_easter.py
│  │     │  │  │  │  ├─ test_fiscal.py
│  │     │  │  │  │  ├─ test_index.py
│  │     │  │  │  │  ├─ test_month.py
│  │     │  │  │  │  ├─ test_offsets.py
│  │     │  │  │  │  ├─ test_offsets_properties.py
│  │     │  │  │  │  ├─ test_quarter.py
│  │     │  │  │  │  ├─ test_ticks.py
│  │     │  │  │  │  ├─ test_week.py
│  │     │  │  │  │  ├─ test_year.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_business_day.cpython-39.pyc
│  │     │  │  │  │     ├─ test_business_hour.cpython-39.pyc
│  │     │  │  │  │     ├─ test_business_month.cpython-39.pyc
│  │     │  │  │  │     ├─ test_business_quarter.cpython-39.pyc
│  │     │  │  │  │     ├─ test_business_year.cpython-39.pyc
│  │     │  │  │  │     ├─ test_custom_business_day.cpython-39.pyc
│  │     │  │  │  │     ├─ test_custom_business_hour.cpython-39.pyc
│  │     │  │  │  │     ├─ test_custom_business_month.cpython-39.pyc
│  │     │  │  │  │     ├─ test_dst.cpython-39.pyc
│  │     │  │  │  │     ├─ test_easter.cpython-39.pyc
│  │     │  │  │  │     ├─ test_fiscal.cpython-39.pyc
│  │     │  │  │  │     ├─ test_index.cpython-39.pyc
│  │     │  │  │  │     ├─ test_month.cpython-39.pyc
│  │     │  │  │  │     ├─ test_offsets.cpython-39.pyc
│  │     │  │  │  │     ├─ test_offsets_properties.cpython-39.pyc
│  │     │  │  │  │     ├─ test_quarter.cpython-39.pyc
│  │     │  │  │  │     ├─ test_ticks.cpython-39.pyc
│  │     │  │  │  │     ├─ test_week.cpython-39.pyc
│  │     │  │  │  │     ├─ test_year.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ tslibs
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_array_to_datetime.py
│  │     │  │  │  ├─ test_ccalendar.py
│  │     │  │  │  ├─ test_conversion.py
│  │     │  │  │  ├─ test_fields.py
│  │     │  │  │  ├─ test_libfrequencies.py
│  │     │  │  │  ├─ test_liboffsets.py
│  │     │  │  │  ├─ test_np_datetime.py
│  │     │  │  │  ├─ test_parse_iso8601.py
│  │     │  │  │  ├─ test_parsing.py
│  │     │  │  │  ├─ test_period_asfreq.py
│  │     │  │  │  ├─ test_resolution.py
│  │     │  │  │  ├─ test_timedeltas.py
│  │     │  │  │  ├─ test_timezones.py
│  │     │  │  │  ├─ test_to_offset.py
│  │     │  │  │  ├─ test_tzconversion.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_api.cpython-39.pyc
│  │     │  │  │     ├─ test_array_to_datetime.cpython-39.pyc
│  │     │  │  │     ├─ test_ccalendar.cpython-39.pyc
│  │     │  │  │     ├─ test_conversion.cpython-39.pyc
│  │     │  │  │     ├─ test_fields.cpython-39.pyc
│  │     │  │  │     ├─ test_libfrequencies.cpython-39.pyc
│  │     │  │  │     ├─ test_liboffsets.cpython-39.pyc
│  │     │  │  │     ├─ test_np_datetime.cpython-39.pyc
│  │     │  │  │     ├─ test_parse_iso8601.cpython-39.pyc
│  │     │  │  │     ├─ test_parsing.cpython-39.pyc
│  │     │  │  │     ├─ test_period_asfreq.cpython-39.pyc
│  │     │  │  │     ├─ test_resolution.cpython-39.pyc
│  │     │  │  │     ├─ test_timedeltas.cpython-39.pyc
│  │     │  │  │     ├─ test_timezones.cpython-39.pyc
│  │     │  │  │     ├─ test_to_offset.cpython-39.pyc
│  │     │  │  │     ├─ test_tzconversion.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ util
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_assert_almost_equal.py
│  │     │  │  │  ├─ test_assert_attr_equal.py
│  │     │  │  │  ├─ test_assert_categorical_equal.py
│  │     │  │  │  ├─ test_assert_extension_array_equal.py
│  │     │  │  │  ├─ test_assert_frame_equal.py
│  │     │  │  │  ├─ test_assert_index_equal.py
│  │     │  │  │  ├─ test_assert_interval_array_equal.py
│  │     │  │  │  ├─ test_assert_numpy_array_equal.py
│  │     │  │  │  ├─ test_assert_produces_warning.py
│  │     │  │  │  ├─ test_assert_series_equal.py
│  │     │  │  │  ├─ test_deprecate.py
│  │     │  │  │  ├─ test_deprecate_kwarg.py
│  │     │  │  │  ├─ test_deprecate_nonkeyword_arguments.py
│  │     │  │  │  ├─ test_doc.py
│  │     │  │  │  ├─ test_hashing.py
│  │     │  │  │  ├─ test_make_objects.py
│  │     │  │  │  ├─ test_numba.py
│  │     │  │  │  ├─ test_rewrite_warning.py
│  │     │  │  │  ├─ test_safe_import.py
│  │     │  │  │  ├─ test_shares_memory.py
│  │     │  │  │  ├─ test_show_versions.py
│  │     │  │  │  ├─ test_util.py
│  │     │  │  │  ├─ test_validate_args.py
│  │     │  │  │  ├─ test_validate_args_and_kwargs.py
│  │     │  │  │  ├─ test_validate_inclusive.py
│  │     │  │  │  ├─ test_validate_kwargs.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_assert_almost_equal.cpython-39.pyc
│  │     │  │  │     ├─ test_assert_attr_equal.cpython-39.pyc
│  │     │  │  │     ├─ test_assert_categorical_equal.cpython-39.pyc
│  │     │  │  │     ├─ test_assert_extension_array_equal.cpython-39.pyc
│  │     │  │  │     ├─ test_assert_frame_equal.cpython-39.pyc
│  │     │  │  │     ├─ test_assert_index_equal.cpython-39.pyc
│  │     │  │  │     ├─ test_assert_interval_array_equal.cpython-39.pyc
│  │     │  │  │     ├─ test_assert_numpy_array_equal.cpython-39.pyc
│  │     │  │  │     ├─ test_assert_produces_warning.cpython-39.pyc
│  │     │  │  │     ├─ test_assert_series_equal.cpython-39.pyc
│  │     │  │  │     ├─ test_deprecate.cpython-39.pyc
│  │     │  │  │     ├─ test_deprecate_kwarg.cpython-39.pyc
│  │     │  │  │     ├─ test_deprecate_nonkeyword_arguments.cpython-39.pyc
│  │     │  │  │     ├─ test_doc.cpython-39.pyc
│  │     │  │  │     ├─ test_hashing.cpython-39.pyc
│  │     │  │  │     ├─ test_make_objects.cpython-39.pyc
│  │     │  │  │     ├─ test_numba.cpython-39.pyc
│  │     │  │  │     ├─ test_rewrite_warning.cpython-39.pyc
│  │     │  │  │     ├─ test_safe_import.cpython-39.pyc
│  │     │  │  │     ├─ test_shares_memory.cpython-39.pyc
│  │     │  │  │     ├─ test_show_versions.cpython-39.pyc
│  │     │  │  │     ├─ test_util.cpython-39.pyc
│  │     │  │  │     ├─ test_validate_args.cpython-39.pyc
│  │     │  │  │     ├─ test_validate_args_and_kwargs.cpython-39.pyc
│  │     │  │  │     ├─ test_validate_inclusive.cpython-39.pyc
│  │     │  │  │     ├─ test_validate_kwargs.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ window
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ moments
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_moments_consistency_ewm.py
│  │     │  │  │  │  ├─ test_moments_consistency_expanding.py
│  │     │  │  │  │  ├─ test_moments_consistency_rolling.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_moments_consistency_ewm.cpython-39.pyc
│  │     │  │  │  │     ├─ test_moments_consistency_expanding.cpython-39.pyc
│  │     │  │  │  │     ├─ test_moments_consistency_rolling.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_apply.py
│  │     │  │  │  ├─ test_base_indexer.py
│  │     │  │  │  ├─ test_cython_aggregations.py
│  │     │  │  │  ├─ test_dtypes.py
│  │     │  │  │  ├─ test_ewm.py
│  │     │  │  │  ├─ test_expanding.py
│  │     │  │  │  ├─ test_groupby.py
│  │     │  │  │  ├─ test_numba.py
│  │     │  │  │  ├─ test_online.py
│  │     │  │  │  ├─ test_pairwise.py
│  │     │  │  │  ├─ test_rolling.py
│  │     │  │  │  ├─ test_rolling_functions.py
│  │     │  │  │  ├─ test_rolling_quantile.py
│  │     │  │  │  ├─ test_rolling_skew_kurt.py
│  │     │  │  │  ├─ test_timeseries_window.py
│  │     │  │  │  ├─ test_win_type.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_api.cpython-39.pyc
│  │     │  │  │     ├─ test_apply.cpython-39.pyc
│  │     │  │  │     ├─ test_base_indexer.cpython-39.pyc
│  │     │  │  │     ├─ test_cython_aggregations.cpython-39.pyc
│  │     │  │  │     ├─ test_dtypes.cpython-39.pyc
│  │     │  │  │     ├─ test_ewm.cpython-39.pyc
│  │     │  │  │     ├─ test_expanding.cpython-39.pyc
│  │     │  │  │     ├─ test_groupby.cpython-39.pyc
│  │     │  │  │     ├─ test_numba.cpython-39.pyc
│  │     │  │  │     ├─ test_online.cpython-39.pyc
│  │     │  │  │     ├─ test_pairwise.cpython-39.pyc
│  │     │  │  │     ├─ test_rolling.cpython-39.pyc
│  │     │  │  │     ├─ test_rolling_functions.cpython-39.pyc
│  │     │  │  │     ├─ test_rolling_quantile.cpython-39.pyc
│  │     │  │  │     ├─ test_rolling_skew_kurt.cpython-39.pyc
│  │     │  │  │     ├─ test_timeseries_window.cpython-39.pyc
│  │     │  │  │     ├─ test_win_type.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ test_aggregation.cpython-39.pyc
│  │     │  │     ├─ test_algos.cpython-39.pyc
│  │     │  │     ├─ test_common.cpython-39.pyc
│  │     │  │     ├─ test_downstream.cpython-39.pyc
│  │     │  │     ├─ test_errors.cpython-39.pyc
│  │     │  │     ├─ test_expressions.cpython-39.pyc
│  │     │  │     ├─ test_flags.cpython-39.pyc
│  │     │  │     ├─ test_multilevel.cpython-39.pyc
│  │     │  │     ├─ test_nanops.cpython-39.pyc
│  │     │  │     ├─ test_optional_dependency.cpython-39.pyc
│  │     │  │     ├─ test_register_accessor.cpython-39.pyc
│  │     │  │     ├─ test_sorting.cpython-39.pyc
│  │     │  │     ├─ test_take.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ tseries
│  │     │  │  ├─ api.py
│  │     │  │  ├─ frequencies.py
│  │     │  │  ├─ holiday.py
│  │     │  │  ├─ offsets.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ api.cpython-39.pyc
│  │     │  │     ├─ frequencies.cpython-39.pyc
│  │     │  │     ├─ holiday.cpython-39.pyc
│  │     │  │     ├─ offsets.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ util
│  │     │  │  ├─ testing.py
│  │     │  │  ├─ version
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _decorators.py
│  │     │  │  ├─ _doctools.py
│  │     │  │  ├─ _exceptions.py
│  │     │  │  ├─ _print_versions.py
│  │     │  │  ├─ _tester.py
│  │     │  │  ├─ _test_decorators.py
│  │     │  │  ├─ _validators.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ testing.cpython-39.pyc
│  │     │  │     ├─ _decorators.cpython-39.pyc
│  │     │  │     ├─ _doctools.cpython-39.pyc
│  │     │  │     ├─ _exceptions.cpython-39.pyc
│  │     │  │     ├─ _print_versions.cpython-39.pyc
│  │     │  │     ├─ _tester.cpython-39.pyc
│  │     │  │     ├─ _test_decorators.cpython-39.pyc
│  │     │  │     ├─ _validators.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _config
│  │     │  │  ├─ config.py
│  │     │  │  ├─ dates.py
│  │     │  │  ├─ display.py
│  │     │  │  ├─ localization.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ config.cpython-39.pyc
│  │     │  │     ├─ dates.cpython-39.pyc
│  │     │  │     ├─ display.cpython-39.pyc
│  │     │  │     ├─ localization.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _libs
│  │     │  │  ├─ algos.cp39-win_amd64.pyd
│  │     │  │  ├─ algos.pxd
│  │     │  │  ├─ algos.pyi
│  │     │  │  ├─ algos.pyx
│  │     │  │  ├─ algos_common_helper.pxi.in
│  │     │  │  ├─ algos_take_helper.pxi.in
│  │     │  │  ├─ arrays.cp39-win_amd64.pyd
│  │     │  │  ├─ arrays.pxd
│  │     │  │  ├─ arrays.pyi
│  │     │  │  ├─ arrays.pyx
│  │     │  │  ├─ dtypes.pxd
│  │     │  │  ├─ groupby.cp39-win_amd64.pyd
│  │     │  │  ├─ groupby.pyi
│  │     │  │  ├─ groupby.pyx
│  │     │  │  ├─ hashing.cp39-win_amd64.pyd
│  │     │  │  ├─ hashing.pyi
│  │     │  │  ├─ hashing.pyx
│  │     │  │  ├─ hashtable.cp39-win_amd64.pyd
│  │     │  │  ├─ hashtable.pxd
│  │     │  │  ├─ hashtable.pyi
│  │     │  │  ├─ hashtable.pyx
│  │     │  │  ├─ hashtable_class_helper.pxi.in
│  │     │  │  ├─ hashtable_func_helper.pxi.in
│  │     │  │  ├─ index.cp39-win_amd64.pyd
│  │     │  │  ├─ index.pyi
│  │     │  │  ├─ index.pyx
│  │     │  │  ├─ indexing.cp39-win_amd64.pyd
│  │     │  │  ├─ indexing.pyi
│  │     │  │  ├─ indexing.pyx
│  │     │  │  ├─ index_class_helper.pxi.in
│  │     │  │  ├─ internals.cp39-win_amd64.pyd
│  │     │  │  ├─ internals.pyi
│  │     │  │  ├─ internals.pyx
│  │     │  │  ├─ interval.cp39-win_amd64.pyd
│  │     │  │  ├─ interval.pyi
│  │     │  │  ├─ interval.pyx
│  │     │  │  ├─ intervaltree.pxi.in
│  │     │  │  ├─ join.cp39-win_amd64.pyd
│  │     │  │  ├─ join.pyi
│  │     │  │  ├─ join.pyx
│  │     │  │  ├─ json.cp39-win_amd64.pyd
│  │     │  │  ├─ json.pyi
│  │     │  │  ├─ khash.pxd
│  │     │  │  ├─ khash_for_primitive_helper.pxi.in
│  │     │  │  ├─ lib.cp39-win_amd64.pyd
│  │     │  │  ├─ lib.pxd
│  │     │  │  ├─ lib.pyi
│  │     │  │  ├─ lib.pyx
│  │     │  │  ├─ missing.cp39-win_amd64.pyd
│  │     │  │  ├─ missing.pxd
│  │     │  │  ├─ missing.pyi
│  │     │  │  ├─ missing.pyx
│  │     │  │  ├─ ops.cp39-win_amd64.pyd
│  │     │  │  ├─ ops.pyi
│  │     │  │  ├─ ops.pyx
│  │     │  │  ├─ ops_dispatch.cp39-win_amd64.pyd
│  │     │  │  ├─ ops_dispatch.pyi
│  │     │  │  ├─ ops_dispatch.pyx
│  │     │  │  ├─ parsers.cp39-win_amd64.pyd
│  │     │  │  ├─ parsers.pyi
│  │     │  │  ├─ parsers.pyx
│  │     │  │  ├─ properties.cp39-win_amd64.pyd
│  │     │  │  ├─ properties.pyi
│  │     │  │  ├─ properties.pyx
│  │     │  │  ├─ reduction.cp39-win_amd64.pyd
│  │     │  │  ├─ reduction.pyi
│  │     │  │  ├─ reduction.pyx
│  │     │  │  ├─ reshape.cp39-win_amd64.pyd
│  │     │  │  ├─ reshape.pyi
│  │     │  │  ├─ reshape.pyx
│  │     │  │  ├─ sparse.cp39-win_amd64.pyd
│  │     │  │  ├─ sparse.pyi
│  │     │  │  ├─ sparse.pyx
│  │     │  │  ├─ sparse_op_helper.pxi.in
│  │     │  │  ├─ testing.cp39-win_amd64.pyd
│  │     │  │  ├─ testing.pyi
│  │     │  │  ├─ testing.pyx
│  │     │  │  ├─ tslib.cp39-win_amd64.pyd
│  │     │  │  ├─ tslib.pyi
│  │     │  │  ├─ tslib.pyx
│  │     │  │  ├─ tslibs
│  │     │  │  │  ├─ base.cp39-win_amd64.pyd
│  │     │  │  │  ├─ base.pxd
│  │     │  │  │  ├─ base.pyx
│  │     │  │  │  ├─ ccalendar.cp39-win_amd64.pyd
│  │     │  │  │  ├─ ccalendar.pxd
│  │     │  │  │  ├─ ccalendar.pyi
│  │     │  │  │  ├─ ccalendar.pyx
│  │     │  │  │  ├─ conversion.cp39-win_amd64.pyd
│  │     │  │  │  ├─ conversion.pxd
│  │     │  │  │  ├─ conversion.pyi
│  │     │  │  │  ├─ conversion.pyx
│  │     │  │  │  ├─ dtypes.cp39-win_amd64.pyd
│  │     │  │  │  ├─ dtypes.pxd
│  │     │  │  │  ├─ dtypes.pyi
│  │     │  │  │  ├─ dtypes.pyx
│  │     │  │  │  ├─ fields.cp39-win_amd64.pyd
│  │     │  │  │  ├─ fields.pyi
│  │     │  │  │  ├─ fields.pyx
│  │     │  │  │  ├─ nattype.cp39-win_amd64.pyd
│  │     │  │  │  ├─ nattype.pxd
│  │     │  │  │  ├─ nattype.pyi
│  │     │  │  │  ├─ nattype.pyx
│  │     │  │  │  ├─ np_datetime.cp39-win_amd64.pyd
│  │     │  │  │  ├─ np_datetime.pxd
│  │     │  │  │  ├─ np_datetime.pyi
│  │     │  │  │  ├─ np_datetime.pyx
│  │     │  │  │  ├─ offsets.cp39-win_amd64.pyd
│  │     │  │  │  ├─ offsets.pxd
│  │     │  │  │  ├─ offsets.pyi
│  │     │  │  │  ├─ offsets.pyx
│  │     │  │  │  ├─ parsing.cp39-win_amd64.pyd
│  │     │  │  │  ├─ parsing.pxd
│  │     │  │  │  ├─ parsing.pyi
│  │     │  │  │  ├─ parsing.pyx
│  │     │  │  │  ├─ period.cp39-win_amd64.pyd
│  │     │  │  │  ├─ period.pxd
│  │     │  │  │  ├─ period.pyi
│  │     │  │  │  ├─ period.pyx
│  │     │  │  │  ├─ strptime.cp39-win_amd64.pyd
│  │     │  │  │  ├─ strptime.pyi
│  │     │  │  │  ├─ strptime.pyx
│  │     │  │  │  ├─ timedeltas.cp39-win_amd64.pyd
│  │     │  │  │  ├─ timedeltas.pxd
│  │     │  │  │  ├─ timedeltas.pyi
│  │     │  │  │  ├─ timedeltas.pyx
│  │     │  │  │  ├─ timestamps.cp39-win_amd64.pyd
│  │     │  │  │  ├─ timestamps.pxd
│  │     │  │  │  ├─ timestamps.pyi
│  │     │  │  │  ├─ timestamps.pyx
│  │     │  │  │  ├─ timezones.cp39-win_amd64.pyd
│  │     │  │  │  ├─ timezones.pxd
│  │     │  │  │  ├─ timezones.pyi
│  │     │  │  │  ├─ timezones.pyx
│  │     │  │  │  ├─ tzconversion.cp39-win_amd64.pyd
│  │     │  │  │  ├─ tzconversion.pxd
│  │     │  │  │  ├─ tzconversion.pyi
│  │     │  │  │  ├─ tzconversion.pyx
│  │     │  │  │  ├─ util.pxd
│  │     │  │  │  ├─ vectorized.cp39-win_amd64.pyd
│  │     │  │  │  ├─ vectorized.pyi
│  │     │  │  │  ├─ vectorized.pyx
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ util.pxd
│  │     │  │  ├─ window
│  │     │  │  │  ├─ aggregations.cp39-win_amd64.pyd
│  │     │  │  │  ├─ aggregations.pyi
│  │     │  │  │  ├─ aggregations.pyx
│  │     │  │  │  ├─ concrt140.dll
│  │     │  │  │  ├─ indexers.cp39-win_amd64.pyd
│  │     │  │  │  ├─ indexers.pyi
│  │     │  │  │  ├─ indexers.pyx
│  │     │  │  │  ├─ msvcp140.dll
│  │     │  │  │  ├─ vcruntime140_1.dll
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ writers.cp39-win_amd64.pyd
│  │     │  │  ├─ writers.pyi
│  │     │  │  ├─ writers.pyx
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _testing
│  │     │  │  ├─ asserters.py
│  │     │  │  ├─ compat.py
│  │     │  │  ├─ contexts.py
│  │     │  │  ├─ _hypothesis.py
│  │     │  │  ├─ _io.py
│  │     │  │  ├─ _random.py
│  │     │  │  ├─ _warnings.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ asserters.cpython-39.pyc
│  │     │  │     ├─ compat.cpython-39.pyc
│  │     │  │     ├─ contexts.cpython-39.pyc
│  │     │  │     ├─ _hypothesis.cpython-39.pyc
│  │     │  │     ├─ _io.cpython-39.pyc
│  │     │  │     ├─ _random.cpython-39.pyc
│  │     │  │     ├─ _warnings.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _typing.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ conftest.cpython-39.pyc
│  │     │     ├─ testing.cpython-39.pyc
│  │     │     ├─ _typing.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ pandas-1.5.3.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ parso
│  │     │  ├─ cache.py
│  │     │  ├─ file_io.py
│  │     │  ├─ grammar.py
│  │     │  ├─ normalizer.py
│  │     │  ├─ parser.py
│  │     │  ├─ pgen2
│  │     │  │  ├─ generator.py
│  │     │  │  ├─ grammar_parser.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ generator.cpython-39.pyc
│  │     │  │     ├─ grammar_parser.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ python
│  │     │  │  ├─ diff.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ grammar310.txt
│  │     │  │  ├─ grammar311.txt
│  │     │  │  ├─ grammar312.txt
│  │     │  │  ├─ grammar36.txt
│  │     │  │  ├─ grammar37.txt
│  │     │  │  ├─ grammar38.txt
│  │     │  │  ├─ grammar39.txt
│  │     │  │  ├─ parser.py
│  │     │  │  ├─ pep8.py
│  │     │  │  ├─ prefix.py
│  │     │  │  ├─ token.py
│  │     │  │  ├─ tokenize.py
│  │     │  │  ├─ tree.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ diff.cpython-39.pyc
│  │     │  │     ├─ errors.cpython-39.pyc
│  │     │  │     ├─ parser.cpython-39.pyc
│  │     │  │     ├─ pep8.cpython-39.pyc
│  │     │  │     ├─ prefix.cpython-39.pyc
│  │     │  │     ├─ token.cpython-39.pyc
│  │     │  │     ├─ tokenize.cpython-39.pyc
│  │     │  │     ├─ tree.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ tree.py
│  │     │  ├─ utils.py
│  │     │  ├─ _compatibility.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ cache.cpython-39.pyc
│  │     │     ├─ file_io.cpython-39.pyc
│  │     │     ├─ grammar.cpython-39.pyc
│  │     │     ├─ normalizer.cpython-39.pyc
│  │     │     ├─ parser.cpython-39.pyc
│  │     │     ├─ tree.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ _compatibility.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ parso-0.8.3.dist-info
│  │     │  ├─ AUTHORS.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pathable
│  │     │  ├─ accessors.py
│  │     │  ├─ dataclasses.py
│  │     │  ├─ parsers.py
│  │     │  ├─ paths.py
│  │     │  ├─ py.typed
│  │     │  ├─ types.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ accessors.cpython-39.pyc
│  │     │     ├─ dataclasses.cpython-39.pyc
│  │     │     ├─ parsers.cpython-39.pyc
│  │     │     ├─ paths.cpython-39.pyc
│  │     │     ├─ types.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ pathable-0.4.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pathlib-1.0.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pathlib.py
│  │     ├─ pathspec
│  │     │  ├─ gitignore.py
│  │     │  ├─ pathspec.py
│  │     │  ├─ pattern.py
│  │     │  ├─ patterns
│  │     │  │  ├─ gitwildmatch.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ gitwildmatch.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ util.py
│  │     │  ├─ _meta.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ gitignore.cpython-39.pyc
│  │     │     ├─ pathspec.cpython-39.pyc
│  │     │     ├─ pattern.cpython-39.pyc
│  │     │     ├─ util.cpython-39.pyc
│  │     │     ├─ _meta.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ pathspec-0.11.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pickleshare-0.7.5.dist-info
│  │     │  ├─ DESCRIPTION.rst
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ metadata.json
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pickleshare.py
│  │     ├─ PIL
│  │     │  ├─ BdfFontFile.py
│  │     │  ├─ BlpImagePlugin.py
│  │     │  ├─ BmpImagePlugin.py
│  │     │  ├─ BufrStubImagePlugin.py
│  │     │  ├─ ContainerIO.py
│  │     │  ├─ CurImagePlugin.py
│  │     │  ├─ DcxImagePlugin.py
│  │     │  ├─ DdsImagePlugin.py
│  │     │  ├─ EpsImagePlugin.py
│  │     │  ├─ ExifTags.py
│  │     │  ├─ features.py
│  │     │  ├─ FitsImagePlugin.py
│  │     │  ├─ FitsStubImagePlugin.py
│  │     │  ├─ FliImagePlugin.py
│  │     │  ├─ FontFile.py
│  │     │  ├─ FpxImagePlugin.py
│  │     │  ├─ FtexImagePlugin.py
│  │     │  ├─ GbrImagePlugin.py
│  │     │  ├─ GdImageFile.py
│  │     │  ├─ GifImagePlugin.py
│  │     │  ├─ GimpGradientFile.py
│  │     │  ├─ GimpPaletteFile.py
│  │     │  ├─ GribStubImagePlugin.py
│  │     │  ├─ Hdf5StubImagePlugin.py
│  │     │  ├─ IcnsImagePlugin.py
│  │     │  ├─ IcoImagePlugin.py
│  │     │  ├─ Image.py
│  │     │  ├─ ImageChops.py
│  │     │  ├─ ImageCms.py
│  │     │  ├─ ImageColor.py
│  │     │  ├─ ImageDraw.py
│  │     │  ├─ ImageDraw2.py
│  │     │  ├─ ImageEnhance.py
│  │     │  ├─ ImageFile.py
│  │     │  ├─ ImageFilter.py
│  │     │  ├─ ImageFont.py
│  │     │  ├─ ImageGrab.py
│  │     │  ├─ ImageMath.py
│  │     │  ├─ ImageMode.py
│  │     │  ├─ ImageMorph.py
│  │     │  ├─ ImageOps.py
│  │     │  ├─ ImagePalette.py
│  │     │  ├─ ImagePath.py
│  │     │  ├─ ImageQt.py
│  │     │  ├─ ImageSequence.py
│  │     │  ├─ ImageShow.py
│  │     │  ├─ ImageStat.py
│  │     │  ├─ ImageTk.py
│  │     │  ├─ ImageTransform.py
│  │     │  ├─ ImageWin.py
│  │     │  ├─ ImImagePlugin.py
│  │     │  ├─ ImtImagePlugin.py
│  │     │  ├─ IptcImagePlugin.py
│  │     │  ├─ Jpeg2KImagePlugin.py
│  │     │  ├─ JpegImagePlugin.py
│  │     │  ├─ JpegPresets.py
│  │     │  ├─ McIdasImagePlugin.py
│  │     │  ├─ MicImagePlugin.py
│  │     │  ├─ MpegImagePlugin.py
│  │     │  ├─ MpoImagePlugin.py
│  │     │  ├─ MspImagePlugin.py
│  │     │  ├─ PaletteFile.py
│  │     │  ├─ PalmImagePlugin.py
│  │     │  ├─ PcdImagePlugin.py
│  │     │  ├─ PcfFontFile.py
│  │     │  ├─ PcxImagePlugin.py
│  │     │  ├─ PdfImagePlugin.py
│  │     │  ├─ PdfParser.py
│  │     │  ├─ PixarImagePlugin.py
│  │     │  ├─ PngImagePlugin.py
│  │     │  ├─ PpmImagePlugin.py
│  │     │  ├─ PsdImagePlugin.py
│  │     │  ├─ PSDraw.py
│  │     │  ├─ PyAccess.py
│  │     │  ├─ QoiImagePlugin.py
│  │     │  ├─ SgiImagePlugin.py
│  │     │  ├─ SpiderImagePlugin.py
│  │     │  ├─ SunImagePlugin.py
│  │     │  ├─ TarIO.py
│  │     │  ├─ TgaImagePlugin.py
│  │     │  ├─ TiffImagePlugin.py
│  │     │  ├─ TiffTags.py
│  │     │  ├─ WalImageFile.py
│  │     │  ├─ WebPImagePlugin.py
│  │     │  ├─ WmfImagePlugin.py
│  │     │  ├─ XbmImagePlugin.py
│  │     │  ├─ XpmImagePlugin.py
│  │     │  ├─ XVThumbImagePlugin.py
│  │     │  ├─ _binary.py
│  │     │  ├─ _deprecate.py
│  │     │  ├─ _imaging.cp39-win_amd64.pyd
│  │     │  ├─ _imagingcms.cp39-win_amd64.pyd
│  │     │  ├─ _imagingft.cp39-win_amd64.pyd
│  │     │  ├─ _imagingmath.cp39-win_amd64.pyd
│  │     │  ├─ _imagingmorph.cp39-win_amd64.pyd
│  │     │  ├─ _imagingtk.cp39-win_amd64.pyd
│  │     │  ├─ _tkinter_finder.py
│  │     │  ├─ _util.py
│  │     │  ├─ _version.py
│  │     │  ├─ _webp.cp39-win_amd64.pyd
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ BdfFontFile.cpython-39.pyc
│  │     │     ├─ BlpImagePlugin.cpython-39.pyc
│  │     │     ├─ BmpImagePlugin.cpython-39.pyc
│  │     │     ├─ BufrStubImagePlugin.cpython-39.pyc
│  │     │     ├─ ContainerIO.cpython-39.pyc
│  │     │     ├─ CurImagePlugin.cpython-39.pyc
│  │     │     ├─ DcxImagePlugin.cpython-39.pyc
│  │     │     ├─ DdsImagePlugin.cpython-39.pyc
│  │     │     ├─ EpsImagePlugin.cpython-39.pyc
│  │     │     ├─ ExifTags.cpython-39.pyc
│  │     │     ├─ features.cpython-39.pyc
│  │     │     ├─ FitsImagePlugin.cpython-39.pyc
│  │     │     ├─ FitsStubImagePlugin.cpython-39.pyc
│  │     │     ├─ FliImagePlugin.cpython-39.pyc
│  │     │     ├─ FontFile.cpython-39.pyc
│  │     │     ├─ FpxImagePlugin.cpython-39.pyc
│  │     │     ├─ FtexImagePlugin.cpython-39.pyc
│  │     │     ├─ GbrImagePlugin.cpython-39.pyc
│  │     │     ├─ GdImageFile.cpython-39.pyc
│  │     │     ├─ GifImagePlugin.cpython-39.pyc
│  │     │     ├─ GimpGradientFile.cpython-39.pyc
│  │     │     ├─ GimpPaletteFile.cpython-39.pyc
│  │     │     ├─ GribStubImagePlugin.cpython-39.pyc
│  │     │     ├─ Hdf5StubImagePlugin.cpython-39.pyc
│  │     │     ├─ IcnsImagePlugin.cpython-39.pyc
│  │     │     ├─ IcoImagePlugin.cpython-39.pyc
│  │     │     ├─ Image.cpython-39.pyc
│  │     │     ├─ ImageChops.cpython-39.pyc
│  │     │     ├─ ImageCms.cpython-39.pyc
│  │     │     ├─ ImageColor.cpython-39.pyc
│  │     │     ├─ ImageDraw.cpython-39.pyc
│  │     │     ├─ ImageDraw2.cpython-39.pyc
│  │     │     ├─ ImageEnhance.cpython-39.pyc
│  │     │     ├─ ImageFile.cpython-39.pyc
│  │     │     ├─ ImageFilter.cpython-39.pyc
│  │     │     ├─ ImageFont.cpython-39.pyc
│  │     │     ├─ ImageGrab.cpython-39.pyc
│  │     │     ├─ ImageMath.cpython-39.pyc
│  │     │     ├─ ImageMode.cpython-39.pyc
│  │     │     ├─ ImageMorph.cpython-39.pyc
│  │     │     ├─ ImageOps.cpython-39.pyc
│  │     │     ├─ ImagePalette.cpython-39.pyc
│  │     │     ├─ ImagePath.cpython-39.pyc
│  │     │     ├─ ImageQt.cpython-39.pyc
│  │     │     ├─ ImageSequence.cpython-39.pyc
│  │     │     ├─ ImageShow.cpython-39.pyc
│  │     │     ├─ ImageStat.cpython-39.pyc
│  │     │     ├─ ImageTk.cpython-39.pyc
│  │     │     ├─ ImageTransform.cpython-39.pyc
│  │     │     ├─ ImageWin.cpython-39.pyc
│  │     │     ├─ ImImagePlugin.cpython-39.pyc
│  │     │     ├─ ImtImagePlugin.cpython-39.pyc
│  │     │     ├─ IptcImagePlugin.cpython-39.pyc
│  │     │     ├─ Jpeg2KImagePlugin.cpython-39.pyc
│  │     │     ├─ JpegImagePlugin.cpython-39.pyc
│  │     │     ├─ JpegPresets.cpython-39.pyc
│  │     │     ├─ McIdasImagePlugin.cpython-39.pyc
│  │     │     ├─ MicImagePlugin.cpython-39.pyc
│  │     │     ├─ MpegImagePlugin.cpython-39.pyc
│  │     │     ├─ MpoImagePlugin.cpython-39.pyc
│  │     │     ├─ MspImagePlugin.cpython-39.pyc
│  │     │     ├─ PaletteFile.cpython-39.pyc
│  │     │     ├─ PalmImagePlugin.cpython-39.pyc
│  │     │     ├─ PcdImagePlugin.cpython-39.pyc
│  │     │     ├─ PcfFontFile.cpython-39.pyc
│  │     │     ├─ PcxImagePlugin.cpython-39.pyc
│  │     │     ├─ PdfImagePlugin.cpython-39.pyc
│  │     │     ├─ PdfParser.cpython-39.pyc
│  │     │     ├─ PixarImagePlugin.cpython-39.pyc
│  │     │     ├─ PngImagePlugin.cpython-39.pyc
│  │     │     ├─ PpmImagePlugin.cpython-39.pyc
│  │     │     ├─ PsdImagePlugin.cpython-39.pyc
│  │     │     ├─ PSDraw.cpython-39.pyc
│  │     │     ├─ PyAccess.cpython-39.pyc
│  │     │     ├─ QoiImagePlugin.cpython-39.pyc
│  │     │     ├─ SgiImagePlugin.cpython-39.pyc
│  │     │     ├─ SpiderImagePlugin.cpython-39.pyc
│  │     │     ├─ SunImagePlugin.cpython-39.pyc
│  │     │     ├─ TarIO.cpython-39.pyc
│  │     │     ├─ TgaImagePlugin.cpython-39.pyc
│  │     │     ├─ TiffImagePlugin.cpython-39.pyc
│  │     │     ├─ TiffTags.cpython-39.pyc
│  │     │     ├─ WalImageFile.cpython-39.pyc
│  │     │     ├─ WebPImagePlugin.cpython-39.pyc
│  │     │     ├─ WmfImagePlugin.cpython-39.pyc
│  │     │     ├─ XbmImagePlugin.cpython-39.pyc
│  │     │     ├─ XpmImagePlugin.cpython-39.pyc
│  │     │     ├─ XVThumbImagePlugin.cpython-39.pyc
│  │     │     ├─ _binary.cpython-39.pyc
│  │     │     ├─ _deprecate.cpython-39.pyc
│  │     │     ├─ _tkinter_finder.cpython-39.pyc
│  │     │     ├─ _util.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ Pillow-9.5.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ pip
│  │     │  ├─ py.typed
│  │     │  ├─ _internal
│  │     │  │  ├─ build_env.py
│  │     │  │  ├─ cache.py
│  │     │  │  ├─ cli
│  │     │  │  │  ├─ autocompletion.py
│  │     │  │  │  ├─ base_command.py
│  │     │  │  │  ├─ cmdoptions.py
│  │     │  │  │  ├─ command_context.py
│  │     │  │  │  ├─ main.py
│  │     │  │  │  ├─ main_parser.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ progress_bars.py
│  │     │  │  │  ├─ req_command.py
│  │     │  │  │  ├─ spinners.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ autocompletion.cpython-39.pyc
│  │     │  │  │     ├─ base_command.cpython-39.pyc
│  │     │  │  │     ├─ cmdoptions.cpython-39.pyc
│  │     │  │  │     ├─ command_context.cpython-39.pyc
│  │     │  │  │     ├─ main.cpython-39.pyc
│  │     │  │  │     ├─ main_parser.cpython-39.pyc
│  │     │  │  │     ├─ parser.cpython-39.pyc
│  │     │  │  │     ├─ progress_bars.cpython-39.pyc
│  │     │  │  │     ├─ req_command.cpython-39.pyc
│  │     │  │  │     ├─ spinners.cpython-39.pyc
│  │     │  │  │     ├─ status_codes.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ commands
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ completion.py
│  │     │  │  │  ├─ configuration.py
│  │     │  │  │  ├─ debug.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ hash.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ install.py
│  │     │  │  │  ├─ list.py
│  │     │  │  │  ├─ search.py
│  │     │  │  │  ├─ show.py
│  │     │  │  │  ├─ uninstall.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cache.cpython-39.pyc
│  │     │  │  │     ├─ check.cpython-39.pyc
│  │     │  │  │     ├─ completion.cpython-39.pyc
│  │     │  │  │     ├─ configuration.cpython-39.pyc
│  │     │  │  │     ├─ debug.cpython-39.pyc
│  │     │  │  │     ├─ download.cpython-39.pyc
│  │     │  │  │     ├─ freeze.cpython-39.pyc
│  │     │  │  │     ├─ hash.cpython-39.pyc
│  │     │  │  │     ├─ help.cpython-39.pyc
│  │     │  │  │     ├─ install.cpython-39.pyc
│  │     │  │  │     ├─ list.cpython-39.pyc
│  │     │  │  │     ├─ search.cpython-39.pyc
│  │     │  │  │     ├─ show.cpython-39.pyc
│  │     │  │  │     ├─ uninstall.cpython-39.pyc
│  │     │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ configuration.py
│  │     │  │  ├─ distributions
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ installed.py
│  │     │  │  │  ├─ sdist.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ installed.cpython-39.pyc
│  │     │  │  │     ├─ sdist.cpython-39.pyc
│  │     │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ index
│  │     │  │  │  ├─ collector.py
│  │     │  │  │  ├─ package_finder.py
│  │     │  │  │  ├─ sources.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ collector.cpython-39.pyc
│  │     │  │  │     ├─ package_finder.cpython-39.pyc
│  │     │  │  │     ├─ sources.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ locations
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ _distutils.py
│  │     │  │  │  ├─ _sysconfig.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ _distutils.cpython-39.pyc
│  │     │  │  │     ├─ _sysconfig.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ main.py
│  │     │  │  ├─ metadata
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ pkg_resources.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ pkg_resources.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ models
│  │     │  │  │  ├─ candidate.py
│  │     │  │  │  ├─ direct_url.py
│  │     │  │  │  ├─ format_control.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ link.py
│  │     │  │  │  ├─ scheme.py
│  │     │  │  │  ├─ search_scope.py
│  │     │  │  │  ├─ selection_prefs.py
│  │     │  │  │  ├─ target_python.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ candidate.cpython-39.pyc
│  │     │  │  │     ├─ direct_url.cpython-39.pyc
│  │     │  │  │     ├─ format_control.cpython-39.pyc
│  │     │  │  │     ├─ index.cpython-39.pyc
│  │     │  │  │     ├─ link.cpython-39.pyc
│  │     │  │  │     ├─ scheme.cpython-39.pyc
│  │     │  │  │     ├─ search_scope.cpython-39.pyc
│  │     │  │  │     ├─ selection_prefs.cpython-39.pyc
│  │     │  │  │     ├─ target_python.cpython-39.pyc
│  │     │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ network
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ lazy_wheel.py
│  │     │  │  │  ├─ session.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ xmlrpc.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ auth.cpython-39.pyc
│  │     │  │  │     ├─ cache.cpython-39.pyc
│  │     │  │  │     ├─ download.cpython-39.pyc
│  │     │  │  │     ├─ lazy_wheel.cpython-39.pyc
│  │     │  │  │     ├─ session.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     ├─ xmlrpc.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ operations
│  │     │  │  │  ├─ build
│  │     │  │  │  │  ├─ metadata.py
│  │     │  │  │  │  ├─ metadata_legacy.py
│  │     │  │  │  │  ├─ wheel.py
│  │     │  │  │  │  ├─ wheel_legacy.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ metadata.cpython-39.pyc
│  │     │  │  │  │     ├─ metadata_legacy.cpython-39.pyc
│  │     │  │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │  │     ├─ wheel_legacy.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ install
│  │     │  │  │  │  ├─ editable_legacy.py
│  │     │  │  │  │  ├─ legacy.py
│  │     │  │  │  │  ├─ wheel.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ editable_legacy.cpython-39.pyc
│  │     │  │  │  │     ├─ legacy.cpython-39.pyc
│  │     │  │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ prepare.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ check.cpython-39.pyc
│  │     │  │  │     ├─ freeze.cpython-39.pyc
│  │     │  │  │     ├─ prepare.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pyproject.py
│  │     │  │  ├─ req
│  │     │  │  │  ├─ constructors.py
│  │     │  │  │  ├─ req_file.py
│  │     │  │  │  ├─ req_install.py
│  │     │  │  │  ├─ req_set.py
│  │     │  │  │  ├─ req_tracker.py
│  │     │  │  │  ├─ req_uninstall.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ constructors.cpython-39.pyc
│  │     │  │  │     ├─ req_file.cpython-39.pyc
│  │     │  │  │     ├─ req_install.cpython-39.pyc
│  │     │  │  │     ├─ req_set.cpython-39.pyc
│  │     │  │  │     ├─ req_tracker.cpython-39.pyc
│  │     │  │  │     ├─ req_uninstall.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ resolution
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ legacy
│  │     │  │  │  │  ├─ resolver.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ resolver.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ resolvelib
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ candidates.py
│  │     │  │  │  │  ├─ factory.py
│  │     │  │  │  │  ├─ found_candidates.py
│  │     │  │  │  │  ├─ provider.py
│  │     │  │  │  │  ├─ reporter.py
│  │     │  │  │  │  ├─ requirements.py
│  │     │  │  │  │  ├─ resolver.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │  │     ├─ candidates.cpython-39.pyc
│  │     │  │  │  │     ├─ factory.cpython-39.pyc
│  │     │  │  │  │     ├─ found_candidates.cpython-39.pyc
│  │     │  │  │  │     ├─ provider.cpython-39.pyc
│  │     │  │  │  │     ├─ reporter.cpython-39.pyc
│  │     │  │  │  │     ├─ requirements.cpython-39.pyc
│  │     │  │  │  │     ├─ resolver.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ self_outdated_check.py
│  │     │  │  ├─ utils
│  │     │  │  │  ├─ appdirs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ compatibility_tags.py
│  │     │  │  │  ├─ datetime.py
│  │     │  │  │  ├─ deprecation.py
│  │     │  │  │  ├─ direct_url_helpers.py
│  │     │  │  │  ├─ distutils_args.py
│  │     │  │  │  ├─ encoding.py
│  │     │  │  │  ├─ entrypoints.py
│  │     │  │  │  ├─ filesystem.py
│  │     │  │  │  ├─ filetypes.py
│  │     │  │  │  ├─ glibc.py
│  │     │  │  │  ├─ hashes.py
│  │     │  │  │  ├─ inject_securetransport.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ misc.py
│  │     │  │  │  ├─ models.py
│  │     │  │  │  ├─ packaging.py
│  │     │  │  │  ├─ parallel.py
│  │     │  │  │  ├─ pkg_resources.py
│  │     │  │  │  ├─ setuptools_build.py
│  │     │  │  │  ├─ subprocess.py
│  │     │  │  │  ├─ temp_dir.py
│  │     │  │  │  ├─ unpacking.py
│  │     │  │  │  ├─ urls.py
│  │     │  │  │  ├─ virtualenv.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ appdirs.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ compatibility_tags.cpython-39.pyc
│  │     │  │  │     ├─ datetime.cpython-39.pyc
│  │     │  │  │     ├─ deprecation.cpython-39.pyc
│  │     │  │  │     ├─ direct_url_helpers.cpython-39.pyc
│  │     │  │  │     ├─ distutils_args.cpython-39.pyc
│  │     │  │  │     ├─ encoding.cpython-39.pyc
│  │     │  │  │     ├─ entrypoints.cpython-39.pyc
│  │     │  │  │     ├─ filesystem.cpython-39.pyc
│  │     │  │  │     ├─ filetypes.cpython-39.pyc
│  │     │  │  │     ├─ glibc.cpython-39.pyc
│  │     │  │  │     ├─ hashes.cpython-39.pyc
│  │     │  │  │     ├─ inject_securetransport.cpython-39.pyc
│  │     │  │  │     ├─ logging.cpython-39.pyc
│  │     │  │  │     ├─ misc.cpython-39.pyc
│  │     │  │  │     ├─ models.cpython-39.pyc
│  │     │  │  │     ├─ packaging.cpython-39.pyc
│  │     │  │  │     ├─ parallel.cpython-39.pyc
│  │     │  │  │     ├─ pkg_resources.cpython-39.pyc
│  │     │  │  │     ├─ setuptools_build.cpython-39.pyc
│  │     │  │  │     ├─ subprocess.cpython-39.pyc
│  │     │  │  │     ├─ temp_dir.cpython-39.pyc
│  │     │  │  │     ├─ unpacking.cpython-39.pyc
│  │     │  │  │     ├─ urls.cpython-39.pyc
│  │     │  │  │     ├─ virtualenv.cpython-39.pyc
│  │     │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ vcs
│  │     │  │  │  ├─ bazaar.py
│  │     │  │  │  ├─ git.py
│  │     │  │  │  ├─ mercurial.py
│  │     │  │  │  ├─ subversion.py
│  │     │  │  │  ├─ versioncontrol.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bazaar.cpython-39.pyc
│  │     │  │  │     ├─ git.cpython-39.pyc
│  │     │  │  │     ├─ mercurial.cpython-39.pyc
│  │     │  │  │     ├─ subversion.cpython-39.pyc
│  │     │  │  │     ├─ versioncontrol.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ wheel_builder.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ build_env.cpython-39.pyc
│  │     │  │     ├─ cache.cpython-39.pyc
│  │     │  │     ├─ configuration.cpython-39.pyc
│  │     │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │     ├─ main.cpython-39.pyc
│  │     │  │     ├─ pyproject.cpython-39.pyc
│  │     │  │     ├─ self_outdated_check.cpython-39.pyc
│  │     │  │     ├─ wheel_builder.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _vendor
│  │     │  │  ├─ appdirs.py
│  │     │  │  ├─ cachecontrol
│  │     │  │  │  ├─ adapter.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ caches
│  │     │  │  │  │  ├─ file_cache.py
│  │     │  │  │  │  ├─ redis_cache.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ file_cache.cpython-39.pyc
│  │     │  │  │  │     ├─ redis_cache.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ controller.py
│  │     │  │  │  ├─ filewrapper.py
│  │     │  │  │  ├─ heuristics.py
│  │     │  │  │  ├─ serialize.py
│  │     │  │  │  ├─ wrapper.py
│  │     │  │  │  ├─ _cmd.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ adapter.cpython-39.pyc
│  │     │  │  │     ├─ cache.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ controller.cpython-39.pyc
│  │     │  │  │     ├─ filewrapper.cpython-39.pyc
│  │     │  │  │     ├─ heuristics.cpython-39.pyc
│  │     │  │  │     ├─ serialize.cpython-39.pyc
│  │     │  │  │     ├─ wrapper.cpython-39.pyc
│  │     │  │  │     ├─ _cmd.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ certifi
│  │     │  │  │  ├─ cacert.pem
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ core.cpython-39.pyc
│  │     │  │  │     ├─ __init__.cpython-39.pyc
│  │     │  │  │     └─ __main__.cpython-39.pyc
│  │     │  │  ├─ chardet
│  │     │  │  │  ├─ big5freq.py
│  │     │  │  │  ├─ big5prober.py
│  │     │  │  │  ├─ chardistribution.py
│  │     │  │  │  ├─ charsetgroupprober.py
│  │     │  │  │  ├─ charsetprober.py
│  │     │  │  │  ├─ cli
│  │     │  │  │  │  ├─ chardetect.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ chardetect.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ codingstatemachine.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ cp949prober.py
│  │     │  │  │  ├─ enums.py
│  │     │  │  │  ├─ escprober.py
│  │     │  │  │  ├─ escsm.py
│  │     │  │  │  ├─ eucjpprober.py
│  │     │  │  │  ├─ euckrfreq.py
│  │     │  │  │  ├─ euckrprober.py
│  │     │  │  │  ├─ euctwfreq.py
│  │     │  │  │  ├─ euctwprober.py
│  │     │  │  │  ├─ gb2312freq.py
│  │     │  │  │  ├─ gb2312prober.py
│  │     │  │  │  ├─ hebrewprober.py
│  │     │  │  │  ├─ jisfreq.py
│  │     │  │  │  ├─ jpcntx.py
│  │     │  │  │  ├─ langbulgarianmodel.py
│  │     │  │  │  ├─ langgreekmodel.py
│  │     │  │  │  ├─ langhebrewmodel.py
│  │     │  │  │  ├─ langhungarianmodel.py
│  │     │  │  │  ├─ langrussianmodel.py
│  │     │  │  │  ├─ langthaimodel.py
│  │     │  │  │  ├─ langturkishmodel.py
│  │     │  │  │  ├─ latin1prober.py
│  │     │  │  │  ├─ mbcharsetprober.py
│  │     │  │  │  ├─ mbcsgroupprober.py
│  │     │  │  │  ├─ mbcssm.py
│  │     │  │  │  ├─ metadata
│  │     │  │  │  │  ├─ languages.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ languages.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ sbcharsetprober.py
│  │     │  │  │  ├─ sbcsgroupprober.py
│  │     │  │  │  ├─ sjisprober.py
│  │     │  │  │  ├─ universaldetector.py
│  │     │  │  │  ├─ utf8prober.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ big5freq.cpython-39.pyc
│  │     │  │  │     ├─ big5prober.cpython-39.pyc
│  │     │  │  │     ├─ chardistribution.cpython-39.pyc
│  │     │  │  │     ├─ charsetgroupprober.cpython-39.pyc
│  │     │  │  │     ├─ charsetprober.cpython-39.pyc
│  │     │  │  │     ├─ codingstatemachine.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ cp949prober.cpython-39.pyc
│  │     │  │  │     ├─ enums.cpython-39.pyc
│  │     │  │  │     ├─ escprober.cpython-39.pyc
│  │     │  │  │     ├─ escsm.cpython-39.pyc
│  │     │  │  │     ├─ eucjpprober.cpython-39.pyc
│  │     │  │  │     ├─ euckrfreq.cpython-39.pyc
│  │     │  │  │     ├─ euckrprober.cpython-39.pyc
│  │     │  │  │     ├─ euctwfreq.cpython-39.pyc
│  │     │  │  │     ├─ euctwprober.cpython-39.pyc
│  │     │  │  │     ├─ gb2312freq.cpython-39.pyc
│  │     │  │  │     ├─ gb2312prober.cpython-39.pyc
│  │     │  │  │     ├─ hebrewprober.cpython-39.pyc
│  │     │  │  │     ├─ jisfreq.cpython-39.pyc
│  │     │  │  │     ├─ jpcntx.cpython-39.pyc
│  │     │  │  │     ├─ langbulgarianmodel.cpython-39.pyc
│  │     │  │  │     ├─ langgreekmodel.cpython-39.pyc
│  │     │  │  │     ├─ langhebrewmodel.cpython-39.pyc
│  │     │  │  │     ├─ langhungarianmodel.cpython-39.pyc
│  │     │  │  │     ├─ langrussianmodel.cpython-39.pyc
│  │     │  │  │     ├─ langthaimodel.cpython-39.pyc
│  │     │  │  │     ├─ langturkishmodel.cpython-39.pyc
│  │     │  │  │     ├─ latin1prober.cpython-39.pyc
│  │     │  │  │     ├─ mbcharsetprober.cpython-39.pyc
│  │     │  │  │     ├─ mbcsgroupprober.cpython-39.pyc
│  │     │  │  │     ├─ mbcssm.cpython-39.pyc
│  │     │  │  │     ├─ sbcharsetprober.cpython-39.pyc
│  │     │  │  │     ├─ sbcsgroupprober.cpython-39.pyc
│  │     │  │  │     ├─ sjisprober.cpython-39.pyc
│  │     │  │  │     ├─ universaldetector.cpython-39.pyc
│  │     │  │  │     ├─ utf8prober.cpython-39.pyc
│  │     │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ colorama
│  │     │  │  │  ├─ ansi.py
│  │     │  │  │  ├─ ansitowin32.py
│  │     │  │  │  ├─ initialise.py
│  │     │  │  │  ├─ win32.py
│  │     │  │  │  ├─ winterm.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ ansi.cpython-39.pyc
│  │     │  │  │     ├─ ansitowin32.cpython-39.pyc
│  │     │  │  │     ├─ initialise.cpython-39.pyc
│  │     │  │  │     ├─ win32.cpython-39.pyc
│  │     │  │  │     ├─ winterm.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ distlib
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ database.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ locators.py
│  │     │  │  │  ├─ manifest.py
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ metadata.py
│  │     │  │  │  ├─ resources.py
│  │     │  │  │  ├─ scripts.py
│  │     │  │  │  ├─ t32.exe
│  │     │  │  │  ├─ t64.exe
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ w32.exe
│  │     │  │  │  ├─ w64.exe
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ _backport
│  │     │  │  │  │  ├─ misc.py
│  │     │  │  │  │  ├─ shutil.py
│  │     │  │  │  │  ├─ sysconfig.cfg
│  │     │  │  │  │  ├─ sysconfig.py
│  │     │  │  │  │  ├─ tarfile.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ misc.cpython-39.pyc
│  │     │  │  │  │     ├─ shutil.cpython-39.pyc
│  │     │  │  │  │     ├─ sysconfig.cpython-39.pyc
│  │     │  │  │  │     ├─ tarfile.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ database.cpython-39.pyc
│  │     │  │  │     ├─ index.cpython-39.pyc
│  │     │  │  │     ├─ locators.cpython-39.pyc
│  │     │  │  │     ├─ manifest.cpython-39.pyc
│  │     │  │  │     ├─ markers.cpython-39.pyc
│  │     │  │  │     ├─ metadata.cpython-39.pyc
│  │     │  │  │     ├─ resources.cpython-39.pyc
│  │     │  │  │     ├─ scripts.cpython-39.pyc
│  │     │  │  │     ├─ util.cpython-39.pyc
│  │     │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ distro.py
│  │     │  │  ├─ html5lib
│  │     │  │  │  ├─ constants.py
│  │     │  │  │  ├─ filters
│  │     │  │  │  │  ├─ alphabeticalattributes.py
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ inject_meta_charset.py
│  │     │  │  │  │  ├─ lint.py
│  │     │  │  │  │  ├─ optionaltags.py
│  │     │  │  │  │  ├─ sanitizer.py
│  │     │  │  │  │  ├─ whitespace.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ alphabeticalattributes.cpython-39.pyc
│  │     │  │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │  │     ├─ inject_meta_charset.cpython-39.pyc
│  │     │  │  │  │     ├─ lint.cpython-39.pyc
│  │     │  │  │  │     ├─ optionaltags.cpython-39.pyc
│  │     │  │  │  │     ├─ sanitizer.cpython-39.pyc
│  │     │  │  │  │     ├─ whitespace.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ html5parser.py
│  │     │  │  │  ├─ serializer.py
│  │     │  │  │  ├─ treeadapters
│  │     │  │  │  │  ├─ genshi.py
│  │     │  │  │  │  ├─ sax.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ genshi.cpython-39.pyc
│  │     │  │  │  │     ├─ sax.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ treebuilders
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ dom.py
│  │     │  │  │  │  ├─ etree.py
│  │     │  │  │  │  ├─ etree_lxml.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │  │     ├─ dom.cpython-39.pyc
│  │     │  │  │  │     ├─ etree.cpython-39.pyc
│  │     │  │  │  │     ├─ etree_lxml.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ treewalkers
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ dom.py
│  │     │  │  │  │  ├─ etree.py
│  │     │  │  │  │  ├─ etree_lxml.py
│  │     │  │  │  │  ├─ genshi.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │  │     ├─ dom.cpython-39.pyc
│  │     │  │  │  │     ├─ etree.cpython-39.pyc
│  │     │  │  │  │     ├─ etree_lxml.cpython-39.pyc
│  │     │  │  │  │     ├─ genshi.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _ihatexml.py
│  │     │  │  │  ├─ _inputstream.py
│  │     │  │  │  ├─ _tokenizer.py
│  │     │  │  │  ├─ _trie
│  │     │  │  │  │  ├─ py.py
│  │     │  │  │  │  ├─ _base.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ py.cpython-39.pyc
│  │     │  │  │  │     ├─ _base.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ constants.cpython-39.pyc
│  │     │  │  │     ├─ html5parser.cpython-39.pyc
│  │     │  │  │     ├─ serializer.cpython-39.pyc
│  │     │  │  │     ├─ _ihatexml.cpython-39.pyc
│  │     │  │  │     ├─ _inputstream.cpython-39.pyc
│  │     │  │  │     ├─ _tokenizer.cpython-39.pyc
│  │     │  │  │     ├─ _utils.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ idna
│  │     │  │  │  ├─ codec.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ idnadata.py
│  │     │  │  │  ├─ intranges.py
│  │     │  │  │  ├─ package_data.py
│  │     │  │  │  ├─ uts46data.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ codec.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ core.cpython-39.pyc
│  │     │  │  │     ├─ idnadata.cpython-39.pyc
│  │     │  │  │     ├─ intranges.cpython-39.pyc
│  │     │  │  │     ├─ package_data.cpython-39.pyc
│  │     │  │  │     ├─ uts46data.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ msgpack
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ ext.py
│  │     │  │  │  ├─ fallback.py
│  │     │  │  │  ├─ _version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │  │     ├─ ext.cpython-39.pyc
│  │     │  │  │     ├─ fallback.cpython-39.pyc
│  │     │  │  │     ├─ _version.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ _typing.py
│  │     │  │  │  ├─ __about__.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-39.pyc
│  │     │  │  │     ├─ requirements.cpython-39.pyc
│  │     │  │  │     ├─ specifiers.cpython-39.pyc
│  │     │  │  │     ├─ tags.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │     ├─ _compat.cpython-39.pyc
│  │     │  │  │     ├─ _structures.cpython-39.pyc
│  │     │  │  │     ├─ _typing.cpython-39.pyc
│  │     │  │  │     ├─ __about__.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pep517
│  │     │  │  │  ├─ build.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ colorlog.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ dirtools.py
│  │     │  │  │  ├─ envbuild.py
│  │     │  │  │  ├─ in_process
│  │     │  │  │  │  ├─ _in_process.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ _in_process.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ meta.py
│  │     │  │  │  ├─ wrappers.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ build.cpython-39.pyc
│  │     │  │  │     ├─ check.cpython-39.pyc
│  │     │  │  │     ├─ colorlog.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ dirtools.cpython-39.pyc
│  │     │  │  │     ├─ envbuild.cpython-39.pyc
│  │     │  │  │     ├─ meta.cpython-39.pyc
│  │     │  │  │     ├─ wrappers.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pkg_resources
│  │     │  │  │  ├─ py31compat.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ py31compat.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ progress
│  │     │  │  │  ├─ bar.py
│  │     │  │  │  ├─ counter.py
│  │     │  │  │  ├─ spinner.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bar.cpython-39.pyc
│  │     │  │  │     ├─ counter.cpython-39.pyc
│  │     │  │  │     ├─ spinner.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pyparsing.py
│  │     │  │  ├─ requests
│  │     │  │  │  ├─ adapters.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ certs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ cookies.py
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ models.py
│  │     │  │  │  ├─ packages.py
│  │     │  │  │  ├─ sessions.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  ├─ structures.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ _internal_utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __pycache__
│  │     │  │  │  │  ├─ adapters.cpython-39.pyc
│  │     │  │  │  │  ├─ api.cpython-39.pyc
│  │     │  │  │  │  ├─ auth.cpython-39.pyc
│  │     │  │  │  │  ├─ certs.cpython-39.pyc
│  │     │  │  │  │  ├─ compat.cpython-39.pyc
│  │     │  │  │  │  ├─ cookies.cpython-39.pyc
│  │     │  │  │  │  ├─ exceptions.cpython-39.pyc
│  │     │  │  │  │  ├─ help.cpython-39.pyc
│  │     │  │  │  │  ├─ models.cpython-39.pyc
│  │     │  │  │  │  ├─ packages.cpython-39.pyc
│  │     │  │  │  │  ├─ sessions.cpython-39.pyc
│  │     │  │  │  │  ├─ status_codes.cpython-39.pyc
│  │     │  │  │  │  ├─ structures.cpython-39.pyc
│  │     │  │  │  │  ├─ utils.cpython-39.pyc
│  │     │  │  │  │  ├─ _internal_utils.cpython-39.pyc
│  │     │  │  │  │  ├─ __init__.cpython-39.pyc
│  │     │  │  │  │  └─ __version__.cpython-39.pyc
│  │     │  │  │  └─ __version__.py
│  │     │  │  ├─ resolvelib
│  │     │  │  │  ├─ compat
│  │     │  │  │  │  ├─ collections_abc.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ collections_abc.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ providers.py
│  │     │  │  │  ├─ reporters.py
│  │     │  │  │  ├─ resolvers.py
│  │     │  │  │  ├─ structs.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ providers.cpython-39.pyc
│  │     │  │  │     ├─ reporters.cpython-39.pyc
│  │     │  │  │     ├─ resolvers.cpython-39.pyc
│  │     │  │  │     ├─ structs.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ six.py
│  │     │  │  ├─ tenacity
│  │     │  │  │  ├─ after.py
│  │     │  │  │  ├─ before.py
│  │     │  │  │  ├─ before_sleep.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ nap.py
│  │     │  │  │  ├─ retry.py
│  │     │  │  │  ├─ stop.py
│  │     │  │  │  ├─ tornadoweb.py
│  │     │  │  │  ├─ wait.py
│  │     │  │  │  ├─ _asyncio.py
│  │     │  │  │  ├─ _utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ after.cpython-39.pyc
│  │     │  │  │     ├─ before.cpython-39.pyc
│  │     │  │  │     ├─ before_sleep.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ nap.cpython-39.pyc
│  │     │  │  │     ├─ retry.cpython-39.pyc
│  │     │  │  │     ├─ stop.cpython-39.pyc
│  │     │  │  │     ├─ tornadoweb.cpython-39.pyc
│  │     │  │  │     ├─ wait.cpython-39.pyc
│  │     │  │  │     ├─ _asyncio.cpython-39.pyc
│  │     │  │  │     ├─ _utils.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ toml
│  │     │  │  │  ├─ decoder.py
│  │     │  │  │  ├─ encoder.py
│  │     │  │  │  ├─ ordered.py
│  │     │  │  │  ├─ tz.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ decoder.cpython-39.pyc
│  │     │  │  │     ├─ encoder.cpython-39.pyc
│  │     │  │  │     ├─ ordered.cpython-39.pyc
│  │     │  │  │     ├─ tz.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ urllib3
│  │     │  │  │  ├─ connection.py
│  │     │  │  │  ├─ connectionpool.py
│  │     │  │  │  ├─ contrib
│  │     │  │  │  │  ├─ appengine.py
│  │     │  │  │  │  ├─ ntlmpool.py
│  │     │  │  │  │  ├─ pyopenssl.py
│  │     │  │  │  │  ├─ securetransport.py
│  │     │  │  │  │  ├─ socks.py
│  │     │  │  │  │  ├─ _appengine_environ.py
│  │     │  │  │  │  ├─ _securetransport
│  │     │  │  │  │  │  ├─ bindings.py
│  │     │  │  │  │  │  ├─ low_level.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ bindings.cpython-39.pyc
│  │     │  │  │  │  │     ├─ low_level.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ appengine.cpython-39.pyc
│  │     │  │  │  │     ├─ ntlmpool.cpython-39.pyc
│  │     │  │  │  │     ├─ pyopenssl.cpython-39.pyc
│  │     │  │  │  │     ├─ securetransport.cpython-39.pyc
│  │     │  │  │  │     ├─ socks.cpython-39.pyc
│  │     │  │  │  │     ├─ _appengine_environ.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ fields.py
│  │     │  │  │  ├─ filepost.py
│  │     │  │  │  ├─ packages
│  │     │  │  │  │  ├─ backports
│  │     │  │  │  │  │  ├─ makefile.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ makefile.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ six.py
│  │     │  │  │  │  ├─ ssl_match_hostname
│  │     │  │  │  │  │  ├─ _implementation.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ _implementation.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ six.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ poolmanager.py
│  │     │  │  │  ├─ request.py
│  │     │  │  │  ├─ response.py
│  │     │  │  │  ├─ util
│  │     │  │  │  │  ├─ connection.py
│  │     │  │  │  │  ├─ proxy.py
│  │     │  │  │  │  ├─ queue.py
│  │     │  │  │  │  ├─ request.py
│  │     │  │  │  │  ├─ response.py
│  │     │  │  │  │  ├─ retry.py
│  │     │  │  │  │  ├─ ssltransport.py
│  │     │  │  │  │  ├─ ssl_.py
│  │     │  │  │  │  ├─ timeout.py
│  │     │  │  │  │  ├─ url.py
│  │     │  │  │  │  ├─ wait.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ connection.cpython-39.pyc
│  │     │  │  │  │     ├─ proxy.cpython-39.pyc
│  │     │  │  │  │     ├─ queue.cpython-39.pyc
│  │     │  │  │  │     ├─ request.cpython-39.pyc
│  │     │  │  │  │     ├─ response.cpython-39.pyc
│  │     │  │  │  │     ├─ retry.cpython-39.pyc
│  │     │  │  │  │     ├─ ssltransport.cpython-39.pyc
│  │     │  │  │  │     ├─ ssl_.cpython-39.pyc
│  │     │  │  │  │     ├─ timeout.cpython-39.pyc
│  │     │  │  │  │     ├─ url.cpython-39.pyc
│  │     │  │  │  │     ├─ wait.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _collections.py
│  │     │  │  │  ├─ _version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ connection.cpython-39.pyc
│  │     │  │  │     ├─ connectionpool.cpython-39.pyc
│  │     │  │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │  │     ├─ fields.cpython-39.pyc
│  │     │  │  │     ├─ filepost.cpython-39.pyc
│  │     │  │  │     ├─ poolmanager.cpython-39.pyc
│  │     │  │  │     ├─ request.cpython-39.pyc
│  │     │  │  │     ├─ response.cpython-39.pyc
│  │     │  │  │     ├─ _collections.cpython-39.pyc
│  │     │  │  │     ├─ _version.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ vendor.txt
│  │     │  │  ├─ webencodings
│  │     │  │  │  ├─ labels.py
│  │     │  │  │  ├─ mklabels.py
│  │     │  │  │  ├─ tests.py
│  │     │  │  │  ├─ x_user_defined.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ labels.cpython-39.pyc
│  │     │  │  │     ├─ mklabels.cpython-39.pyc
│  │     │  │  │     ├─ tests.cpython-39.pyc
│  │     │  │  │     ├─ x_user_defined.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ appdirs.cpython-39.pyc
│  │     │  │     ├─ distro.cpython-39.pyc
│  │     │  │     ├─ pyparsing.cpython-39.pyc
│  │     │  │     ├─ six.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ pip-21.1.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pkg_resources
│  │     │  ├─ extern
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ tests
│  │     │  │  └─ data
│  │     │  │     └─ my-test-package-source
│  │     │  │        ├─ setup.py
│  │     │  │        └─ __pycache__
│  │     │  │           └─ setup.cpython-39.pyc
│  │     │  ├─ _vendor
│  │     │  │  ├─ appdirs.py
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ _typing.py
│  │     │  │  │  ├─ __about__.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-39.pyc
│  │     │  │  │     ├─ requirements.cpython-39.pyc
│  │     │  │  │     ├─ specifiers.cpython-39.pyc
│  │     │  │  │     ├─ tags.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │     ├─ _compat.cpython-39.pyc
│  │     │  │  │     ├─ _structures.cpython-39.pyc
│  │     │  │  │     ├─ _typing.cpython-39.pyc
│  │     │  │  │     ├─ __about__.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pyparsing.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ appdirs.cpython-39.pyc
│  │     │  │     ├─ pyparsing.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ platformdirs
│  │     │  ├─ android.py
│  │     │  ├─ api.py
│  │     │  ├─ macos.py
│  │     │  ├─ py.typed
│  │     │  ├─ unix.py
│  │     │  ├─ version.py
│  │     │  ├─ windows.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ android.cpython-39.pyc
│  │     │     ├─ api.cpython-39.pyc
│  │     │     ├─ macos.cpython-39.pyc
│  │     │     ├─ unix.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     ├─ windows.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ platformdirs-3.2.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ prance
│  │     │  ├─ cli.py
│  │     │  ├─ convert.py
│  │     │  ├─ mixins.py
│  │     │  ├─ util
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ formats.py
│  │     │  │  ├─ fs.py
│  │     │  │  ├─ iterators.py
│  │     │  │  ├─ path.py
│  │     │  │  ├─ resolver.py
│  │     │  │  ├─ translator.py
│  │     │  │  ├─ url.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │     ├─ formats.cpython-39.pyc
│  │     │  │     ├─ fs.cpython-39.pyc
│  │     │  │     ├─ iterators.cpython-39.pyc
│  │     │  │     ├─ path.cpython-39.pyc
│  │     │  │     ├─ resolver.cpython-39.pyc
│  │     │  │     ├─ translator.cpython-39.pyc
│  │     │  │     ├─ url.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ cli.cpython-39.pyc
│  │     │     ├─ convert.cpython-39.pyc
│  │     │     ├─ mixins.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ prance-0.22.2.22.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ prompt_toolkit
│  │     │  ├─ application
│  │     │  │  ├─ application.py
│  │     │  │  ├─ current.py
│  │     │  │  ├─ dummy.py
│  │     │  │  ├─ run_in_terminal.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ application.cpython-39.pyc
│  │     │  │     ├─ current.cpython-39.pyc
│  │     │  │     ├─ dummy.cpython-39.pyc
│  │     │  │     ├─ run_in_terminal.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ auto_suggest.py
│  │     │  ├─ buffer.py
│  │     │  ├─ cache.py
│  │     │  ├─ clipboard
│  │     │  │  ├─ base.py
│  │     │  │  ├─ in_memory.py
│  │     │  │  ├─ pyperclip.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ in_memory.cpython-39.pyc
│  │     │  │     ├─ pyperclip.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ completion
│  │     │  │  ├─ base.py
│  │     │  │  ├─ deduplicate.py
│  │     │  │  ├─ filesystem.py
│  │     │  │  ├─ fuzzy_completer.py
│  │     │  │  ├─ nested.py
│  │     │  │  ├─ word_completer.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ deduplicate.cpython-39.pyc
│  │     │  │     ├─ filesystem.cpython-39.pyc
│  │     │  │     ├─ fuzzy_completer.cpython-39.pyc
│  │     │  │     ├─ nested.cpython-39.pyc
│  │     │  │     ├─ word_completer.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ contrib
│  │     │  │  ├─ completers
│  │     │  │  │  ├─ system.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ system.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ regular_languages
│  │     │  │  │  ├─ compiler.py
│  │     │  │  │  ├─ completion.py
│  │     │  │  │  ├─ lexer.py
│  │     │  │  │  ├─ regex_parser.py
│  │     │  │  │  ├─ validation.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ compiler.cpython-39.pyc
│  │     │  │  │     ├─ completion.cpython-39.pyc
│  │     │  │  │     ├─ lexer.cpython-39.pyc
│  │     │  │  │     ├─ regex_parser.cpython-39.pyc
│  │     │  │  │     ├─ validation.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ ssh
│  │     │  │  │  ├─ server.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ server.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ telnet
│  │     │  │  │  ├─ log.py
│  │     │  │  │  ├─ protocol.py
│  │     │  │  │  ├─ server.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ log.cpython-39.pyc
│  │     │  │  │     ├─ protocol.cpython-39.pyc
│  │     │  │  │     ├─ server.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ cursor_shapes.py
│  │     │  ├─ data_structures.py
│  │     │  ├─ document.py
│  │     │  ├─ enums.py
│  │     │  ├─ eventloop
│  │     │  │  ├─ async_generator.py
│  │     │  │  ├─ inputhook.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ win32.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ async_generator.cpython-39.pyc
│  │     │  │     ├─ inputhook.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     ├─ win32.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ filters
│  │     │  │  ├─ app.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ cli.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ app.cpython-39.pyc
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ cli.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ formatted_text
│  │     │  │  ├─ ansi.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ html.py
│  │     │  │  ├─ pygments.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ansi.cpython-39.pyc
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ html.cpython-39.pyc
│  │     │  │     ├─ pygments.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ history.py
│  │     │  ├─ input
│  │     │  │  ├─ ansi_escape_sequences.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ defaults.py
│  │     │  │  ├─ posix_pipe.py
│  │     │  │  ├─ posix_utils.py
│  │     │  │  ├─ typeahead.py
│  │     │  │  ├─ vt100.py
│  │     │  │  ├─ vt100_parser.py
│  │     │  │  ├─ win32.py
│  │     │  │  ├─ win32_pipe.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ansi_escape_sequences.cpython-39.pyc
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ defaults.cpython-39.pyc
│  │     │  │     ├─ posix_pipe.cpython-39.pyc
│  │     │  │     ├─ posix_utils.cpython-39.pyc
│  │     │  │     ├─ typeahead.cpython-39.pyc
│  │     │  │     ├─ vt100.cpython-39.pyc
│  │     │  │     ├─ vt100_parser.cpython-39.pyc
│  │     │  │     ├─ win32.cpython-39.pyc
│  │     │  │     ├─ win32_pipe.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ keys.py
│  │     │  ├─ key_binding
│  │     │  │  ├─ bindings
│  │     │  │  │  ├─ auto_suggest.py
│  │     │  │  │  ├─ basic.py
│  │     │  │  │  ├─ completion.py
│  │     │  │  │  ├─ cpr.py
│  │     │  │  │  ├─ emacs.py
│  │     │  │  │  ├─ focus.py
│  │     │  │  │  ├─ mouse.py
│  │     │  │  │  ├─ named_commands.py
│  │     │  │  │  ├─ open_in_editor.py
│  │     │  │  │  ├─ page_navigation.py
│  │     │  │  │  ├─ scroll.py
│  │     │  │  │  ├─ search.py
│  │     │  │  │  ├─ vi.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ auto_suggest.cpython-39.pyc
│  │     │  │  │     ├─ basic.cpython-39.pyc
│  │     │  │  │     ├─ completion.cpython-39.pyc
│  │     │  │  │     ├─ cpr.cpython-39.pyc
│  │     │  │  │     ├─ emacs.cpython-39.pyc
│  │     │  │  │     ├─ focus.cpython-39.pyc
│  │     │  │  │     ├─ mouse.cpython-39.pyc
│  │     │  │  │     ├─ named_commands.cpython-39.pyc
│  │     │  │  │     ├─ open_in_editor.cpython-39.pyc
│  │     │  │  │     ├─ page_navigation.cpython-39.pyc
│  │     │  │  │     ├─ scroll.cpython-39.pyc
│  │     │  │  │     ├─ search.cpython-39.pyc
│  │     │  │  │     ├─ vi.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ defaults.py
│  │     │  │  ├─ digraphs.py
│  │     │  │  ├─ emacs_state.py
│  │     │  │  ├─ key_bindings.py
│  │     │  │  ├─ key_processor.py
│  │     │  │  ├─ vi_state.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ defaults.cpython-39.pyc
│  │     │  │     ├─ digraphs.cpython-39.pyc
│  │     │  │     ├─ emacs_state.cpython-39.pyc
│  │     │  │     ├─ key_bindings.cpython-39.pyc
│  │     │  │     ├─ key_processor.cpython-39.pyc
│  │     │  │     ├─ vi_state.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ layout
│  │     │  │  ├─ containers.py
│  │     │  │  ├─ controls.py
│  │     │  │  ├─ dimension.py
│  │     │  │  ├─ dummy.py
│  │     │  │  ├─ layout.py
│  │     │  │  ├─ margins.py
│  │     │  │  ├─ menus.py
│  │     │  │  ├─ mouse_handlers.py
│  │     │  │  ├─ processors.py
│  │     │  │  ├─ screen.py
│  │     │  │  ├─ scrollable_pane.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ containers.cpython-39.pyc
│  │     │  │     ├─ controls.cpython-39.pyc
│  │     │  │     ├─ dimension.cpython-39.pyc
│  │     │  │     ├─ dummy.cpython-39.pyc
│  │     │  │     ├─ layout.cpython-39.pyc
│  │     │  │     ├─ margins.cpython-39.pyc
│  │     │  │     ├─ menus.cpython-39.pyc
│  │     │  │     ├─ mouse_handlers.cpython-39.pyc
│  │     │  │     ├─ processors.cpython-39.pyc
│  │     │  │     ├─ screen.cpython-39.pyc
│  │     │  │     ├─ scrollable_pane.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ lexers
│  │     │  │  ├─ base.py
│  │     │  │  ├─ pygments.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ pygments.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ log.py
│  │     │  ├─ mouse_events.py
│  │     │  ├─ output
│  │     │  │  ├─ base.py
│  │     │  │  ├─ color_depth.py
│  │     │  │  ├─ conemu.py
│  │     │  │  ├─ defaults.py
│  │     │  │  ├─ flush_stdout.py
│  │     │  │  ├─ plain_text.py
│  │     │  │  ├─ vt100.py
│  │     │  │  ├─ win32.py
│  │     │  │  ├─ windows10.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ color_depth.cpython-39.pyc
│  │     │  │     ├─ conemu.cpython-39.pyc
│  │     │  │     ├─ defaults.cpython-39.pyc
│  │     │  │     ├─ flush_stdout.cpython-39.pyc
│  │     │  │     ├─ plain_text.cpython-39.pyc
│  │     │  │     ├─ vt100.cpython-39.pyc
│  │     │  │     ├─ win32.cpython-39.pyc
│  │     │  │     ├─ windows10.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ patch_stdout.py
│  │     │  ├─ py.typed
│  │     │  ├─ renderer.py
│  │     │  ├─ search.py
│  │     │  ├─ selection.py
│  │     │  ├─ shortcuts
│  │     │  │  ├─ dialogs.py
│  │     │  │  ├─ progress_bar
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ formatters.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ formatters.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ prompt.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ dialogs.cpython-39.pyc
│  │     │  │     ├─ prompt.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ styles
│  │     │  │  ├─ base.py
│  │     │  │  ├─ defaults.py
│  │     │  │  ├─ named_colors.py
│  │     │  │  ├─ pygments.py
│  │     │  │  ├─ style.py
│  │     │  │  ├─ style_transformation.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ defaults.cpython-39.pyc
│  │     │  │     ├─ named_colors.cpython-39.pyc
│  │     │  │     ├─ pygments.cpython-39.pyc
│  │     │  │     ├─ style.cpython-39.pyc
│  │     │  │     ├─ style_transformation.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ token.py
│  │     │  ├─ utils.py
│  │     │  ├─ validation.py
│  │     │  ├─ widgets
│  │     │  │  ├─ base.py
│  │     │  │  ├─ dialogs.py
│  │     │  │  ├─ menus.py
│  │     │  │  ├─ toolbars.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ dialogs.cpython-39.pyc
│  │     │  │     ├─ menus.cpython-39.pyc
│  │     │  │     ├─ toolbars.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ win32_types.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ auto_suggest.cpython-39.pyc
│  │     │     ├─ buffer.cpython-39.pyc
│  │     │     ├─ cache.cpython-39.pyc
│  │     │     ├─ cursor_shapes.cpython-39.pyc
│  │     │     ├─ data_structures.cpython-39.pyc
│  │     │     ├─ document.cpython-39.pyc
│  │     │     ├─ enums.cpython-39.pyc
│  │     │     ├─ history.cpython-39.pyc
│  │     │     ├─ keys.cpython-39.pyc
│  │     │     ├─ log.cpython-39.pyc
│  │     │     ├─ mouse_events.cpython-39.pyc
│  │     │     ├─ patch_stdout.cpython-39.pyc
│  │     │     ├─ renderer.cpython-39.pyc
│  │     │     ├─ search.cpython-39.pyc
│  │     │     ├─ selection.cpython-39.pyc
│  │     │     ├─ token.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ validation.cpython-39.pyc
│  │     │     ├─ win32_types.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ prompt_toolkit-3.0.38.dist-info
│  │     │  ├─ AUTHORS.rst
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ psutil
│  │     │  ├─ tests
│  │     │  │  ├─ runner.py
│  │     │  │  ├─ test_aix.py
│  │     │  │  ├─ test_bsd.py
│  │     │  │  ├─ test_connections.py
│  │     │  │  ├─ test_contracts.py
│  │     │  │  ├─ test_linux.py
│  │     │  │  ├─ test_memleaks.py
│  │     │  │  ├─ test_misc.py
│  │     │  │  ├─ test_osx.py
│  │     │  │  ├─ test_posix.py
│  │     │  │  ├─ test_process.py
│  │     │  │  ├─ test_sunos.py
│  │     │  │  ├─ test_system.py
│  │     │  │  ├─ test_testutils.py
│  │     │  │  ├─ test_unicode.py
│  │     │  │  ├─ test_windows.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ runner.cpython-39.pyc
│  │     │  │     ├─ test_aix.cpython-39.pyc
│  │     │  │     ├─ test_bsd.cpython-39.pyc
│  │     │  │     ├─ test_connections.cpython-39.pyc
│  │     │  │     ├─ test_contracts.cpython-39.pyc
│  │     │  │     ├─ test_linux.cpython-39.pyc
│  │     │  │     ├─ test_memleaks.cpython-39.pyc
│  │     │  │     ├─ test_misc.cpython-39.pyc
│  │     │  │     ├─ test_osx.cpython-39.pyc
│  │     │  │     ├─ test_posix.cpython-39.pyc
│  │     │  │     ├─ test_process.cpython-39.pyc
│  │     │  │     ├─ test_sunos.cpython-39.pyc
│  │     │  │     ├─ test_system.cpython-39.pyc
│  │     │  │     ├─ test_testutils.cpython-39.pyc
│  │     │  │     ├─ test_unicode.cpython-39.pyc
│  │     │  │     ├─ test_windows.cpython-39.pyc
│  │     │  │     ├─ __init__.cpython-39.pyc
│  │     │  │     └─ __main__.cpython-39.pyc
│  │     │  ├─ _common.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _psaix.py
│  │     │  ├─ _psbsd.py
│  │     │  ├─ _pslinux.py
│  │     │  ├─ _psosx.py
│  │     │  ├─ _psposix.py
│  │     │  ├─ _pssunos.py
│  │     │  ├─ _psutil_windows.pyd
│  │     │  ├─ _pswindows.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ _common.cpython-39.pyc
│  │     │     ├─ _compat.cpython-39.pyc
│  │     │     ├─ _psaix.cpython-39.pyc
│  │     │     ├─ _psbsd.cpython-39.pyc
│  │     │     ├─ _pslinux.cpython-39.pyc
│  │     │     ├─ _psosx.cpython-39.pyc
│  │     │     ├─ _psposix.cpython-39.pyc
│  │     │     ├─ _pssunos.cpython-39.pyc
│  │     │     ├─ _pswindows.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ psutil-5.9.5.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pure_eval
│  │     │  ├─ core.py
│  │     │  ├─ my_getattr_static.py
│  │     │  ├─ py.typed
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ core.cpython-39.pyc
│  │     │     ├─ my_getattr_static.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ pure_eval-0.2.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pvectorc.cp39-win_amd64.pyd
│  │     ├─ pydantic
│  │     │  ├─ annotated_types.cp39-win_amd64.pyd
│  │     │  ├─ annotated_types.py
│  │     │  ├─ class_validators.cp39-win_amd64.pyd
│  │     │  ├─ class_validators.py
│  │     │  ├─ color.cp39-win_amd64.pyd
│  │     │  ├─ color.py
│  │     │  ├─ config.cp39-win_amd64.pyd
│  │     │  ├─ config.py
│  │     │  ├─ dataclasses.cp39-win_amd64.pyd
│  │     │  ├─ dataclasses.py
│  │     │  ├─ datetime_parse.cp39-win_amd64.pyd
│  │     │  ├─ datetime_parse.py
│  │     │  ├─ decorator.cp39-win_amd64.pyd
│  │     │  ├─ decorator.py
│  │     │  ├─ env_settings.cp39-win_amd64.pyd
│  │     │  ├─ env_settings.py
│  │     │  ├─ errors.cp39-win_amd64.pyd
│  │     │  ├─ errors.py
│  │     │  ├─ error_wrappers.cp39-win_amd64.pyd
│  │     │  ├─ error_wrappers.py
│  │     │  ├─ fields.cp39-win_amd64.pyd
│  │     │  ├─ fields.py
│  │     │  ├─ generics.py
│  │     │  ├─ json.cp39-win_amd64.pyd
│  │     │  ├─ json.py
│  │     │  ├─ main.cp39-win_amd64.pyd
│  │     │  ├─ main.py
│  │     │  ├─ mypy.cp39-win_amd64.pyd
│  │     │  ├─ mypy.py
│  │     │  ├─ networks.cp39-win_amd64.pyd
│  │     │  ├─ networks.py
│  │     │  ├─ parse.cp39-win_amd64.pyd
│  │     │  ├─ parse.py
│  │     │  ├─ py.typed
│  │     │  ├─ schema.cp39-win_amd64.pyd
│  │     │  ├─ schema.py
│  │     │  ├─ tools.cp39-win_amd64.pyd
│  │     │  ├─ tools.py
│  │     │  ├─ types.cp39-win_amd64.pyd
│  │     │  ├─ types.py
│  │     │  ├─ typing.cp39-win_amd64.pyd
│  │     │  ├─ typing.py
│  │     │  ├─ utils.cp39-win_amd64.pyd
│  │     │  ├─ utils.py
│  │     │  ├─ validators.cp39-win_amd64.pyd
│  │     │  ├─ validators.py
│  │     │  ├─ version.cp39-win_amd64.pyd
│  │     │  ├─ version.py
│  │     │  ├─ _hypothesis_plugin.cp39-win_amd64.pyd
│  │     │  ├─ _hypothesis_plugin.py
│  │     │  ├─ __init__.cp39-win_amd64.pyd
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ annotated_types.cpython-39.pyc
│  │     │     ├─ class_validators.cpython-39.pyc
│  │     │     ├─ color.cpython-39.pyc
│  │     │     ├─ config.cpython-39.pyc
│  │     │     ├─ dataclasses.cpython-39.pyc
│  │     │     ├─ datetime_parse.cpython-39.pyc
│  │     │     ├─ decorator.cpython-39.pyc
│  │     │     ├─ env_settings.cpython-39.pyc
│  │     │     ├─ errors.cpython-39.pyc
│  │     │     ├─ error_wrappers.cpython-39.pyc
│  │     │     ├─ fields.cpython-39.pyc
│  │     │     ├─ generics.cpython-39.pyc
│  │     │     ├─ json.cpython-39.pyc
│  │     │     ├─ main.cpython-39.pyc
│  │     │     ├─ mypy.cpython-39.pyc
│  │     │     ├─ networks.cpython-39.pyc
│  │     │     ├─ parse.cpython-39.pyc
│  │     │     ├─ schema.cpython-39.pyc
│  │     │     ├─ tools.cpython-39.pyc
│  │     │     ├─ types.cpython-39.pyc
│  │     │     ├─ typing.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ validators.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     ├─ _hypothesis_plugin.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ pydantic-1.10.7.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pygments
│  │     │  ├─ cmdline.py
│  │     │  ├─ console.py
│  │     │  ├─ filter.py
│  │     │  ├─ filters
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ formatter.py
│  │     │  ├─ formatters
│  │     │  │  ├─ bbcode.py
│  │     │  │  ├─ groff.py
│  │     │  │  ├─ html.py
│  │     │  │  ├─ img.py
│  │     │  │  ├─ irc.py
│  │     │  │  ├─ latex.py
│  │     │  │  ├─ other.py
│  │     │  │  ├─ pangomarkup.py
│  │     │  │  ├─ rtf.py
│  │     │  │  ├─ svg.py
│  │     │  │  ├─ terminal.py
│  │     │  │  ├─ terminal256.py
│  │     │  │  ├─ _mapping.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ bbcode.cpython-39.pyc
│  │     │  │     ├─ groff.cpython-39.pyc
│  │     │  │     ├─ html.cpython-39.pyc
│  │     │  │     ├─ img.cpython-39.pyc
│  │     │  │     ├─ irc.cpython-39.pyc
│  │     │  │     ├─ latex.cpython-39.pyc
│  │     │  │     ├─ other.cpython-39.pyc
│  │     │  │     ├─ pangomarkup.cpython-39.pyc
│  │     │  │     ├─ rtf.cpython-39.pyc
│  │     │  │     ├─ svg.cpython-39.pyc
│  │     │  │     ├─ terminal.cpython-39.pyc
│  │     │  │     ├─ terminal256.cpython-39.pyc
│  │     │  │     ├─ _mapping.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ lexer.py
│  │     │  ├─ lexers
│  │     │  │  ├─ actionscript.py
│  │     │  │  ├─ ada.py
│  │     │  │  ├─ agile.py
│  │     │  │  ├─ algebra.py
│  │     │  │  ├─ ambient.py
│  │     │  │  ├─ amdgpu.py
│  │     │  │  ├─ ampl.py
│  │     │  │  ├─ apdlexer.py
│  │     │  │  ├─ apl.py
│  │     │  │  ├─ archetype.py
│  │     │  │  ├─ arrow.py
│  │     │  │  ├─ arturo.py
│  │     │  │  ├─ asc.py
│  │     │  │  ├─ asm.py
│  │     │  │  ├─ automation.py
│  │     │  │  ├─ bare.py
│  │     │  │  ├─ basic.py
│  │     │  │  ├─ bdd.py
│  │     │  │  ├─ berry.py
│  │     │  │  ├─ bibtex.py
│  │     │  │  ├─ boa.py
│  │     │  │  ├─ business.py
│  │     │  │  ├─ capnproto.py
│  │     │  │  ├─ carbon.py
│  │     │  │  ├─ cddl.py
│  │     │  │  ├─ chapel.py
│  │     │  │  ├─ clean.py
│  │     │  │  ├─ comal.py
│  │     │  │  ├─ compiled.py
│  │     │  │  ├─ configs.py
│  │     │  │  ├─ console.py
│  │     │  │  ├─ cplint.py
│  │     │  │  ├─ crystal.py
│  │     │  │  ├─ csound.py
│  │     │  │  ├─ css.py
│  │     │  │  ├─ c_cpp.py
│  │     │  │  ├─ c_like.py
│  │     │  │  ├─ d.py
│  │     │  │  ├─ dalvik.py
│  │     │  │  ├─ data.py
│  │     │  │  ├─ dax.py
│  │     │  │  ├─ devicetree.py
│  │     │  │  ├─ diff.py
│  │     │  │  ├─ dotnet.py
│  │     │  │  ├─ dsls.py
│  │     │  │  ├─ dylan.py
│  │     │  │  ├─ ecl.py
│  │     │  │  ├─ eiffel.py
│  │     │  │  ├─ elm.py
│  │     │  │  ├─ elpi.py
│  │     │  │  ├─ email.py
│  │     │  │  ├─ erlang.py
│  │     │  │  ├─ esoteric.py
│  │     │  │  ├─ ezhil.py
│  │     │  │  ├─ factor.py
│  │     │  │  ├─ fantom.py
│  │     │  │  ├─ felix.py
│  │     │  │  ├─ fift.py
│  │     │  │  ├─ floscript.py
│  │     │  │  ├─ forth.py
│  │     │  │  ├─ fortran.py
│  │     │  │  ├─ foxpro.py
│  │     │  │  ├─ freefem.py
│  │     │  │  ├─ func.py
│  │     │  │  ├─ functional.py
│  │     │  │  ├─ futhark.py
│  │     │  │  ├─ gcodelexer.py
│  │     │  │  ├─ gdscript.py
│  │     │  │  ├─ go.py
│  │     │  │  ├─ grammar_notation.py
│  │     │  │  ├─ graph.py
│  │     │  │  ├─ graphics.py
│  │     │  │  ├─ graphviz.py
│  │     │  │  ├─ gsql.py
│  │     │  │  ├─ haskell.py
│  │     │  │  ├─ haxe.py
│  │     │  │  ├─ hdl.py
│  │     │  │  ├─ hexdump.py
│  │     │  │  ├─ html.py
│  │     │  │  ├─ idl.py
│  │     │  │  ├─ igor.py
│  │     │  │  ├─ inferno.py
│  │     │  │  ├─ installers.py
│  │     │  │  ├─ int_fiction.py
│  │     │  │  ├─ iolang.py
│  │     │  │  ├─ j.py
│  │     │  │  ├─ javascript.py
│  │     │  │  ├─ jmespath.py
│  │     │  │  ├─ jslt.py
│  │     │  │  ├─ jsonnet.py
│  │     │  │  ├─ julia.py
│  │     │  │  ├─ jvm.py
│  │     │  │  ├─ kuin.py
│  │     │  │  ├─ lilypond.py
│  │     │  │  ├─ lisp.py
│  │     │  │  ├─ macaulay2.py
│  │     │  │  ├─ make.py
│  │     │  │  ├─ markup.py
│  │     │  │  ├─ math.py
│  │     │  │  ├─ matlab.py
│  │     │  │  ├─ maxima.py
│  │     │  │  ├─ meson.py
│  │     │  │  ├─ mime.py
│  │     │  │  ├─ minecraft.py
│  │     │  │  ├─ mips.py
│  │     │  │  ├─ ml.py
│  │     │  │  ├─ modeling.py
│  │     │  │  ├─ modula2.py
│  │     │  │  ├─ monte.py
│  │     │  │  ├─ mosel.py
│  │     │  │  ├─ ncl.py
│  │     │  │  ├─ nimrod.py
│  │     │  │  ├─ nit.py
│  │     │  │  ├─ nix.py
│  │     │  │  ├─ oberon.py
│  │     │  │  ├─ objective.py
│  │     │  │  ├─ ooc.py
│  │     │  │  ├─ other.py
│  │     │  │  ├─ parasail.py
│  │     │  │  ├─ parsers.py
│  │     │  │  ├─ pascal.py
│  │     │  │  ├─ pawn.py
│  │     │  │  ├─ perl.py
│  │     │  │  ├─ phix.py
│  │     │  │  ├─ php.py
│  │     │  │  ├─ pointless.py
│  │     │  │  ├─ pony.py
│  │     │  │  ├─ praat.py
│  │     │  │  ├─ procfile.py
│  │     │  │  ├─ prolog.py
│  │     │  │  ├─ promql.py
│  │     │  │  ├─ python.py
│  │     │  │  ├─ q.py
│  │     │  │  ├─ qlik.py
│  │     │  │  ├─ qvt.py
│  │     │  │  ├─ r.py
│  │     │  │  ├─ rdf.py
│  │     │  │  ├─ rebol.py
│  │     │  │  ├─ resource.py
│  │     │  │  ├─ ride.py
│  │     │  │  ├─ rita.py
│  │     │  │  ├─ rnc.py
│  │     │  │  ├─ roboconf.py
│  │     │  │  ├─ robotframework.py
│  │     │  │  ├─ ruby.py
│  │     │  │  ├─ rust.py
│  │     │  │  ├─ sas.py
│  │     │  │  ├─ savi.py
│  │     │  │  ├─ scdoc.py
│  │     │  │  ├─ scripting.py
│  │     │  │  ├─ sgf.py
│  │     │  │  ├─ shell.py
│  │     │  │  ├─ sieve.py
│  │     │  │  ├─ slash.py
│  │     │  │  ├─ smalltalk.py
│  │     │  │  ├─ smithy.py
│  │     │  │  ├─ smv.py
│  │     │  │  ├─ snobol.py
│  │     │  │  ├─ solidity.py
│  │     │  │  ├─ sophia.py
│  │     │  │  ├─ special.py
│  │     │  │  ├─ spice.py
│  │     │  │  ├─ sql.py
│  │     │  │  ├─ srcinfo.py
│  │     │  │  ├─ stata.py
│  │     │  │  ├─ supercollider.py
│  │     │  │  ├─ tal.py
│  │     │  │  ├─ tcl.py
│  │     │  │  ├─ teal.py
│  │     │  │  ├─ templates.py
│  │     │  │  ├─ teraterm.py
│  │     │  │  ├─ testing.py
│  │     │  │  ├─ text.py
│  │     │  │  ├─ textedit.py
│  │     │  │  ├─ textfmts.py
│  │     │  │  ├─ theorem.py
│  │     │  │  ├─ thingsdb.py
│  │     │  │  ├─ tlb.py
│  │     │  │  ├─ tnt.py
│  │     │  │  ├─ trafficscript.py
│  │     │  │  ├─ typoscript.py
│  │     │  │  ├─ ul4.py
│  │     │  │  ├─ unicon.py
│  │     │  │  ├─ urbi.py
│  │     │  │  ├─ usd.py
│  │     │  │  ├─ varnish.py
│  │     │  │  ├─ verification.py
│  │     │  │  ├─ web.py
│  │     │  │  ├─ webassembly.py
│  │     │  │  ├─ webidl.py
│  │     │  │  ├─ webmisc.py
│  │     │  │  ├─ wgsl.py
│  │     │  │  ├─ whiley.py
│  │     │  │  ├─ wowtoc.py
│  │     │  │  ├─ wren.py
│  │     │  │  ├─ x10.py
│  │     │  │  ├─ xorg.py
│  │     │  │  ├─ yang.py
│  │     │  │  ├─ zig.py
│  │     │  │  ├─ _ada_builtins.py
│  │     │  │  ├─ _asy_builtins.py
│  │     │  │  ├─ _cl_builtins.py
│  │     │  │  ├─ _cocoa_builtins.py
│  │     │  │  ├─ _csound_builtins.py
│  │     │  │  ├─ _css_builtins.py
│  │     │  │  ├─ _julia_builtins.py
│  │     │  │  ├─ _lasso_builtins.py
│  │     │  │  ├─ _lilypond_builtins.py
│  │     │  │  ├─ _lua_builtins.py
│  │     │  │  ├─ _mapping.py
│  │     │  │  ├─ _mql_builtins.py
│  │     │  │  ├─ _mysql_builtins.py
│  │     │  │  ├─ _openedge_builtins.py
│  │     │  │  ├─ _php_builtins.py
│  │     │  │  ├─ _postgres_builtins.py
│  │     │  │  ├─ _qlik_builtins.py
│  │     │  │  ├─ _scheme_builtins.py
│  │     │  │  ├─ _scilab_builtins.py
│  │     │  │  ├─ _sourcemod_builtins.py
│  │     │  │  ├─ _stan_builtins.py
│  │     │  │  ├─ _stata_builtins.py
│  │     │  │  ├─ _tsql_builtins.py
│  │     │  │  ├─ _usd_builtins.py
│  │     │  │  ├─ _vbscript_builtins.py
│  │     │  │  ├─ _vim_builtins.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ actionscript.cpython-39.pyc
│  │     │  │     ├─ ada.cpython-39.pyc
│  │     │  │     ├─ agile.cpython-39.pyc
│  │     │  │     ├─ algebra.cpython-39.pyc
│  │     │  │     ├─ ambient.cpython-39.pyc
│  │     │  │     ├─ amdgpu.cpython-39.pyc
│  │     │  │     ├─ ampl.cpython-39.pyc
│  │     │  │     ├─ apdlexer.cpython-39.pyc
│  │     │  │     ├─ apl.cpython-39.pyc
│  │     │  │     ├─ archetype.cpython-39.pyc
│  │     │  │     ├─ arrow.cpython-39.pyc
│  │     │  │     ├─ arturo.cpython-39.pyc
│  │     │  │     ├─ asc.cpython-39.pyc
│  │     │  │     ├─ asm.cpython-39.pyc
│  │     │  │     ├─ automation.cpython-39.pyc
│  │     │  │     ├─ bare.cpython-39.pyc
│  │     │  │     ├─ basic.cpython-39.pyc
│  │     │  │     ├─ bdd.cpython-39.pyc
│  │     │  │     ├─ berry.cpython-39.pyc
│  │     │  │     ├─ bibtex.cpython-39.pyc
│  │     │  │     ├─ boa.cpython-39.pyc
│  │     │  │     ├─ business.cpython-39.pyc
│  │     │  │     ├─ capnproto.cpython-39.pyc
│  │     │  │     ├─ carbon.cpython-39.pyc
│  │     │  │     ├─ cddl.cpython-39.pyc
│  │     │  │     ├─ chapel.cpython-39.pyc
│  │     │  │     ├─ clean.cpython-39.pyc
│  │     │  │     ├─ comal.cpython-39.pyc
│  │     │  │     ├─ compiled.cpython-39.pyc
│  │     │  │     ├─ configs.cpython-39.pyc
│  │     │  │     ├─ console.cpython-39.pyc
│  │     │  │     ├─ cplint.cpython-39.pyc
│  │     │  │     ├─ crystal.cpython-39.pyc
│  │     │  │     ├─ csound.cpython-39.pyc
│  │     │  │     ├─ css.cpython-39.pyc
│  │     │  │     ├─ c_cpp.cpython-39.pyc
│  │     │  │     ├─ c_like.cpython-39.pyc
│  │     │  │     ├─ d.cpython-39.pyc
│  │     │  │     ├─ dalvik.cpython-39.pyc
│  │     │  │     ├─ data.cpython-39.pyc
│  │     │  │     ├─ dax.cpython-39.pyc
│  │     │  │     ├─ devicetree.cpython-39.pyc
│  │     │  │     ├─ diff.cpython-39.pyc
│  │     │  │     ├─ dotnet.cpython-39.pyc
│  │     │  │     ├─ dsls.cpython-39.pyc
│  │     │  │     ├─ dylan.cpython-39.pyc
│  │     │  │     ├─ ecl.cpython-39.pyc
│  │     │  │     ├─ eiffel.cpython-39.pyc
│  │     │  │     ├─ elm.cpython-39.pyc
│  │     │  │     ├─ elpi.cpython-39.pyc
│  │     │  │     ├─ email.cpython-39.pyc
│  │     │  │     ├─ erlang.cpython-39.pyc
│  │     │  │     ├─ esoteric.cpython-39.pyc
│  │     │  │     ├─ ezhil.cpython-39.pyc
│  │     │  │     ├─ factor.cpython-39.pyc
│  │     │  │     ├─ fantom.cpython-39.pyc
│  │     │  │     ├─ felix.cpython-39.pyc
│  │     │  │     ├─ fift.cpython-39.pyc
│  │     │  │     ├─ floscript.cpython-39.pyc
│  │     │  │     ├─ forth.cpython-39.pyc
│  │     │  │     ├─ fortran.cpython-39.pyc
│  │     │  │     ├─ foxpro.cpython-39.pyc
│  │     │  │     ├─ freefem.cpython-39.pyc
│  │     │  │     ├─ func.cpython-39.pyc
│  │     │  │     ├─ functional.cpython-39.pyc
│  │     │  │     ├─ futhark.cpython-39.pyc
│  │     │  │     ├─ gcodelexer.cpython-39.pyc
│  │     │  │     ├─ gdscript.cpython-39.pyc
│  │     │  │     ├─ go.cpython-39.pyc
│  │     │  │     ├─ grammar_notation.cpython-39.pyc
│  │     │  │     ├─ graph.cpython-39.pyc
│  │     │  │     ├─ graphics.cpython-39.pyc
│  │     │  │     ├─ graphviz.cpython-39.pyc
│  │     │  │     ├─ gsql.cpython-39.pyc
│  │     │  │     ├─ haskell.cpython-39.pyc
│  │     │  │     ├─ haxe.cpython-39.pyc
│  │     │  │     ├─ hdl.cpython-39.pyc
│  │     │  │     ├─ hexdump.cpython-39.pyc
│  │     │  │     ├─ html.cpython-39.pyc
│  │     │  │     ├─ idl.cpython-39.pyc
│  │     │  │     ├─ igor.cpython-39.pyc
│  │     │  │     ├─ inferno.cpython-39.pyc
│  │     │  │     ├─ installers.cpython-39.pyc
│  │     │  │     ├─ int_fiction.cpython-39.pyc
│  │     │  │     ├─ iolang.cpython-39.pyc
│  │     │  │     ├─ j.cpython-39.pyc
│  │     │  │     ├─ javascript.cpython-39.pyc
│  │     │  │     ├─ jmespath.cpython-39.pyc
│  │     │  │     ├─ jslt.cpython-39.pyc
│  │     │  │     ├─ jsonnet.cpython-39.pyc
│  │     │  │     ├─ julia.cpython-39.pyc
│  │     │  │     ├─ jvm.cpython-39.pyc
│  │     │  │     ├─ kuin.cpython-39.pyc
│  │     │  │     ├─ lilypond.cpython-39.pyc
│  │     │  │     ├─ lisp.cpython-39.pyc
│  │     │  │     ├─ macaulay2.cpython-39.pyc
│  │     │  │     ├─ make.cpython-39.pyc
│  │     │  │     ├─ markup.cpython-39.pyc
│  │     │  │     ├─ math.cpython-39.pyc
│  │     │  │     ├─ matlab.cpython-39.pyc
│  │     │  │     ├─ maxima.cpython-39.pyc
│  │     │  │     ├─ meson.cpython-39.pyc
│  │     │  │     ├─ mime.cpython-39.pyc
│  │     │  │     ├─ minecraft.cpython-39.pyc
│  │     │  │     ├─ mips.cpython-39.pyc
│  │     │  │     ├─ ml.cpython-39.pyc
│  │     │  │     ├─ modeling.cpython-39.pyc
│  │     │  │     ├─ modula2.cpython-39.pyc
│  │     │  │     ├─ monte.cpython-39.pyc
│  │     │  │     ├─ mosel.cpython-39.pyc
│  │     │  │     ├─ ncl.cpython-39.pyc
│  │     │  │     ├─ nimrod.cpython-39.pyc
│  │     │  │     ├─ nit.cpython-39.pyc
│  │     │  │     ├─ nix.cpython-39.pyc
│  │     │  │     ├─ oberon.cpython-39.pyc
│  │     │  │     ├─ objective.cpython-39.pyc
│  │     │  │     ├─ ooc.cpython-39.pyc
│  │     │  │     ├─ other.cpython-39.pyc
│  │     │  │     ├─ parasail.cpython-39.pyc
│  │     │  │     ├─ parsers.cpython-39.pyc
│  │     │  │     ├─ pascal.cpython-39.pyc
│  │     │  │     ├─ pawn.cpython-39.pyc
│  │     │  │     ├─ perl.cpython-39.pyc
│  │     │  │     ├─ phix.cpython-39.pyc
│  │     │  │     ├─ php.cpython-39.pyc
│  │     │  │     ├─ pointless.cpython-39.pyc
│  │     │  │     ├─ pony.cpython-39.pyc
│  │     │  │     ├─ praat.cpython-39.pyc
│  │     │  │     ├─ procfile.cpython-39.pyc
│  │     │  │     ├─ prolog.cpython-39.pyc
│  │     │  │     ├─ promql.cpython-39.pyc
│  │     │  │     ├─ python.cpython-39.pyc
│  │     │  │     ├─ q.cpython-39.pyc
│  │     │  │     ├─ qlik.cpython-39.pyc
│  │     │  │     ├─ qvt.cpython-39.pyc
│  │     │  │     ├─ r.cpython-39.pyc
│  │     │  │     ├─ rdf.cpython-39.pyc
│  │     │  │     ├─ rebol.cpython-39.pyc
│  │     │  │     ├─ resource.cpython-39.pyc
│  │     │  │     ├─ ride.cpython-39.pyc
│  │     │  │     ├─ rita.cpython-39.pyc
│  │     │  │     ├─ rnc.cpython-39.pyc
│  │     │  │     ├─ roboconf.cpython-39.pyc
│  │     │  │     ├─ robotframework.cpython-39.pyc
│  │     │  │     ├─ ruby.cpython-39.pyc
│  │     │  │     ├─ rust.cpython-39.pyc
│  │     │  │     ├─ sas.cpython-39.pyc
│  │     │  │     ├─ savi.cpython-39.pyc
│  │     │  │     ├─ scdoc.cpython-39.pyc
│  │     │  │     ├─ scripting.cpython-39.pyc
│  │     │  │     ├─ sgf.cpython-39.pyc
│  │     │  │     ├─ shell.cpython-39.pyc
│  │     │  │     ├─ sieve.cpython-39.pyc
│  │     │  │     ├─ slash.cpython-39.pyc
│  │     │  │     ├─ smalltalk.cpython-39.pyc
│  │     │  │     ├─ smithy.cpython-39.pyc
│  │     │  │     ├─ smv.cpython-39.pyc
│  │     │  │     ├─ snobol.cpython-39.pyc
│  │     │  │     ├─ solidity.cpython-39.pyc
│  │     │  │     ├─ sophia.cpython-39.pyc
│  │     │  │     ├─ special.cpython-39.pyc
│  │     │  │     ├─ spice.cpython-39.pyc
│  │     │  │     ├─ sql.cpython-39.pyc
│  │     │  │     ├─ srcinfo.cpython-39.pyc
│  │     │  │     ├─ stata.cpython-39.pyc
│  │     │  │     ├─ supercollider.cpython-39.pyc
│  │     │  │     ├─ tal.cpython-39.pyc
│  │     │  │     ├─ tcl.cpython-39.pyc
│  │     │  │     ├─ teal.cpython-39.pyc
│  │     │  │     ├─ templates.cpython-39.pyc
│  │     │  │     ├─ teraterm.cpython-39.pyc
│  │     │  │     ├─ testing.cpython-39.pyc
│  │     │  │     ├─ text.cpython-39.pyc
│  │     │  │     ├─ textedit.cpython-39.pyc
│  │     │  │     ├─ textfmts.cpython-39.pyc
│  │     │  │     ├─ theorem.cpython-39.pyc
│  │     │  │     ├─ thingsdb.cpython-39.pyc
│  │     │  │     ├─ tlb.cpython-39.pyc
│  │     │  │     ├─ tnt.cpython-39.pyc
│  │     │  │     ├─ trafficscript.cpython-39.pyc
│  │     │  │     ├─ typoscript.cpython-39.pyc
│  │     │  │     ├─ ul4.cpython-39.pyc
│  │     │  │     ├─ unicon.cpython-39.pyc
│  │     │  │     ├─ urbi.cpython-39.pyc
│  │     │  │     ├─ usd.cpython-39.pyc
│  │     │  │     ├─ varnish.cpython-39.pyc
│  │     │  │     ├─ verification.cpython-39.pyc
│  │     │  │     ├─ web.cpython-39.pyc
│  │     │  │     ├─ webassembly.cpython-39.pyc
│  │     │  │     ├─ webidl.cpython-39.pyc
│  │     │  │     ├─ webmisc.cpython-39.pyc
│  │     │  │     ├─ wgsl.cpython-39.pyc
│  │     │  │     ├─ whiley.cpython-39.pyc
│  │     │  │     ├─ wowtoc.cpython-39.pyc
│  │     │  │     ├─ wren.cpython-39.pyc
│  │     │  │     ├─ x10.cpython-39.pyc
│  │     │  │     ├─ xorg.cpython-39.pyc
│  │     │  │     ├─ yang.cpython-39.pyc
│  │     │  │     ├─ zig.cpython-39.pyc
│  │     │  │     ├─ _ada_builtins.cpython-39.pyc
│  │     │  │     ├─ _asy_builtins.cpython-39.pyc
│  │     │  │     ├─ _cl_builtins.cpython-39.pyc
│  │     │  │     ├─ _cocoa_builtins.cpython-39.pyc
│  │     │  │     ├─ _csound_builtins.cpython-39.pyc
│  │     │  │     ├─ _css_builtins.cpython-39.pyc
│  │     │  │     ├─ _julia_builtins.cpython-39.pyc
│  │     │  │     ├─ _lasso_builtins.cpython-39.pyc
│  │     │  │     ├─ _lilypond_builtins.cpython-39.pyc
│  │     │  │     ├─ _lua_builtins.cpython-39.pyc
│  │     │  │     ├─ _mapping.cpython-39.pyc
│  │     │  │     ├─ _mql_builtins.cpython-39.pyc
│  │     │  │     ├─ _mysql_builtins.cpython-39.pyc
│  │     │  │     ├─ _openedge_builtins.cpython-39.pyc
│  │     │  │     ├─ _php_builtins.cpython-39.pyc
│  │     │  │     ├─ _postgres_builtins.cpython-39.pyc
│  │     │  │     ├─ _qlik_builtins.cpython-39.pyc
│  │     │  │     ├─ _scheme_builtins.cpython-39.pyc
│  │     │  │     ├─ _scilab_builtins.cpython-39.pyc
│  │     │  │     ├─ _sourcemod_builtins.cpython-39.pyc
│  │     │  │     ├─ _stan_builtins.cpython-39.pyc
│  │     │  │     ├─ _stata_builtins.cpython-39.pyc
│  │     │  │     ├─ _tsql_builtins.cpython-39.pyc
│  │     │  │     ├─ _usd_builtins.cpython-39.pyc
│  │     │  │     ├─ _vbscript_builtins.cpython-39.pyc
│  │     │  │     ├─ _vim_builtins.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ modeline.py
│  │     │  ├─ plugin.py
│  │     │  ├─ regexopt.py
│  │     │  ├─ scanner.py
│  │     │  ├─ sphinxext.py
│  │     │  ├─ style.py
│  │     │  ├─ styles
│  │     │  │  ├─ abap.py
│  │     │  │  ├─ algol.py
│  │     │  │  ├─ algol_nu.py
│  │     │  │  ├─ arduino.py
│  │     │  │  ├─ autumn.py
│  │     │  │  ├─ borland.py
│  │     │  │  ├─ bw.py
│  │     │  │  ├─ colorful.py
│  │     │  │  ├─ default.py
│  │     │  │  ├─ dracula.py
│  │     │  │  ├─ emacs.py
│  │     │  │  ├─ friendly.py
│  │     │  │  ├─ friendly_grayscale.py
│  │     │  │  ├─ fruity.py
│  │     │  │  ├─ gh_dark.py
│  │     │  │  ├─ gruvbox.py
│  │     │  │  ├─ igor.py
│  │     │  │  ├─ inkpot.py
│  │     │  │  ├─ lilypond.py
│  │     │  │  ├─ lovelace.py
│  │     │  │  ├─ manni.py
│  │     │  │  ├─ material.py
│  │     │  │  ├─ monokai.py
│  │     │  │  ├─ murphy.py
│  │     │  │  ├─ native.py
│  │     │  │  ├─ nord.py
│  │     │  │  ├─ onedark.py
│  │     │  │  ├─ paraiso_dark.py
│  │     │  │  ├─ paraiso_light.py
│  │     │  │  ├─ pastie.py
│  │     │  │  ├─ perldoc.py
│  │     │  │  ├─ rainbow_dash.py
│  │     │  │  ├─ rrt.py
│  │     │  │  ├─ sas.py
│  │     │  │  ├─ solarized.py
│  │     │  │  ├─ staroffice.py
│  │     │  │  ├─ stata_dark.py
│  │     │  │  ├─ stata_light.py
│  │     │  │  ├─ tango.py
│  │     │  │  ├─ trac.py
│  │     │  │  ├─ vim.py
│  │     │  │  ├─ vs.py
│  │     │  │  ├─ xcode.py
│  │     │  │  ├─ zenburn.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ abap.cpython-39.pyc
│  │     │  │     ├─ algol.cpython-39.pyc
│  │     │  │     ├─ algol_nu.cpython-39.pyc
│  │     │  │     ├─ arduino.cpython-39.pyc
│  │     │  │     ├─ autumn.cpython-39.pyc
│  │     │  │     ├─ borland.cpython-39.pyc
│  │     │  │     ├─ bw.cpython-39.pyc
│  │     │  │     ├─ colorful.cpython-39.pyc
│  │     │  │     ├─ default.cpython-39.pyc
│  │     │  │     ├─ dracula.cpython-39.pyc
│  │     │  │     ├─ emacs.cpython-39.pyc
│  │     │  │     ├─ friendly.cpython-39.pyc
│  │     │  │     ├─ friendly_grayscale.cpython-39.pyc
│  │     │  │     ├─ fruity.cpython-39.pyc
│  │     │  │     ├─ gh_dark.cpython-39.pyc
│  │     │  │     ├─ gruvbox.cpython-39.pyc
│  │     │  │     ├─ igor.cpython-39.pyc
│  │     │  │     ├─ inkpot.cpython-39.pyc
│  │     │  │     ├─ lilypond.cpython-39.pyc
│  │     │  │     ├─ lovelace.cpython-39.pyc
│  │     │  │     ├─ manni.cpython-39.pyc
│  │     │  │     ├─ material.cpython-39.pyc
│  │     │  │     ├─ monokai.cpython-39.pyc
│  │     │  │     ├─ murphy.cpython-39.pyc
│  │     │  │     ├─ native.cpython-39.pyc
│  │     │  │     ├─ nord.cpython-39.pyc
│  │     │  │     ├─ onedark.cpython-39.pyc
│  │     │  │     ├─ paraiso_dark.cpython-39.pyc
│  │     │  │     ├─ paraiso_light.cpython-39.pyc
│  │     │  │     ├─ pastie.cpython-39.pyc
│  │     │  │     ├─ perldoc.cpython-39.pyc
│  │     │  │     ├─ rainbow_dash.cpython-39.pyc
│  │     │  │     ├─ rrt.cpython-39.pyc
│  │     │  │     ├─ sas.cpython-39.pyc
│  │     │  │     ├─ solarized.cpython-39.pyc
│  │     │  │     ├─ staroffice.cpython-39.pyc
│  │     │  │     ├─ stata_dark.cpython-39.pyc
│  │     │  │     ├─ stata_light.cpython-39.pyc
│  │     │  │     ├─ tango.cpython-39.pyc
│  │     │  │     ├─ trac.cpython-39.pyc
│  │     │  │     ├─ vim.cpython-39.pyc
│  │     │  │     ├─ vs.cpython-39.pyc
│  │     │  │     ├─ xcode.cpython-39.pyc
│  │     │  │     ├─ zenburn.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ token.py
│  │     │  ├─ unistring.py
│  │     │  ├─ util.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ cmdline.cpython-39.pyc
│  │     │     ├─ console.cpython-39.pyc
│  │     │     ├─ filter.cpython-39.pyc
│  │     │     ├─ formatter.cpython-39.pyc
│  │     │     ├─ lexer.cpython-39.pyc
│  │     │     ├─ modeline.cpython-39.pyc
│  │     │     ├─ plugin.cpython-39.pyc
│  │     │     ├─ regexopt.cpython-39.pyc
│  │     │     ├─ scanner.cpython-39.pyc
│  │     │     ├─ sphinxext.cpython-39.pyc
│  │     │     ├─ style.cpython-39.pyc
│  │     │     ├─ token.cpython-39.pyc
│  │     │     ├─ unistring.cpython-39.pyc
│  │     │     ├─ util.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ Pygments-2.15.1.dist-info
│  │     │  ├─ AUTHORS
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pylab.py
│  │     ├─ pyparsing
│  │     │  ├─ actions.py
│  │     │  ├─ common.py
│  │     │  ├─ core.py
│  │     │  ├─ diagram
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ exceptions.py
│  │     │  ├─ helpers.py
│  │     │  ├─ py.typed
│  │     │  ├─ results.py
│  │     │  ├─ testing.py
│  │     │  ├─ unicode.py
│  │     │  ├─ util.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ actions.cpython-39.pyc
│  │     │     ├─ common.cpython-39.pyc
│  │     │     ├─ core.cpython-39.pyc
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ helpers.cpython-39.pyc
│  │     │     ├─ results.cpython-39.pyc
│  │     │     ├─ testing.cpython-39.pyc
│  │     │     ├─ unicode.cpython-39.pyc
│  │     │     ├─ util.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ pyparsing-3.0.9.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pyrsistent
│  │     │  ├─ py.typed
│  │     │  ├─ typing.py
│  │     │  ├─ typing.pyi
│  │     │  ├─ _checked_types.py
│  │     │  ├─ _field_common.py
│  │     │  ├─ _helpers.py
│  │     │  ├─ _immutable.py
│  │     │  ├─ _pbag.py
│  │     │  ├─ _pclass.py
│  │     │  ├─ _pdeque.py
│  │     │  ├─ _plist.py
│  │     │  ├─ _pmap.py
│  │     │  ├─ _precord.py
│  │     │  ├─ _pset.py
│  │     │  ├─ _pvector.py
│  │     │  ├─ _toolz.py
│  │     │  ├─ _transformations.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  └─ __pycache__
│  │     │     ├─ typing.cpython-39.pyc
│  │     │     ├─ _checked_types.cpython-39.pyc
│  │     │     ├─ _field_common.cpython-39.pyc
│  │     │     ├─ _helpers.cpython-39.pyc
│  │     │     ├─ _immutable.cpython-39.pyc
│  │     │     ├─ _pbag.cpython-39.pyc
│  │     │     ├─ _pclass.cpython-39.pyc
│  │     │     ├─ _pdeque.cpython-39.pyc
│  │     │     ├─ _plist.cpython-39.pyc
│  │     │     ├─ _pmap.cpython-39.pyc
│  │     │     ├─ _precord.cpython-39.pyc
│  │     │     ├─ _pset.cpython-39.pyc
│  │     │     ├─ _pvector.cpython-39.pyc
│  │     │     ├─ _toolz.cpython-39.pyc
│  │     │     ├─ _transformations.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ pyrsistent-0.19.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.mit
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pysnooper
│  │     │  ├─ pycompat.py
│  │     │  ├─ tracer.py
│  │     │  ├─ utils.py
│  │     │  ├─ variables.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ pycompat.cpython-39.pyc
│  │     │     ├─ tracer.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ variables.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ PySnooper-1.1.1.dist-info
│  │     │  ├─ AUTHORS
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pythoncom.py
│  │     ├─ pythonwin
│  │     │  ├─ dde.pyd
│  │     │  ├─ license.txt
│  │     │  ├─ mfc140u.dll
│  │     │  ├─ Pythonwin.exe
│  │     │  ├─ pywin
│  │     │  │  ├─ debugger
│  │     │  │  │  ├─ configui.py
│  │     │  │  │  ├─ dbgcon.py
│  │     │  │  │  ├─ dbgpyapp.py
│  │     │  │  │  ├─ debugger.py
│  │     │  │  │  ├─ fail.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ configui.cpython-39.pyc
│  │     │  │  │     ├─ dbgcon.cpython-39.pyc
│  │     │  │  │     ├─ dbgpyapp.cpython-39.pyc
│  │     │  │  │     ├─ debugger.cpython-39.pyc
│  │     │  │  │     ├─ fail.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ default.cfg
│  │     │  │  ├─ Demos
│  │     │  │  │  ├─ app
│  │     │  │  │  │  ├─ basictimerapp.py
│  │     │  │  │  │  ├─ customprint.py
│  │     │  │  │  │  ├─ demoutils.py
│  │     │  │  │  │  ├─ dlgappdemo.py
│  │     │  │  │  │  ├─ dojobapp.py
│  │     │  │  │  │  ├─ helloapp.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ basictimerapp.cpython-39.pyc
│  │     │  │  │  │     ├─ customprint.cpython-39.pyc
│  │     │  │  │  │     ├─ demoutils.cpython-39.pyc
│  │     │  │  │  │     ├─ dlgappdemo.cpython-39.pyc
│  │     │  │  │  │     ├─ dojobapp.cpython-39.pyc
│  │     │  │  │  │     └─ helloapp.cpython-39.pyc
│  │     │  │  │  ├─ cmdserver.py
│  │     │  │  │  ├─ createwin.py
│  │     │  │  │  ├─ demoutils.py
│  │     │  │  │  ├─ dibdemo.py
│  │     │  │  │  ├─ dlgtest.py
│  │     │  │  │  ├─ dyndlg.py
│  │     │  │  │  ├─ fontdemo.py
│  │     │  │  │  ├─ guidemo.py
│  │     │  │  │  ├─ hiertest.py
│  │     │  │  │  ├─ menutest.py
│  │     │  │  │  ├─ objdoc.py
│  │     │  │  │  ├─ ocx
│  │     │  │  │  │  ├─ demoutils.py
│  │     │  │  │  │  ├─ flash.py
│  │     │  │  │  │  ├─ msoffice.py
│  │     │  │  │  │  ├─ ocxserialtest.py
│  │     │  │  │  │  ├─ ocxtest.py
│  │     │  │  │  │  ├─ webbrowser.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ demoutils.cpython-39.pyc
│  │     │  │  │  │     ├─ flash.cpython-39.pyc
│  │     │  │  │  │     ├─ msoffice.cpython-39.pyc
│  │     │  │  │  │     ├─ ocxserialtest.cpython-39.pyc
│  │     │  │  │  │     ├─ ocxtest.cpython-39.pyc
│  │     │  │  │  │     ├─ webbrowser.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ openGLDemo.py
│  │     │  │  │  ├─ progressbar.py
│  │     │  │  │  ├─ sliderdemo.py
│  │     │  │  │  ├─ splittst.py
│  │     │  │  │  ├─ threadedgui.py
│  │     │  │  │  ├─ toolbar.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cmdserver.cpython-39.pyc
│  │     │  │  │     ├─ createwin.cpython-39.pyc
│  │     │  │  │     ├─ demoutils.cpython-39.pyc
│  │     │  │  │     ├─ dibdemo.cpython-39.pyc
│  │     │  │  │     ├─ dlgtest.cpython-39.pyc
│  │     │  │  │     ├─ dyndlg.cpython-39.pyc
│  │     │  │  │     ├─ fontdemo.cpython-39.pyc
│  │     │  │  │     ├─ guidemo.cpython-39.pyc
│  │     │  │  │     ├─ hiertest.cpython-39.pyc
│  │     │  │  │     ├─ menutest.cpython-39.pyc
│  │     │  │  │     ├─ objdoc.cpython-39.pyc
│  │     │  │  │     ├─ openGLDemo.cpython-39.pyc
│  │     │  │  │     ├─ progressbar.cpython-39.pyc
│  │     │  │  │     ├─ sliderdemo.cpython-39.pyc
│  │     │  │  │     ├─ splittst.cpython-39.pyc
│  │     │  │  │     ├─ threadedgui.cpython-39.pyc
│  │     │  │  │     └─ toolbar.cpython-39.pyc
│  │     │  │  ├─ dialogs
│  │     │  │  │  ├─ ideoptions.py
│  │     │  │  │  ├─ list.py
│  │     │  │  │  ├─ login.py
│  │     │  │  │  ├─ status.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ ideoptions.cpython-39.pyc
│  │     │  │  │     ├─ list.cpython-39.pyc
│  │     │  │  │     ├─ login.cpython-39.pyc
│  │     │  │  │     ├─ status.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ docking
│  │     │  │  │  ├─ DockingBar.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ DockingBar.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ framework
│  │     │  │  │  ├─ app.py
│  │     │  │  │  ├─ bitmap.py
│  │     │  │  │  ├─ cmdline.py
│  │     │  │  │  ├─ dbgcommands.py
│  │     │  │  │  ├─ dlgappcore.py
│  │     │  │  │  ├─ editor
│  │     │  │  │  │  ├─ color
│  │     │  │  │  │  │  ├─ coloreditor.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ coloreditor.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ configui.py
│  │     │  │  │  │  ├─ document.py
│  │     │  │  │  │  ├─ editor.py
│  │     │  │  │  │  ├─ frame.py
│  │     │  │  │  │  ├─ ModuleBrowser.py
│  │     │  │  │  │  ├─ template.py
│  │     │  │  │  │  ├─ vss.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ configui.cpython-39.pyc
│  │     │  │  │  │     ├─ document.cpython-39.pyc
│  │     │  │  │  │     ├─ editor.cpython-39.pyc
│  │     │  │  │  │     ├─ frame.cpython-39.pyc
│  │     │  │  │  │     ├─ ModuleBrowser.cpython-39.pyc
│  │     │  │  │  │     ├─ template.cpython-39.pyc
│  │     │  │  │  │     ├─ vss.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ interact.py
│  │     │  │  │  ├─ intpyapp.py
│  │     │  │  │  ├─ intpydde.py
│  │     │  │  │  ├─ mdi_pychecker.py
│  │     │  │  │  ├─ scriptutils.py
│  │     │  │  │  ├─ sgrepmdi.py
│  │     │  │  │  ├─ startup.py
│  │     │  │  │  ├─ stdin.py
│  │     │  │  │  ├─ toolmenu.py
│  │     │  │  │  ├─ window.py
│  │     │  │  │  ├─ winout.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ app.cpython-39.pyc
│  │     │  │  │     ├─ bitmap.cpython-39.pyc
│  │     │  │  │     ├─ cmdline.cpython-39.pyc
│  │     │  │  │     ├─ dbgcommands.cpython-39.pyc
│  │     │  │  │     ├─ dlgappcore.cpython-39.pyc
│  │     │  │  │     ├─ help.cpython-39.pyc
│  │     │  │  │     ├─ interact.cpython-39.pyc
│  │     │  │  │     ├─ intpyapp.cpython-39.pyc
│  │     │  │  │     ├─ intpydde.cpython-39.pyc
│  │     │  │  │     ├─ mdi_pychecker.cpython-39.pyc
│  │     │  │  │     ├─ scriptutils.cpython-39.pyc
│  │     │  │  │     ├─ sgrepmdi.cpython-39.pyc
│  │     │  │  │     ├─ startup.cpython-39.pyc
│  │     │  │  │     ├─ stdin.cpython-39.pyc
│  │     │  │  │     ├─ toolmenu.cpython-39.pyc
│  │     │  │  │     ├─ window.cpython-39.pyc
│  │     │  │  │     ├─ winout.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ idle
│  │     │  │  │  ├─ AutoExpand.py
│  │     │  │  │  ├─ AutoIndent.py
│  │     │  │  │  ├─ CallTips.py
│  │     │  │  │  ├─ FormatParagraph.py
│  │     │  │  │  ├─ IdleHistory.py
│  │     │  │  │  ├─ PyParse.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ AutoExpand.cpython-39.pyc
│  │     │  │  │     ├─ AutoIndent.cpython-39.pyc
│  │     │  │  │     ├─ CallTips.cpython-39.pyc
│  │     │  │  │     ├─ FormatParagraph.cpython-39.pyc
│  │     │  │  │     ├─ IdleHistory.cpython-39.pyc
│  │     │  │  │     ├─ PyParse.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ IDLE.cfg
│  │     │  │  ├─ mfc
│  │     │  │  │  ├─ activex.py
│  │     │  │  │  ├─ afxres.py
│  │     │  │  │  ├─ dialog.py
│  │     │  │  │  ├─ docview.py
│  │     │  │  │  ├─ object.py
│  │     │  │  │  ├─ thread.py
│  │     │  │  │  ├─ window.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ activex.cpython-39.pyc
│  │     │  │  │     ├─ afxres.cpython-39.pyc
│  │     │  │  │     ├─ dialog.cpython-39.pyc
│  │     │  │  │     ├─ docview.cpython-39.pyc
│  │     │  │  │     ├─ object.cpython-39.pyc
│  │     │  │  │     ├─ thread.cpython-39.pyc
│  │     │  │  │     ├─ window.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ scintilla
│  │     │  │  │  ├─ bindings.py
│  │     │  │  │  ├─ config.py
│  │     │  │  │  ├─ configui.py
│  │     │  │  │  ├─ control.py
│  │     │  │  │  ├─ document.py
│  │     │  │  │  ├─ find.py
│  │     │  │  │  ├─ formatter.py
│  │     │  │  │  ├─ IDLEenvironment.py
│  │     │  │  │  ├─ keycodes.py
│  │     │  │  │  ├─ scintillacon.py
│  │     │  │  │  ├─ view.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bindings.cpython-39.pyc
│  │     │  │  │     ├─ config.cpython-39.pyc
│  │     │  │  │     ├─ configui.cpython-39.pyc
│  │     │  │  │     ├─ control.cpython-39.pyc
│  │     │  │  │     ├─ document.cpython-39.pyc
│  │     │  │  │     ├─ find.cpython-39.pyc
│  │     │  │  │     ├─ formatter.cpython-39.pyc
│  │     │  │  │     ├─ IDLEenvironment.cpython-39.pyc
│  │     │  │  │     ├─ keycodes.cpython-39.pyc
│  │     │  │  │     ├─ scintillacon.cpython-39.pyc
│  │     │  │  │     ├─ view.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ tools
│  │     │  │  │  ├─ browseProjects.py
│  │     │  │  │  ├─ browser.py
│  │     │  │  │  ├─ hierlist.py
│  │     │  │  │  ├─ regedit.py
│  │     │  │  │  ├─ regpy.py
│  │     │  │  │  ├─ TraceCollector.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ browseProjects.cpython-39.pyc
│  │     │  │  │     ├─ browser.cpython-39.pyc
│  │     │  │  │     ├─ hierlist.cpython-39.pyc
│  │     │  │  │     ├─ regedit.cpython-39.pyc
│  │     │  │  │     ├─ regpy.cpython-39.pyc
│  │     │  │  │     ├─ TraceCollector.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ scintilla.dll
│  │     │  ├─ start_pythonwin.pyw
│  │     │  ├─ win32ui.pyd
│  │     │  └─ win32uiole.pyd
│  │     ├─ python_dateutil-2.8.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ pytz
│  │     │  ├─ exceptions.py
│  │     │  ├─ lazy.py
│  │     │  ├─ reference.py
│  │     │  ├─ tzfile.py
│  │     │  ├─ tzinfo.py
│  │     │  ├─ zoneinfo
│  │     │  │  ├─ Africa
│  │     │  │  │  ├─ Abidjan
│  │     │  │  │  ├─ Accra
│  │     │  │  │  ├─ Addis_Ababa
│  │     │  │  │  ├─ Algiers
│  │     │  │  │  ├─ Asmara
│  │     │  │  │  ├─ Asmera
│  │     │  │  │  ├─ Bamako
│  │     │  │  │  ├─ Bangui
│  │     │  │  │  ├─ Banjul
│  │     │  │  │  ├─ Bissau
│  │     │  │  │  ├─ Blantyre
│  │     │  │  │  ├─ Brazzaville
│  │     │  │  │  ├─ Bujumbura
│  │     │  │  │  ├─ Cairo
│  │     │  │  │  ├─ Casablanca
│  │     │  │  │  ├─ Ceuta
│  │     │  │  │  ├─ Conakry
│  │     │  │  │  ├─ Dakar
│  │     │  │  │  ├─ Dar_es_Salaam
│  │     │  │  │  ├─ Djibouti
│  │     │  │  │  ├─ Douala
│  │     │  │  │  ├─ El_Aaiun
│  │     │  │  │  ├─ Freetown
│  │     │  │  │  ├─ Gaborone
│  │     │  │  │  ├─ Harare
│  │     │  │  │  ├─ Johannesburg
│  │     │  │  │  ├─ Juba
│  │     │  │  │  ├─ Kampala
│  │     │  │  │  ├─ Khartoum
│  │     │  │  │  ├─ Kigali
│  │     │  │  │  ├─ Kinshasa
│  │     │  │  │  ├─ Lagos
│  │     │  │  │  ├─ Libreville
│  │     │  │  │  ├─ Lome
│  │     │  │  │  ├─ Luanda
│  │     │  │  │  ├─ Lubumbashi
│  │     │  │  │  ├─ Lusaka
│  │     │  │  │  ├─ Malabo
│  │     │  │  │  ├─ Maputo
│  │     │  │  │  ├─ Maseru
│  │     │  │  │  ├─ Mbabane
│  │     │  │  │  ├─ Mogadishu
│  │     │  │  │  ├─ Monrovia
│  │     │  │  │  ├─ Nairobi
│  │     │  │  │  ├─ Ndjamena
│  │     │  │  │  ├─ Niamey
│  │     │  │  │  ├─ Nouakchott
│  │     │  │  │  ├─ Ouagadougou
│  │     │  │  │  ├─ Porto-Novo
│  │     │  │  │  ├─ Sao_Tome
│  │     │  │  │  ├─ Timbuktu
│  │     │  │  │  ├─ Tripoli
│  │     │  │  │  ├─ Tunis
│  │     │  │  │  └─ Windhoek
│  │     │  │  ├─ America
│  │     │  │  │  ├─ Adak
│  │     │  │  │  ├─ Anchorage
│  │     │  │  │  ├─ Anguilla
│  │     │  │  │  ├─ Antigua
│  │     │  │  │  ├─ Araguaina
│  │     │  │  │  ├─ Argentina
│  │     │  │  │  │  ├─ Buenos_Aires
│  │     │  │  │  │  ├─ Catamarca
│  │     │  │  │  │  ├─ ComodRivadavia
│  │     │  │  │  │  ├─ Cordoba
│  │     │  │  │  │  ├─ Jujuy
│  │     │  │  │  │  ├─ La_Rioja
│  │     │  │  │  │  ├─ Mendoza
│  │     │  │  │  │  ├─ Rio_Gallegos
│  │     │  │  │  │  ├─ Salta
│  │     │  │  │  │  ├─ San_Juan
│  │     │  │  │  │  ├─ San_Luis
│  │     │  │  │  │  ├─ Tucuman
│  │     │  │  │  │  └─ Ushuaia
│  │     │  │  │  ├─ Aruba
│  │     │  │  │  ├─ Asuncion
│  │     │  │  │  ├─ Atikokan
│  │     │  │  │  ├─ Atka
│  │     │  │  │  ├─ Bahia
│  │     │  │  │  ├─ Bahia_Banderas
│  │     │  │  │  ├─ Barbados
│  │     │  │  │  ├─ Belem
│  │     │  │  │  ├─ Belize
│  │     │  │  │  ├─ Blanc-Sablon
│  │     │  │  │  ├─ Boa_Vista
│  │     │  │  │  ├─ Bogota
│  │     │  │  │  ├─ Boise
│  │     │  │  │  ├─ Buenos_Aires
│  │     │  │  │  ├─ Cambridge_Bay
│  │     │  │  │  ├─ Campo_Grande
│  │     │  │  │  ├─ Cancun
│  │     │  │  │  ├─ Caracas
│  │     │  │  │  ├─ Catamarca
│  │     │  │  │  ├─ Cayenne
│  │     │  │  │  ├─ Cayman
│  │     │  │  │  ├─ Chicago
│  │     │  │  │  ├─ Chihuahua
│  │     │  │  │  ├─ Ciudad_Juarez
│  │     │  │  │  ├─ Coral_Harbour
│  │     │  │  │  ├─ Cordoba
│  │     │  │  │  ├─ Costa_Rica
│  │     │  │  │  ├─ Creston
│  │     │  │  │  ├─ Cuiaba
│  │     │  │  │  ├─ Curacao
│  │     │  │  │  ├─ Danmarkshavn
│  │     │  │  │  ├─ Dawson
│  │     │  │  │  ├─ Dawson_Creek
│  │     │  │  │  ├─ Denver
│  │     │  │  │  ├─ Detroit
│  │     │  │  │  ├─ Dominica
│  │     │  │  │  ├─ Edmonton
│  │     │  │  │  ├─ Eirunepe
│  │     │  │  │  ├─ El_Salvador
│  │     │  │  │  ├─ Ensenada
│  │     │  │  │  ├─ Fortaleza
│  │     │  │  │  ├─ Fort_Nelson
│  │     │  │  │  ├─ Fort_Wayne
│  │     │  │  │  ├─ Glace_Bay
│  │     │  │  │  ├─ Godthab
│  │     │  │  │  ├─ Goose_Bay
│  │     │  │  │  ├─ Grand_Turk
│  │     │  │  │  ├─ Grenada
│  │     │  │  │  ├─ Guadeloupe
│  │     │  │  │  ├─ Guatemala
│  │     │  │  │  ├─ Guayaquil
│  │     │  │  │  ├─ Guyana
│  │     │  │  │  ├─ Halifax
│  │     │  │  │  ├─ Havana
│  │     │  │  │  ├─ Hermosillo
│  │     │  │  │  ├─ Indiana
│  │     │  │  │  │  ├─ Indianapolis
│  │     │  │  │  │  ├─ Knox
│  │     │  │  │  │  ├─ Marengo
│  │     │  │  │  │  ├─ Petersburg
│  │     │  │  │  │  ├─ Tell_City
│  │     │  │  │  │  ├─ Vevay
│  │     │  │  │  │  ├─ Vincennes
│  │     │  │  │  │  └─ Winamac
│  │     │  │  │  ├─ Indianapolis
│  │     │  │  │  ├─ Inuvik
│  │     │  │  │  ├─ Iqaluit
│  │     │  │  │  ├─ Jamaica
│  │     │  │  │  ├─ Jujuy
│  │     │  │  │  ├─ Juneau
│  │     │  │  │  ├─ Kentucky
│  │     │  │  │  │  ├─ Louisville
│  │     │  │  │  │  └─ Monticello
│  │     │  │  │  ├─ Knox_IN
│  │     │  │  │  ├─ Kralendijk
│  │     │  │  │  ├─ La_Paz
│  │     │  │  │  ├─ Lima
│  │     │  │  │  ├─ Los_Angeles
│  │     │  │  │  ├─ Louisville
│  │     │  │  │  ├─ Lower_Princes
│  │     │  │  │  ├─ Maceio
│  │     │  │  │  ├─ Managua
│  │     │  │  │  ├─ Manaus
│  │     │  │  │  ├─ Marigot
│  │     │  │  │  ├─ Martinique
│  │     │  │  │  ├─ Matamoros
│  │     │  │  │  ├─ Mazatlan
│  │     │  │  │  ├─ Mendoza
│  │     │  │  │  ├─ Menominee
│  │     │  │  │  ├─ Merida
│  │     │  │  │  ├─ Metlakatla
│  │     │  │  │  ├─ Mexico_City
│  │     │  │  │  ├─ Miquelon
│  │     │  │  │  ├─ Moncton
│  │     │  │  │  ├─ Monterrey
│  │     │  │  │  ├─ Montevideo
│  │     │  │  │  ├─ Montreal
│  │     │  │  │  ├─ Montserrat
│  │     │  │  │  ├─ Nassau
│  │     │  │  │  ├─ New_York
│  │     │  │  │  ├─ Nipigon
│  │     │  │  │  ├─ Nome
│  │     │  │  │  ├─ Noronha
│  │     │  │  │  ├─ North_Dakota
│  │     │  │  │  │  ├─ Beulah
│  │     │  │  │  │  ├─ Center
│  │     │  │  │  │  └─ New_Salem
│  │     │  │  │  ├─ Nuuk
│  │     │  │  │  ├─ Ojinaga
│  │     │  │  │  ├─ Panama
│  │     │  │  │  ├─ Pangnirtung
│  │     │  │  │  ├─ Paramaribo
│  │     │  │  │  ├─ Phoenix
│  │     │  │  │  ├─ Port-au-Prince
│  │     │  │  │  ├─ Porto_Acre
│  │     │  │  │  ├─ Porto_Velho
│  │     │  │  │  ├─ Port_of_Spain
│  │     │  │  │  ├─ Puerto_Rico
│  │     │  │  │  ├─ Punta_Arenas
│  │     │  │  │  ├─ Rainy_River
│  │     │  │  │  ├─ Rankin_Inlet
│  │     │  │  │  ├─ Recife
│  │     │  │  │  ├─ Regina
│  │     │  │  │  ├─ Resolute
│  │     │  │  │  ├─ Rio_Branco
│  │     │  │  │  ├─ Rosario
│  │     │  │  │  ├─ Santarem
│  │     │  │  │  ├─ Santa_Isabel
│  │     │  │  │  ├─ Santiago
│  │     │  │  │  ├─ Santo_Domingo
│  │     │  │  │  ├─ Sao_Paulo
│  │     │  │  │  ├─ Scoresbysund
│  │     │  │  │  ├─ Shiprock
│  │     │  │  │  ├─ Sitka
│  │     │  │  │  ├─ St_Barthelemy
│  │     │  │  │  ├─ St_Johns
│  │     │  │  │  ├─ St_Kitts
│  │     │  │  │  ├─ St_Lucia
│  │     │  │  │  ├─ St_Thomas
│  │     │  │  │  ├─ St_Vincent
│  │     │  │  │  ├─ Swift_Current
│  │     │  │  │  ├─ Tegucigalpa
│  │     │  │  │  ├─ Thule
│  │     │  │  │  ├─ Thunder_Bay
│  │     │  │  │  ├─ Tijuana
│  │     │  │  │  ├─ Toronto
│  │     │  │  │  ├─ Tortola
│  │     │  │  │  ├─ Vancouver
│  │     │  │  │  ├─ Virgin
│  │     │  │  │  ├─ Whitehorse
│  │     │  │  │  ├─ Winnipeg
│  │     │  │  │  ├─ Yakutat
│  │     │  │  │  └─ Yellowknife
│  │     │  │  ├─ Antarctica
│  │     │  │  │  ├─ Casey
│  │     │  │  │  ├─ Davis
│  │     │  │  │  ├─ DumontDUrville
│  │     │  │  │  ├─ Macquarie
│  │     │  │  │  ├─ Mawson
│  │     │  │  │  ├─ McMurdo
│  │     │  │  │  ├─ Palmer
│  │     │  │  │  ├─ Rothera
│  │     │  │  │  ├─ South_Pole
│  │     │  │  │  ├─ Syowa
│  │     │  │  │  ├─ Troll
│  │     │  │  │  └─ Vostok
│  │     │  │  ├─ Arctic
│  │     │  │  │  └─ Longyearbyen
│  │     │  │  ├─ Asia
│  │     │  │  │  ├─ Aden
│  │     │  │  │  ├─ Almaty
│  │     │  │  │  ├─ Amman
│  │     │  │  │  ├─ Anadyr
│  │     │  │  │  ├─ Aqtau
│  │     │  │  │  ├─ Aqtobe
│  │     │  │  │  ├─ Ashgabat
│  │     │  │  │  ├─ Ashkhabad
│  │     │  │  │  ├─ Atyrau
│  │     │  │  │  ├─ Baghdad
│  │     │  │  │  ├─ Bahrain
│  │     │  │  │  ├─ Baku
│  │     │  │  │  ├─ Bangkok
│  │     │  │  │  ├─ Barnaul
│  │     │  │  │  ├─ Beirut
│  │     │  │  │  ├─ Bishkek
│  │     │  │  │  ├─ Brunei
│  │     │  │  │  ├─ Calcutta
│  │     │  │  │  ├─ Chita
│  │     │  │  │  ├─ Choibalsan
│  │     │  │  │  ├─ Chongqing
│  │     │  │  │  ├─ Chungking
│  │     │  │  │  ├─ Colombo
│  │     │  │  │  ├─ Dacca
│  │     │  │  │  ├─ Damascus
│  │     │  │  │  ├─ Dhaka
│  │     │  │  │  ├─ Dili
│  │     │  │  │  ├─ Dubai
│  │     │  │  │  ├─ Dushanbe
│  │     │  │  │  ├─ Famagusta
│  │     │  │  │  ├─ Gaza
│  │     │  │  │  ├─ Harbin
│  │     │  │  │  ├─ Hebron
│  │     │  │  │  ├─ Hong_Kong
│  │     │  │  │  ├─ Hovd
│  │     │  │  │  ├─ Ho_Chi_Minh
│  │     │  │  │  ├─ Irkutsk
│  │     │  │  │  ├─ Istanbul
│  │     │  │  │  ├─ Jakarta
│  │     │  │  │  ├─ Jayapura
│  │     │  │  │  ├─ Jerusalem
│  │     │  │  │  ├─ Kabul
│  │     │  │  │  ├─ Kamchatka
│  │     │  │  │  ├─ Karachi
│  │     │  │  │  ├─ Kashgar
│  │     │  │  │  ├─ Kathmandu
│  │     │  │  │  ├─ Katmandu
│  │     │  │  │  ├─ Khandyga
│  │     │  │  │  ├─ Kolkata
│  │     │  │  │  ├─ Krasnoyarsk
│  │     │  │  │  ├─ Kuala_Lumpur
│  │     │  │  │  ├─ Kuching
│  │     │  │  │  ├─ Kuwait
│  │     │  │  │  ├─ Macao
│  │     │  │  │  ├─ Macau
│  │     │  │  │  ├─ Magadan
│  │     │  │  │  ├─ Makassar
│  │     │  │  │  ├─ Manila
│  │     │  │  │  ├─ Muscat
│  │     │  │  │  ├─ Nicosia
│  │     │  │  │  ├─ Novokuznetsk
│  │     │  │  │  ├─ Novosibirsk
│  │     │  │  │  ├─ Omsk
│  │     │  │  │  ├─ Oral
│  │     │  │  │  ├─ Phnom_Penh
│  │     │  │  │  ├─ Pontianak
│  │     │  │  │  ├─ Pyongyang
│  │     │  │  │  ├─ Qatar
│  │     │  │  │  ├─ Qostanay
│  │     │  │  │  ├─ Qyzylorda
│  │     │  │  │  ├─ Rangoon
│  │     │  │  │  ├─ Riyadh
│  │     │  │  │  ├─ Saigon
│  │     │  │  │  ├─ Sakhalin
│  │     │  │  │  ├─ Samarkand
│  │     │  │  │  ├─ Seoul
│  │     │  │  │  ├─ Shanghai
│  │     │  │  │  ├─ Singapore
│  │     │  │  │  ├─ Srednekolymsk
│  │     │  │  │  ├─ Taipei
│  │     │  │  │  ├─ Tashkent
│  │     │  │  │  ├─ Tbilisi
│  │     │  │  │  ├─ Tehran
│  │     │  │  │  ├─ Tel_Aviv
│  │     │  │  │  ├─ Thimbu
│  │     │  │  │  ├─ Thimphu
│  │     │  │  │  ├─ Tokyo
│  │     │  │  │  ├─ Tomsk
│  │     │  │  │  ├─ Ujung_Pandang
│  │     │  │  │  ├─ Ulaanbaatar
│  │     │  │  │  ├─ Ulan_Bator
│  │     │  │  │  ├─ Urumqi
│  │     │  │  │  ├─ Ust-Nera
│  │     │  │  │  ├─ Vientiane
│  │     │  │  │  ├─ Vladivostok
│  │     │  │  │  ├─ Yakutsk
│  │     │  │  │  ├─ Yangon
│  │     │  │  │  ├─ Yekaterinburg
│  │     │  │  │  └─ Yerevan
│  │     │  │  ├─ Atlantic
│  │     │  │  │  ├─ Azores
│  │     │  │  │  ├─ Bermuda
│  │     │  │  │  ├─ Canary
│  │     │  │  │  ├─ Cape_Verde
│  │     │  │  │  ├─ Faeroe
│  │     │  │  │  ├─ Faroe
│  │     │  │  │  ├─ Jan_Mayen
│  │     │  │  │  ├─ Madeira
│  │     │  │  │  ├─ Reykjavik
│  │     │  │  │  ├─ South_Georgia
│  │     │  │  │  ├─ Stanley
│  │     │  │  │  └─ St_Helena
│  │     │  │  ├─ Australia
│  │     │  │  │  ├─ ACT
│  │     │  │  │  ├─ Adelaide
│  │     │  │  │  ├─ Brisbane
│  │     │  │  │  ├─ Broken_Hill
│  │     │  │  │  ├─ Canberra
│  │     │  │  │  ├─ Currie
│  │     │  │  │  ├─ Darwin
│  │     │  │  │  ├─ Eucla
│  │     │  │  │  ├─ Hobart
│  │     │  │  │  ├─ LHI
│  │     │  │  │  ├─ Lindeman
│  │     │  │  │  ├─ Lord_Howe
│  │     │  │  │  ├─ Melbourne
│  │     │  │  │  ├─ North
│  │     │  │  │  ├─ NSW
│  │     │  │  │  ├─ Perth
│  │     │  │  │  ├─ Queensland
│  │     │  │  │  ├─ South
│  │     │  │  │  ├─ Sydney
│  │     │  │  │  ├─ Tasmania
│  │     │  │  │  ├─ Victoria
│  │     │  │  │  ├─ West
│  │     │  │  │  └─ Yancowinna
│  │     │  │  ├─ Brazil
│  │     │  │  │  ├─ Acre
│  │     │  │  │  ├─ DeNoronha
│  │     │  │  │  ├─ East
│  │     │  │  │  └─ West
│  │     │  │  ├─ Canada
│  │     │  │  │  ├─ Atlantic
│  │     │  │  │  ├─ Central
│  │     │  │  │  ├─ Eastern
│  │     │  │  │  ├─ Mountain
│  │     │  │  │  ├─ Newfoundland
│  │     │  │  │  ├─ Pacific
│  │     │  │  │  ├─ Saskatchewan
│  │     │  │  │  └─ Yukon
│  │     │  │  ├─ CET
│  │     │  │  ├─ Chile
│  │     │  │  │  ├─ Continental
│  │     │  │  │  └─ EasterIsland
│  │     │  │  ├─ CST6CDT
│  │     │  │  ├─ Cuba
│  │     │  │  ├─ EET
│  │     │  │  ├─ Egypt
│  │     │  │  ├─ Eire
│  │     │  │  ├─ EST
│  │     │  │  ├─ EST5EDT
│  │     │  │  ├─ Etc
│  │     │  │  │  ├─ GMT
│  │     │  │  │  ├─ GMT+0
│  │     │  │  │  ├─ GMT+1
│  │     │  │  │  ├─ GMT+10
│  │     │  │  │  ├─ GMT+11
│  │     │  │  │  ├─ GMT+12
│  │     │  │  │  ├─ GMT+2
│  │     │  │  │  ├─ GMT+3
│  │     │  │  │  ├─ GMT+4
│  │     │  │  │  ├─ GMT+5
│  │     │  │  │  ├─ GMT+6
│  │     │  │  │  ├─ GMT+7
│  │     │  │  │  ├─ GMT+8
│  │     │  │  │  ├─ GMT+9
│  │     │  │  │  ├─ GMT-0
│  │     │  │  │  ├─ GMT-1
│  │     │  │  │  ├─ GMT-10
│  │     │  │  │  ├─ GMT-11
│  │     │  │  │  ├─ GMT-12
│  │     │  │  │  ├─ GMT-13
│  │     │  │  │  ├─ GMT-14
│  │     │  │  │  ├─ GMT-2
│  │     │  │  │  ├─ GMT-3
│  │     │  │  │  ├─ GMT-4
│  │     │  │  │  ├─ GMT-5
│  │     │  │  │  ├─ GMT-6
│  │     │  │  │  ├─ GMT-7
│  │     │  │  │  ├─ GMT-8
│  │     │  │  │  ├─ GMT-9
│  │     │  │  │  ├─ GMT0
│  │     │  │  │  ├─ Greenwich
│  │     │  │  │  ├─ UCT
│  │     │  │  │  ├─ Universal
│  │     │  │  │  ├─ UTC
│  │     │  │  │  └─ Zulu
│  │     │  │  ├─ Europe
│  │     │  │  │  ├─ Amsterdam
│  │     │  │  │  ├─ Andorra
│  │     │  │  │  ├─ Astrakhan
│  │     │  │  │  ├─ Athens
│  │     │  │  │  ├─ Belfast
│  │     │  │  │  ├─ Belgrade
│  │     │  │  │  ├─ Berlin
│  │     │  │  │  ├─ Bratislava
│  │     │  │  │  ├─ Brussels
│  │     │  │  │  ├─ Bucharest
│  │     │  │  │  ├─ Budapest
│  │     │  │  │  ├─ Busingen
│  │     │  │  │  ├─ Chisinau
│  │     │  │  │  ├─ Copenhagen
│  │     │  │  │  ├─ Dublin
│  │     │  │  │  ├─ Gibraltar
│  │     │  │  │  ├─ Guernsey
│  │     │  │  │  ├─ Helsinki
│  │     │  │  │  ├─ Isle_of_Man
│  │     │  │  │  ├─ Istanbul
│  │     │  │  │  ├─ Jersey
│  │     │  │  │  ├─ Kaliningrad
│  │     │  │  │  ├─ Kiev
│  │     │  │  │  ├─ Kirov
│  │     │  │  │  ├─ Kyiv
│  │     │  │  │  ├─ Lisbon
│  │     │  │  │  ├─ Ljubljana
│  │     │  │  │  ├─ London
│  │     │  │  │  ├─ Luxembourg
│  │     │  │  │  ├─ Madrid
│  │     │  │  │  ├─ Malta
│  │     │  │  │  ├─ Mariehamn
│  │     │  │  │  ├─ Minsk
│  │     │  │  │  ├─ Monaco
│  │     │  │  │  ├─ Moscow
│  │     │  │  │  ├─ Nicosia
│  │     │  │  │  ├─ Oslo
│  │     │  │  │  ├─ Paris
│  │     │  │  │  ├─ Podgorica
│  │     │  │  │  ├─ Prague
│  │     │  │  │  ├─ Riga
│  │     │  │  │  ├─ Rome
│  │     │  │  │  ├─ Samara
│  │     │  │  │  ├─ San_Marino
│  │     │  │  │  ├─ Sarajevo
│  │     │  │  │  ├─ Saratov
│  │     │  │  │  ├─ Simferopol
│  │     │  │  │  ├─ Skopje
│  │     │  │  │  ├─ Sofia
│  │     │  │  │  ├─ Stockholm
│  │     │  │  │  ├─ Tallinn
│  │     │  │  │  ├─ Tirane
│  │     │  │  │  ├─ Tiraspol
│  │     │  │  │  ├─ Ulyanovsk
│  │     │  │  │  ├─ Uzhgorod
│  │     │  │  │  ├─ Vaduz
│  │     │  │  │  ├─ Vatican
│  │     │  │  │  ├─ Vienna
│  │     │  │  │  ├─ Vilnius
│  │     │  │  │  ├─ Volgograd
│  │     │  │  │  ├─ Warsaw
│  │     │  │  │  ├─ Zagreb
│  │     │  │  │  ├─ Zaporozhye
│  │     │  │  │  └─ Zurich
│  │     │  │  ├─ Factory
│  │     │  │  ├─ GB
│  │     │  │  ├─ GB-Eire
│  │     │  │  ├─ GMT
│  │     │  │  ├─ GMT+0
│  │     │  │  ├─ GMT-0
│  │     │  │  ├─ GMT0
│  │     │  │  ├─ Greenwich
│  │     │  │  ├─ Hongkong
│  │     │  │  ├─ HST
│  │     │  │  ├─ Iceland
│  │     │  │  ├─ Indian
│  │     │  │  │  ├─ Antananarivo
│  │     │  │  │  ├─ Chagos
│  │     │  │  │  ├─ Christmas
│  │     │  │  │  ├─ Cocos
│  │     │  │  │  ├─ Comoro
│  │     │  │  │  ├─ Kerguelen
│  │     │  │  │  ├─ Mahe
│  │     │  │  │  ├─ Maldives
│  │     │  │  │  ├─ Mauritius
│  │     │  │  │  ├─ Mayotte
│  │     │  │  │  └─ Reunion
│  │     │  │  ├─ Iran
│  │     │  │  ├─ iso3166.tab
│  │     │  │  ├─ Israel
│  │     │  │  ├─ Jamaica
│  │     │  │  ├─ Japan
│  │     │  │  ├─ Kwajalein
│  │     │  │  ├─ leapseconds
│  │     │  │  ├─ Libya
│  │     │  │  ├─ MET
│  │     │  │  ├─ Mexico
│  │     │  │  │  ├─ BajaNorte
│  │     │  │  │  ├─ BajaSur
│  │     │  │  │  └─ General
│  │     │  │  ├─ MST
│  │     │  │  ├─ MST7MDT
│  │     │  │  ├─ Navajo
│  │     │  │  ├─ NZ
│  │     │  │  ├─ NZ-CHAT
│  │     │  │  ├─ Pacific
│  │     │  │  │  ├─ Apia
│  │     │  │  │  ├─ Auckland
│  │     │  │  │  ├─ Bougainville
│  │     │  │  │  ├─ Chatham
│  │     │  │  │  ├─ Chuuk
│  │     │  │  │  ├─ Easter
│  │     │  │  │  ├─ Efate
│  │     │  │  │  ├─ Enderbury
│  │     │  │  │  ├─ Fakaofo
│  │     │  │  │  ├─ Fiji
│  │     │  │  │  ├─ Funafuti
│  │     │  │  │  ├─ Galapagos
│  │     │  │  │  ├─ Gambier
│  │     │  │  │  ├─ Guadalcanal
│  │     │  │  │  ├─ Guam
│  │     │  │  │  ├─ Honolulu
│  │     │  │  │  ├─ Johnston
│  │     │  │  │  ├─ Kanton
│  │     │  │  │  ├─ Kiritimati
│  │     │  │  │  ├─ Kosrae
│  │     │  │  │  ├─ Kwajalein
│  │     │  │  │  ├─ Majuro
│  │     │  │  │  ├─ Marquesas
│  │     │  │  │  ├─ Midway
│  │     │  │  │  ├─ Nauru
│  │     │  │  │  ├─ Niue
│  │     │  │  │  ├─ Norfolk
│  │     │  │  │  ├─ Noumea
│  │     │  │  │  ├─ Pago_Pago
│  │     │  │  │  ├─ Palau
│  │     │  │  │  ├─ Pitcairn
│  │     │  │  │  ├─ Pohnpei
│  │     │  │  │  ├─ Ponape
│  │     │  │  │  ├─ Port_Moresby
│  │     │  │  │  ├─ Rarotonga
│  │     │  │  │  ├─ Saipan
│  │     │  │  │  ├─ Samoa
│  │     │  │  │  ├─ Tahiti
│  │     │  │  │  ├─ Tarawa
│  │     │  │  │  ├─ Tongatapu
│  │     │  │  │  ├─ Truk
│  │     │  │  │  ├─ Wake
│  │     │  │  │  ├─ Wallis
│  │     │  │  │  └─ Yap
│  │     │  │  ├─ Poland
│  │     │  │  ├─ Portugal
│  │     │  │  ├─ PRC
│  │     │  │  ├─ PST8PDT
│  │     │  │  ├─ ROC
│  │     │  │  ├─ ROK
│  │     │  │  ├─ Singapore
│  │     │  │  ├─ Turkey
│  │     │  │  ├─ tzdata.zi
│  │     │  │  ├─ UCT
│  │     │  │  ├─ Universal
│  │     │  │  ├─ US
│  │     │  │  │  ├─ Alaska
│  │     │  │  │  ├─ Aleutian
│  │     │  │  │  ├─ Arizona
│  │     │  │  │  ├─ Central
│  │     │  │  │  ├─ East-Indiana
│  │     │  │  │  ├─ Eastern
│  │     │  │  │  ├─ Hawaii
│  │     │  │  │  ├─ Indiana-Starke
│  │     │  │  │  ├─ Michigan
│  │     │  │  │  ├─ Mountain
│  │     │  │  │  ├─ Pacific
│  │     │  │  │  └─ Samoa
│  │     │  │  ├─ UTC
│  │     │  │  ├─ W-SU
│  │     │  │  ├─ WET
│  │     │  │  ├─ zone.tab
│  │     │  │  ├─ zone1970.tab
│  │     │  │  └─ Zulu
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ lazy.cpython-39.pyc
│  │     │     ├─ reference.cpython-39.pyc
│  │     │     ├─ tzfile.cpython-39.pyc
│  │     │     ├─ tzinfo.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ pytz-2023.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ pywin32-306.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ PyWin32.chm
│  │     ├─ pywin32.pth
│  │     ├─ pywin32.version.txt
│  │     ├─ pywin32_system32
│  │     │  ├─ pythoncom39.dll
│  │     │  └─ pywintypes39.dll
│  │     ├─ PyYAML-6.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pyzmq-25.0.2.dist-info
│  │     │  ├─ AUTHORS.md
│  │     │  ├─ DELVEWHEEL
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.BSD
│  │     │  ├─ LICENSE.LESSER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pyzmq.libs
│  │     │  ├─ .load-order-pyzmq-25.0.2
│  │     │  ├─ concrt140.dll
│  │     │  ├─ libsodium-ac42d648.dll
│  │     │  ├─ libzmq-v141-mt-4_3_4-0a6f51ca.dll
│  │     │  └─ msvcp140.dll
│  │     ├─ requests
│  │     │  ├─ adapters.py
│  │     │  ├─ api.py
│  │     │  ├─ auth.py
│  │     │  ├─ certs.py
│  │     │  ├─ compat.py
│  │     │  ├─ cookies.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ help.py
│  │     │  ├─ models.py
│  │     │  ├─ packages.py
│  │     │  ├─ sessions.py
│  │     │  ├─ status_codes.py
│  │     │  ├─ structures.py
│  │     │  ├─ utils.py
│  │     │  ├─ _internal_utils.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __pycache__
│  │     │  │  ├─ adapters.cpython-39.pyc
│  │     │  │  ├─ api.cpython-39.pyc
│  │     │  │  ├─ auth.cpython-39.pyc
│  │     │  │  ├─ certs.cpython-39.pyc
│  │     │  │  ├─ compat.cpython-39.pyc
│  │     │  │  ├─ cookies.cpython-39.pyc
│  │     │  │  ├─ exceptions.cpython-39.pyc
│  │     │  │  ├─ help.cpython-39.pyc
│  │     │  │  ├─ models.cpython-39.pyc
│  │     │  │  ├─ packages.cpython-39.pyc
│  │     │  │  ├─ sessions.cpython-39.pyc
│  │     │  │  ├─ status_codes.cpython-39.pyc
│  │     │  │  ├─ structures.cpython-39.pyc
│  │     │  │  ├─ utils.cpython-39.pyc
│  │     │  │  ├─ _internal_utils.cpython-39.pyc
│  │     │  │  ├─ __init__.cpython-39.pyc
│  │     │  │  └─ __version__.cpython-39.pyc
│  │     │  └─ __version__.py
│  │     ├─ requests-2.29.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ ruamel
│  │     │  └─ yaml
│  │     │     ├─ anchor.py
│  │     │     ├─ comments.py
│  │     │     ├─ compat.py
│  │     │     ├─ composer.py
│  │     │     ├─ configobjwalker.py
│  │     │     ├─ constructor.py
│  │     │     ├─ cyaml.py
│  │     │     ├─ dumper.py
│  │     │     ├─ emitter.py
│  │     │     ├─ error.py
│  │     │     ├─ events.py
│  │     │     ├─ loader.py
│  │     │     ├─ main.py
│  │     │     ├─ nodes.py
│  │     │     ├─ parser.py
│  │     │     ├─ py.typed
│  │     │     ├─ reader.py
│  │     │     ├─ representer.py
│  │     │     ├─ resolver.py
│  │     │     ├─ scalarbool.py
│  │     │     ├─ scalarfloat.py
│  │     │     ├─ scalarint.py
│  │     │     ├─ scalarstring.py
│  │     │     ├─ scanner.py
│  │     │     ├─ serializer.py
│  │     │     ├─ timestamp.py
│  │     │     ├─ tokens.py
│  │     │     ├─ util.py
│  │     │     ├─ __init__.py
│  │     │     └─ __pycache__
│  │     │        ├─ anchor.cpython-39.pyc
│  │     │        ├─ comments.cpython-39.pyc
│  │     │        ├─ compat.cpython-39.pyc
│  │     │        ├─ composer.cpython-39.pyc
│  │     │        ├─ configobjwalker.cpython-39.pyc
│  │     │        ├─ constructor.cpython-39.pyc
│  │     │        ├─ cyaml.cpython-39.pyc
│  │     │        ├─ dumper.cpython-39.pyc
│  │     │        ├─ emitter.cpython-39.pyc
│  │     │        ├─ error.cpython-39.pyc
│  │     │        ├─ events.cpython-39.pyc
│  │     │        ├─ loader.cpython-39.pyc
│  │     │        ├─ main.cpython-39.pyc
│  │     │        ├─ nodes.cpython-39.pyc
│  │     │        ├─ parser.cpython-39.pyc
│  │     │        ├─ reader.cpython-39.pyc
│  │     │        ├─ representer.cpython-39.pyc
│  │     │        ├─ resolver.cpython-39.pyc
│  │     │        ├─ scalarbool.cpython-39.pyc
│  │     │        ├─ scalarfloat.cpython-39.pyc
│  │     │        ├─ scalarint.cpython-39.pyc
│  │     │        ├─ scalarstring.cpython-39.pyc
│  │     │        ├─ scanner.cpython-39.pyc
│  │     │        ├─ serializer.cpython-39.pyc
│  │     │        ├─ timestamp.cpython-39.pyc
│  │     │        ├─ tokens.cpython-39.pyc
│  │     │        ├─ util.cpython-39.pyc
│  │     │        └─ __init__.cpython-39.pyc
│  │     ├─ ruamel.yaml-0.17.21-py3.9-nspkg.pth
│  │     ├─ ruamel.yaml-0.17.21.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ namespace_packages.txt
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ ruamel.yaml.clib-0.2.7.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ namespace_packages.txt
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ scikit_learn-1.2.2.dist-info
│  │     │  ├─ COPYING
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ scipy
│  │     │  ├─ cluster
│  │     │  │  ├─ hierarchy.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ hierarchy_test_data.py
│  │     │  │  │  ├─ test_disjoint_set.py
│  │     │  │  │  ├─ test_hierarchy.py
│  │     │  │  │  ├─ test_vq.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ hierarchy_test_data.cpython-39.pyc
│  │     │  │  │     ├─ test_disjoint_set.cpython-39.pyc
│  │     │  │  │     ├─ test_hierarchy.cpython-39.pyc
│  │     │  │  │     ├─ test_vq.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ vq.py
│  │     │  │  ├─ _hierarchy.cp39-win_amd64.dll.a
│  │     │  │  ├─ _hierarchy.cp39-win_amd64.pyd
│  │     │  │  ├─ _optimal_leaf_ordering.cp39-win_amd64.dll.a
│  │     │  │  ├─ _optimal_leaf_ordering.cp39-win_amd64.pyd
│  │     │  │  ├─ _vq.cp39-win_amd64.dll.a
│  │     │  │  ├─ _vq.cp39-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ hierarchy.cpython-39.pyc
│  │     │  │     ├─ vq.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ conftest.py
│  │     │  ├─ constants
│  │     │  │  ├─ codata.py
│  │     │  │  ├─ constants.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_codata.py
│  │     │  │  │  ├─ test_constants.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_codata.cpython-39.pyc
│  │     │  │  │     ├─ test_constants.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _codata.py
│  │     │  │  ├─ _constants.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ codata.cpython-39.pyc
│  │     │  │     ├─ constants.cpython-39.pyc
│  │     │  │     ├─ _codata.cpython-39.pyc
│  │     │  │     ├─ _constants.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ datasets
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_data.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_data.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _download_all.py
│  │     │  │  ├─ _fetchers.py
│  │     │  │  ├─ _registry.py
│  │     │  │  ├─ _utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _download_all.cpython-39.pyc
│  │     │  │     ├─ _fetchers.cpython-39.pyc
│  │     │  │     ├─ _registry.cpython-39.pyc
│  │     │  │     ├─ _utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ fft
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ mock_backend.py
│  │     │  │  │  ├─ test_backend.py
│  │     │  │  │  ├─ test_fftlog.py
│  │     │  │  │  ├─ test_fft_function.py
│  │     │  │  │  ├─ test_helper.py
│  │     │  │  │  ├─ test_multithreading.py
│  │     │  │  │  ├─ test_numpy.py
│  │     │  │  │  ├─ test_real_transforms.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ mock_backend.cpython-39.pyc
│  │     │  │  │     ├─ test_backend.cpython-39.pyc
│  │     │  │  │     ├─ test_fftlog.cpython-39.pyc
│  │     │  │  │     ├─ test_fft_function.cpython-39.pyc
│  │     │  │  │     ├─ test_helper.cpython-39.pyc
│  │     │  │  │     ├─ test_multithreading.cpython-39.pyc
│  │     │  │  │     ├─ test_numpy.cpython-39.pyc
│  │     │  │  │     ├─ test_real_transforms.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _backend.py
│  │     │  │  ├─ _basic.py
│  │     │  │  ├─ _debug_backends.py
│  │     │  │  ├─ _fftlog.py
│  │     │  │  ├─ _fftlog_multimethods.py
│  │     │  │  ├─ _helper.py
│  │     │  │  ├─ _pocketfft
│  │     │  │  │  ├─ basic.py
│  │     │  │  │  ├─ helper.py
│  │     │  │  │  ├─ LICENSE.md
│  │     │  │  │  ├─ pypocketfft.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ pypocketfft.cp39-win_amd64.pyd
│  │     │  │  │  ├─ realtransforms.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ test_basic.py
│  │     │  │  │  │  ├─ test_real_transforms.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_basic.cpython-39.pyc
│  │     │  │  │  │     ├─ test_real_transforms.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ basic.cpython-39.pyc
│  │     │  │  │     ├─ helper.cpython-39.pyc
│  │     │  │  │     ├─ realtransforms.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _realtransforms.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _backend.cpython-39.pyc
│  │     │  │     ├─ _basic.cpython-39.pyc
│  │     │  │     ├─ _debug_backends.cpython-39.pyc
│  │     │  │     ├─ _fftlog.cpython-39.pyc
│  │     │  │     ├─ _fftlog_multimethods.cpython-39.pyc
│  │     │  │     ├─ _helper.cpython-39.pyc
│  │     │  │     ├─ _realtransforms.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ fftpack
│  │     │  │  ├─ basic.py
│  │     │  │  ├─ convolve.cp39-win_amd64.dll.a
│  │     │  │  ├─ convolve.cp39-win_amd64.pyd
│  │     │  │  ├─ helper.py
│  │     │  │  ├─ pseudo_diffs.py
│  │     │  │  ├─ realtransforms.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ fftw_double_ref.npz
│  │     │  │  │  ├─ fftw_longdouble_ref.npz
│  │     │  │  │  ├─ fftw_single_ref.npz
│  │     │  │  │  ├─ test.npz
│  │     │  │  │  ├─ test_basic.py
│  │     │  │  │  ├─ test_helper.py
│  │     │  │  │  ├─ test_import.py
│  │     │  │  │  ├─ test_pseudo_diffs.py
│  │     │  │  │  ├─ test_real_transforms.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_basic.cpython-39.pyc
│  │     │  │  │     ├─ test_helper.cpython-39.pyc
│  │     │  │  │     ├─ test_import.cpython-39.pyc
│  │     │  │  │     ├─ test_pseudo_diffs.cpython-39.pyc
│  │     │  │  │     ├─ test_real_transforms.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _basic.py
│  │     │  │  ├─ _helper.py
│  │     │  │  ├─ _pseudo_diffs.py
│  │     │  │  ├─ _realtransforms.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ basic.cpython-39.pyc
│  │     │  │     ├─ helper.cpython-39.pyc
│  │     │  │     ├─ pseudo_diffs.cpython-39.pyc
│  │     │  │     ├─ realtransforms.cpython-39.pyc
│  │     │  │     ├─ _basic.cpython-39.pyc
│  │     │  │     ├─ _helper.cpython-39.pyc
│  │     │  │     ├─ _pseudo_diffs.cpython-39.pyc
│  │     │  │     ├─ _realtransforms.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ integrate
│  │     │  │  ├─ dop.py
│  │     │  │  ├─ lsoda.py
│  │     │  │  ├─ odepack.py
│  │     │  │  ├─ quadpack.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_banded_ode_solvers.py
│  │     │  │  │  ├─ test_bvp.py
│  │     │  │  │  ├─ test_integrate.py
│  │     │  │  │  ├─ test_odeint_jac.py
│  │     │  │  │  ├─ test_quadpack.py
│  │     │  │  │  ├─ test_quadrature.py
│  │     │  │  │  ├─ test__quad_vec.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_banded_ode_solvers.cpython-39.pyc
│  │     │  │  │     ├─ test_bvp.cpython-39.pyc
│  │     │  │  │     ├─ test_integrate.cpython-39.pyc
│  │     │  │  │     ├─ test_odeint_jac.cpython-39.pyc
│  │     │  │  │     ├─ test_quadpack.cpython-39.pyc
│  │     │  │  │     ├─ test_quadrature.cpython-39.pyc
│  │     │  │  │     ├─ test__quad_vec.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ vode.py
│  │     │  │  ├─ _bvp.py
│  │     │  │  ├─ _dop.cp39-win_amd64.dll.a
│  │     │  │  ├─ _dop.cp39-win_amd64.pyd
│  │     │  │  ├─ _ivp
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ bdf.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ dop853_coefficients.py
│  │     │  │  │  ├─ ivp.py
│  │     │  │  │  ├─ lsoda.py
│  │     │  │  │  ├─ radau.py
│  │     │  │  │  ├─ rk.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ test_ivp.py
│  │     │  │  │  │  ├─ test_rk.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_ivp.cpython-39.pyc
│  │     │  │  │  │     ├─ test_rk.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ bdf.cpython-39.pyc
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ dop853_coefficients.cpython-39.pyc
│  │     │  │  │     ├─ ivp.cpython-39.pyc
│  │     │  │  │     ├─ lsoda.cpython-39.pyc
│  │     │  │  │     ├─ radau.cpython-39.pyc
│  │     │  │  │     ├─ rk.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _lsoda.cp39-win_amd64.dll.a
│  │     │  │  ├─ _lsoda.cp39-win_amd64.pyd
│  │     │  │  ├─ _ode.py
│  │     │  │  ├─ _odepack.cp39-win_amd64.dll.a
│  │     │  │  ├─ _odepack.cp39-win_amd64.pyd
│  │     │  │  ├─ _odepack_py.py
│  │     │  │  ├─ _quadpack.cp39-win_amd64.dll.a
│  │     │  │  ├─ _quadpack.cp39-win_amd64.pyd
│  │     │  │  ├─ _quadpack_py.py
│  │     │  │  ├─ _quadrature.py
│  │     │  │  ├─ _quad_vec.py
│  │     │  │  ├─ _test_multivariate.cp39-win_amd64.dll.a
│  │     │  │  ├─ _test_multivariate.cp39-win_amd64.pyd
│  │     │  │  ├─ _test_odeint_banded.cp39-win_amd64.dll.a
│  │     │  │  ├─ _test_odeint_banded.cp39-win_amd64.pyd
│  │     │  │  ├─ _vode.cp39-win_amd64.dll.a
│  │     │  │  ├─ _vode.cp39-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ dop.cpython-39.pyc
│  │     │  │     ├─ lsoda.cpython-39.pyc
│  │     │  │     ├─ odepack.cpython-39.pyc
│  │     │  │     ├─ quadpack.cpython-39.pyc
│  │     │  │     ├─ vode.cpython-39.pyc
│  │     │  │     ├─ _bvp.cpython-39.pyc
│  │     │  │     ├─ _ode.cpython-39.pyc
│  │     │  │     ├─ _odepack_py.cpython-39.pyc
│  │     │  │     ├─ _quadpack_py.cpython-39.pyc
│  │     │  │     ├─ _quadrature.cpython-39.pyc
│  │     │  │     ├─ _quad_vec.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ interpolate
│  │     │  │  ├─ dfitpack.cp39-win_amd64.dll.a
│  │     │  │  ├─ dfitpack.cp39-win_amd64.pyd
│  │     │  │  ├─ fitpack.py
│  │     │  │  ├─ fitpack2.py
│  │     │  │  ├─ interpnd.cp39-win_amd64.dll.a
│  │     │  │  ├─ interpnd.cp39-win_amd64.pyd
│  │     │  │  ├─ interpolate.py
│  │     │  │  ├─ ndgriddata.py
│  │     │  │  ├─ polyint.py
│  │     │  │  ├─ rbf.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ bug-1310.npz
│  │     │  │  │  │  ├─ estimate_gradients_hang.npy
│  │     │  │  │  │  └─ gcvspl.npz
│  │     │  │  │  ├─ test_bsplines.py
│  │     │  │  │  ├─ test_fitpack.py
│  │     │  │  │  ├─ test_fitpack2.py
│  │     │  │  │  ├─ test_gil.py
│  │     │  │  │  ├─ test_interpnd.py
│  │     │  │  │  ├─ test_interpolate.py
│  │     │  │  │  ├─ test_ndgriddata.py
│  │     │  │  │  ├─ test_pade.py
│  │     │  │  │  ├─ test_polyint.py
│  │     │  │  │  ├─ test_rbf.py
│  │     │  │  │  ├─ test_rbfinterp.py
│  │     │  │  │  ├─ test_rgi.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_bsplines.cpython-39.pyc
│  │     │  │  │     ├─ test_fitpack.cpython-39.pyc
│  │     │  │  │     ├─ test_fitpack2.cpython-39.pyc
│  │     │  │  │     ├─ test_gil.cpython-39.pyc
│  │     │  │  │     ├─ test_interpnd.cpython-39.pyc
│  │     │  │  │     ├─ test_interpolate.cpython-39.pyc
│  │     │  │  │     ├─ test_ndgriddata.cpython-39.pyc
│  │     │  │  │     ├─ test_pade.cpython-39.pyc
│  │     │  │  │     ├─ test_polyint.cpython-39.pyc
│  │     │  │  │     ├─ test_rbf.cpython-39.pyc
│  │     │  │  │     ├─ test_rbfinterp.cpython-39.pyc
│  │     │  │  │     ├─ test_rgi.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _bspl.cp39-win_amd64.dll.a
│  │     │  │  ├─ _bspl.cp39-win_amd64.pyd
│  │     │  │  ├─ _bsplines.py
│  │     │  │  ├─ _cubic.py
│  │     │  │  ├─ _fitpack.cp39-win_amd64.dll.a
│  │     │  │  ├─ _fitpack.cp39-win_amd64.pyd
│  │     │  │  ├─ _fitpack2.py
│  │     │  │  ├─ _fitpack_impl.py
│  │     │  │  ├─ _fitpack_py.py
│  │     │  │  ├─ _interpnd_info.py
│  │     │  │  ├─ _interpolate.py
│  │     │  │  ├─ _ndgriddata.py
│  │     │  │  ├─ _pade.py
│  │     │  │  ├─ _polyint.py
│  │     │  │  ├─ _ppoly.cp39-win_amd64.dll.a
│  │     │  │  ├─ _ppoly.cp39-win_amd64.pyd
│  │     │  │  ├─ _rbf.py
│  │     │  │  ├─ _rbfinterp.py
│  │     │  │  ├─ _rbfinterp_pythran.cp39-win_amd64.dll.a
│  │     │  │  ├─ _rbfinterp_pythran.cp39-win_amd64.pyd
│  │     │  │  ├─ _rgi.py
│  │     │  │  ├─ _rgi_cython.cp39-win_amd64.dll.a
│  │     │  │  ├─ _rgi_cython.cp39-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ fitpack.cpython-39.pyc
│  │     │  │     ├─ fitpack2.cpython-39.pyc
│  │     │  │     ├─ interpolate.cpython-39.pyc
│  │     │  │     ├─ ndgriddata.cpython-39.pyc
│  │     │  │     ├─ polyint.cpython-39.pyc
│  │     │  │     ├─ rbf.cpython-39.pyc
│  │     │  │     ├─ _bsplines.cpython-39.pyc
│  │     │  │     ├─ _cubic.cpython-39.pyc
│  │     │  │     ├─ _fitpack2.cpython-39.pyc
│  │     │  │     ├─ _fitpack_impl.cpython-39.pyc
│  │     │  │     ├─ _fitpack_py.cpython-39.pyc
│  │     │  │     ├─ _interpnd_info.cpython-39.pyc
│  │     │  │     ├─ _interpolate.cpython-39.pyc
│  │     │  │     ├─ _ndgriddata.cpython-39.pyc
│  │     │  │     ├─ _pade.cpython-39.pyc
│  │     │  │     ├─ _polyint.cpython-39.pyc
│  │     │  │     ├─ _rbf.cpython-39.pyc
│  │     │  │     ├─ _rbfinterp.cpython-39.pyc
│  │     │  │     ├─ _rgi.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ io
│  │     │  │  ├─ arff
│  │     │  │  │  ├─ arffread.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ data
│  │     │  │  │  │  │  ├─ iris.arff
│  │     │  │  │  │  │  ├─ missing.arff
│  │     │  │  │  │  │  ├─ nodata.arff
│  │     │  │  │  │  │  ├─ quoted_nominal.arff
│  │     │  │  │  │  │  ├─ quoted_nominal_spaces.arff
│  │     │  │  │  │  │  ├─ test1.arff
│  │     │  │  │  │  │  ├─ test10.arff
│  │     │  │  │  │  │  ├─ test11.arff
│  │     │  │  │  │  │  ├─ test2.arff
│  │     │  │  │  │  │  ├─ test3.arff
│  │     │  │  │  │  │  ├─ test4.arff
│  │     │  │  │  │  │  ├─ test5.arff
│  │     │  │  │  │  │  ├─ test6.arff
│  │     │  │  │  │  │  ├─ test7.arff
│  │     │  │  │  │  │  ├─ test8.arff
│  │     │  │  │  │  │  └─ test9.arff
│  │     │  │  │  │  ├─ test_arffread.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_arffread.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _arffread.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ arffread.cpython-39.pyc
│  │     │  │  │     ├─ _arffread.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ harwell_boeing.py
│  │     │  │  ├─ idl.py
│  │     │  │  ├─ matlab
│  │     │  │  │  ├─ byteordercodes.py
│  │     │  │  │  ├─ mio.py
│  │     │  │  │  ├─ mio4.py
│  │     │  │  │  ├─ mio5.py
│  │     │  │  │  ├─ mio5_params.py
│  │     │  │  │  ├─ mio5_utils.py
│  │     │  │  │  ├─ miobase.py
│  │     │  │  │  ├─ mio_utils.py
│  │     │  │  │  ├─ streams.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ data
│  │     │  │  │  │  │  ├─ bad_miuint32.mat
│  │     │  │  │  │  │  ├─ bad_miutf8_array_name.mat
│  │     │  │  │  │  │  ├─ big_endian.mat
│  │     │  │  │  │  │  ├─ broken_utf8.mat
│  │     │  │  │  │  │  ├─ corrupted_zlib_checksum.mat
│  │     │  │  │  │  │  ├─ corrupted_zlib_data.mat
│  │     │  │  │  │  │  ├─ japanese_utf8.txt
│  │     │  │  │  │  │  ├─ little_endian.mat
│  │     │  │  │  │  │  ├─ logical_sparse.mat
│  │     │  │  │  │  │  ├─ malformed1.mat
│  │     │  │  │  │  │  ├─ miuint32_for_miint32.mat
│  │     │  │  │  │  │  ├─ miutf8_array_name.mat
│  │     │  │  │  │  │  ├─ nasty_duplicate_fieldnames.mat
│  │     │  │  │  │  │  ├─ one_by_zero_char.mat
│  │     │  │  │  │  │  ├─ parabola.mat
│  │     │  │  │  │  │  ├─ single_empty_string.mat
│  │     │  │  │  │  │  ├─ some_functions.mat
│  │     │  │  │  │  │  ├─ sqr.mat
│  │     │  │  │  │  │  ├─ test3dmatrix_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ test3dmatrix_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ test3dmatrix_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ test3dmatrix_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testbool_8_WIN64.mat
│  │     │  │  │  │  │  ├─ testcellnest_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ testcellnest_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testcellnest_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testcellnest_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testcell_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ testcell_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testcell_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testcell_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testcomplex_4.2c_SOL2.mat
│  │     │  │  │  │  │  ├─ testcomplex_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ testcomplex_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testcomplex_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testcomplex_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testdouble_4.2c_SOL2.mat
│  │     │  │  │  │  │  ├─ testdouble_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ testdouble_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testdouble_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testdouble_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testemptycell_5.3_SOL2.mat
│  │     │  │  │  │  │  ├─ testemptycell_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testemptycell_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testemptycell_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testfunc_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testhdf5_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testmatrix_4.2c_SOL2.mat
│  │     │  │  │  │  │  ├─ testmatrix_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ testmatrix_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testmatrix_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testmatrix_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testminus_4.2c_SOL2.mat
│  │     │  │  │  │  │  ├─ testminus_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ testminus_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testminus_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testminus_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testmulti_4.2c_SOL2.mat
│  │     │  │  │  │  │  ├─ testmulti_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testmulti_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testobject_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ testobject_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testobject_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testobject_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testonechar_4.2c_SOL2.mat
│  │     │  │  │  │  │  ├─ testonechar_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ testonechar_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testonechar_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testonechar_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testscalarcell_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testsimplecell.mat
│  │     │  │  │  │  │  ├─ testsparsecomplex_4.2c_SOL2.mat
│  │     │  │  │  │  │  ├─ testsparsecomplex_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ testsparsecomplex_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testsparsecomplex_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testsparsecomplex_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testsparsefloat_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testsparse_4.2c_SOL2.mat
│  │     │  │  │  │  │  ├─ testsparse_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ testsparse_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testsparse_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testsparse_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststringarray_4.2c_SOL2.mat
│  │     │  │  │  │  │  ├─ teststringarray_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ teststringarray_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststringarray_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststringarray_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststring_4.2c_SOL2.mat
│  │     │  │  │  │  │  ├─ teststring_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ teststring_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststring_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststring_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststructarr_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ teststructarr_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststructarr_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststructarr_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststructnest_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ teststructnest_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststructnest_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststructnest_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststruct_6.1_SOL2.mat
│  │     │  │  │  │  │  ├─ teststruct_6.5.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststruct_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ teststruct_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testunicode_7.1_GLNX86.mat
│  │     │  │  │  │  │  ├─ testunicode_7.4_GLNX86.mat
│  │     │  │  │  │  │  ├─ testvec_4_GLNX86.mat
│  │     │  │  │  │  │  ├─ test_empty_struct.mat
│  │     │  │  │  │  │  ├─ test_mat4_le_floats.mat
│  │     │  │  │  │  │  └─ test_skip_variable.mat
│  │     │  │  │  │  ├─ test_byteordercodes.py
│  │     │  │  │  │  ├─ test_mio.py
│  │     │  │  │  │  ├─ test_mio5_utils.py
│  │     │  │  │  │  ├─ test_miobase.py
│  │     │  │  │  │  ├─ test_mio_funcs.py
│  │     │  │  │  │  ├─ test_mio_utils.py
│  │     │  │  │  │  ├─ test_pathological.py
│  │     │  │  │  │  ├─ test_streams.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_byteordercodes.cpython-39.pyc
│  │     │  │  │  │     ├─ test_mio.cpython-39.pyc
│  │     │  │  │  │     ├─ test_mio5_utils.cpython-39.pyc
│  │     │  │  │  │     ├─ test_miobase.cpython-39.pyc
│  │     │  │  │  │     ├─ test_mio_funcs.cpython-39.pyc
│  │     │  │  │  │     ├─ test_mio_utils.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pathological.cpython-39.pyc
│  │     │  │  │  │     ├─ test_streams.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _byteordercodes.py
│  │     │  │  │  ├─ _mio.py
│  │     │  │  │  ├─ _mio4.py
│  │     │  │  │  ├─ _mio5.py
│  │     │  │  │  ├─ _mio5_params.py
│  │     │  │  │  ├─ _mio5_utils.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _mio5_utils.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _miobase.py
│  │     │  │  │  ├─ _mio_utils.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _mio_utils.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _streams.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _streams.cp39-win_amd64.pyd
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ byteordercodes.cpython-39.pyc
│  │     │  │  │     ├─ mio.cpython-39.pyc
│  │     │  │  │     ├─ mio4.cpython-39.pyc
│  │     │  │  │     ├─ mio5.cpython-39.pyc
│  │     │  │  │     ├─ mio5_params.cpython-39.pyc
│  │     │  │  │     ├─ mio5_utils.cpython-39.pyc
│  │     │  │  │     ├─ miobase.cpython-39.pyc
│  │     │  │  │     ├─ mio_utils.cpython-39.pyc
│  │     │  │  │     ├─ streams.cpython-39.pyc
│  │     │  │  │     ├─ _byteordercodes.cpython-39.pyc
│  │     │  │  │     ├─ _mio.cpython-39.pyc
│  │     │  │  │     ├─ _mio4.cpython-39.pyc
│  │     │  │  │     ├─ _mio5.cpython-39.pyc
│  │     │  │  │     ├─ _mio5_params.cpython-39.pyc
│  │     │  │  │     ├─ _miobase.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ mmio.py
│  │     │  │  ├─ netcdf.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ array_float32_1d.sav
│  │     │  │  │  │  ├─ array_float32_2d.sav
│  │     │  │  │  │  ├─ array_float32_3d.sav
│  │     │  │  │  │  ├─ array_float32_4d.sav
│  │     │  │  │  │  ├─ array_float32_5d.sav
│  │     │  │  │  │  ├─ array_float32_6d.sav
│  │     │  │  │  │  ├─ array_float32_7d.sav
│  │     │  │  │  │  ├─ array_float32_8d.sav
│  │     │  │  │  │  ├─ array_float32_pointer_1d.sav
│  │     │  │  │  │  ├─ array_float32_pointer_2d.sav
│  │     │  │  │  │  ├─ array_float32_pointer_3d.sav
│  │     │  │  │  │  ├─ array_float32_pointer_4d.sav
│  │     │  │  │  │  ├─ array_float32_pointer_5d.sav
│  │     │  │  │  │  ├─ array_float32_pointer_6d.sav
│  │     │  │  │  │  ├─ array_float32_pointer_7d.sav
│  │     │  │  │  │  ├─ array_float32_pointer_8d.sav
│  │     │  │  │  │  ├─ example_1.nc
│  │     │  │  │  │  ├─ example_2.nc
│  │     │  │  │  │  ├─ example_3_maskedvals.nc
│  │     │  │  │  │  ├─ fortran-3x3d-2i.dat
│  │     │  │  │  │  ├─ fortran-mixed.dat
│  │     │  │  │  │  ├─ fortran-sf8-11x1x10.dat
│  │     │  │  │  │  ├─ fortran-sf8-15x10x22.dat
│  │     │  │  │  │  ├─ fortran-sf8-1x1x1.dat
│  │     │  │  │  │  ├─ fortran-sf8-1x1x5.dat
│  │     │  │  │  │  ├─ fortran-sf8-1x1x7.dat
│  │     │  │  │  │  ├─ fortran-sf8-1x3x5.dat
│  │     │  │  │  │  ├─ fortran-si4-11x1x10.dat
│  │     │  │  │  │  ├─ fortran-si4-15x10x22.dat
│  │     │  │  │  │  ├─ fortran-si4-1x1x1.dat
│  │     │  │  │  │  ├─ fortran-si4-1x1x5.dat
│  │     │  │  │  │  ├─ fortran-si4-1x1x7.dat
│  │     │  │  │  │  ├─ fortran-si4-1x3x5.dat
│  │     │  │  │  │  ├─ invalid_pointer.sav
│  │     │  │  │  │  ├─ null_pointer.sav
│  │     │  │  │  │  ├─ scalar_byte.sav
│  │     │  │  │  │  ├─ scalar_byte_descr.sav
│  │     │  │  │  │  ├─ scalar_complex32.sav
│  │     │  │  │  │  ├─ scalar_complex64.sav
│  │     │  │  │  │  ├─ scalar_float32.sav
│  │     │  │  │  │  ├─ scalar_float64.sav
│  │     │  │  │  │  ├─ scalar_heap_pointer.sav
│  │     │  │  │  │  ├─ scalar_int16.sav
│  │     │  │  │  │  ├─ scalar_int32.sav
│  │     │  │  │  │  ├─ scalar_int64.sav
│  │     │  │  │  │  ├─ scalar_string.sav
│  │     │  │  │  │  ├─ scalar_uint16.sav
│  │     │  │  │  │  ├─ scalar_uint32.sav
│  │     │  │  │  │  ├─ scalar_uint64.sav
│  │     │  │  │  │  ├─ struct_arrays.sav
│  │     │  │  │  │  ├─ struct_arrays_byte_idl80.sav
│  │     │  │  │  │  ├─ struct_arrays_replicated.sav
│  │     │  │  │  │  ├─ struct_arrays_replicated_3d.sav
│  │     │  │  │  │  ├─ struct_inherit.sav
│  │     │  │  │  │  ├─ struct_pointers.sav
│  │     │  │  │  │  ├─ struct_pointers_replicated.sav
│  │     │  │  │  │  ├─ struct_pointers_replicated_3d.sav
│  │     │  │  │  │  ├─ struct_pointer_arrays.sav
│  │     │  │  │  │  ├─ struct_pointer_arrays_replicated.sav
│  │     │  │  │  │  ├─ struct_pointer_arrays_replicated_3d.sav
│  │     │  │  │  │  ├─ struct_scalars.sav
│  │     │  │  │  │  ├─ struct_scalars_replicated.sav
│  │     │  │  │  │  ├─ struct_scalars_replicated_3d.sav
│  │     │  │  │  │  ├─ test-44100Hz-2ch-32bit-float-be.wav
│  │     │  │  │  │  ├─ test-44100Hz-2ch-32bit-float-le.wav
│  │     │  │  │  │  ├─ test-44100Hz-be-1ch-4bytes.wav
│  │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-early-eof-no-data.wav
│  │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-early-eof.wav
│  │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-incomplete-chunk.wav
│  │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes.wav
│  │     │  │  │  │  ├─ test-48000Hz-2ch-64bit-float-le-wavex.wav
│  │     │  │  │  │  ├─ test-8000Hz-be-3ch-5S-24bit.wav
│  │     │  │  │  │  ├─ test-8000Hz-le-1ch-10S-20bit-extra.wav
│  │     │  │  │  │  ├─ test-8000Hz-le-1ch-1byte-ulaw.wav
│  │     │  │  │  │  ├─ test-8000Hz-le-2ch-1byteu.wav
│  │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-24bit-inconsistent.wav
│  │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-24bit.wav
│  │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-36bit.wav
│  │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-45bit.wav
│  │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-53bit.wav
│  │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-64bit.wav
│  │     │  │  │  │  ├─ test-8000Hz-le-4ch-9S-12bit.wav
│  │     │  │  │  │  ├─ test-8000Hz-le-5ch-9S-5bit.wav
│  │     │  │  │  │  ├─ Transparent Busy.ani
│  │     │  │  │  │  └─ various_compressed.sav
│  │     │  │  │  ├─ test_fortran.py
│  │     │  │  │  ├─ test_idl.py
│  │     │  │  │  ├─ test_mmio.py
│  │     │  │  │  ├─ test_netcdf.py
│  │     │  │  │  ├─ test_paths.py
│  │     │  │  │  ├─ test_wavfile.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_fortran.cpython-39.pyc
│  │     │  │  │     ├─ test_idl.cpython-39.pyc
│  │     │  │  │     ├─ test_mmio.cpython-39.pyc
│  │     │  │  │     ├─ test_netcdf.cpython-39.pyc
│  │     │  │  │     ├─ test_paths.cpython-39.pyc
│  │     │  │  │     ├─ test_wavfile.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ wavfile.py
│  │     │  │  ├─ _fortran.py
│  │     │  │  ├─ _harwell_boeing
│  │     │  │  │  ├─ hb.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ test_fortran_format.py
│  │     │  │  │  │  ├─ test_hb.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_fortran_format.cpython-39.pyc
│  │     │  │  │  │     ├─ test_hb.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _fortran_format_parser.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ hb.cpython-39.pyc
│  │     │  │  │     ├─ _fortran_format_parser.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _idl.py
│  │     │  │  ├─ _mmio.py
│  │     │  │  ├─ _netcdf.py
│  │     │  │  ├─ _test_fortran.cp39-win_amd64.dll.a
│  │     │  │  ├─ _test_fortran.cp39-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ harwell_boeing.cpython-39.pyc
│  │     │  │     ├─ idl.cpython-39.pyc
│  │     │  │     ├─ mmio.cpython-39.pyc
│  │     │  │     ├─ netcdf.cpython-39.pyc
│  │     │  │     ├─ wavfile.cpython-39.pyc
│  │     │  │     ├─ _fortran.cpython-39.pyc
│  │     │  │     ├─ _idl.cpython-39.pyc
│  │     │  │     ├─ _mmio.cpython-39.pyc
│  │     │  │     ├─ _netcdf.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ linalg
│  │     │  │  ├─ basic.py
│  │     │  │  ├─ blas.py
│  │     │  │  ├─ cython_blas.cp39-win_amd64.dll.a
│  │     │  │  ├─ cython_blas.cp39-win_amd64.pyd
│  │     │  │  ├─ cython_blas.pxd
│  │     │  │  ├─ cython_blas.pyx
│  │     │  │  ├─ cython_lapack.cp39-win_amd64.dll.a
│  │     │  │  ├─ cython_lapack.cp39-win_amd64.pyd
│  │     │  │  ├─ cython_lapack.pxd
│  │     │  │  ├─ cython_lapack.pyx
│  │     │  │  ├─ decomp.py
│  │     │  │  ├─ decomp_cholesky.py
│  │     │  │  ├─ decomp_lu.py
│  │     │  │  ├─ decomp_qr.py
│  │     │  │  ├─ decomp_schur.py
│  │     │  │  ├─ decomp_svd.py
│  │     │  │  ├─ flinalg.py
│  │     │  │  ├─ interpolative.py
│  │     │  │  ├─ lapack.py
│  │     │  │  ├─ matfuncs.py
│  │     │  │  ├─ misc.py
│  │     │  │  ├─ special_matrices.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ carex_15_data.npz
│  │     │  │  │  │  ├─ carex_18_data.npz
│  │     │  │  │  │  ├─ carex_19_data.npz
│  │     │  │  │  │  ├─ carex_20_data.npz
│  │     │  │  │  │  ├─ carex_6_data.npz
│  │     │  │  │  │  └─ gendare_20170120_data.npz
│  │     │  │  │  ├─ test_basic.py
│  │     │  │  │  ├─ test_blas.py
│  │     │  │  │  ├─ test_cythonized_array_utils.py
│  │     │  │  │  ├─ test_cython_blas.py
│  │     │  │  │  ├─ test_cython_lapack.py
│  │     │  │  │  ├─ test_decomp.py
│  │     │  │  │  ├─ test_decomp_cholesky.py
│  │     │  │  │  ├─ test_decomp_cossin.py
│  │     │  │  │  ├─ test_decomp_ldl.py
│  │     │  │  │  ├─ test_decomp_polar.py
│  │     │  │  │  ├─ test_decomp_update.py
│  │     │  │  │  ├─ test_fblas.py
│  │     │  │  │  ├─ test_interpolative.py
│  │     │  │  │  ├─ test_lapack.py
│  │     │  │  │  ├─ test_matfuncs.py
│  │     │  │  │  ├─ test_matmul_toeplitz.py
│  │     │  │  │  ├─ test_misc.py
│  │     │  │  │  ├─ test_procrustes.py
│  │     │  │  │  ├─ test_sketches.py
│  │     │  │  │  ├─ test_solvers.py
│  │     │  │  │  ├─ test_solve_toeplitz.py
│  │     │  │  │  ├─ test_special_matrices.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_basic.cpython-39.pyc
│  │     │  │  │     ├─ test_blas.cpython-39.pyc
│  │     │  │  │     ├─ test_cythonized_array_utils.cpython-39.pyc
│  │     │  │  │     ├─ test_cython_blas.cpython-39.pyc
│  │     │  │  │     ├─ test_cython_lapack.cpython-39.pyc
│  │     │  │  │     ├─ test_decomp.cpython-39.pyc
│  │     │  │  │     ├─ test_decomp_cholesky.cpython-39.pyc
│  │     │  │  │     ├─ test_decomp_cossin.cpython-39.pyc
│  │     │  │  │     ├─ test_decomp_ldl.cpython-39.pyc
│  │     │  │  │     ├─ test_decomp_polar.cpython-39.pyc
│  │     │  │  │     ├─ test_decomp_update.cpython-39.pyc
│  │     │  │  │     ├─ test_fblas.cpython-39.pyc
│  │     │  │  │     ├─ test_interpolative.cpython-39.pyc
│  │     │  │  │     ├─ test_lapack.cpython-39.pyc
│  │     │  │  │     ├─ test_matfuncs.cpython-39.pyc
│  │     │  │  │     ├─ test_matmul_toeplitz.cpython-39.pyc
│  │     │  │  │     ├─ test_misc.cpython-39.pyc
│  │     │  │  │     ├─ test_procrustes.cpython-39.pyc
│  │     │  │  │     ├─ test_sketches.cpython-39.pyc
│  │     │  │  │     ├─ test_solvers.cpython-39.pyc
│  │     │  │  │     ├─ test_solve_toeplitz.cpython-39.pyc
│  │     │  │  │     ├─ test_special_matrices.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _basic.py
│  │     │  │  ├─ _blas_subroutines.h
│  │     │  │  ├─ _blas_subroutine_wrappers.f
│  │     │  │  ├─ _cythonized_array_utils.cp39-win_amd64.dll.a
│  │     │  │  ├─ _cythonized_array_utils.cp39-win_amd64.pyd
│  │     │  │  ├─ _cythonized_array_utils.pxd
│  │     │  │  ├─ _cythonized_array_utils.pyi
│  │     │  │  ├─ _decomp.py
│  │     │  │  ├─ _decomp_cholesky.py
│  │     │  │  ├─ _decomp_cossin.py
│  │     │  │  ├─ _decomp_ldl.py
│  │     │  │  ├─ _decomp_lu.py
│  │     │  │  ├─ _decomp_polar.py
│  │     │  │  ├─ _decomp_qr.py
│  │     │  │  ├─ _decomp_qz.py
│  │     │  │  ├─ _decomp_schur.py
│  │     │  │  ├─ _decomp_svd.py
│  │     │  │  ├─ _decomp_update.cp39-win_amd64.dll.a
│  │     │  │  ├─ _decomp_update.cp39-win_amd64.pyd
│  │     │  │  ├─ _expm_frechet.py
│  │     │  │  ├─ _fblas.cp39-win_amd64.dll.a
│  │     │  │  ├─ _fblas.cp39-win_amd64.pyd
│  │     │  │  ├─ _flapack.cp39-win_amd64.dll.a
│  │     │  │  ├─ _flapack.cp39-win_amd64.pyd
│  │     │  │  ├─ _flinalg.cp39-win_amd64.dll.a
│  │     │  │  ├─ _flinalg.cp39-win_amd64.pyd
│  │     │  │  ├─ _flinalg_py.py
│  │     │  │  ├─ _interpolative.cp39-win_amd64.dll.a
│  │     │  │  ├─ _interpolative.cp39-win_amd64.pyd
│  │     │  │  ├─ _interpolative_backend.py
│  │     │  │  ├─ _lapack_subroutines.h
│  │     │  │  ├─ _lapack_subroutine_wrappers.f
│  │     │  │  ├─ _matfuncs.py
│  │     │  │  ├─ _matfuncs_expm.cp39-win_amd64.dll.a
│  │     │  │  ├─ _matfuncs_expm.cp39-win_amd64.pyd
│  │     │  │  ├─ _matfuncs_expm.pyi
│  │     │  │  ├─ _matfuncs_inv_ssq.py
│  │     │  │  ├─ _matfuncs_sqrtm.py
│  │     │  │  ├─ _matfuncs_sqrtm_triu.cp39-win_amd64.dll.a
│  │     │  │  ├─ _matfuncs_sqrtm_triu.cp39-win_amd64.pyd
│  │     │  │  ├─ _misc.py
│  │     │  │  ├─ _procrustes.py
│  │     │  │  ├─ _sketches.py
│  │     │  │  ├─ _solvers.py
│  │     │  │  ├─ _solve_toeplitz.cp39-win_amd64.dll.a
│  │     │  │  ├─ _solve_toeplitz.cp39-win_amd64.pyd
│  │     │  │  ├─ _special_matrices.py
│  │     │  │  ├─ _testutils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ basic.cpython-39.pyc
│  │     │  │     ├─ blas.cpython-39.pyc
│  │     │  │     ├─ decomp.cpython-39.pyc
│  │     │  │     ├─ decomp_cholesky.cpython-39.pyc
│  │     │  │     ├─ decomp_lu.cpython-39.pyc
│  │     │  │     ├─ decomp_qr.cpython-39.pyc
│  │     │  │     ├─ decomp_schur.cpython-39.pyc
│  │     │  │     ├─ decomp_svd.cpython-39.pyc
│  │     │  │     ├─ flinalg.cpython-39.pyc
│  │     │  │     ├─ interpolative.cpython-39.pyc
│  │     │  │     ├─ lapack.cpython-39.pyc
│  │     │  │     ├─ matfuncs.cpython-39.pyc
│  │     │  │     ├─ misc.cpython-39.pyc
│  │     │  │     ├─ special_matrices.cpython-39.pyc
│  │     │  │     ├─ _basic.cpython-39.pyc
│  │     │  │     ├─ _decomp.cpython-39.pyc
│  │     │  │     ├─ _decomp_cholesky.cpython-39.pyc
│  │     │  │     ├─ _decomp_cossin.cpython-39.pyc
│  │     │  │     ├─ _decomp_ldl.cpython-39.pyc
│  │     │  │     ├─ _decomp_lu.cpython-39.pyc
│  │     │  │     ├─ _decomp_polar.cpython-39.pyc
│  │     │  │     ├─ _decomp_qr.cpython-39.pyc
│  │     │  │     ├─ _decomp_qz.cpython-39.pyc
│  │     │  │     ├─ _decomp_schur.cpython-39.pyc
│  │     │  │     ├─ _decomp_svd.cpython-39.pyc
│  │     │  │     ├─ _expm_frechet.cpython-39.pyc
│  │     │  │     ├─ _flinalg_py.cpython-39.pyc
│  │     │  │     ├─ _interpolative_backend.cpython-39.pyc
│  │     │  │     ├─ _matfuncs.cpython-39.pyc
│  │     │  │     ├─ _matfuncs_inv_ssq.cpython-39.pyc
│  │     │  │     ├─ _matfuncs_sqrtm.cpython-39.pyc
│  │     │  │     ├─ _misc.cpython-39.pyc
│  │     │  │     ├─ _procrustes.cpython-39.pyc
│  │     │  │     ├─ _sketches.cpython-39.pyc
│  │     │  │     ├─ _solvers.cpython-39.pyc
│  │     │  │     ├─ _special_matrices.cpython-39.pyc
│  │     │  │     ├─ _testutils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ linalg.pxd
│  │     │  ├─ misc
│  │     │  │  ├─ ascent.dat
│  │     │  │  ├─ common.py
│  │     │  │  ├─ doccer.py
│  │     │  │  ├─ ecg.dat
│  │     │  │  ├─ face.dat
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_config.py
│  │     │  │  │  ├─ test_doccer.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_config.cpython-39.pyc
│  │     │  │  │     ├─ test_doccer.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _common.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ common.cpython-39.pyc
│  │     │  │     ├─ doccer.cpython-39.pyc
│  │     │  │     ├─ _common.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ ndimage
│  │     │  │  ├─ filters.py
│  │     │  │  ├─ fourier.py
│  │     │  │  ├─ interpolation.py
│  │     │  │  ├─ measurements.py
│  │     │  │  ├─ morphology.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ label_inputs.txt
│  │     │  │  │  │  ├─ label_results.txt
│  │     │  │  │  │  └─ label_strels.txt
│  │     │  │  │  ├─ dots.png
│  │     │  │  │  ├─ test_c_api.py
│  │     │  │  │  ├─ test_datatypes.py
│  │     │  │  │  ├─ test_filters.py
│  │     │  │  │  ├─ test_fourier.py
│  │     │  │  │  ├─ test_interpolation.py
│  │     │  │  │  ├─ test_measurements.py
│  │     │  │  │  ├─ test_morphology.py
│  │     │  │  │  ├─ test_splines.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_c_api.cpython-39.pyc
│  │     │  │  │     ├─ test_datatypes.cpython-39.pyc
│  │     │  │  │     ├─ test_filters.cpython-39.pyc
│  │     │  │  │     ├─ test_fourier.cpython-39.pyc
│  │     │  │  │     ├─ test_interpolation.cpython-39.pyc
│  │     │  │  │     ├─ test_measurements.cpython-39.pyc
│  │     │  │  │     ├─ test_morphology.cpython-39.pyc
│  │     │  │  │     ├─ test_splines.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _ctest.cp39-win_amd64.dll.a
│  │     │  │  ├─ _ctest.cp39-win_amd64.pyd
│  │     │  │  ├─ _cytest.cp39-win_amd64.dll.a
│  │     │  │  ├─ _cytest.cp39-win_amd64.pyd
│  │     │  │  ├─ _filters.py
│  │     │  │  ├─ _fourier.py
│  │     │  │  ├─ _interpolation.py
│  │     │  │  ├─ _measurements.py
│  │     │  │  ├─ _morphology.py
│  │     │  │  ├─ _nd_image.cp39-win_amd64.dll.a
│  │     │  │  ├─ _nd_image.cp39-win_amd64.pyd
│  │     │  │  ├─ _ni_docstrings.py
│  │     │  │  ├─ _ni_label.cp39-win_amd64.dll.a
│  │     │  │  ├─ _ni_label.cp39-win_amd64.pyd
│  │     │  │  ├─ _ni_support.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ filters.cpython-39.pyc
│  │     │  │     ├─ fourier.cpython-39.pyc
│  │     │  │     ├─ interpolation.cpython-39.pyc
│  │     │  │     ├─ measurements.cpython-39.pyc
│  │     │  │     ├─ morphology.cpython-39.pyc
│  │     │  │     ├─ _filters.cpython-39.pyc
│  │     │  │     ├─ _fourier.cpython-39.pyc
│  │     │  │     ├─ _interpolation.cpython-39.pyc
│  │     │  │     ├─ _measurements.cpython-39.pyc
│  │     │  │     ├─ _morphology.cpython-39.pyc
│  │     │  │     ├─ _ni_docstrings.cpython-39.pyc
│  │     │  │     ├─ _ni_support.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ odr
│  │     │  │  ├─ models.py
│  │     │  │  ├─ odrpack.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_odr.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_odr.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _add_newdocs.py
│  │     │  │  ├─ _models.py
│  │     │  │  ├─ _odrpack.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __odrpack.cp39-win_amd64.dll.a
│  │     │  │  ├─ __odrpack.cp39-win_amd64.pyd
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ models.cpython-39.pyc
│  │     │  │     ├─ odrpack.cpython-39.pyc
│  │     │  │     ├─ _add_newdocs.cpython-39.pyc
│  │     │  │     ├─ _models.cpython-39.pyc
│  │     │  │     ├─ _odrpack.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ optimize
│  │     │  │  ├─ cobyla.py
│  │     │  │  ├─ cython_optimize
│  │     │  │  │  ├─ c_zeros.pxd
│  │     │  │  │  ├─ _zeros.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _zeros.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _zeros.pxd
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ cython_optimize.pxd
│  │     │  │  ├─ lbfgsb.py
│  │     │  │  ├─ linesearch.py
│  │     │  │  ├─ minpack.py
│  │     │  │  ├─ minpack2.py
│  │     │  │  ├─ moduleTNC.py
│  │     │  │  ├─ nonlin.py
│  │     │  │  ├─ optimize.py
│  │     │  │  ├─ README
│  │     │  │  ├─ slsqp.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_cobyla.py
│  │     │  │  │  ├─ test_constraints.py
│  │     │  │  │  ├─ test_constraint_conversion.py
│  │     │  │  │  ├─ test_cython_optimize.py
│  │     │  │  │  ├─ test_differentiable_functions.py
│  │     │  │  │  ├─ test_direct.py
│  │     │  │  │  ├─ test_hessian_update_strategy.py
│  │     │  │  │  ├─ test_lbfgsb_hessinv.py
│  │     │  │  │  ├─ test_lbfgsb_setulb.py
│  │     │  │  │  ├─ test_least_squares.py
│  │     │  │  │  ├─ test_linear_assignment.py
│  │     │  │  │  ├─ test_linesearch.py
│  │     │  │  │  ├─ test_linprog.py
│  │     │  │  │  ├─ test_lsq_common.py
│  │     │  │  │  ├─ test_lsq_linear.py
│  │     │  │  │  ├─ test_milp.py
│  │     │  │  │  ├─ test_minimize_constrained.py
│  │     │  │  │  ├─ test_minpack.py
│  │     │  │  │  ├─ test_nnls.py
│  │     │  │  │  ├─ test_nonlin.py
│  │     │  │  │  ├─ test_optimize.py
│  │     │  │  │  ├─ test_quadratic_assignment.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_slsqp.py
│  │     │  │  │  ├─ test_tnc.py
│  │     │  │  │  ├─ test_trustregion.py
│  │     │  │  │  ├─ test_trustregion_exact.py
│  │     │  │  │  ├─ test_trustregion_krylov.py
│  │     │  │  │  ├─ test_zeros.py
│  │     │  │  │  ├─ test__basinhopping.py
│  │     │  │  │  ├─ test__differential_evolution.py
│  │     │  │  │  ├─ test__dual_annealing.py
│  │     │  │  │  ├─ test__linprog_clean_inputs.py
│  │     │  │  │  ├─ test__numdiff.py
│  │     │  │  │  ├─ test__remove_redundancy.py
│  │     │  │  │  ├─ test__root.py
│  │     │  │  │  ├─ test__shgo.py
│  │     │  │  │  ├─ test__spectral.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_cobyla.cpython-39.pyc
│  │     │  │  │     ├─ test_constraints.cpython-39.pyc
│  │     │  │  │     ├─ test_constraint_conversion.cpython-39.pyc
│  │     │  │  │     ├─ test_cython_optimize.cpython-39.pyc
│  │     │  │  │     ├─ test_differentiable_functions.cpython-39.pyc
│  │     │  │  │     ├─ test_direct.cpython-39.pyc
│  │     │  │  │     ├─ test_hessian_update_strategy.cpython-39.pyc
│  │     │  │  │     ├─ test_lbfgsb_hessinv.cpython-39.pyc
│  │     │  │  │     ├─ test_lbfgsb_setulb.cpython-39.pyc
│  │     │  │  │     ├─ test_least_squares.cpython-39.pyc
│  │     │  │  │     ├─ test_linear_assignment.cpython-39.pyc
│  │     │  │  │     ├─ test_linesearch.cpython-39.pyc
│  │     │  │  │     ├─ test_linprog.cpython-39.pyc
│  │     │  │  │     ├─ test_lsq_common.cpython-39.pyc
│  │     │  │  │     ├─ test_lsq_linear.cpython-39.pyc
│  │     │  │  │     ├─ test_milp.cpython-39.pyc
│  │     │  │  │     ├─ test_minimize_constrained.cpython-39.pyc
│  │     │  │  │     ├─ test_minpack.cpython-39.pyc
│  │     │  │  │     ├─ test_nnls.cpython-39.pyc
│  │     │  │  │     ├─ test_nonlin.cpython-39.pyc
│  │     │  │  │     ├─ test_optimize.cpython-39.pyc
│  │     │  │  │     ├─ test_quadratic_assignment.cpython-39.pyc
│  │     │  │  │     ├─ test_regression.cpython-39.pyc
│  │     │  │  │     ├─ test_slsqp.cpython-39.pyc
│  │     │  │  │     ├─ test_tnc.cpython-39.pyc
│  │     │  │  │     ├─ test_trustregion.cpython-39.pyc
│  │     │  │  │     ├─ test_trustregion_exact.cpython-39.pyc
│  │     │  │  │     ├─ test_trustregion_krylov.cpython-39.pyc
│  │     │  │  │     ├─ test_zeros.cpython-39.pyc
│  │     │  │  │     ├─ test__basinhopping.cpython-39.pyc
│  │     │  │  │     ├─ test__differential_evolution.cpython-39.pyc
│  │     │  │  │     ├─ test__dual_annealing.cpython-39.pyc
│  │     │  │  │     ├─ test__linprog_clean_inputs.cpython-39.pyc
│  │     │  │  │     ├─ test__numdiff.cpython-39.pyc
│  │     │  │  │     ├─ test__remove_redundancy.cpython-39.pyc
│  │     │  │  │     ├─ test__root.cpython-39.pyc
│  │     │  │  │     ├─ test__shgo.cpython-39.pyc
│  │     │  │  │     ├─ test__spectral.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ tnc.py
│  │     │  │  ├─ zeros.py
│  │     │  │  ├─ _basinhopping.py
│  │     │  │  ├─ _bglu_dense.cp39-win_amd64.dll.a
│  │     │  │  ├─ _bglu_dense.cp39-win_amd64.pyd
│  │     │  │  ├─ _cobyla.cp39-win_amd64.dll.a
│  │     │  │  ├─ _cobyla.cp39-win_amd64.pyd
│  │     │  │  ├─ _cobyla_py.py
│  │     │  │  ├─ _constraints.py
│  │     │  │  ├─ _differentiable_functions.py
│  │     │  │  ├─ _differentialevolution.py
│  │     │  │  ├─ _direct.cp39-win_amd64.dll.a
│  │     │  │  ├─ _direct.cp39-win_amd64.pyd
│  │     │  │  ├─ _direct_py.py
│  │     │  │  ├─ _dual_annealing.py
│  │     │  │  ├─ _group_columns.cp39-win_amd64.dll.a
│  │     │  │  ├─ _group_columns.cp39-win_amd64.pyd
│  │     │  │  ├─ _hessian_update_strategy.py
│  │     │  │  ├─ _highs
│  │     │  │  │  ├─ src
│  │     │  │  │  │  └─ cython
│  │     │  │  │  │     ├─ HConst.pxd
│  │     │  │  │  │     ├─ Highs.pxd
│  │     │  │  │  │     ├─ HighsInfo.pxd
│  │     │  │  │  │     ├─ HighsIO.pxd
│  │     │  │  │  │     ├─ HighsLp.pxd
│  │     │  │  │  │     ├─ HighsLpUtils.pxd
│  │     │  │  │  │     ├─ HighsModelUtils.pxd
│  │     │  │  │  │     ├─ HighsOptions.pxd
│  │     │  │  │  │     ├─ HighsRuntimeOptions.pxd
│  │     │  │  │  │     ├─ HighsStatus.pxd
│  │     │  │  │  │     ├─ highs_c_api.pxd
│  │     │  │  │  │     └─ SimplexConst.pxd
│  │     │  │  │  ├─ _highs_constants.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _highs_constants.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _highs_wrapper.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _highs_wrapper.cp39-win_amd64.pyd
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _lbfgsb.cp39-win_amd64.dll.a
│  │     │  │  ├─ _lbfgsb.cp39-win_amd64.pyd
│  │     │  │  ├─ _lbfgsb_py.py
│  │     │  │  ├─ _linesearch.py
│  │     │  │  ├─ _linprog.py
│  │     │  │  ├─ _linprog_doc.py
│  │     │  │  ├─ _linprog_highs.py
│  │     │  │  ├─ _linprog_ip.py
│  │     │  │  ├─ _linprog_rs.py
│  │     │  │  ├─ _linprog_simplex.py
│  │     │  │  ├─ _linprog_util.py
│  │     │  │  ├─ _lsap.cp39-win_amd64.dll.a
│  │     │  │  ├─ _lsap.cp39-win_amd64.pyd
│  │     │  │  ├─ _lsq
│  │     │  │  │  ├─ bvls.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ dogbox.py
│  │     │  │  │  ├─ givens_elimination.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ givens_elimination.cp39-win_amd64.pyd
│  │     │  │  │  ├─ least_squares.py
│  │     │  │  │  ├─ lsq_linear.py
│  │     │  │  │  ├─ trf.py
│  │     │  │  │  ├─ trf_linear.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bvls.cpython-39.pyc
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ dogbox.cpython-39.pyc
│  │     │  │  │     ├─ least_squares.cpython-39.pyc
│  │     │  │  │     ├─ lsq_linear.cpython-39.pyc
│  │     │  │  │     ├─ trf.cpython-39.pyc
│  │     │  │  │     ├─ trf_linear.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _milp.py
│  │     │  │  ├─ _minimize.py
│  │     │  │  ├─ _minpack.cp39-win_amd64.dll.a
│  │     │  │  ├─ _minpack.cp39-win_amd64.pyd
│  │     │  │  ├─ _minpack2.cp39-win_amd64.dll.a
│  │     │  │  ├─ _minpack2.cp39-win_amd64.pyd
│  │     │  │  ├─ _minpack_py.py
│  │     │  │  ├─ _moduleTNC.cp39-win_amd64.dll.a
│  │     │  │  ├─ _moduleTNC.cp39-win_amd64.pyd
│  │     │  │  ├─ _nnls.py
│  │     │  │  ├─ _nonlin.py
│  │     │  │  ├─ _numdiff.py
│  │     │  │  ├─ _optimize.py
│  │     │  │  ├─ _qap.py
│  │     │  │  ├─ _remove_redundancy.py
│  │     │  │  ├─ _root.py
│  │     │  │  ├─ _root_scalar.py
│  │     │  │  ├─ _shgo.py
│  │     │  │  ├─ _shgo_lib
│  │     │  │  │  ├─ triangulation.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ triangulation.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _slsqp.cp39-win_amd64.dll.a
│  │     │  │  ├─ _slsqp.cp39-win_amd64.pyd
│  │     │  │  ├─ _slsqp_py.py
│  │     │  │  ├─ _spectral.py
│  │     │  │  ├─ _tnc.py
│  │     │  │  ├─ _trlib
│  │     │  │  │  ├─ _trlib.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _trlib.cp39-win_amd64.pyd
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _trustregion.py
│  │     │  │  ├─ _trustregion_constr
│  │     │  │  │  ├─ canonical_constraint.py
│  │     │  │  │  ├─ equality_constrained_sqp.py
│  │     │  │  │  ├─ minimize_trustregion_constr.py
│  │     │  │  │  ├─ projections.py
│  │     │  │  │  ├─ qp_subproblem.py
│  │     │  │  │  ├─ report.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ test_canonical_constraint.py
│  │     │  │  │  │  ├─ test_projections.py
│  │     │  │  │  │  ├─ test_qp_subproblem.py
│  │     │  │  │  │  ├─ test_report.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_canonical_constraint.cpython-39.pyc
│  │     │  │  │  │     ├─ test_projections.cpython-39.pyc
│  │     │  │  │  │     ├─ test_qp_subproblem.cpython-39.pyc
│  │     │  │  │  │     ├─ test_report.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ tr_interior_point.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ canonical_constraint.cpython-39.pyc
│  │     │  │  │     ├─ equality_constrained_sqp.cpython-39.pyc
│  │     │  │  │     ├─ minimize_trustregion_constr.cpython-39.pyc
│  │     │  │  │     ├─ projections.cpython-39.pyc
│  │     │  │  │     ├─ qp_subproblem.cpython-39.pyc
│  │     │  │  │     ├─ report.cpython-39.pyc
│  │     │  │  │     ├─ tr_interior_point.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _trustregion_dogleg.py
│  │     │  │  ├─ _trustregion_exact.py
│  │     │  │  ├─ _trustregion_krylov.py
│  │     │  │  ├─ _trustregion_ncg.py
│  │     │  │  ├─ _tstutils.py
│  │     │  │  ├─ _zeros.cp39-win_amd64.dll.a
│  │     │  │  ├─ _zeros.cp39-win_amd64.pyd
│  │     │  │  ├─ _zeros_py.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __nnls.cp39-win_amd64.dll.a
│  │     │  │  ├─ __nnls.cp39-win_amd64.pyd
│  │     │  │  ├─ __nnls.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ cobyla.cpython-39.pyc
│  │     │  │     ├─ lbfgsb.cpython-39.pyc
│  │     │  │     ├─ linesearch.cpython-39.pyc
│  │     │  │     ├─ minpack.cpython-39.pyc
│  │     │  │     ├─ minpack2.cpython-39.pyc
│  │     │  │     ├─ moduleTNC.cpython-39.pyc
│  │     │  │     ├─ nonlin.cpython-39.pyc
│  │     │  │     ├─ optimize.cpython-39.pyc
│  │     │  │     ├─ slsqp.cpython-39.pyc
│  │     │  │     ├─ tnc.cpython-39.pyc
│  │     │  │     ├─ zeros.cpython-39.pyc
│  │     │  │     ├─ _basinhopping.cpython-39.pyc
│  │     │  │     ├─ _cobyla_py.cpython-39.pyc
│  │     │  │     ├─ _constraints.cpython-39.pyc
│  │     │  │     ├─ _differentiable_functions.cpython-39.pyc
│  │     │  │     ├─ _differentialevolution.cpython-39.pyc
│  │     │  │     ├─ _direct_py.cpython-39.pyc
│  │     │  │     ├─ _dual_annealing.cpython-39.pyc
│  │     │  │     ├─ _hessian_update_strategy.cpython-39.pyc
│  │     │  │     ├─ _lbfgsb_py.cpython-39.pyc
│  │     │  │     ├─ _linesearch.cpython-39.pyc
│  │     │  │     ├─ _linprog.cpython-39.pyc
│  │     │  │     ├─ _linprog_doc.cpython-39.pyc
│  │     │  │     ├─ _linprog_highs.cpython-39.pyc
│  │     │  │     ├─ _linprog_ip.cpython-39.pyc
│  │     │  │     ├─ _linprog_rs.cpython-39.pyc
│  │     │  │     ├─ _linprog_simplex.cpython-39.pyc
│  │     │  │     ├─ _linprog_util.cpython-39.pyc
│  │     │  │     ├─ _milp.cpython-39.pyc
│  │     │  │     ├─ _minimize.cpython-39.pyc
│  │     │  │     ├─ _minpack_py.cpython-39.pyc
│  │     │  │     ├─ _nnls.cpython-39.pyc
│  │     │  │     ├─ _nonlin.cpython-39.pyc
│  │     │  │     ├─ _numdiff.cpython-39.pyc
│  │     │  │     ├─ _optimize.cpython-39.pyc
│  │     │  │     ├─ _qap.cpython-39.pyc
│  │     │  │     ├─ _remove_redundancy.cpython-39.pyc
│  │     │  │     ├─ _root.cpython-39.pyc
│  │     │  │     ├─ _root_scalar.cpython-39.pyc
│  │     │  │     ├─ _shgo.cpython-39.pyc
│  │     │  │     ├─ _slsqp_py.cpython-39.pyc
│  │     │  │     ├─ _spectral.cpython-39.pyc
│  │     │  │     ├─ _tnc.cpython-39.pyc
│  │     │  │     ├─ _trustregion.cpython-39.pyc
│  │     │  │     ├─ _trustregion_dogleg.cpython-39.pyc
│  │     │  │     ├─ _trustregion_exact.cpython-39.pyc
│  │     │  │     ├─ _trustregion_krylov.cpython-39.pyc
│  │     │  │     ├─ _trustregion_ncg.cpython-39.pyc
│  │     │  │     ├─ _tstutils.cpython-39.pyc
│  │     │  │     ├─ _zeros_py.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ optimize.pxd
│  │     │  ├─ signal
│  │     │  │  ├─ bsplines.py
│  │     │  │  ├─ filter_design.py
│  │     │  │  ├─ fir_filter_design.py
│  │     │  │  ├─ ltisys.py
│  │     │  │  ├─ lti_conversion.py
│  │     │  │  ├─ signaltools.py
│  │     │  │  ├─ spectral.py
│  │     │  │  ├─ spline.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ mpsig.py
│  │     │  │  │  ├─ test_array_tools.py
│  │     │  │  │  ├─ test_bsplines.py
│  │     │  │  │  ├─ test_cont2discrete.py
│  │     │  │  │  ├─ test_czt.py
│  │     │  │  │  ├─ test_dltisys.py
│  │     │  │  │  ├─ test_filter_design.py
│  │     │  │  │  ├─ test_fir_filter_design.py
│  │     │  │  │  ├─ test_ltisys.py
│  │     │  │  │  ├─ test_max_len_seq.py
│  │     │  │  │  ├─ test_peak_finding.py
│  │     │  │  │  ├─ test_result_type.py
│  │     │  │  │  ├─ test_savitzky_golay.py
│  │     │  │  │  ├─ test_signaltools.py
│  │     │  │  │  ├─ test_spectral.py
│  │     │  │  │  ├─ test_upfirdn.py
│  │     │  │  │  ├─ test_waveforms.py
│  │     │  │  │  ├─ test_wavelets.py
│  │     │  │  │  ├─ test_windows.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ mpsig.cpython-39.pyc
│  │     │  │  │     ├─ test_array_tools.cpython-39.pyc
│  │     │  │  │     ├─ test_bsplines.cpython-39.pyc
│  │     │  │  │     ├─ test_cont2discrete.cpython-39.pyc
│  │     │  │  │     ├─ test_czt.cpython-39.pyc
│  │     │  │  │     ├─ test_dltisys.cpython-39.pyc
│  │     │  │  │     ├─ test_filter_design.cpython-39.pyc
│  │     │  │  │     ├─ test_fir_filter_design.cpython-39.pyc
│  │     │  │  │     ├─ test_ltisys.cpython-39.pyc
│  │     │  │  │     ├─ test_max_len_seq.cpython-39.pyc
│  │     │  │  │     ├─ test_peak_finding.cpython-39.pyc
│  │     │  │  │     ├─ test_result_type.cpython-39.pyc
│  │     │  │  │     ├─ test_savitzky_golay.cpython-39.pyc
│  │     │  │  │     ├─ test_signaltools.cpython-39.pyc
│  │     │  │  │     ├─ test_spectral.cpython-39.pyc
│  │     │  │  │     ├─ test_upfirdn.cpython-39.pyc
│  │     │  │  │     ├─ test_waveforms.cpython-39.pyc
│  │     │  │  │     ├─ test_wavelets.cpython-39.pyc
│  │     │  │  │     ├─ test_windows.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ waveforms.py
│  │     │  │  ├─ wavelets.py
│  │     │  │  ├─ windows
│  │     │  │  │  ├─ windows.py
│  │     │  │  │  ├─ _windows.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ windows.cpython-39.pyc
│  │     │  │  │     ├─ _windows.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _arraytools.py
│  │     │  │  ├─ _bsplines.py
│  │     │  │  ├─ _czt.py
│  │     │  │  ├─ _filter_design.py
│  │     │  │  ├─ _fir_filter_design.py
│  │     │  │  ├─ _ltisys.py
│  │     │  │  ├─ _lti_conversion.py
│  │     │  │  ├─ _max_len_seq.py
│  │     │  │  ├─ _max_len_seq_inner.cp39-win_amd64.dll.a
│  │     │  │  ├─ _max_len_seq_inner.cp39-win_amd64.pyd
│  │     │  │  ├─ _peak_finding.py
│  │     │  │  ├─ _peak_finding_utils.cp39-win_amd64.dll.a
│  │     │  │  ├─ _peak_finding_utils.cp39-win_amd64.pyd
│  │     │  │  ├─ _savitzky_golay.py
│  │     │  │  ├─ _signaltools.py
│  │     │  │  ├─ _sigtools.cp39-win_amd64.dll.a
│  │     │  │  ├─ _sigtools.cp39-win_amd64.pyd
│  │     │  │  ├─ _sosfilt.cp39-win_amd64.dll.a
│  │     │  │  ├─ _sosfilt.cp39-win_amd64.pyd
│  │     │  │  ├─ _spectral.cp39-win_amd64.dll.a
│  │     │  │  ├─ _spectral.cp39-win_amd64.pyd
│  │     │  │  ├─ _spectral.py
│  │     │  │  ├─ _spectral_py.py
│  │     │  │  ├─ _spline.cp39-win_amd64.dll.a
│  │     │  │  ├─ _spline.cp39-win_amd64.pyd
│  │     │  │  ├─ _upfirdn.py
│  │     │  │  ├─ _upfirdn_apply.cp39-win_amd64.dll.a
│  │     │  │  ├─ _upfirdn_apply.cp39-win_amd64.pyd
│  │     │  │  ├─ _waveforms.py
│  │     │  │  ├─ _wavelets.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ bsplines.cpython-39.pyc
│  │     │  │     ├─ filter_design.cpython-39.pyc
│  │     │  │     ├─ fir_filter_design.cpython-39.pyc
│  │     │  │     ├─ ltisys.cpython-39.pyc
│  │     │  │     ├─ lti_conversion.cpython-39.pyc
│  │     │  │     ├─ signaltools.cpython-39.pyc
│  │     │  │     ├─ spectral.cpython-39.pyc
│  │     │  │     ├─ spline.cpython-39.pyc
│  │     │  │     ├─ waveforms.cpython-39.pyc
│  │     │  │     ├─ wavelets.cpython-39.pyc
│  │     │  │     ├─ _arraytools.cpython-39.pyc
│  │     │  │     ├─ _bsplines.cpython-39.pyc
│  │     │  │     ├─ _czt.cpython-39.pyc
│  │     │  │     ├─ _filter_design.cpython-39.pyc
│  │     │  │     ├─ _fir_filter_design.cpython-39.pyc
│  │     │  │     ├─ _ltisys.cpython-39.pyc
│  │     │  │     ├─ _lti_conversion.cpython-39.pyc
│  │     │  │     ├─ _max_len_seq.cpython-39.pyc
│  │     │  │     ├─ _peak_finding.cpython-39.pyc
│  │     │  │     ├─ _savitzky_golay.cpython-39.pyc
│  │     │  │     ├─ _signaltools.cpython-39.pyc
│  │     │  │     ├─ _spectral.cpython-39.pyc
│  │     │  │     ├─ _spectral_py.cpython-39.pyc
│  │     │  │     ├─ _upfirdn.cpython-39.pyc
│  │     │  │     ├─ _waveforms.cpython-39.pyc
│  │     │  │     ├─ _wavelets.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ sparse
│  │     │  │  ├─ base.py
│  │     │  │  ├─ bsr.py
│  │     │  │  ├─ compressed.py
│  │     │  │  ├─ construct.py
│  │     │  │  ├─ coo.py
│  │     │  │  ├─ csc.py
│  │     │  │  ├─ csgraph
│  │     │  │  │  ├─ setup.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ test_connected_components.py
│  │     │  │  │  │  ├─ test_conversions.py
│  │     │  │  │  │  ├─ test_flow.py
│  │     │  │  │  │  ├─ test_graph_laplacian.py
│  │     │  │  │  │  ├─ test_matching.py
│  │     │  │  │  │  ├─ test_reordering.py
│  │     │  │  │  │  ├─ test_shortest_path.py
│  │     │  │  │  │  ├─ test_spanning_tree.py
│  │     │  │  │  │  ├─ test_traversal.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_connected_components.cpython-39.pyc
│  │     │  │  │  │     ├─ test_conversions.cpython-39.pyc
│  │     │  │  │  │     ├─ test_flow.cpython-39.pyc
│  │     │  │  │  │     ├─ test_graph_laplacian.cpython-39.pyc
│  │     │  │  │  │     ├─ test_matching.cpython-39.pyc
│  │     │  │  │  │     ├─ test_reordering.cpython-39.pyc
│  │     │  │  │  │     ├─ test_shortest_path.cpython-39.pyc
│  │     │  │  │  │     ├─ test_spanning_tree.cpython-39.pyc
│  │     │  │  │  │     ├─ test_traversal.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _flow.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _flow.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _laplacian.py
│  │     │  │  │  ├─ _matching.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _matching.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _min_spanning_tree.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _min_spanning_tree.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _reordering.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _reordering.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _shortest_path.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _shortest_path.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _tools.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _tools.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _traversal.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _traversal.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _validation.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ setup.cpython-39.pyc
│  │     │  │  │     ├─ _laplacian.cpython-39.pyc
│  │     │  │  │     ├─ _validation.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ csr.py
│  │     │  │  ├─ data.py
│  │     │  │  ├─ dia.py
│  │     │  │  ├─ dok.py
│  │     │  │  ├─ extract.py
│  │     │  │  ├─ lil.py
│  │     │  │  ├─ linalg
│  │     │  │  │  ├─ dsolve.py
│  │     │  │  │  ├─ eigen.py
│  │     │  │  │  ├─ interface.py
│  │     │  │  │  ├─ isolve.py
│  │     │  │  │  ├─ matfuncs.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ propack_test_data.npz
│  │     │  │  │  │  ├─ test_expm_multiply.py
│  │     │  │  │  │  ├─ test_interface.py
│  │     │  │  │  │  ├─ test_matfuncs.py
│  │     │  │  │  │  ├─ test_norm.py
│  │     │  │  │  │  ├─ test_onenormest.py
│  │     │  │  │  │  ├─ test_propack.py
│  │     │  │  │  │  ├─ test_pydata_sparse.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_expm_multiply.cpython-39.pyc
│  │     │  │  │  │     ├─ test_interface.cpython-39.pyc
│  │     │  │  │  │     ├─ test_matfuncs.cpython-39.pyc
│  │     │  │  │  │     ├─ test_norm.cpython-39.pyc
│  │     │  │  │  │     ├─ test_onenormest.cpython-39.pyc
│  │     │  │  │  │     ├─ test_propack.cpython-39.pyc
│  │     │  │  │  │     ├─ test_pydata_sparse.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _dsolve
│  │     │  │  │  │  ├─ linsolve.py
│  │     │  │  │  │  ├─ tests
│  │     │  │  │  │  │  ├─ test_linsolve.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ test_linsolve.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ _add_newdocs.py
│  │     │  │  │  │  ├─ _superlu.cp39-win_amd64.dll.a
│  │     │  │  │  │  ├─ _superlu.cp39-win_amd64.pyd
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ linsolve.cpython-39.pyc
│  │     │  │  │  │     ├─ _add_newdocs.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _eigen
│  │     │  │  │  │  ├─ arpack
│  │     │  │  │  │  │  ├─ arpack.py
│  │     │  │  │  │  │  ├─ COPYING
│  │     │  │  │  │  │  ├─ tests
│  │     │  │  │  │  │  │  ├─ test_arpack.py
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     ├─ test_arpack.cpython-39.pyc
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ _arpack.cp39-win_amd64.dll.a
│  │     │  │  │  │  │  ├─ _arpack.cp39-win_amd64.pyd
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ arpack.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ lobpcg
│  │     │  │  │  │  │  ├─ lobpcg.py
│  │     │  │  │  │  │  ├─ tests
│  │     │  │  │  │  │  │  ├─ test_lobpcg.py
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     ├─ test_lobpcg.cpython-39.pyc
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ lobpcg.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ tests
│  │     │  │  │  │  │  ├─ test_svds.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ test_svds.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ _svds.py
│  │     │  │  │  │  ├─ _svds_doc.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ _svds.cpython-39.pyc
│  │     │  │  │  │     ├─ _svds_doc.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _expm_multiply.py
│  │     │  │  │  ├─ _interface.py
│  │     │  │  │  ├─ _isolve
│  │     │  │  │  │  ├─ iterative.py
│  │     │  │  │  │  ├─ lgmres.py
│  │     │  │  │  │  ├─ lsmr.py
│  │     │  │  │  │  ├─ lsqr.py
│  │     │  │  │  │  ├─ minres.py
│  │     │  │  │  │  ├─ tests
│  │     │  │  │  │  │  ├─ test_gcrotmk.py
│  │     │  │  │  │  │  ├─ test_iterative.py
│  │     │  │  │  │  │  ├─ test_lgmres.py
│  │     │  │  │  │  │  ├─ test_lsmr.py
│  │     │  │  │  │  │  ├─ test_lsqr.py
│  │     │  │  │  │  │  ├─ test_minres.py
│  │     │  │  │  │  │  ├─ test_utils.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ test_gcrotmk.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_iterative.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_lgmres.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_lsmr.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_lsqr.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_minres.cpython-39.pyc
│  │     │  │  │  │  │     ├─ test_utils.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ tfqmr.py
│  │     │  │  │  │  ├─ utils.py
│  │     │  │  │  │  ├─ _gcrotmk.py
│  │     │  │  │  │  ├─ _iterative.cp39-win_amd64.dll.a
│  │     │  │  │  │  ├─ _iterative.cp39-win_amd64.pyd
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ iterative.cpython-39.pyc
│  │     │  │  │  │     ├─ lgmres.cpython-39.pyc
│  │     │  │  │  │     ├─ lsmr.cpython-39.pyc
│  │     │  │  │  │     ├─ lsqr.cpython-39.pyc
│  │     │  │  │  │     ├─ minres.cpython-39.pyc
│  │     │  │  │  │     ├─ tfqmr.cpython-39.pyc
│  │     │  │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │  │     ├─ _gcrotmk.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _matfuncs.py
│  │     │  │  │  ├─ _norm.py
│  │     │  │  │  ├─ _onenormest.py
│  │     │  │  │  ├─ _propack
│  │     │  │  │  │  ├─ _cpropack.cp39-win_amd64.dll.a
│  │     │  │  │  │  ├─ _cpropack.cp39-win_amd64.pyd
│  │     │  │  │  │  ├─ _dpropack.cp39-win_amd64.dll.a
│  │     │  │  │  │  ├─ _dpropack.cp39-win_amd64.pyd
│  │     │  │  │  │  ├─ _spropack.cp39-win_amd64.dll.a
│  │     │  │  │  │  ├─ _spropack.cp39-win_amd64.pyd
│  │     │  │  │  │  ├─ _zpropack.cp39-win_amd64.dll.a
│  │     │  │  │  │  └─ _zpropack.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _svdp.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ dsolve.cpython-39.pyc
│  │     │  │  │     ├─ eigen.cpython-39.pyc
│  │     │  │  │     ├─ interface.cpython-39.pyc
│  │     │  │  │     ├─ isolve.cpython-39.pyc
│  │     │  │  │     ├─ matfuncs.cpython-39.pyc
│  │     │  │  │     ├─ _expm_multiply.cpython-39.pyc
│  │     │  │  │     ├─ _interface.cpython-39.pyc
│  │     │  │  │     ├─ _matfuncs.cpython-39.pyc
│  │     │  │  │     ├─ _norm.cpython-39.pyc
│  │     │  │  │     ├─ _onenormest.cpython-39.pyc
│  │     │  │  │     ├─ _svdp.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ sparsetools.py
│  │     │  │  ├─ spfuncs.py
│  │     │  │  ├─ sputils.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ csc_py2.npz
│  │     │  │  │  │  └─ csc_py3.npz
│  │     │  │  │  ├─ test_array_api.py
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_construct.py
│  │     │  │  │  ├─ test_csc.py
│  │     │  │  │  ├─ test_csr.py
│  │     │  │  │  ├─ test_extract.py
│  │     │  │  │  ├─ test_matrix_io.py
│  │     │  │  │  ├─ test_sparsetools.py
│  │     │  │  │  ├─ test_spfuncs.py
│  │     │  │  │  ├─ test_sputils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_array_api.cpython-39.pyc
│  │     │  │  │     ├─ test_base.cpython-39.pyc
│  │     │  │  │     ├─ test_construct.cpython-39.pyc
│  │     │  │  │     ├─ test_csc.cpython-39.pyc
│  │     │  │  │     ├─ test_csr.cpython-39.pyc
│  │     │  │  │     ├─ test_extract.cpython-39.pyc
│  │     │  │  │     ├─ test_matrix_io.cpython-39.pyc
│  │     │  │  │     ├─ test_sparsetools.cpython-39.pyc
│  │     │  │  │     ├─ test_spfuncs.cpython-39.pyc
│  │     │  │  │     ├─ test_sputils.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _arrays.py
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _bsr.py
│  │     │  │  ├─ _compressed.py
│  │     │  │  ├─ _construct.py
│  │     │  │  ├─ _coo.py
│  │     │  │  ├─ _csc.py
│  │     │  │  ├─ _csparsetools.cp39-win_amd64.dll.a
│  │     │  │  ├─ _csparsetools.cp39-win_amd64.pyd
│  │     │  │  ├─ _csr.py
│  │     │  │  ├─ _data.py
│  │     │  │  ├─ _dia.py
│  │     │  │  ├─ _dok.py
│  │     │  │  ├─ _extract.py
│  │     │  │  ├─ _index.py
│  │     │  │  ├─ _lil.py
│  │     │  │  ├─ _matrix_io.py
│  │     │  │  ├─ _sparsetools.cp39-win_amd64.dll.a
│  │     │  │  ├─ _sparsetools.cp39-win_amd64.pyd
│  │     │  │  ├─ _spfuncs.py
│  │     │  │  ├─ _sputils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ bsr.cpython-39.pyc
│  │     │  │     ├─ compressed.cpython-39.pyc
│  │     │  │     ├─ construct.cpython-39.pyc
│  │     │  │     ├─ coo.cpython-39.pyc
│  │     │  │     ├─ csc.cpython-39.pyc
│  │     │  │     ├─ csr.cpython-39.pyc
│  │     │  │     ├─ data.cpython-39.pyc
│  │     │  │     ├─ dia.cpython-39.pyc
│  │     │  │     ├─ dok.cpython-39.pyc
│  │     │  │     ├─ extract.cpython-39.pyc
│  │     │  │     ├─ lil.cpython-39.pyc
│  │     │  │     ├─ sparsetools.cpython-39.pyc
│  │     │  │     ├─ spfuncs.cpython-39.pyc
│  │     │  │     ├─ sputils.cpython-39.pyc
│  │     │  │     ├─ _arrays.cpython-39.pyc
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _bsr.cpython-39.pyc
│  │     │  │     ├─ _compressed.cpython-39.pyc
│  │     │  │     ├─ _construct.cpython-39.pyc
│  │     │  │     ├─ _coo.cpython-39.pyc
│  │     │  │     ├─ _csc.cpython-39.pyc
│  │     │  │     ├─ _csr.cpython-39.pyc
│  │     │  │     ├─ _data.cpython-39.pyc
│  │     │  │     ├─ _dia.cpython-39.pyc
│  │     │  │     ├─ _dok.cpython-39.pyc
│  │     │  │     ├─ _extract.cpython-39.pyc
│  │     │  │     ├─ _index.cpython-39.pyc
│  │     │  │     ├─ _lil.cpython-39.pyc
│  │     │  │     ├─ _matrix_io.cpython-39.pyc
│  │     │  │     ├─ _spfuncs.cpython-39.pyc
│  │     │  │     ├─ _sputils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ spatial
│  │     │  │  ├─ ckdtree.py
│  │     │  │  ├─ distance.py
│  │     │  │  ├─ distance.pyi
│  │     │  │  ├─ kdtree.py
│  │     │  │  ├─ qhull.py
│  │     │  │  ├─ qhull_src
│  │     │  │  │  └─ COPYING.txt
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ cdist-X1.txt
│  │     │  │  │  │  ├─ cdist-X2.txt
│  │     │  │  │  │  ├─ degenerate_pointset.npz
│  │     │  │  │  │  ├─ iris.txt
│  │     │  │  │  │  ├─ pdist-boolean-inp.txt
│  │     │  │  │  │  ├─ pdist-chebyshev-ml-iris.txt
│  │     │  │  │  │  ├─ pdist-chebyshev-ml.txt
│  │     │  │  │  │  ├─ pdist-cityblock-ml-iris.txt
│  │     │  │  │  │  ├─ pdist-cityblock-ml.txt
│  │     │  │  │  │  ├─ pdist-correlation-ml-iris.txt
│  │     │  │  │  │  ├─ pdist-correlation-ml.txt
│  │     │  │  │  │  ├─ pdist-cosine-ml-iris.txt
│  │     │  │  │  │  ├─ pdist-cosine-ml.txt
│  │     │  │  │  │  ├─ pdist-double-inp.txt
│  │     │  │  │  │  ├─ pdist-euclidean-ml-iris.txt
│  │     │  │  │  │  ├─ pdist-euclidean-ml.txt
│  │     │  │  │  │  ├─ pdist-hamming-ml.txt
│  │     │  │  │  │  ├─ pdist-jaccard-ml.txt
│  │     │  │  │  │  ├─ pdist-jensenshannon-ml-iris.txt
│  │     │  │  │  │  ├─ pdist-jensenshannon-ml.txt
│  │     │  │  │  │  ├─ pdist-minkowski-3.2-ml-iris.txt
│  │     │  │  │  │  ├─ pdist-minkowski-3.2-ml.txt
│  │     │  │  │  │  ├─ pdist-minkowski-5.8-ml-iris.txt
│  │     │  │  │  │  ├─ pdist-seuclidean-ml-iris.txt
│  │     │  │  │  │  ├─ pdist-seuclidean-ml.txt
│  │     │  │  │  │  ├─ pdist-spearman-ml.txt
│  │     │  │  │  │  ├─ random-bool-data.txt
│  │     │  │  │  │  ├─ random-double-data.txt
│  │     │  │  │  │  ├─ random-int-data.txt
│  │     │  │  │  │  ├─ random-uint-data.txt
│  │     │  │  │  │  └─ selfdual-4d-polytope.txt
│  │     │  │  │  ├─ test_distance.py
│  │     │  │  │  ├─ test_hausdorff.py
│  │     │  │  │  ├─ test_kdtree.py
│  │     │  │  │  ├─ test_qhull.py
│  │     │  │  │  ├─ test_slerp.py
│  │     │  │  │  ├─ test_spherical_voronoi.py
│  │     │  │  │  ├─ test__plotutils.py
│  │     │  │  │  ├─ test__procrustes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_distance.cpython-39.pyc
│  │     │  │  │     ├─ test_hausdorff.cpython-39.pyc
│  │     │  │  │     ├─ test_kdtree.cpython-39.pyc
│  │     │  │  │     ├─ test_qhull.cpython-39.pyc
│  │     │  │  │     ├─ test_slerp.cpython-39.pyc
│  │     │  │  │     ├─ test_spherical_voronoi.cpython-39.pyc
│  │     │  │  │     ├─ test__plotutils.cpython-39.pyc
│  │     │  │  │     ├─ test__procrustes.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ transform
│  │     │  │  │  ├─ rotation.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ test_rotation.py
│  │     │  │  │  │  ├─ test_rotation_groups.py
│  │     │  │  │  │  ├─ test_rotation_spline.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_rotation.cpython-39.pyc
│  │     │  │  │  │     ├─ test_rotation_groups.cpython-39.pyc
│  │     │  │  │  │     ├─ test_rotation_spline.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _rotation.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _rotation.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _rotation.pyi
│  │     │  │  │  ├─ _rotation_groups.py
│  │     │  │  │  ├─ _rotation_spline.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ rotation.cpython-39.pyc
│  │     │  │  │     ├─ _rotation_groups.cpython-39.pyc
│  │     │  │  │     ├─ _rotation_spline.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _ckdtree.cp39-win_amd64.dll.a
│  │     │  │  ├─ _ckdtree.cp39-win_amd64.pyd
│  │     │  │  ├─ _ckdtree.pyi
│  │     │  │  ├─ _distance_pybind.cp39-win_amd64.dll.a
│  │     │  │  ├─ _distance_pybind.cp39-win_amd64.pyd
│  │     │  │  ├─ _distance_wrap.cp39-win_amd64.dll.a
│  │     │  │  ├─ _distance_wrap.cp39-win_amd64.pyd
│  │     │  │  ├─ _geometric_slerp.py
│  │     │  │  ├─ _hausdorff.cp39-win_amd64.dll.a
│  │     │  │  ├─ _hausdorff.cp39-win_amd64.pyd
│  │     │  │  ├─ _kdtree.py
│  │     │  │  ├─ _plotutils.py
│  │     │  │  ├─ _procrustes.py
│  │     │  │  ├─ _qhull.cp39-win_amd64.dll.a
│  │     │  │  ├─ _qhull.cp39-win_amd64.pyd
│  │     │  │  ├─ _qhull.pyi
│  │     │  │  ├─ _spherical_voronoi.py
│  │     │  │  ├─ _voronoi.cp39-win_amd64.dll.a
│  │     │  │  ├─ _voronoi.cp39-win_amd64.pyd
│  │     │  │  ├─ _voronoi.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ckdtree.cpython-39.pyc
│  │     │  │     ├─ distance.cpython-39.pyc
│  │     │  │     ├─ kdtree.cpython-39.pyc
│  │     │  │     ├─ qhull.cpython-39.pyc
│  │     │  │     ├─ _geometric_slerp.cpython-39.pyc
│  │     │  │     ├─ _kdtree.cpython-39.pyc
│  │     │  │     ├─ _plotutils.cpython-39.pyc
│  │     │  │     ├─ _procrustes.cpython-39.pyc
│  │     │  │     ├─ _spherical_voronoi.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ special
│  │     │  │  ├─ add_newdocs.py
│  │     │  │  ├─ basic.py
│  │     │  │  ├─ cython_special.cp39-win_amd64.dll.a
│  │     │  │  ├─ cython_special.cp39-win_amd64.pyd
│  │     │  │  ├─ cython_special.pxd
│  │     │  │  ├─ cython_special.pyi
│  │     │  │  ├─ cython_special.pyx
│  │     │  │  ├─ orthogonal.py
│  │     │  │  ├─ sf_error.py
│  │     │  │  ├─ specfun.py
│  │     │  │  ├─ spfun_stats.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ boost.npz
│  │     │  │  │  │  ├─ gsl.npz
│  │     │  │  │  │  └─ local.npz
│  │     │  │  │  ├─ test_basic.py
│  │     │  │  │  ├─ test_bdtr.py
│  │     │  │  │  ├─ test_boxcox.py
│  │     │  │  │  ├─ test_cdflib.py
│  │     │  │  │  ├─ test_cdft_asymptotic.py
│  │     │  │  │  ├─ test_cosine_distr.py
│  │     │  │  │  ├─ test_cython_special.py
│  │     │  │  │  ├─ test_data.py
│  │     │  │  │  ├─ test_dd.py
│  │     │  │  │  ├─ test_digamma.py
│  │     │  │  │  ├─ test_ellip_harm.py
│  │     │  │  │  ├─ test_erfinv.py
│  │     │  │  │  ├─ test_exponential_integrals.py
│  │     │  │  │  ├─ test_faddeeva.py
│  │     │  │  │  ├─ test_gamma.py
│  │     │  │  │  ├─ test_gammainc.py
│  │     │  │  │  ├─ test_hyp2f1.py
│  │     │  │  │  ├─ test_hypergeometric.py
│  │     │  │  │  ├─ test_kolmogorov.py
│  │     │  │  │  ├─ test_lambertw.py
│  │     │  │  │  ├─ test_loggamma.py
│  │     │  │  │  ├─ test_logit.py
│  │     │  │  │  ├─ test_logsumexp.py
│  │     │  │  │  ├─ test_log_softmax.py
│  │     │  │  │  ├─ test_mpmath.py
│  │     │  │  │  ├─ test_nan_inputs.py
│  │     │  │  │  ├─ test_ndtr.py
│  │     │  │  │  ├─ test_ndtri_exp.py
│  │     │  │  │  ├─ test_orthogonal.py
│  │     │  │  │  ├─ test_orthogonal_eval.py
│  │     │  │  │  ├─ test_owens_t.py
│  │     │  │  │  ├─ test_pcf.py
│  │     │  │  │  ├─ test_pdtr.py
│  │     │  │  │  ├─ test_powm1.py
│  │     │  │  │  ├─ test_precompute_expn_asy.py
│  │     │  │  │  ├─ test_precompute_gammainc.py
│  │     │  │  │  ├─ test_precompute_utils.py
│  │     │  │  │  ├─ test_round.py
│  │     │  │  │  ├─ test_sf_error.py
│  │     │  │  │  ├─ test_sici.py
│  │     │  │  │  ├─ test_spence.py
│  │     │  │  │  ├─ test_spfun_stats.py
│  │     │  │  │  ├─ test_spherical_bessel.py
│  │     │  │  │  ├─ test_sph_harm.py
│  │     │  │  │  ├─ test_trig.py
│  │     │  │  │  ├─ test_wrightomega.py
│  │     │  │  │  ├─ test_wright_bessel.py
│  │     │  │  │  ├─ test_zeta.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_basic.cpython-39.pyc
│  │     │  │  │     ├─ test_bdtr.cpython-39.pyc
│  │     │  │  │     ├─ test_boxcox.cpython-39.pyc
│  │     │  │  │     ├─ test_cdflib.cpython-39.pyc
│  │     │  │  │     ├─ test_cdft_asymptotic.cpython-39.pyc
│  │     │  │  │     ├─ test_cosine_distr.cpython-39.pyc
│  │     │  │  │     ├─ test_cython_special.cpython-39.pyc
│  │     │  │  │     ├─ test_data.cpython-39.pyc
│  │     │  │  │     ├─ test_dd.cpython-39.pyc
│  │     │  │  │     ├─ test_digamma.cpython-39.pyc
│  │     │  │  │     ├─ test_ellip_harm.cpython-39.pyc
│  │     │  │  │     ├─ test_erfinv.cpython-39.pyc
│  │     │  │  │     ├─ test_exponential_integrals.cpython-39.pyc
│  │     │  │  │     ├─ test_faddeeva.cpython-39.pyc
│  │     │  │  │     ├─ test_gamma.cpython-39.pyc
│  │     │  │  │     ├─ test_gammainc.cpython-39.pyc
│  │     │  │  │     ├─ test_hyp2f1.cpython-39.pyc
│  │     │  │  │     ├─ test_hypergeometric.cpython-39.pyc
│  │     │  │  │     ├─ test_kolmogorov.cpython-39.pyc
│  │     │  │  │     ├─ test_lambertw.cpython-39.pyc
│  │     │  │  │     ├─ test_loggamma.cpython-39.pyc
│  │     │  │  │     ├─ test_logit.cpython-39.pyc
│  │     │  │  │     ├─ test_logsumexp.cpython-39.pyc
│  │     │  │  │     ├─ test_log_softmax.cpython-39.pyc
│  │     │  │  │     ├─ test_mpmath.cpython-39.pyc
│  │     │  │  │     ├─ test_nan_inputs.cpython-39.pyc
│  │     │  │  │     ├─ test_ndtr.cpython-39.pyc
│  │     │  │  │     ├─ test_ndtri_exp.cpython-39.pyc
│  │     │  │  │     ├─ test_orthogonal.cpython-39.pyc
│  │     │  │  │     ├─ test_orthogonal_eval.cpython-39.pyc
│  │     │  │  │     ├─ test_owens_t.cpython-39.pyc
│  │     │  │  │     ├─ test_pcf.cpython-39.pyc
│  │     │  │  │     ├─ test_pdtr.cpython-39.pyc
│  │     │  │  │     ├─ test_powm1.cpython-39.pyc
│  │     │  │  │     ├─ test_precompute_expn_asy.cpython-39.pyc
│  │     │  │  │     ├─ test_precompute_gammainc.cpython-39.pyc
│  │     │  │  │     ├─ test_precompute_utils.cpython-39.pyc
│  │     │  │  │     ├─ test_round.cpython-39.pyc
│  │     │  │  │     ├─ test_sf_error.cpython-39.pyc
│  │     │  │  │     ├─ test_sici.cpython-39.pyc
│  │     │  │  │     ├─ test_spence.cpython-39.pyc
│  │     │  │  │     ├─ test_spfun_stats.cpython-39.pyc
│  │     │  │  │     ├─ test_spherical_bessel.cpython-39.pyc
│  │     │  │  │     ├─ test_sph_harm.cpython-39.pyc
│  │     │  │  │     ├─ test_trig.cpython-39.pyc
│  │     │  │  │     ├─ test_wrightomega.cpython-39.pyc
│  │     │  │  │     ├─ test_wright_bessel.cpython-39.pyc
│  │     │  │  │     ├─ test_zeta.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _add_newdocs.py
│  │     │  │  ├─ _basic.py
│  │     │  │  ├─ _comb.cp39-win_amd64.dll.a
│  │     │  │  ├─ _comb.cp39-win_amd64.pyd
│  │     │  │  ├─ _ellip_harm.py
│  │     │  │  ├─ _ellip_harm_2.cp39-win_amd64.dll.a
│  │     │  │  ├─ _ellip_harm_2.cp39-win_amd64.pyd
│  │     │  │  ├─ _lambertw.py
│  │     │  │  ├─ _logsumexp.py
│  │     │  │  ├─ _mptestutils.py
│  │     │  │  ├─ _orthogonal.py
│  │     │  │  ├─ _orthogonal.pyi
│  │     │  │  ├─ _precompute
│  │     │  │  │  ├─ cosine_cdf.py
│  │     │  │  │  ├─ expn_asy.py
│  │     │  │  │  ├─ gammainc_asy.py
│  │     │  │  │  ├─ gammainc_data.py
│  │     │  │  │  ├─ lambertw.py
│  │     │  │  │  ├─ loggamma.py
│  │     │  │  │  ├─ struve_convergence.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ wrightomega.py
│  │     │  │  │  ├─ wright_bessel.py
│  │     │  │  │  ├─ wright_bessel_data.py
│  │     │  │  │  ├─ zetac.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cosine_cdf.cpython-39.pyc
│  │     │  │  │     ├─ expn_asy.cpython-39.pyc
│  │     │  │  │     ├─ gammainc_asy.cpython-39.pyc
│  │     │  │  │     ├─ gammainc_data.cpython-39.pyc
│  │     │  │  │     ├─ lambertw.cpython-39.pyc
│  │     │  │  │     ├─ loggamma.cpython-39.pyc
│  │     │  │  │     ├─ struve_convergence.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     ├─ wrightomega.cpython-39.pyc
│  │     │  │  │     ├─ wright_bessel.cpython-39.pyc
│  │     │  │  │     ├─ wright_bessel_data.cpython-39.pyc
│  │     │  │  │     ├─ zetac.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _sf_error.py
│  │     │  │  ├─ _specfun.cp39-win_amd64.dll.a
│  │     │  │  ├─ _specfun.cp39-win_amd64.pyd
│  │     │  │  ├─ _spfun_stats.py
│  │     │  │  ├─ _spherical_bessel.py
│  │     │  │  ├─ _testutils.py
│  │     │  │  ├─ _test_internal.cp39-win_amd64.dll.a
│  │     │  │  ├─ _test_internal.cp39-win_amd64.pyd
│  │     │  │  ├─ _test_internal.pyi
│  │     │  │  ├─ _ufuncs.cp39-win_amd64.dll.a
│  │     │  │  ├─ _ufuncs.cp39-win_amd64.pyd
│  │     │  │  ├─ _ufuncs.pyi
│  │     │  │  ├─ _ufuncs.pyx
│  │     │  │  ├─ _ufuncs_cxx.cp39-win_amd64.dll.a
│  │     │  │  ├─ _ufuncs_cxx.cp39-win_amd64.pyd
│  │     │  │  ├─ _ufuncs_cxx.pxd
│  │     │  │  ├─ _ufuncs_cxx.pyx
│  │     │  │  ├─ _ufuncs_cxx_defs.h
│  │     │  │  ├─ _ufuncs_defs.h
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ add_newdocs.cpython-39.pyc
│  │     │  │     ├─ basic.cpython-39.pyc
│  │     │  │     ├─ orthogonal.cpython-39.pyc
│  │     │  │     ├─ sf_error.cpython-39.pyc
│  │     │  │     ├─ specfun.cpython-39.pyc
│  │     │  │     ├─ spfun_stats.cpython-39.pyc
│  │     │  │     ├─ _add_newdocs.cpython-39.pyc
│  │     │  │     ├─ _basic.cpython-39.pyc
│  │     │  │     ├─ _ellip_harm.cpython-39.pyc
│  │     │  │     ├─ _lambertw.cpython-39.pyc
│  │     │  │     ├─ _logsumexp.cpython-39.pyc
│  │     │  │     ├─ _mptestutils.cpython-39.pyc
│  │     │  │     ├─ _orthogonal.cpython-39.pyc
│  │     │  │     ├─ _sf_error.cpython-39.pyc
│  │     │  │     ├─ _spfun_stats.cpython-39.pyc
│  │     │  │     ├─ _spherical_bessel.cpython-39.pyc
│  │     │  │     ├─ _testutils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ special.pxd
│  │     │  ├─ stats
│  │     │  │  ├─ biasedurn.py
│  │     │  │  ├─ contingency.py
│  │     │  │  ├─ distributions.py
│  │     │  │  ├─ kde.py
│  │     │  │  ├─ morestats.py
│  │     │  │  ├─ mstats.py
│  │     │  │  ├─ mstats_basic.py
│  │     │  │  ├─ mstats_extras.py
│  │     │  │  ├─ mvn.py
│  │     │  │  ├─ qmc.py
│  │     │  │  ├─ sampling.py
│  │     │  │  ├─ statlib.py
│  │     │  │  ├─ stats.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ common_tests.py
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ fisher_exact_results_from_r.py
│  │     │  │  │  │  ├─ levy_stable
│  │     │  │  │  │  │  ├─ stable-loc-scale-sample-data.npy
│  │     │  │  │  │  │  ├─ stable-Z1-cdf-sample-data.npy
│  │     │  │  │  │  │  └─ stable-Z1-pdf-sample-data.npy
│  │     │  │  │  │  ├─ nist_anova
│  │     │  │  │  │  │  ├─ AtmWtAg.dat
│  │     │  │  │  │  │  ├─ SiRstv.dat
│  │     │  │  │  │  │  ├─ SmLs01.dat
│  │     │  │  │  │  │  ├─ SmLs02.dat
│  │     │  │  │  │  │  ├─ SmLs03.dat
│  │     │  │  │  │  │  ├─ SmLs04.dat
│  │     │  │  │  │  │  ├─ SmLs05.dat
│  │     │  │  │  │  │  ├─ SmLs06.dat
│  │     │  │  │  │  │  ├─ SmLs07.dat
│  │     │  │  │  │  │  ├─ SmLs08.dat
│  │     │  │  │  │  │  └─ SmLs09.dat
│  │     │  │  │  │  ├─ nist_linregress
│  │     │  │  │  │  │  └─ Norris.dat
│  │     │  │  │  │  ├─ studentized_range_mpmath_ref.json
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ fisher_exact_results_from_r.cpython-39.pyc
│  │     │  │  │  ├─ test_axis_nan_policy.py
│  │     │  │  │  ├─ test_binned_statistic.py
│  │     │  │  │  ├─ test_boost_ufuncs.py
│  │     │  │  │  ├─ test_contingency.py
│  │     │  │  │  ├─ test_continuous_basic.py
│  │     │  │  │  ├─ test_crosstab.py
│  │     │  │  │  ├─ test_discrete_basic.py
│  │     │  │  │  ├─ test_discrete_distns.py
│  │     │  │  │  ├─ test_distributions.py
│  │     │  │  │  ├─ test_entropy.py
│  │     │  │  │  ├─ test_fit.py
│  │     │  │  │  ├─ test_hypotests.py
│  │     │  │  │  ├─ test_kdeoth.py
│  │     │  │  │  ├─ test_morestats.py
│  │     │  │  │  ├─ test_mstats_basic.py
│  │     │  │  │  ├─ test_mstats_extras.py
│  │     │  │  │  ├─ test_multivariate.py
│  │     │  │  │  ├─ test_odds_ratio.py
│  │     │  │  │  ├─ test_qmc.py
│  │     │  │  │  ├─ test_rank.py
│  │     │  │  │  ├─ test_relative_risk.py
│  │     │  │  │  ├─ test_resampling.py
│  │     │  │  │  ├─ test_sampling.py
│  │     │  │  │  ├─ test_stats.py
│  │     │  │  │  ├─ test_tukeylambda_stats.py
│  │     │  │  │  ├─ test_variation.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ common_tests.cpython-39.pyc
│  │     │  │  │     ├─ test_axis_nan_policy.cpython-39.pyc
│  │     │  │  │     ├─ test_binned_statistic.cpython-39.pyc
│  │     │  │  │     ├─ test_boost_ufuncs.cpython-39.pyc
│  │     │  │  │     ├─ test_contingency.cpython-39.pyc
│  │     │  │  │     ├─ test_continuous_basic.cpython-39.pyc
│  │     │  │  │     ├─ test_crosstab.cpython-39.pyc
│  │     │  │  │     ├─ test_discrete_basic.cpython-39.pyc
│  │     │  │  │     ├─ test_discrete_distns.cpython-39.pyc
│  │     │  │  │     ├─ test_distributions.cpython-39.pyc
│  │     │  │  │     ├─ test_entropy.cpython-39.pyc
│  │     │  │  │     ├─ test_fit.cpython-39.pyc
│  │     │  │  │     ├─ test_hypotests.cpython-39.pyc
│  │     │  │  │     ├─ test_kdeoth.cpython-39.pyc
│  │     │  │  │     ├─ test_morestats.cpython-39.pyc
│  │     │  │  │     ├─ test_mstats_basic.cpython-39.pyc
│  │     │  │  │     ├─ test_mstats_extras.cpython-39.pyc
│  │     │  │  │     ├─ test_multivariate.cpython-39.pyc
│  │     │  │  │     ├─ test_odds_ratio.cpython-39.pyc
│  │     │  │  │     ├─ test_qmc.cpython-39.pyc
│  │     │  │  │     ├─ test_rank.cpython-39.pyc
│  │     │  │  │     ├─ test_relative_risk.cpython-39.pyc
│  │     │  │  │     ├─ test_resampling.cpython-39.pyc
│  │     │  │  │     ├─ test_sampling.cpython-39.pyc
│  │     │  │  │     ├─ test_stats.cpython-39.pyc
│  │     │  │  │     ├─ test_tukeylambda_stats.cpython-39.pyc
│  │     │  │  │     ├─ test_variation.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _axis_nan_policy.py
│  │     │  │  ├─ _biasedurn.cp39-win_amd64.dll.a
│  │     │  │  ├─ _biasedurn.cp39-win_amd64.pyd
│  │     │  │  ├─ _biasedurn.pxd
│  │     │  │  ├─ _binned_statistic.py
│  │     │  │  ├─ _binomtest.py
│  │     │  │  ├─ _boost
│  │     │  │  │  ├─ beta_ufunc.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ beta_ufunc.cp39-win_amd64.pyd
│  │     │  │  │  ├─ binom_ufunc.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ binom_ufunc.cp39-win_amd64.pyd
│  │     │  │  │  ├─ hypergeom_ufunc.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ hypergeom_ufunc.cp39-win_amd64.pyd
│  │     │  │  │  ├─ invgauss_ufunc.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ invgauss_ufunc.cp39-win_amd64.pyd
│  │     │  │  │  ├─ nbinom_ufunc.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ nbinom_ufunc.cp39-win_amd64.pyd
│  │     │  │  │  ├─ ncf_ufunc.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ ncf_ufunc.cp39-win_amd64.pyd
│  │     │  │  │  ├─ nct_ufunc.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ nct_ufunc.cp39-win_amd64.pyd
│  │     │  │  │  ├─ ncx2_ufunc.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ ncx2_ufunc.cp39-win_amd64.pyd
│  │     │  │  │  ├─ skewnorm_ufunc.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ skewnorm_ufunc.cp39-win_amd64.pyd
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _common.py
│  │     │  │  ├─ _constants.py
│  │     │  │  ├─ _continuous_distns.py
│  │     │  │  ├─ _covariance.py
│  │     │  │  ├─ _crosstab.py
│  │     │  │  ├─ _discrete_distns.py
│  │     │  │  ├─ _distn_infrastructure.py
│  │     │  │  ├─ _distr_params.py
│  │     │  │  ├─ _entropy.py
│  │     │  │  ├─ _fit.py
│  │     │  │  ├─ _generate_pyx.py
│  │     │  │  ├─ _hypotests.py
│  │     │  │  ├─ _kde.py
│  │     │  │  ├─ _ksstats.py
│  │     │  │  ├─ _levy_stable
│  │     │  │  │  ├─ levyst.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ levyst.cp39-win_amd64.pyd
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _mannwhitneyu.py
│  │     │  │  ├─ _morestats.py
│  │     │  │  ├─ _mstats_basic.py
│  │     │  │  ├─ _mstats_extras.py
│  │     │  │  ├─ _multivariate.py
│  │     │  │  ├─ _mvn.cp39-win_amd64.dll.a
│  │     │  │  ├─ _mvn.cp39-win_amd64.pyd
│  │     │  │  ├─ _odds_ratio.py
│  │     │  │  ├─ _page_trend_test.py
│  │     │  │  ├─ _qmc.py
│  │     │  │  ├─ _qmc_cy.cp39-win_amd64.dll.a
│  │     │  │  ├─ _qmc_cy.cp39-win_amd64.pyd
│  │     │  │  ├─ _qmc_cy.pyi
│  │     │  │  ├─ _rcont
│  │     │  │  │  ├─ rcont.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ rcont.cp39-win_amd64.pyd
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _relative_risk.py
│  │     │  │  ├─ _resampling.py
│  │     │  │  ├─ _result_classes.py
│  │     │  │  ├─ _rvs_sampling.py
│  │     │  │  ├─ _sobol.cp39-win_amd64.dll.a
│  │     │  │  ├─ _sobol.cp39-win_amd64.pyd
│  │     │  │  ├─ _sobol.pyi
│  │     │  │  ├─ _sobol_direction_numbers.npz
│  │     │  │  ├─ _statlib.cp39-win_amd64.dll.a
│  │     │  │  ├─ _statlib.cp39-win_amd64.pyd
│  │     │  │  ├─ _stats.cp39-win_amd64.dll.a
│  │     │  │  ├─ _stats.cp39-win_amd64.pyd
│  │     │  │  ├─ _stats.pxd
│  │     │  │  ├─ _stats_mstats_common.py
│  │     │  │  ├─ _stats_py.py
│  │     │  │  ├─ _stats_pythran.cp39-win_amd64.dll.a
│  │     │  │  ├─ _stats_pythran.cp39-win_amd64.pyd
│  │     │  │  ├─ _tukeylambda_stats.py
│  │     │  │  ├─ _unuran
│  │     │  │  │  ├─ unuran.pxd
│  │     │  │  │  ├─ unuran_wrapper.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ unuran_wrapper.cp39-win_amd64.pyd
│  │     │  │  │  ├─ unuran_wrapper.pyi
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _variation.py
│  │     │  │  ├─ _warnings_errors.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ biasedurn.cpython-39.pyc
│  │     │  │     ├─ contingency.cpython-39.pyc
│  │     │  │     ├─ distributions.cpython-39.pyc
│  │     │  │     ├─ kde.cpython-39.pyc
│  │     │  │     ├─ morestats.cpython-39.pyc
│  │     │  │     ├─ mstats.cpython-39.pyc
│  │     │  │     ├─ mstats_basic.cpython-39.pyc
│  │     │  │     ├─ mstats_extras.cpython-39.pyc
│  │     │  │     ├─ mvn.cpython-39.pyc
│  │     │  │     ├─ qmc.cpython-39.pyc
│  │     │  │     ├─ sampling.cpython-39.pyc
│  │     │  │     ├─ statlib.cpython-39.pyc
│  │     │  │     ├─ stats.cpython-39.pyc
│  │     │  │     ├─ _axis_nan_policy.cpython-39.pyc
│  │     │  │     ├─ _binned_statistic.cpython-39.pyc
│  │     │  │     ├─ _binomtest.cpython-39.pyc
│  │     │  │     ├─ _common.cpython-39.pyc
│  │     │  │     ├─ _constants.cpython-39.pyc
│  │     │  │     ├─ _continuous_distns.cpython-39.pyc
│  │     │  │     ├─ _covariance.cpython-39.pyc
│  │     │  │     ├─ _crosstab.cpython-39.pyc
│  │     │  │     ├─ _discrete_distns.cpython-39.pyc
│  │     │  │     ├─ _distn_infrastructure.cpython-39.pyc
│  │     │  │     ├─ _distr_params.cpython-39.pyc
│  │     │  │     ├─ _entropy.cpython-39.pyc
│  │     │  │     ├─ _fit.cpython-39.pyc
│  │     │  │     ├─ _generate_pyx.cpython-39.pyc
│  │     │  │     ├─ _hypotests.cpython-39.pyc
│  │     │  │     ├─ _kde.cpython-39.pyc
│  │     │  │     ├─ _ksstats.cpython-39.pyc
│  │     │  │     ├─ _mannwhitneyu.cpython-39.pyc
│  │     │  │     ├─ _morestats.cpython-39.pyc
│  │     │  │     ├─ _mstats_basic.cpython-39.pyc
│  │     │  │     ├─ _mstats_extras.cpython-39.pyc
│  │     │  │     ├─ _multivariate.cpython-39.pyc
│  │     │  │     ├─ _odds_ratio.cpython-39.pyc
│  │     │  │     ├─ _page_trend_test.cpython-39.pyc
│  │     │  │     ├─ _qmc.cpython-39.pyc
│  │     │  │     ├─ _relative_risk.cpython-39.pyc
│  │     │  │     ├─ _resampling.cpython-39.pyc
│  │     │  │     ├─ _result_classes.cpython-39.pyc
│  │     │  │     ├─ _rvs_sampling.cpython-39.pyc
│  │     │  │     ├─ _stats_mstats_common.cpython-39.pyc
│  │     │  │     ├─ _stats_py.cpython-39.pyc
│  │     │  │     ├─ _tukeylambda_stats.cpython-39.pyc
│  │     │  │     ├─ _variation.cpython-39.pyc
│  │     │  │     ├─ _warnings_errors.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ version.py
│  │     │  ├─ _distributor_init.py
│  │     │  ├─ _lib
│  │     │  │  ├─ decorator.py
│  │     │  │  ├─ deprecation.py
│  │     │  │  ├─ doccer.py
│  │     │  │  ├─ messagestream.cp39-win_amd64.dll.a
│  │     │  │  ├─ messagestream.cp39-win_amd64.pyd
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_bunch.py
│  │     │  │  │  ├─ test_ccallback.py
│  │     │  │  │  ├─ test_deprecation.py
│  │     │  │  │  ├─ test_import_cycles.py
│  │     │  │  │  ├─ test_public_api.py
│  │     │  │  │  ├─ test_scipy_version.py
│  │     │  │  │  ├─ test_tmpdirs.py
│  │     │  │  │  ├─ test_warnings.py
│  │     │  │  │  ├─ test__gcutils.py
│  │     │  │  │  ├─ test__pep440.py
│  │     │  │  │  ├─ test__testutils.py
│  │     │  │  │  ├─ test__threadsafety.py
│  │     │  │  │  ├─ test__util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_bunch.cpython-39.pyc
│  │     │  │  │     ├─ test_ccallback.cpython-39.pyc
│  │     │  │  │     ├─ test_deprecation.cpython-39.pyc
│  │     │  │  │     ├─ test_import_cycles.cpython-39.pyc
│  │     │  │  │     ├─ test_public_api.cpython-39.pyc
│  │     │  │  │     ├─ test_scipy_version.cpython-39.pyc
│  │     │  │  │     ├─ test_tmpdirs.cpython-39.pyc
│  │     │  │  │     ├─ test_warnings.cpython-39.pyc
│  │     │  │  │     ├─ test__gcutils.cpython-39.pyc
│  │     │  │  │     ├─ test__pep440.cpython-39.pyc
│  │     │  │  │     ├─ test__testutils.cpython-39.pyc
│  │     │  │  │     ├─ test__threadsafety.cpython-39.pyc
│  │     │  │  │     ├─ test__util.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ uarray.py
│  │     │  │  ├─ _bunch.py
│  │     │  │  ├─ _ccallback.py
│  │     │  │  ├─ _ccallback_c.cp39-win_amd64.dll.a
│  │     │  │  ├─ _ccallback_c.cp39-win_amd64.pyd
│  │     │  │  ├─ _disjoint_set.py
│  │     │  │  ├─ _docscrape.py
│  │     │  │  ├─ _finite_differences.py
│  │     │  │  ├─ _fpumode.cp39-win_amd64.dll.a
│  │     │  │  ├─ _fpumode.cp39-win_amd64.pyd
│  │     │  │  ├─ _gcutils.py
│  │     │  │  ├─ _pep440.py
│  │     │  │  ├─ _testutils.py
│  │     │  │  ├─ _test_ccallback.cp39-win_amd64.dll.a
│  │     │  │  ├─ _test_ccallback.cp39-win_amd64.pyd
│  │     │  │  ├─ _test_deprecation_call.cp39-win_amd64.dll.a
│  │     │  │  ├─ _test_deprecation_call.cp39-win_amd64.pyd
│  │     │  │  ├─ _test_deprecation_def.cp39-win_amd64.dll.a
│  │     │  │  ├─ _test_deprecation_def.cp39-win_amd64.pyd
│  │     │  │  ├─ _threadsafety.py
│  │     │  │  ├─ _tmpdirs.py
│  │     │  │  ├─ _uarray
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ _backend.py
│  │     │  │  │  ├─ _uarray.cp39-win_amd64.dll.a
│  │     │  │  │  ├─ _uarray.cp39-win_amd64.pyd
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _backend.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ decorator.cpython-39.pyc
│  │     │  │     ├─ deprecation.cpython-39.pyc
│  │     │  │     ├─ doccer.cpython-39.pyc
│  │     │  │     ├─ uarray.cpython-39.pyc
│  │     │  │     ├─ _bunch.cpython-39.pyc
│  │     │  │     ├─ _ccallback.cpython-39.pyc
│  │     │  │     ├─ _disjoint_set.cpython-39.pyc
│  │     │  │     ├─ _docscrape.cpython-39.pyc
│  │     │  │     ├─ _finite_differences.cpython-39.pyc
│  │     │  │     ├─ _gcutils.cpython-39.pyc
│  │     │  │     ├─ _pep440.cpython-39.pyc
│  │     │  │     ├─ _testutils.cpython-39.pyc
│  │     │  │     ├─ _threadsafety.cpython-39.pyc
│  │     │  │     ├─ _tmpdirs.cpython-39.pyc
│  │     │  │     ├─ _util.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __config__.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ conftest.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     ├─ _distributor_init.cpython-39.pyc
│  │     │     ├─ __config__.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ scipy-1.10.1-cp39-cp39-win_amd64.whl
│  │     ├─ scipy-1.10.1.dist-info
│  │     │  ├─ DELVEWHEEL
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ scipy.libs
│  │     │  ├─ .load-order-scipy-1.10.1
│  │     │  └─ libopenblas-802f9ed1179cb9c9b03d67ff79f48187.dll
│  │     ├─ seaborn
│  │     │  ├─ algorithms.py
│  │     │  ├─ axisgrid.py
│  │     │  ├─ categorical.py
│  │     │  ├─ cm.py
│  │     │  ├─ colors
│  │     │  │  ├─ crayons.py
│  │     │  │  ├─ xkcd_rgb.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ crayons.cpython-39.pyc
│  │     │  │     ├─ xkcd_rgb.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ distributions.py
│  │     │  ├─ external
│  │     │  │  ├─ appdirs.py
│  │     │  │  ├─ docscrape.py
│  │     │  │  ├─ husl.py
│  │     │  │  ├─ kde.py
│  │     │  │  ├─ version.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ appdirs.cpython-39.pyc
│  │     │  │     ├─ docscrape.cpython-39.pyc
│  │     │  │     ├─ husl.cpython-39.pyc
│  │     │  │     ├─ kde.cpython-39.pyc
│  │     │  │     ├─ version.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ matrix.py
│  │     │  ├─ miscplot.py
│  │     │  ├─ objects.py
│  │     │  ├─ palettes.py
│  │     │  ├─ rcmod.py
│  │     │  ├─ regression.py
│  │     │  ├─ relational.py
│  │     │  ├─ utils.py
│  │     │  ├─ widgets.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _core
│  │     │  │  ├─ data.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ groupby.py
│  │     │  │  ├─ moves.py
│  │     │  │  ├─ plot.py
│  │     │  │  ├─ properties.py
│  │     │  │  ├─ rules.py
│  │     │  │  ├─ scales.py
│  │     │  │  ├─ subplots.py
│  │     │  │  ├─ typing.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ data.cpython-39.pyc
│  │     │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │     ├─ groupby.cpython-39.pyc
│  │     │  │     ├─ moves.cpython-39.pyc
│  │     │  │     ├─ plot.cpython-39.pyc
│  │     │  │     ├─ properties.cpython-39.pyc
│  │     │  │     ├─ rules.cpython-39.pyc
│  │     │  │     ├─ scales.cpython-39.pyc
│  │     │  │     ├─ subplots.cpython-39.pyc
│  │     │  │     ├─ typing.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _decorators.py
│  │     │  ├─ _docstrings.py
│  │     │  ├─ _marks
│  │     │  │  ├─ area.py
│  │     │  │  ├─ bar.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ dot.py
│  │     │  │  ├─ line.py
│  │     │  │  ├─ text.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ area.cpython-39.pyc
│  │     │  │     ├─ bar.cpython-39.pyc
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ dot.cpython-39.pyc
│  │     │  │     ├─ line.cpython-39.pyc
│  │     │  │     ├─ text.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _oldcore.py
│  │     │  ├─ _statistics.py
│  │     │  ├─ _stats
│  │     │  │  ├─ aggregation.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ counting.py
│  │     │  │  ├─ density.py
│  │     │  │  ├─ order.py
│  │     │  │  ├─ regression.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ aggregation.cpython-39.pyc
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ counting.cpython-39.pyc
│  │     │  │     ├─ density.cpython-39.pyc
│  │     │  │     ├─ order.cpython-39.pyc
│  │     │  │     ├─ regression.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _testing.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ algorithms.cpython-39.pyc
│  │     │     ├─ axisgrid.cpython-39.pyc
│  │     │     ├─ categorical.cpython-39.pyc
│  │     │     ├─ cm.cpython-39.pyc
│  │     │     ├─ distributions.cpython-39.pyc
│  │     │     ├─ matrix.cpython-39.pyc
│  │     │     ├─ miscplot.cpython-39.pyc
│  │     │     ├─ objects.cpython-39.pyc
│  │     │     ├─ palettes.cpython-39.pyc
│  │     │     ├─ rcmod.cpython-39.pyc
│  │     │     ├─ regression.cpython-39.pyc
│  │     │     ├─ relational.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ widgets.cpython-39.pyc
│  │     │     ├─ _compat.cpython-39.pyc
│  │     │     ├─ _decorators.cpython-39.pyc
│  │     │     ├─ _docstrings.cpython-39.pyc
│  │     │     ├─ _oldcore.cpython-39.pyc
│  │     │     ├─ _statistics.cpython-39.pyc
│  │     │     ├─ _testing.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ seaborn-0.12.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ setuptools
│  │     │  ├─ archive_util.py
│  │     │  ├─ build_meta.py
│  │     │  ├─ cli-32.exe
│  │     │  ├─ cli-64.exe
│  │     │  ├─ cli.exe
│  │     │  ├─ command
│  │     │  │  ├─ alias.py
│  │     │  │  ├─ bdist_egg.py
│  │     │  │  ├─ bdist_rpm.py
│  │     │  │  ├─ build_clib.py
│  │     │  │  ├─ build_ext.py
│  │     │  │  ├─ build_py.py
│  │     │  │  ├─ develop.py
│  │     │  │  ├─ dist_info.py
│  │     │  │  ├─ easy_install.py
│  │     │  │  ├─ egg_info.py
│  │     │  │  ├─ install.py
│  │     │  │  ├─ install_egg_info.py
│  │     │  │  ├─ install_lib.py
│  │     │  │  ├─ install_scripts.py
│  │     │  │  ├─ launcher manifest.xml
│  │     │  │  ├─ py36compat.py
│  │     │  │  ├─ register.py
│  │     │  │  ├─ rotate.py
│  │     │  │  ├─ saveopts.py
│  │     │  │  ├─ sdist.py
│  │     │  │  ├─ setopt.py
│  │     │  │  ├─ test.py
│  │     │  │  ├─ upload.py
│  │     │  │  ├─ upload_docs.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ alias.cpython-39.pyc
│  │     │  │     ├─ bdist_egg.cpython-39.pyc
│  │     │  │     ├─ bdist_rpm.cpython-39.pyc
│  │     │  │     ├─ build_clib.cpython-39.pyc
│  │     │  │     ├─ build_ext.cpython-39.pyc
│  │     │  │     ├─ build_py.cpython-39.pyc
│  │     │  │     ├─ develop.cpython-39.pyc
│  │     │  │     ├─ dist_info.cpython-39.pyc
│  │     │  │     ├─ easy_install.cpython-39.pyc
│  │     │  │     ├─ egg_info.cpython-39.pyc
│  │     │  │     ├─ install.cpython-39.pyc
│  │     │  │     ├─ install_egg_info.cpython-39.pyc
│  │     │  │     ├─ install_lib.cpython-39.pyc
│  │     │  │     ├─ install_scripts.cpython-39.pyc
│  │     │  │     ├─ py36compat.cpython-39.pyc
│  │     │  │     ├─ register.cpython-39.pyc
│  │     │  │     ├─ rotate.cpython-39.pyc
│  │     │  │     ├─ saveopts.cpython-39.pyc
│  │     │  │     ├─ sdist.cpython-39.pyc
│  │     │  │     ├─ setopt.cpython-39.pyc
│  │     │  │     ├─ test.cpython-39.pyc
│  │     │  │     ├─ upload.cpython-39.pyc
│  │     │  │     ├─ upload_docs.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ config.py
│  │     │  ├─ depends.py
│  │     │  ├─ dep_util.py
│  │     │  ├─ dist.py
│  │     │  ├─ errors.py
│  │     │  ├─ extension.py
│  │     │  ├─ extern
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ glob.py
│  │     │  ├─ gui-32.exe
│  │     │  ├─ gui-64.exe
│  │     │  ├─ gui.exe
│  │     │  ├─ installer.py
│  │     │  ├─ launch.py
│  │     │  ├─ lib2to3_ex.py
│  │     │  ├─ monkey.py
│  │     │  ├─ msvc.py
│  │     │  ├─ namespaces.py
│  │     │  ├─ package_index.py
│  │     │  ├─ py34compat.py
│  │     │  ├─ sandbox.py
│  │     │  ├─ script (dev).tmpl
│  │     │  ├─ script.tmpl
│  │     │  ├─ ssl_support.py
│  │     │  ├─ unicode_utils.py
│  │     │  ├─ version.py
│  │     │  ├─ wheel.py
│  │     │  ├─ windows_support.py
│  │     │  ├─ _deprecation_warning.py
│  │     │  ├─ _distutils
│  │     │  │  ├─ archive_util.py
│  │     │  │  ├─ bcppcompiler.py
│  │     │  │  ├─ ccompiler.py
│  │     │  │  ├─ cmd.py
│  │     │  │  ├─ command
│  │     │  │  │  ├─ bdist.py
│  │     │  │  │  ├─ bdist_dumb.py
│  │     │  │  │  ├─ bdist_msi.py
│  │     │  │  │  ├─ bdist_rpm.py
│  │     │  │  │  ├─ bdist_wininst.py
│  │     │  │  │  ├─ build.py
│  │     │  │  │  ├─ build_clib.py
│  │     │  │  │  ├─ build_ext.py
│  │     │  │  │  ├─ build_py.py
│  │     │  │  │  ├─ build_scripts.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ clean.py
│  │     │  │  │  ├─ config.py
│  │     │  │  │  ├─ install.py
│  │     │  │  │  ├─ install_data.py
│  │     │  │  │  ├─ install_egg_info.py
│  │     │  │  │  ├─ install_headers.py
│  │     │  │  │  ├─ install_lib.py
│  │     │  │  │  ├─ install_scripts.py
│  │     │  │  │  ├─ py37compat.py
│  │     │  │  │  ├─ register.py
│  │     │  │  │  ├─ sdist.py
│  │     │  │  │  ├─ upload.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bdist.cpython-39.pyc
│  │     │  │  │     ├─ bdist_dumb.cpython-39.pyc
│  │     │  │  │     ├─ bdist_msi.cpython-39.pyc
│  │     │  │  │     ├─ bdist_rpm.cpython-39.pyc
│  │     │  │  │     ├─ bdist_wininst.cpython-39.pyc
│  │     │  │  │     ├─ build.cpython-39.pyc
│  │     │  │  │     ├─ build_clib.cpython-39.pyc
│  │     │  │  │     ├─ build_ext.cpython-39.pyc
│  │     │  │  │     ├─ build_py.cpython-39.pyc
│  │     │  │  │     ├─ build_scripts.cpython-39.pyc
│  │     │  │  │     ├─ check.cpython-39.pyc
│  │     │  │  │     ├─ clean.cpython-39.pyc
│  │     │  │  │     ├─ config.cpython-39.pyc
│  │     │  │  │     ├─ install.cpython-39.pyc
│  │     │  │  │     ├─ install_data.cpython-39.pyc
│  │     │  │  │     ├─ install_egg_info.cpython-39.pyc
│  │     │  │  │     ├─ install_headers.cpython-39.pyc
│  │     │  │  │     ├─ install_lib.cpython-39.pyc
│  │     │  │  │     ├─ install_scripts.cpython-39.pyc
│  │     │  │  │     ├─ py37compat.cpython-39.pyc
│  │     │  │  │     ├─ register.cpython-39.pyc
│  │     │  │  │     ├─ sdist.cpython-39.pyc
│  │     │  │  │     ├─ upload.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ config.py
│  │     │  │  ├─ core.py
│  │     │  │  ├─ cygwinccompiler.py
│  │     │  │  ├─ debug.py
│  │     │  │  ├─ dep_util.py
│  │     │  │  ├─ dir_util.py
│  │     │  │  ├─ dist.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ extension.py
│  │     │  │  ├─ fancy_getopt.py
│  │     │  │  ├─ filelist.py
│  │     │  │  ├─ file_util.py
│  │     │  │  ├─ log.py
│  │     │  │  ├─ msvc9compiler.py
│  │     │  │  ├─ msvccompiler.py
│  │     │  │  ├─ py35compat.py
│  │     │  │  ├─ py38compat.py
│  │     │  │  ├─ spawn.py
│  │     │  │  ├─ sysconfig.py
│  │     │  │  ├─ text_file.py
│  │     │  │  ├─ unixccompiler.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ version.py
│  │     │  │  ├─ versionpredicate.py
│  │     │  │  ├─ _msvccompiler.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ archive_util.cpython-39.pyc
│  │     │  │     ├─ bcppcompiler.cpython-39.pyc
│  │     │  │     ├─ ccompiler.cpython-39.pyc
│  │     │  │     ├─ cmd.cpython-39.pyc
│  │     │  │     ├─ config.cpython-39.pyc
│  │     │  │     ├─ core.cpython-39.pyc
│  │     │  │     ├─ cygwinccompiler.cpython-39.pyc
│  │     │  │     ├─ debug.cpython-39.pyc
│  │     │  │     ├─ dep_util.cpython-39.pyc
│  │     │  │     ├─ dir_util.cpython-39.pyc
│  │     │  │     ├─ dist.cpython-39.pyc
│  │     │  │     ├─ errors.cpython-39.pyc
│  │     │  │     ├─ extension.cpython-39.pyc
│  │     │  │     ├─ fancy_getopt.cpython-39.pyc
│  │     │  │     ├─ filelist.cpython-39.pyc
│  │     │  │     ├─ file_util.cpython-39.pyc
│  │     │  │     ├─ log.cpython-39.pyc
│  │     │  │     ├─ msvc9compiler.cpython-39.pyc
│  │     │  │     ├─ msvccompiler.cpython-39.pyc
│  │     │  │     ├─ py35compat.cpython-39.pyc
│  │     │  │     ├─ py38compat.cpython-39.pyc
│  │     │  │     ├─ spawn.cpython-39.pyc
│  │     │  │     ├─ sysconfig.cpython-39.pyc
│  │     │  │     ├─ text_file.cpython-39.pyc
│  │     │  │     ├─ unixccompiler.cpython-39.pyc
│  │     │  │     ├─ util.cpython-39.pyc
│  │     │  │     ├─ version.cpython-39.pyc
│  │     │  │     ├─ versionpredicate.cpython-39.pyc
│  │     │  │     ├─ _msvccompiler.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _imp.py
│  │     │  ├─ _vendor
│  │     │  │  ├─ ordered_set.py
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ _typing.py
│  │     │  │  │  ├─ __about__.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-39.pyc
│  │     │  │  │     ├─ requirements.cpython-39.pyc
│  │     │  │  │     ├─ specifiers.cpython-39.pyc
│  │     │  │  │     ├─ tags.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │     ├─ _compat.cpython-39.pyc
│  │     │  │  │     ├─ _structures.cpython-39.pyc
│  │     │  │  │     ├─ _typing.cpython-39.pyc
│  │     │  │  │     ├─ __about__.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pyparsing.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ordered_set.cpython-39.pyc
│  │     │  │     ├─ pyparsing.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ archive_util.cpython-39.pyc
│  │     │     ├─ build_meta.cpython-39.pyc
│  │     │     ├─ config.cpython-39.pyc
│  │     │     ├─ depends.cpython-39.pyc
│  │     │     ├─ dep_util.cpython-39.pyc
│  │     │     ├─ dist.cpython-39.pyc
│  │     │     ├─ errors.cpython-39.pyc
│  │     │     ├─ extension.cpython-39.pyc
│  │     │     ├─ glob.cpython-39.pyc
│  │     │     ├─ installer.cpython-39.pyc
│  │     │     ├─ launch.cpython-39.pyc
│  │     │     ├─ lib2to3_ex.cpython-39.pyc
│  │     │     ├─ monkey.cpython-39.pyc
│  │     │     ├─ msvc.cpython-39.pyc
│  │     │     ├─ namespaces.cpython-39.pyc
│  │     │     ├─ package_index.cpython-39.pyc
│  │     │     ├─ py34compat.cpython-39.pyc
│  │     │     ├─ sandbox.cpython-39.pyc
│  │     │     ├─ ssl_support.cpython-39.pyc
│  │     │     ├─ unicode_utils.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     ├─ wheel.cpython-39.pyc
│  │     │     ├─ windows_support.cpython-39.pyc
│  │     │     ├─ _deprecation_warning.cpython-39.pyc
│  │     │     ├─ _imp.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ setuptools-56.0.0.dist-info
│  │     │  ├─ dependency_links.txt
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ six-1.16.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ six.py
│  │     ├─ sklearn
│  │     │  ├─ .libs
│  │     │  │  ├─ msvcp140.dll
│  │     │  │  └─ vcomp140.dll
│  │     │  ├─ base.py
│  │     │  ├─ calibration.py
│  │     │  ├─ cluster
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ test_affinity_propagation.py
│  │     │  │  │  ├─ test_bicluster.py
│  │     │  │  │  ├─ test_birch.py
│  │     │  │  │  ├─ test_bisect_k_means.py
│  │     │  │  │  ├─ test_dbscan.py
│  │     │  │  │  ├─ test_feature_agglomeration.py
│  │     │  │  │  ├─ test_hierarchical.py
│  │     │  │  │  ├─ test_k_means.py
│  │     │  │  │  ├─ test_mean_shift.py
│  │     │  │  │  ├─ test_optics.py
│  │     │  │  │  ├─ test_spectral.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ test_affinity_propagation.cpython-39.pyc
│  │     │  │  │     ├─ test_bicluster.cpython-39.pyc
│  │     │  │  │     ├─ test_birch.cpython-39.pyc
│  │     │  │  │     ├─ test_bisect_k_means.cpython-39.pyc
│  │     │  │  │     ├─ test_dbscan.cpython-39.pyc
│  │     │  │  │     ├─ test_feature_agglomeration.cpython-39.pyc
│  │     │  │  │     ├─ test_hierarchical.cpython-39.pyc
│  │     │  │  │     ├─ test_k_means.cpython-39.pyc
│  │     │  │  │     ├─ test_mean_shift.cpython-39.pyc
│  │     │  │  │     ├─ test_optics.cpython-39.pyc
│  │     │  │  │     ├─ test_spectral.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _affinity_propagation.py
│  │     │  │  ├─ _agglomerative.py
│  │     │  │  ├─ _bicluster.py
│  │     │  │  ├─ _birch.py
│  │     │  │  ├─ _bisect_k_means.py
│  │     │  │  ├─ _dbscan.py
│  │     │  │  ├─ _dbscan_inner.cp39-win_amd64.pyd
│  │     │  │  ├─ _feature_agglomeration.py
│  │     │  │  ├─ _hierarchical_fast.cp39-win_amd64.pyd
│  │     │  │  ├─ _kmeans.py
│  │     │  │  ├─ _k_means_common.cp39-win_amd64.pyd
│  │     │  │  ├─ _k_means_common.pxd
│  │     │  │  ├─ _k_means_elkan.cp39-win_amd64.pyd
│  │     │  │  ├─ _k_means_lloyd.cp39-win_amd64.pyd
│  │     │  │  ├─ _k_means_minibatch.cp39-win_amd64.pyd
│  │     │  │  ├─ _mean_shift.py
│  │     │  │  ├─ _optics.py
│  │     │  │  ├─ _spectral.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _affinity_propagation.cpython-39.pyc
│  │     │  │     ├─ _agglomerative.cpython-39.pyc
│  │     │  │     ├─ _bicluster.cpython-39.pyc
│  │     │  │     ├─ _birch.cpython-39.pyc
│  │     │  │     ├─ _bisect_k_means.cpython-39.pyc
│  │     │  │     ├─ _dbscan.cpython-39.pyc
│  │     │  │     ├─ _feature_agglomeration.cpython-39.pyc
│  │     │  │     ├─ _kmeans.cpython-39.pyc
│  │     │  │     ├─ _mean_shift.cpython-39.pyc
│  │     │  │     ├─ _optics.cpython-39.pyc
│  │     │  │     ├─ _spectral.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ compose
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_column_transformer.py
│  │     │  │  │  ├─ test_target.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_column_transformer.cpython-39.pyc
│  │     │  │  │     ├─ test_target.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _column_transformer.py
│  │     │  │  ├─ _target.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _column_transformer.cpython-39.pyc
│  │     │  │     ├─ _target.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ conftest.py
│  │     │  ├─ covariance
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_covariance.py
│  │     │  │  │  ├─ test_elliptic_envelope.py
│  │     │  │  │  ├─ test_graphical_lasso.py
│  │     │  │  │  ├─ test_robust_covariance.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_covariance.cpython-39.pyc
│  │     │  │  │     ├─ test_elliptic_envelope.cpython-39.pyc
│  │     │  │  │     ├─ test_graphical_lasso.cpython-39.pyc
│  │     │  │  │     ├─ test_robust_covariance.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _elliptic_envelope.py
│  │     │  │  ├─ _empirical_covariance.py
│  │     │  │  ├─ _graph_lasso.py
│  │     │  │  ├─ _robust_covariance.py
│  │     │  │  ├─ _shrunk_covariance.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _elliptic_envelope.cpython-39.pyc
│  │     │  │     ├─ _empirical_covariance.cpython-39.pyc
│  │     │  │     ├─ _graph_lasso.cpython-39.pyc
│  │     │  │     ├─ _robust_covariance.cpython-39.pyc
│  │     │  │     ├─ _shrunk_covariance.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ cross_decomposition
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_pls.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_pls.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _pls.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _pls.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ datasets
│  │     │  │  ├─ data
│  │     │  │  │  ├─ boston_house_prices.csv
│  │     │  │  │  ├─ breast_cancer.csv
│  │     │  │  │  ├─ diabetes_data_raw.csv.gz
│  │     │  │  │  ├─ diabetes_target.csv.gz
│  │     │  │  │  ├─ digits.csv.gz
│  │     │  │  │  ├─ iris.csv
│  │     │  │  │  ├─ linnerud_exercise.csv
│  │     │  │  │  ├─ linnerud_physiological.csv
│  │     │  │  │  ├─ wine_data.csv
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ descr
│  │     │  │  │  ├─ breast_cancer.rst
│  │     │  │  │  ├─ california_housing.rst
│  │     │  │  │  ├─ covtype.rst
│  │     │  │  │  ├─ diabetes.rst
│  │     │  │  │  ├─ digits.rst
│  │     │  │  │  ├─ iris.rst
│  │     │  │  │  ├─ kddcup99.rst
│  │     │  │  │  ├─ lfw.rst
│  │     │  │  │  ├─ linnerud.rst
│  │     │  │  │  ├─ olivetti_faces.rst
│  │     │  │  │  ├─ rcv1.rst
│  │     │  │  │  ├─ twenty_newsgroups.rst
│  │     │  │  │  ├─ wine_data.rst
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ images
│  │     │  │  │  ├─ china.jpg
│  │     │  │  │  ├─ flower.jpg
│  │     │  │  │  ├─ README.txt
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ openml
│  │     │  │  │  │  │  ├─ id_1
│  │     │  │  │  │  │  │  ├─ api-v1-jd-1.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-1.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-1.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-1.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_1119
│  │     │  │  │  │  │  │  ├─ api-v1-jd-1119.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-1119.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-adult-census-l-2-dv-1.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-adult-census-l-2-s-act-.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-1119.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-54002.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_1590
│  │     │  │  │  │  │  │  ├─ api-v1-jd-1590.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-1590.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-1590.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-1595261.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_2
│  │     │  │  │  │  │  │  ├─ api-v1-jd-2.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-2.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-anneal-l-2-dv-1.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-anneal-l-2-s-act-.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-2.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-1666876.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_292
│  │     │  │  │  │  │  │  ├─ api-v1-jd-292.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jd-40981.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-292.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-40981.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-australian-l-2-dv-1-s-dact.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-australian-l-2-dv-1.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-australian-l-2-s-act-.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-49822.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_3
│  │     │  │  │  │  │  │  ├─ api-v1-jd-3.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-3.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-3.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-3.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_40589
│  │     │  │  │  │  │  │  ├─ api-v1-jd-40589.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-40589.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-emotions-l-2-dv-3.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-emotions-l-2-s-act-.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-40589.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-4644182.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_40675
│  │     │  │  │  │  │  │  ├─ api-v1-jd-40675.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-40675.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-glass2-l-2-dv-1-s-dact.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-glass2-l-2-dv-1.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-glass2-l-2-s-act-.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-40675.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-4965250.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_40945
│  │     │  │  │  │  │  │  ├─ api-v1-jd-40945.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-40945.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-40945.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-16826755.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_40966
│  │     │  │  │  │  │  │  ├─ api-v1-jd-40966.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-40966.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-miceprotein-l-2-dv-4.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-miceprotein-l-2-s-act-.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-40966.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-17928620.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_42074
│  │     │  │  │  │  │  │  ├─ api-v1-jd-42074.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-42074.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-42074.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-21552912.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_42585
│  │     │  │  │  │  │  │  ├─ api-v1-jd-42585.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-42585.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-42585.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-21854866.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_561
│  │     │  │  │  │  │  │  ├─ api-v1-jd-561.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-561.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-cpu-l-2-dv-1.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-cpu-l-2-s-act-.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-561.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-52739.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_61
│  │     │  │  │  │  │  │  ├─ api-v1-jd-61.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-61.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-iris-l-2-dv-1.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-iris-l-2-s-act-.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-61.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-61.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ id_62
│  │     │  │  │  │  │  │  ├─ api-v1-jd-62.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdf-62.json.gz
│  │     │  │  │  │  │  │  ├─ api-v1-jdq-62.json.gz
│  │     │  │  │  │  │  │  ├─ data-v1-dl-52352.arff.gz
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ svmlight_classification.txt
│  │     │  │  │  │  ├─ svmlight_invalid.txt
│  │     │  │  │  │  ├─ svmlight_invalid_order.txt
│  │     │  │  │  │  ├─ svmlight_multilabel.txt
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ test_20news.py
│  │     │  │  │  ├─ test_arff_parser.py
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_california_housing.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_covtype.py
│  │     │  │  │  ├─ test_kddcup99.py
│  │     │  │  │  ├─ test_lfw.py
│  │     │  │  │  ├─ test_olivetti_faces.py
│  │     │  │  │  ├─ test_openml.py
│  │     │  │  │  ├─ test_rcv1.py
│  │     │  │  │  ├─ test_samples_generator.py
│  │     │  │  │  ├─ test_svmlight_format.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_20news.cpython-39.pyc
│  │     │  │  │     ├─ test_arff_parser.cpython-39.pyc
│  │     │  │  │     ├─ test_base.cpython-39.pyc
│  │     │  │  │     ├─ test_california_housing.cpython-39.pyc
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_covtype.cpython-39.pyc
│  │     │  │  │     ├─ test_kddcup99.cpython-39.pyc
│  │     │  │  │     ├─ test_lfw.cpython-39.pyc
│  │     │  │  │     ├─ test_olivetti_faces.cpython-39.pyc
│  │     │  │  │     ├─ test_openml.cpython-39.pyc
│  │     │  │  │     ├─ test_rcv1.cpython-39.pyc
│  │     │  │  │     ├─ test_samples_generator.cpython-39.pyc
│  │     │  │  │     ├─ test_svmlight_format.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _arff_parser.py
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _california_housing.py
│  │     │  │  ├─ _covtype.py
│  │     │  │  ├─ _kddcup99.py
│  │     │  │  ├─ _lfw.py
│  │     │  │  ├─ _olivetti_faces.py
│  │     │  │  ├─ _openml.py
│  │     │  │  ├─ _rcv1.py
│  │     │  │  ├─ _samples_generator.py
│  │     │  │  ├─ _species_distributions.py
│  │     │  │  ├─ _svmlight_format_fast.cp39-win_amd64.pyd
│  │     │  │  ├─ _svmlight_format_io.py
│  │     │  │  ├─ _twenty_newsgroups.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _arff_parser.cpython-39.pyc
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _california_housing.cpython-39.pyc
│  │     │  │     ├─ _covtype.cpython-39.pyc
│  │     │  │     ├─ _kddcup99.cpython-39.pyc
│  │     │  │     ├─ _lfw.cpython-39.pyc
│  │     │  │     ├─ _olivetti_faces.cpython-39.pyc
│  │     │  │     ├─ _openml.cpython-39.pyc
│  │     │  │     ├─ _rcv1.cpython-39.pyc
│  │     │  │     ├─ _samples_generator.cpython-39.pyc
│  │     │  │     ├─ _species_distributions.cpython-39.pyc
│  │     │  │     ├─ _svmlight_format_io.cpython-39.pyc
│  │     │  │     ├─ _twenty_newsgroups.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ decomposition
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_dict_learning.py
│  │     │  │  │  ├─ test_factor_analysis.py
│  │     │  │  │  ├─ test_fastica.py
│  │     │  │  │  ├─ test_incremental_pca.py
│  │     │  │  │  ├─ test_kernel_pca.py
│  │     │  │  │  ├─ test_nmf.py
│  │     │  │  │  ├─ test_online_lda.py
│  │     │  │  │  ├─ test_pca.py
│  │     │  │  │  ├─ test_sparse_pca.py
│  │     │  │  │  ├─ test_truncated_svd.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_dict_learning.cpython-39.pyc
│  │     │  │  │     ├─ test_factor_analysis.cpython-39.pyc
│  │     │  │  │     ├─ test_fastica.cpython-39.pyc
│  │     │  │  │     ├─ test_incremental_pca.cpython-39.pyc
│  │     │  │  │     ├─ test_kernel_pca.cpython-39.pyc
│  │     │  │  │     ├─ test_nmf.cpython-39.pyc
│  │     │  │  │     ├─ test_online_lda.cpython-39.pyc
│  │     │  │  │     ├─ test_pca.cpython-39.pyc
│  │     │  │  │     ├─ test_sparse_pca.cpython-39.pyc
│  │     │  │  │     ├─ test_truncated_svd.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _cdnmf_fast.cp39-win_amd64.pyd
│  │     │  │  ├─ _dict_learning.py
│  │     │  │  ├─ _factor_analysis.py
│  │     │  │  ├─ _fastica.py
│  │     │  │  ├─ _incremental_pca.py
│  │     │  │  ├─ _kernel_pca.py
│  │     │  │  ├─ _lda.py
│  │     │  │  ├─ _nmf.py
│  │     │  │  ├─ _online_lda_fast.cp39-win_amd64.pyd
│  │     │  │  ├─ _pca.py
│  │     │  │  ├─ _sparse_pca.py
│  │     │  │  ├─ _truncated_svd.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _dict_learning.cpython-39.pyc
│  │     │  │     ├─ _factor_analysis.cpython-39.pyc
│  │     │  │     ├─ _fastica.cpython-39.pyc
│  │     │  │     ├─ _incremental_pca.cpython-39.pyc
│  │     │  │     ├─ _kernel_pca.cpython-39.pyc
│  │     │  │     ├─ _lda.cpython-39.pyc
│  │     │  │     ├─ _nmf.cpython-39.pyc
│  │     │  │     ├─ _pca.cpython-39.pyc
│  │     │  │     ├─ _sparse_pca.cpython-39.pyc
│  │     │  │     ├─ _truncated_svd.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ discriminant_analysis.py
│  │     │  ├─ dummy.py
│  │     │  ├─ ensemble
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_bagging.py
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_forest.py
│  │     │  │  │  ├─ test_gradient_boosting.py
│  │     │  │  │  ├─ test_gradient_boosting_loss_functions.py
│  │     │  │  │  ├─ test_iforest.py
│  │     │  │  │  ├─ test_stacking.py
│  │     │  │  │  ├─ test_voting.py
│  │     │  │  │  ├─ test_weight_boosting.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_bagging.cpython-39.pyc
│  │     │  │  │     ├─ test_base.cpython-39.pyc
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_forest.cpython-39.pyc
│  │     │  │  │     ├─ test_gradient_boosting.cpython-39.pyc
│  │     │  │  │     ├─ test_gradient_boosting_loss_functions.cpython-39.pyc
│  │     │  │  │     ├─ test_iforest.cpython-39.pyc
│  │     │  │  │     ├─ test_stacking.cpython-39.pyc
│  │     │  │  │     ├─ test_voting.cpython-39.pyc
│  │     │  │  │     ├─ test_weight_boosting.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _bagging.py
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _forest.py
│  │     │  │  ├─ _gb.py
│  │     │  │  ├─ _gb_losses.py
│  │     │  │  ├─ _gradient_boosting.cp39-win_amd64.pyd
│  │     │  │  ├─ _hist_gradient_boosting
│  │     │  │  │  ├─ binning.py
│  │     │  │  │  ├─ common.cp39-win_amd64.pyd
│  │     │  │  │  ├─ common.pxd
│  │     │  │  │  ├─ gradient_boosting.py
│  │     │  │  │  ├─ grower.py
│  │     │  │  │  ├─ histogram.cp39-win_amd64.pyd
│  │     │  │  │  ├─ predictor.py
│  │     │  │  │  ├─ splitting.cp39-win_amd64.pyd
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ test_binning.py
│  │     │  │  │  │  ├─ test_bitset.py
│  │     │  │  │  │  ├─ test_compare_lightgbm.py
│  │     │  │  │  │  ├─ test_gradient_boosting.py
│  │     │  │  │  │  ├─ test_grower.py
│  │     │  │  │  │  ├─ test_histogram.py
│  │     │  │  │  │  ├─ test_monotonic_contraints.py
│  │     │  │  │  │  ├─ test_predictor.py
│  │     │  │  │  │  ├─ test_splitting.py
│  │     │  │  │  │  ├─ test_warm_start.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_binning.cpython-39.pyc
│  │     │  │  │  │     ├─ test_bitset.cpython-39.pyc
│  │     │  │  │  │     ├─ test_compare_lightgbm.cpython-39.pyc
│  │     │  │  │  │     ├─ test_gradient_boosting.cpython-39.pyc
│  │     │  │  │  │     ├─ test_grower.cpython-39.pyc
│  │     │  │  │  │     ├─ test_histogram.cpython-39.pyc
│  │     │  │  │  │     ├─ test_monotonic_contraints.cpython-39.pyc
│  │     │  │  │  │     ├─ test_predictor.cpython-39.pyc
│  │     │  │  │  │     ├─ test_splitting.cpython-39.pyc
│  │     │  │  │  │     ├─ test_warm_start.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ utils.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _binning.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _bitset.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _bitset.pxd
│  │     │  │  │  ├─ _gradient_boosting.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _predictor.cp39-win_amd64.pyd
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ binning.cpython-39.pyc
│  │     │  │  │     ├─ gradient_boosting.cpython-39.pyc
│  │     │  │  │     ├─ grower.cpython-39.pyc
│  │     │  │  │     ├─ predictor.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _iforest.py
│  │     │  │  ├─ _stacking.py
│  │     │  │  ├─ _voting.py
│  │     │  │  ├─ _weight_boosting.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _bagging.cpython-39.pyc
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _forest.cpython-39.pyc
│  │     │  │     ├─ _gb.cpython-39.pyc
│  │     │  │     ├─ _gb_losses.cpython-39.pyc
│  │     │  │     ├─ _iforest.cpython-39.pyc
│  │     │  │     ├─ _stacking.cpython-39.pyc
│  │     │  │     ├─ _voting.cpython-39.pyc
│  │     │  │     ├─ _weight_boosting.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ exceptions.py
│  │     │  ├─ experimental
│  │     │  │  ├─ enable_halving_search_cv.py
│  │     │  │  ├─ enable_hist_gradient_boosting.py
│  │     │  │  ├─ enable_iterative_imputer.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_enable_hist_gradient_boosting.py
│  │     │  │  │  ├─ test_enable_iterative_imputer.py
│  │     │  │  │  ├─ test_enable_successive_halving.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_enable_hist_gradient_boosting.cpython-39.pyc
│  │     │  │  │     ├─ test_enable_iterative_imputer.cpython-39.pyc
│  │     │  │  │     ├─ test_enable_successive_halving.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ enable_halving_search_cv.cpython-39.pyc
│  │     │  │     ├─ enable_hist_gradient_boosting.cpython-39.pyc
│  │     │  │     ├─ enable_iterative_imputer.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ externals
│  │     │  │  ├─ conftest.py
│  │     │  │  ├─ _arff.py
│  │     │  │  ├─ _lobpcg.py
│  │     │  │  ├─ _packaging
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │     ├─ _structures.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ conftest.cpython-39.pyc
│  │     │  │     ├─ _arff.cpython-39.pyc
│  │     │  │     ├─ _lobpcg.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ feature_extraction
│  │     │  │  ├─ image.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_dict_vectorizer.py
│  │     │  │  │  ├─ test_feature_hasher.py
│  │     │  │  │  ├─ test_image.py
│  │     │  │  │  ├─ test_text.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_dict_vectorizer.cpython-39.pyc
│  │     │  │  │     ├─ test_feature_hasher.cpython-39.pyc
│  │     │  │  │     ├─ test_image.cpython-39.pyc
│  │     │  │  │     ├─ test_text.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ text.py
│  │     │  │  ├─ _dict_vectorizer.py
│  │     │  │  ├─ _hash.py
│  │     │  │  ├─ _hashing_fast.cp39-win_amd64.pyd
│  │     │  │  ├─ _stop_words.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ image.cpython-39.pyc
│  │     │  │     ├─ text.cpython-39.pyc
│  │     │  │     ├─ _dict_vectorizer.cpython-39.pyc
│  │     │  │     ├─ _hash.cpython-39.pyc
│  │     │  │     ├─ _stop_words.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ feature_selection
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_chi2.py
│  │     │  │  │  ├─ test_feature_select.py
│  │     │  │  │  ├─ test_from_model.py
│  │     │  │  │  ├─ test_mutual_info.py
│  │     │  │  │  ├─ test_rfe.py
│  │     │  │  │  ├─ test_sequential.py
│  │     │  │  │  ├─ test_variance_threshold.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_base.cpython-39.pyc
│  │     │  │  │     ├─ test_chi2.cpython-39.pyc
│  │     │  │  │     ├─ test_feature_select.cpython-39.pyc
│  │     │  │  │     ├─ test_from_model.cpython-39.pyc
│  │     │  │  │     ├─ test_mutual_info.cpython-39.pyc
│  │     │  │  │     ├─ test_rfe.cpython-39.pyc
│  │     │  │  │     ├─ test_sequential.cpython-39.pyc
│  │     │  │  │     ├─ test_variance_threshold.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _from_model.py
│  │     │  │  ├─ _mutual_info.py
│  │     │  │  ├─ _rfe.py
│  │     │  │  ├─ _sequential.py
│  │     │  │  ├─ _univariate_selection.py
│  │     │  │  ├─ _variance_threshold.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _from_model.cpython-39.pyc
│  │     │  │     ├─ _mutual_info.cpython-39.pyc
│  │     │  │     ├─ _rfe.cpython-39.pyc
│  │     │  │     ├─ _sequential.cpython-39.pyc
│  │     │  │     ├─ _univariate_selection.cpython-39.pyc
│  │     │  │     ├─ _variance_threshold.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ gaussian_process
│  │     │  │  ├─ kernels.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_gpc.py
│  │     │  │  │  ├─ test_gpr.py
│  │     │  │  │  ├─ test_kernels.py
│  │     │  │  │  ├─ _mini_sequence_kernel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_gpc.cpython-39.pyc
│  │     │  │  │     ├─ test_gpr.cpython-39.pyc
│  │     │  │  │     ├─ test_kernels.cpython-39.pyc
│  │     │  │  │     ├─ _mini_sequence_kernel.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _gpc.py
│  │     │  │  ├─ _gpr.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ kernels.cpython-39.pyc
│  │     │  │     ├─ _gpc.cpython-39.pyc
│  │     │  │     ├─ _gpr.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ impute
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_impute.py
│  │     │  │  │  ├─ test_knn.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_base.cpython-39.pyc
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_impute.cpython-39.pyc
│  │     │  │  │     ├─ test_knn.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _iterative.py
│  │     │  │  ├─ _knn.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _iterative.cpython-39.pyc
│  │     │  │     ├─ _knn.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ inspection
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_partial_dependence.py
│  │     │  │  │  ├─ test_pd_utils.py
│  │     │  │  │  ├─ test_permutation_importance.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_partial_dependence.cpython-39.pyc
│  │     │  │  │     ├─ test_pd_utils.cpython-39.pyc
│  │     │  │  │     ├─ test_permutation_importance.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _partial_dependence.py
│  │     │  │  ├─ _pd_utils.py
│  │     │  │  ├─ _permutation_importance.py
│  │     │  │  ├─ _plot
│  │     │  │  │  ├─ decision_boundary.py
│  │     │  │  │  ├─ partial_dependence.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ test_boundary_decision_display.py
│  │     │  │  │  │  ├─ test_plot_partial_dependence.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_boundary_decision_display.cpython-39.pyc
│  │     │  │  │  │     ├─ test_plot_partial_dependence.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ decision_boundary.cpython-39.pyc
│  │     │  │  │     ├─ partial_dependence.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _partial_dependence.cpython-39.pyc
│  │     │  │     ├─ _pd_utils.cpython-39.pyc
│  │     │  │     ├─ _permutation_importance.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ isotonic.py
│  │     │  ├─ kernel_approximation.py
│  │     │  ├─ kernel_ridge.py
│  │     │  ├─ linear_model
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_bayes.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_coordinate_descent.py
│  │     │  │  │  ├─ test_huber.py
│  │     │  │  │  ├─ test_least_angle.py
│  │     │  │  │  ├─ test_linear_loss.py
│  │     │  │  │  ├─ test_logistic.py
│  │     │  │  │  ├─ test_omp.py
│  │     │  │  │  ├─ test_passive_aggressive.py
│  │     │  │  │  ├─ test_perceptron.py
│  │     │  │  │  ├─ test_quantile.py
│  │     │  │  │  ├─ test_ransac.py
│  │     │  │  │  ├─ test_ridge.py
│  │     │  │  │  ├─ test_sag.py
│  │     │  │  │  ├─ test_sgd.py
│  │     │  │  │  ├─ test_sparse_coordinate_descent.py
│  │     │  │  │  ├─ test_theil_sen.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_base.cpython-39.pyc
│  │     │  │  │     ├─ test_bayes.cpython-39.pyc
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_coordinate_descent.cpython-39.pyc
│  │     │  │  │     ├─ test_huber.cpython-39.pyc
│  │     │  │  │     ├─ test_least_angle.cpython-39.pyc
│  │     │  │  │     ├─ test_linear_loss.cpython-39.pyc
│  │     │  │  │     ├─ test_logistic.cpython-39.pyc
│  │     │  │  │     ├─ test_omp.cpython-39.pyc
│  │     │  │  │     ├─ test_passive_aggressive.cpython-39.pyc
│  │     │  │  │     ├─ test_perceptron.cpython-39.pyc
│  │     │  │  │     ├─ test_quantile.cpython-39.pyc
│  │     │  │  │     ├─ test_ransac.cpython-39.pyc
│  │     │  │  │     ├─ test_ridge.cpython-39.pyc
│  │     │  │  │     ├─ test_sag.cpython-39.pyc
│  │     │  │  │     ├─ test_sgd.cpython-39.pyc
│  │     │  │  │     ├─ test_sparse_coordinate_descent.cpython-39.pyc
│  │     │  │  │     ├─ test_theil_sen.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _bayes.py
│  │     │  │  ├─ _cd_fast.cp39-win_amd64.pyd
│  │     │  │  ├─ _coordinate_descent.py
│  │     │  │  ├─ _glm
│  │     │  │  │  ├─ glm.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ test_glm.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_glm.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _newton_solver.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ glm.cpython-39.pyc
│  │     │  │  │     ├─ _newton_solver.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _huber.py
│  │     │  │  ├─ _least_angle.py
│  │     │  │  ├─ _linear_loss.py
│  │     │  │  ├─ _logistic.py
│  │     │  │  ├─ _omp.py
│  │     │  │  ├─ _passive_aggressive.py
│  │     │  │  ├─ _perceptron.py
│  │     │  │  ├─ _quantile.py
│  │     │  │  ├─ _ransac.py
│  │     │  │  ├─ _ridge.py
│  │     │  │  ├─ _sag.py
│  │     │  │  ├─ _sag_fast.cp39-win_amd64.pyd
│  │     │  │  ├─ _sgd_fast.cp39-win_amd64.pyd
│  │     │  │  ├─ _sgd_fast.pxd
│  │     │  │  ├─ _stochastic_gradient.py
│  │     │  │  ├─ _theil_sen.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _bayes.cpython-39.pyc
│  │     │  │     ├─ _coordinate_descent.cpython-39.pyc
│  │     │  │     ├─ _huber.cpython-39.pyc
│  │     │  │     ├─ _least_angle.cpython-39.pyc
│  │     │  │     ├─ _linear_loss.cpython-39.pyc
│  │     │  │     ├─ _logistic.cpython-39.pyc
│  │     │  │     ├─ _omp.cpython-39.pyc
│  │     │  │     ├─ _passive_aggressive.cpython-39.pyc
│  │     │  │     ├─ _perceptron.cpython-39.pyc
│  │     │  │     ├─ _quantile.cpython-39.pyc
│  │     │  │     ├─ _ransac.cpython-39.pyc
│  │     │  │     ├─ _ridge.cpython-39.pyc
│  │     │  │     ├─ _sag.cpython-39.pyc
│  │     │  │     ├─ _stochastic_gradient.cpython-39.pyc
│  │     │  │     ├─ _theil_sen.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ manifold
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_isomap.py
│  │     │  │  │  ├─ test_locally_linear.py
│  │     │  │  │  ├─ test_mds.py
│  │     │  │  │  ├─ test_spectral_embedding.py
│  │     │  │  │  ├─ test_t_sne.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_isomap.cpython-39.pyc
│  │     │  │  │     ├─ test_locally_linear.cpython-39.pyc
│  │     │  │  │     ├─ test_mds.cpython-39.pyc
│  │     │  │  │     ├─ test_spectral_embedding.cpython-39.pyc
│  │     │  │  │     ├─ test_t_sne.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _barnes_hut_tsne.cp39-win_amd64.pyd
│  │     │  │  ├─ _isomap.py
│  │     │  │  ├─ _locally_linear.py
│  │     │  │  ├─ _mds.py
│  │     │  │  ├─ _spectral_embedding.py
│  │     │  │  ├─ _t_sne.py
│  │     │  │  ├─ _utils.cp39-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _isomap.cpython-39.pyc
│  │     │  │     ├─ _locally_linear.cpython-39.pyc
│  │     │  │     ├─ _mds.cpython-39.pyc
│  │     │  │     ├─ _spectral_embedding.cpython-39.pyc
│  │     │  │     ├─ _t_sne.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ metrics
│  │     │  │  ├─ cluster
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ test_bicluster.py
│  │     │  │  │  │  ├─ test_common.py
│  │     │  │  │  │  ├─ test_supervised.py
│  │     │  │  │  │  ├─ test_unsupervised.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_bicluster.cpython-39.pyc
│  │     │  │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │  │     ├─ test_supervised.cpython-39.pyc
│  │     │  │  │  │     ├─ test_unsupervised.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _bicluster.py
│  │     │  │  │  ├─ _expected_mutual_info_fast.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _supervised.py
│  │     │  │  │  ├─ _unsupervised.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _bicluster.cpython-39.pyc
│  │     │  │  │     ├─ _supervised.cpython-39.pyc
│  │     │  │  │     ├─ _unsupervised.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pairwise.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_classification.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_dist_metrics.py
│  │     │  │  │  ├─ test_pairwise.py
│  │     │  │  │  ├─ test_pairwise_distances_reduction.py
│  │     │  │  │  ├─ test_ranking.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_score_objects.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_classification.cpython-39.pyc
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_dist_metrics.cpython-39.pyc
│  │     │  │  │     ├─ test_pairwise.cpython-39.pyc
│  │     │  │  │     ├─ test_pairwise_distances_reduction.cpython-39.pyc
│  │     │  │  │     ├─ test_ranking.cpython-39.pyc
│  │     │  │  │     ├─ test_regression.cpython-39.pyc
│  │     │  │  │     ├─ test_score_objects.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _classification.py
│  │     │  │  ├─ _dist_metrics.cp39-win_amd64.pyd
│  │     │  │  ├─ _dist_metrics.pxd
│  │     │  │  ├─ _pairwise_distances_reduction
│  │     │  │  │  ├─ _argkmin.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _argkmin.pxd
│  │     │  │  │  ├─ _base.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _base.pxd
│  │     │  │  │  ├─ _datasets_pair.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _datasets_pair.pxd
│  │     │  │  │  ├─ _dispatcher.py
│  │     │  │  │  ├─ _middle_term_computer.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _middle_term_computer.pxd
│  │     │  │  │  ├─ _radius_neighbors.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _radius_neighbors.pxd
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _dispatcher.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _pairwise_fast.cp39-win_amd64.pyd
│  │     │  │  ├─ _plot
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ confusion_matrix.py
│  │     │  │  │  ├─ det_curve.py
│  │     │  │  │  ├─ precision_recall_curve.py
│  │     │  │  │  ├─ regression.py
│  │     │  │  │  ├─ roc_curve.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ test_base.py
│  │     │  │  │  │  ├─ test_common_curve_display.py
│  │     │  │  │  │  ├─ test_confusion_matrix_display.py
│  │     │  │  │  │  ├─ test_det_curve_display.py
│  │     │  │  │  │  ├─ test_precision_recall_display.py
│  │     │  │  │  │  ├─ test_predict_error_display.py
│  │     │  │  │  │  ├─ test_roc_curve_display.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_base.cpython-39.pyc
│  │     │  │  │  │     ├─ test_common_curve_display.cpython-39.pyc
│  │     │  │  │  │     ├─ test_confusion_matrix_display.cpython-39.pyc
│  │     │  │  │  │     ├─ test_det_curve_display.cpython-39.pyc
│  │     │  │  │  │     ├─ test_precision_recall_display.cpython-39.pyc
│  │     │  │  │  │     ├─ test_predict_error_display.cpython-39.pyc
│  │     │  │  │  │     ├─ test_roc_curve_display.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ confusion_matrix.cpython-39.pyc
│  │     │  │  │     ├─ det_curve.cpython-39.pyc
│  │     │  │  │     ├─ precision_recall_curve.cpython-39.pyc
│  │     │  │  │     ├─ regression.cpython-39.pyc
│  │     │  │  │     ├─ roc_curve.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _ranking.py
│  │     │  │  ├─ _regression.py
│  │     │  │  ├─ _scorer.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ pairwise.cpython-39.pyc
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _classification.cpython-39.pyc
│  │     │  │     ├─ _ranking.cpython-39.pyc
│  │     │  │     ├─ _regression.cpython-39.pyc
│  │     │  │     ├─ _scorer.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ mixture
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_bayesian_mixture.py
│  │     │  │  │  ├─ test_gaussian_mixture.py
│  │     │  │  │  ├─ test_mixture.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_bayesian_mixture.cpython-39.pyc
│  │     │  │  │     ├─ test_gaussian_mixture.cpython-39.pyc
│  │     │  │  │     ├─ test_mixture.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _bayesian_mixture.py
│  │     │  │  ├─ _gaussian_mixture.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _bayesian_mixture.cpython-39.pyc
│  │     │  │     ├─ _gaussian_mixture.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ model_selection
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ test_plot.py
│  │     │  │  │  ├─ test_search.py
│  │     │  │  │  ├─ test_split.py
│  │     │  │  │  ├─ test_successive_halving.py
│  │     │  │  │  ├─ test_validation.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ test_plot.cpython-39.pyc
│  │     │  │  │     ├─ test_search.cpython-39.pyc
│  │     │  │  │     ├─ test_split.cpython-39.pyc
│  │     │  │  │     ├─ test_successive_halving.cpython-39.pyc
│  │     │  │  │     ├─ test_validation.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _plot.py
│  │     │  │  ├─ _search.py
│  │     │  │  ├─ _search_successive_halving.py
│  │     │  │  ├─ _split.py
│  │     │  │  ├─ _validation.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _plot.cpython-39.pyc
│  │     │  │     ├─ _search.cpython-39.pyc
│  │     │  │     ├─ _search_successive_halving.cpython-39.pyc
│  │     │  │     ├─ _split.cpython-39.pyc
│  │     │  │     ├─ _validation.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ multiclass.py
│  │     │  ├─ multioutput.py
│  │     │  ├─ naive_bayes.py
│  │     │  ├─ neighbors
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_ball_tree.py
│  │     │  │  │  ├─ test_graph.py
│  │     │  │  │  ├─ test_kde.py
│  │     │  │  │  ├─ test_kd_tree.py
│  │     │  │  │  ├─ test_lof.py
│  │     │  │  │  ├─ test_nca.py
│  │     │  │  │  ├─ test_nearest_centroid.py
│  │     │  │  │  ├─ test_neighbors.py
│  │     │  │  │  ├─ test_neighbors_pipeline.py
│  │     │  │  │  ├─ test_neighbors_tree.py
│  │     │  │  │  ├─ test_quad_tree.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_ball_tree.cpython-39.pyc
│  │     │  │  │     ├─ test_graph.cpython-39.pyc
│  │     │  │  │     ├─ test_kde.cpython-39.pyc
│  │     │  │  │     ├─ test_kd_tree.cpython-39.pyc
│  │     │  │  │     ├─ test_lof.cpython-39.pyc
│  │     │  │  │     ├─ test_nca.cpython-39.pyc
│  │     │  │  │     ├─ test_nearest_centroid.cpython-39.pyc
│  │     │  │  │     ├─ test_neighbors.cpython-39.pyc
│  │     │  │  │     ├─ test_neighbors_pipeline.cpython-39.pyc
│  │     │  │  │     ├─ test_neighbors_tree.cpython-39.pyc
│  │     │  │  │     ├─ test_quad_tree.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _ball_tree.cp39-win_amd64.pyd
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _classification.py
│  │     │  │  ├─ _distance_metric.py
│  │     │  │  ├─ _graph.py
│  │     │  │  ├─ _kde.py
│  │     │  │  ├─ _kd_tree.cp39-win_amd64.pyd
│  │     │  │  ├─ _lof.py
│  │     │  │  ├─ _nca.py
│  │     │  │  ├─ _nearest_centroid.py
│  │     │  │  ├─ _partition_nodes.cp39-win_amd64.pyd
│  │     │  │  ├─ _partition_nodes.pxd
│  │     │  │  ├─ _quad_tree.cp39-win_amd64.pyd
│  │     │  │  ├─ _quad_tree.pxd
│  │     │  │  ├─ _regression.py
│  │     │  │  ├─ _unsupervised.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _classification.cpython-39.pyc
│  │     │  │     ├─ _distance_metric.cpython-39.pyc
│  │     │  │     ├─ _graph.cpython-39.pyc
│  │     │  │     ├─ _kde.cpython-39.pyc
│  │     │  │     ├─ _lof.cpython-39.pyc
│  │     │  │     ├─ _nca.cpython-39.pyc
│  │     │  │     ├─ _nearest_centroid.cpython-39.pyc
│  │     │  │     ├─ _regression.cpython-39.pyc
│  │     │  │     ├─ _unsupervised.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ neural_network
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_mlp.py
│  │     │  │  │  ├─ test_rbm.py
│  │     │  │  │  ├─ test_stochastic_optimizers.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_base.cpython-39.pyc
│  │     │  │  │     ├─ test_mlp.cpython-39.pyc
│  │     │  │  │     ├─ test_rbm.cpython-39.pyc
│  │     │  │  │     ├─ test_stochastic_optimizers.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _multilayer_perceptron.py
│  │     │  │  ├─ _rbm.py
│  │     │  │  ├─ _stochastic_optimizers.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _multilayer_perceptron.cpython-39.pyc
│  │     │  │     ├─ _rbm.cpython-39.pyc
│  │     │  │     ├─ _stochastic_optimizers.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ pipeline.py
│  │     │  ├─ preprocessing
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_data.py
│  │     │  │  │  ├─ test_discretization.py
│  │     │  │  │  ├─ test_encoders.py
│  │     │  │  │  ├─ test_function_transformer.py
│  │     │  │  │  ├─ test_label.py
│  │     │  │  │  ├─ test_polynomial.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_common.cpython-39.pyc
│  │     │  │  │     ├─ test_data.cpython-39.pyc
│  │     │  │  │     ├─ test_discretization.cpython-39.pyc
│  │     │  │  │     ├─ test_encoders.cpython-39.pyc
│  │     │  │  │     ├─ test_function_transformer.cpython-39.pyc
│  │     │  │  │     ├─ test_label.cpython-39.pyc
│  │     │  │  │     ├─ test_polynomial.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _csr_polynomial_expansion.cp39-win_amd64.pyd
│  │     │  │  ├─ _data.py
│  │     │  │  ├─ _discretization.py
│  │     │  │  ├─ _encoders.py
│  │     │  │  ├─ _function_transformer.py
│  │     │  │  ├─ _label.py
│  │     │  │  ├─ _polynomial.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _data.cpython-39.pyc
│  │     │  │     ├─ _discretization.cpython-39.pyc
│  │     │  │     ├─ _encoders.cpython-39.pyc
│  │     │  │     ├─ _function_transformer.cpython-39.pyc
│  │     │  │     ├─ _label.cpython-39.pyc
│  │     │  │     ├─ _polynomial.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ random_projection.py
│  │     │  ├─ semi_supervised
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_label_propagation.py
│  │     │  │  │  ├─ test_self_training.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_label_propagation.cpython-39.pyc
│  │     │  │  │     ├─ test_self_training.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _label_propagation.py
│  │     │  │  ├─ _self_training.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _label_propagation.cpython-39.pyc
│  │     │  │     ├─ _self_training.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ svm
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_bounds.py
│  │     │  │  │  ├─ test_sparse.py
│  │     │  │  │  ├─ test_svm.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_bounds.cpython-39.pyc
│  │     │  │  │     ├─ test_sparse.cpython-39.pyc
│  │     │  │  │     ├─ test_svm.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _bounds.py
│  │     │  │  ├─ _classes.py
│  │     │  │  ├─ _liblinear.cp39-win_amd64.pyd
│  │     │  │  ├─ _libsvm.cp39-win_amd64.pyd
│  │     │  │  ├─ _libsvm_sparse.cp39-win_amd64.pyd
│  │     │  │  ├─ _newrand.cp39-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _base.cpython-39.pyc
│  │     │  │     ├─ _bounds.cpython-39.pyc
│  │     │  │     ├─ _classes.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ tests
│  │     │  │  ├─ random_seed.py
│  │     │  │  ├─ test_base.py
│  │     │  │  ├─ test_build.py
│  │     │  │  ├─ test_calibration.py
│  │     │  │  ├─ test_check_build.py
│  │     │  │  ├─ test_common.py
│  │     │  │  ├─ test_config.py
│  │     │  │  ├─ test_discriminant_analysis.py
│  │     │  │  ├─ test_docstrings.py
│  │     │  │  ├─ test_docstring_parameters.py
│  │     │  │  ├─ test_dummy.py
│  │     │  │  ├─ test_init.py
│  │     │  │  ├─ test_isotonic.py
│  │     │  │  ├─ test_kernel_approximation.py
│  │     │  │  ├─ test_kernel_ridge.py
│  │     │  │  ├─ test_metaestimators.py
│  │     │  │  ├─ test_min_dependencies_readme.py
│  │     │  │  ├─ test_multiclass.py
│  │     │  │  ├─ test_multioutput.py
│  │     │  │  ├─ test_naive_bayes.py
│  │     │  │  ├─ test_pipeline.py
│  │     │  │  ├─ test_public_functions.py
│  │     │  │  ├─ test_random_projection.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ random_seed.cpython-39.pyc
│  │     │  │     ├─ test_base.cpython-39.pyc
│  │     │  │     ├─ test_build.cpython-39.pyc
│  │     │  │     ├─ test_calibration.cpython-39.pyc
│  │     │  │     ├─ test_check_build.cpython-39.pyc
│  │     │  │     ├─ test_common.cpython-39.pyc
│  │     │  │     ├─ test_config.cpython-39.pyc
│  │     │  │     ├─ test_discriminant_analysis.cpython-39.pyc
│  │     │  │     ├─ test_docstrings.cpython-39.pyc
│  │     │  │     ├─ test_docstring_parameters.cpython-39.pyc
│  │     │  │     ├─ test_dummy.cpython-39.pyc
│  │     │  │     ├─ test_init.cpython-39.pyc
│  │     │  │     ├─ test_isotonic.cpython-39.pyc
│  │     │  │     ├─ test_kernel_approximation.cpython-39.pyc
│  │     │  │     ├─ test_kernel_ridge.cpython-39.pyc
│  │     │  │     ├─ test_metaestimators.cpython-39.pyc
│  │     │  │     ├─ test_min_dependencies_readme.cpython-39.pyc
│  │     │  │     ├─ test_multiclass.cpython-39.pyc
│  │     │  │     ├─ test_multioutput.cpython-39.pyc
│  │     │  │     ├─ test_naive_bayes.cpython-39.pyc
│  │     │  │     ├─ test_pipeline.cpython-39.pyc
│  │     │  │     ├─ test_public_functions.cpython-39.pyc
│  │     │  │     ├─ test_random_projection.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ tree
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_export.py
│  │     │  │  │  ├─ test_reingold_tilford.py
│  │     │  │  │  ├─ test_tree.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_export.cpython-39.pyc
│  │     │  │  │     ├─ test_reingold_tilford.cpython-39.pyc
│  │     │  │  │     ├─ test_tree.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _classes.py
│  │     │  │  ├─ _criterion.cp39-win_amd64.pyd
│  │     │  │  ├─ _criterion.pxd
│  │     │  │  ├─ _export.py
│  │     │  │  ├─ _reingold_tilford.py
│  │     │  │  ├─ _splitter.cp39-win_amd64.pyd
│  │     │  │  ├─ _splitter.pxd
│  │     │  │  ├─ _tree.cp39-win_amd64.pyd
│  │     │  │  ├─ _tree.pxd
│  │     │  │  ├─ _utils.cp39-win_amd64.pyd
│  │     │  │  ├─ _utils.pxd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _classes.cpython-39.pyc
│  │     │  │     ├─ _export.cpython-39.pyc
│  │     │  │     ├─ _reingold_tilford.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ utils
│  │     │  │  ├─ arrayfuncs.cp39-win_amd64.pyd
│  │     │  │  ├─ class_weight.py
│  │     │  │  ├─ deprecation.py
│  │     │  │  ├─ discovery.py
│  │     │  │  ├─ estimator_checks.py
│  │     │  │  ├─ extmath.py
│  │     │  │  ├─ fixes.py
│  │     │  │  ├─ graph.py
│  │     │  │  ├─ metaestimators.py
│  │     │  │  ├─ multiclass.py
│  │     │  │  ├─ murmurhash.cp39-win_amd64.pyd
│  │     │  │  ├─ murmurhash.pxd
│  │     │  │  ├─ optimize.py
│  │     │  │  ├─ parallel.py
│  │     │  │  ├─ random.py
│  │     │  │  ├─ sparsefuncs.py
│  │     │  │  ├─ sparsefuncs_fast.cp39-win_amd64.pyd
│  │     │  │  ├─ stats.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_arpack.py
│  │     │  │  │  ├─ test_arrayfuncs.py
│  │     │  │  │  ├─ test_array_api.py
│  │     │  │  │  ├─ test_class_weight.py
│  │     │  │  │  ├─ test_cython_blas.py
│  │     │  │  │  ├─ test_cython_templating.py
│  │     │  │  │  ├─ test_deprecation.py
│  │     │  │  │  ├─ test_encode.py
│  │     │  │  │  ├─ test_estimator_checks.py
│  │     │  │  │  ├─ test_estimator_html_repr.py
│  │     │  │  │  ├─ test_extmath.py
│  │     │  │  │  ├─ test_fast_dict.py
│  │     │  │  │  ├─ test_fixes.py
│  │     │  │  │  ├─ test_graph.py
│  │     │  │  │  ├─ test_metaestimators.py
│  │     │  │  │  ├─ test_mocking.py
│  │     │  │  │  ├─ test_multiclass.py
│  │     │  │  │  ├─ test_murmurhash.py
│  │     │  │  │  ├─ test_optimize.py
│  │     │  │  │  ├─ test_parallel.py
│  │     │  │  │  ├─ test_param_validation.py
│  │     │  │  │  ├─ test_pprint.py
│  │     │  │  │  ├─ test_random.py
│  │     │  │  │  ├─ test_readonly_wrapper.py
│  │     │  │  │  ├─ test_seq_dataset.py
│  │     │  │  │  ├─ test_set_output.py
│  │     │  │  │  ├─ test_shortest_path.py
│  │     │  │  │  ├─ test_show_versions.py
│  │     │  │  │  ├─ test_sparsefuncs.py
│  │     │  │  │  ├─ test_stats.py
│  │     │  │  │  ├─ test_tags.py
│  │     │  │  │  ├─ test_testing.py
│  │     │  │  │  ├─ test_utils.py
│  │     │  │  │  ├─ test_validation.py
│  │     │  │  │  ├─ test_weight_vector.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-39.pyc
│  │     │  │  │     ├─ test_arpack.cpython-39.pyc
│  │     │  │  │     ├─ test_arrayfuncs.cpython-39.pyc
│  │     │  │  │     ├─ test_array_api.cpython-39.pyc
│  │     │  │  │     ├─ test_class_weight.cpython-39.pyc
│  │     │  │  │     ├─ test_cython_blas.cpython-39.pyc
│  │     │  │  │     ├─ test_cython_templating.cpython-39.pyc
│  │     │  │  │     ├─ test_deprecation.cpython-39.pyc
│  │     │  │  │     ├─ test_encode.cpython-39.pyc
│  │     │  │  │     ├─ test_estimator_checks.cpython-39.pyc
│  │     │  │  │     ├─ test_estimator_html_repr.cpython-39.pyc
│  │     │  │  │     ├─ test_extmath.cpython-39.pyc
│  │     │  │  │     ├─ test_fast_dict.cpython-39.pyc
│  │     │  │  │     ├─ test_fixes.cpython-39.pyc
│  │     │  │  │     ├─ test_graph.cpython-39.pyc
│  │     │  │  │     ├─ test_metaestimators.cpython-39.pyc
│  │     │  │  │     ├─ test_mocking.cpython-39.pyc
│  │     │  │  │     ├─ test_multiclass.cpython-39.pyc
│  │     │  │  │     ├─ test_murmurhash.cpython-39.pyc
│  │     │  │  │     ├─ test_optimize.cpython-39.pyc
│  │     │  │  │     ├─ test_parallel.cpython-39.pyc
│  │     │  │  │     ├─ test_param_validation.cpython-39.pyc
│  │     │  │  │     ├─ test_pprint.cpython-39.pyc
│  │     │  │  │     ├─ test_random.cpython-39.pyc
│  │     │  │  │     ├─ test_readonly_wrapper.cpython-39.pyc
│  │     │  │  │     ├─ test_seq_dataset.cpython-39.pyc
│  │     │  │  │     ├─ test_set_output.cpython-39.pyc
│  │     │  │  │     ├─ test_shortest_path.cpython-39.pyc
│  │     │  │  │     ├─ test_show_versions.cpython-39.pyc
│  │     │  │  │     ├─ test_sparsefuncs.cpython-39.pyc
│  │     │  │  │     ├─ test_stats.cpython-39.pyc
│  │     │  │  │     ├─ test_tags.cpython-39.pyc
│  │     │  │  │     ├─ test_testing.cpython-39.pyc
│  │     │  │  │     ├─ test_utils.cpython-39.pyc
│  │     │  │  │     ├─ test_validation.cpython-39.pyc
│  │     │  │  │     ├─ test_weight_vector.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ validation.py
│  │     │  │  ├─ _arpack.py
│  │     │  │  ├─ _array_api.py
│  │     │  │  ├─ _available_if.py
│  │     │  │  ├─ _bunch.py
│  │     │  │  ├─ _cython_blas.cp39-win_amd64.pyd
│  │     │  │  ├─ _cython_blas.pxd
│  │     │  │  ├─ _encode.py
│  │     │  │  ├─ _estimator_html_repr.py
│  │     │  │  ├─ _fast_dict.cp39-win_amd64.pyd
│  │     │  │  ├─ _fast_dict.pxd
│  │     │  │  ├─ _heap.cp39-win_amd64.pyd
│  │     │  │  ├─ _heap.pxd
│  │     │  │  ├─ _isfinite.cp39-win_amd64.pyd
│  │     │  │  ├─ _joblib.py
│  │     │  │  ├─ _logistic_sigmoid.cp39-win_amd64.pyd
│  │     │  │  ├─ _mask.py
│  │     │  │  ├─ _mocking.py
│  │     │  │  ├─ _openmp_helpers.cp39-win_amd64.pyd
│  │     │  │  ├─ _openmp_helpers.pxd
│  │     │  │  ├─ _param_validation.py
│  │     │  │  ├─ _pprint.py
│  │     │  │  ├─ _random.cp39-win_amd64.pyd
│  │     │  │  ├─ _random.pxd
│  │     │  │  ├─ _readonly_array_wrapper.cp39-win_amd64.pyd
│  │     │  │  ├─ _seq_dataset.cp39-win_amd64.pyd
│  │     │  │  ├─ _seq_dataset.pxd
│  │     │  │  ├─ _set_output.py
│  │     │  │  ├─ _show_versions.py
│  │     │  │  ├─ _sorting.cp39-win_amd64.pyd
│  │     │  │  ├─ _sorting.pxd
│  │     │  │  ├─ _tags.py
│  │     │  │  ├─ _testing.py
│  │     │  │  ├─ _typedefs.cp39-win_amd64.pyd
│  │     │  │  ├─ _typedefs.pxd
│  │     │  │  ├─ _vector_sentinel.cp39-win_amd64.pyd
│  │     │  │  ├─ _vector_sentinel.pxd
│  │     │  │  ├─ _weight_vector.cp39-win_amd64.pyd
│  │     │  │  ├─ _weight_vector.pxd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ class_weight.cpython-39.pyc
│  │     │  │     ├─ deprecation.cpython-39.pyc
│  │     │  │     ├─ discovery.cpython-39.pyc
│  │     │  │     ├─ estimator_checks.cpython-39.pyc
│  │     │  │     ├─ extmath.cpython-39.pyc
│  │     │  │     ├─ fixes.cpython-39.pyc
│  │     │  │     ├─ graph.cpython-39.pyc
│  │     │  │     ├─ metaestimators.cpython-39.pyc
│  │     │  │     ├─ multiclass.cpython-39.pyc
│  │     │  │     ├─ optimize.cpython-39.pyc
│  │     │  │     ├─ parallel.cpython-39.pyc
│  │     │  │     ├─ random.cpython-39.pyc
│  │     │  │     ├─ sparsefuncs.cpython-39.pyc
│  │     │  │     ├─ stats.cpython-39.pyc
│  │     │  │     ├─ validation.cpython-39.pyc
│  │     │  │     ├─ _arpack.cpython-39.pyc
│  │     │  │     ├─ _array_api.cpython-39.pyc
│  │     │  │     ├─ _available_if.cpython-39.pyc
│  │     │  │     ├─ _bunch.cpython-39.pyc
│  │     │  │     ├─ _encode.cpython-39.pyc
│  │     │  │     ├─ _estimator_html_repr.cpython-39.pyc
│  │     │  │     ├─ _joblib.cpython-39.pyc
│  │     │  │     ├─ _mask.cpython-39.pyc
│  │     │  │     ├─ _mocking.cpython-39.pyc
│  │     │  │     ├─ _param_validation.cpython-39.pyc
│  │     │  │     ├─ _pprint.cpython-39.pyc
│  │     │  │     ├─ _set_output.cpython-39.pyc
│  │     │  │     ├─ _show_versions.cpython-39.pyc
│  │     │  │     ├─ _tags.cpython-39.pyc
│  │     │  │     ├─ _testing.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _build_utils
│  │     │  │  ├─ openmp_helpers.py
│  │     │  │  ├─ pre_build_helpers.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ openmp_helpers.cpython-39.pyc
│  │     │  │     ├─ pre_build_helpers.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _config.py
│  │     │  ├─ _distributor_init.py
│  │     │  ├─ _isotonic.cp39-win_amd64.pyd
│  │     │  ├─ _loss
│  │     │  │  ├─ glm_distribution.py
│  │     │  │  ├─ link.py
│  │     │  │  ├─ loss.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_glm_distribution.py
│  │     │  │  │  ├─ test_link.py
│  │     │  │  │  ├─ test_loss.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_glm_distribution.cpython-39.pyc
│  │     │  │  │     ├─ test_link.cpython-39.pyc
│  │     │  │  │     ├─ test_loss.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ _loss.cp39-win_amd64.pyd
│  │     │  │  ├─ _loss.pxd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ glm_distribution.cpython-39.pyc
│  │     │  │     ├─ link.cpython-39.pyc
│  │     │  │     ├─ loss.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _min_dependencies.py
│  │     │  ├─ __check_build
│  │     │  │  ├─ _check_build.cp39-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ base.cpython-39.pyc
│  │     │     ├─ calibration.cpython-39.pyc
│  │     │     ├─ conftest.cpython-39.pyc
│  │     │     ├─ discriminant_analysis.cpython-39.pyc
│  │     │     ├─ dummy.cpython-39.pyc
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ isotonic.cpython-39.pyc
│  │     │     ├─ kernel_approximation.cpython-39.pyc
│  │     │     ├─ kernel_ridge.cpython-39.pyc
│  │     │     ├─ multiclass.cpython-39.pyc
│  │     │     ├─ multioutput.cpython-39.pyc
│  │     │     ├─ naive_bayes.cpython-39.pyc
│  │     │     ├─ pipeline.cpython-39.pyc
│  │     │     ├─ random_projection.cpython-39.pyc
│  │     │     ├─ _config.cpython-39.pyc
│  │     │     ├─ _distributor_init.cpython-39.pyc
│  │     │     ├─ _min_dependencies.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ sklearn-0.0-py3.9.egg-info
│  │     │  ├─ dependency_links.txt
│  │     │  ├─ installed-files.txt
│  │     │  ├─ not-zip-safe
│  │     │  ├─ PKG-INFO
│  │     │  ├─ requires.txt
│  │     │  ├─ SOURCES.txt
│  │     │  └─ top_level.txt
│  │     ├─ sniffio
│  │     │  ├─ py.typed
│  │     │  ├─ _impl.py
│  │     │  ├─ _tests
│  │     │  │  ├─ test_sniffio.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ test_sniffio.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ _impl.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ sniffio-1.3.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ LICENSE.APACHE2
│  │     │  ├─ LICENSE.MIT
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ stack_data
│  │     │  ├─ core.py
│  │     │  ├─ formatting.py
│  │     │  ├─ py.typed
│  │     │  ├─ serializing.py
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ core.cpython-39.pyc
│  │     │     ├─ formatting.cpython-39.pyc
│  │     │     ├─ serializing.cpython-39.pyc
│  │     │     ├─ utils.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ stack_data-0.6.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ starlette
│  │     │  ├─ applications.py
│  │     │  ├─ authentication.py
│  │     │  ├─ background.py
│  │     │  ├─ concurrency.py
│  │     │  ├─ config.py
│  │     │  ├─ convertors.py
│  │     │  ├─ datastructures.py
│  │     │  ├─ endpoints.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ formparsers.py
│  │     │  ├─ middleware
│  │     │  │  ├─ authentication.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ cors.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ gzip.py
│  │     │  │  ├─ httpsredirect.py
│  │     │  │  ├─ sessions.py
│  │     │  │  ├─ trustedhost.py
│  │     │  │  ├─ wsgi.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ authentication.cpython-39.pyc
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ cors.cpython-39.pyc
│  │     │  │     ├─ errors.cpython-39.pyc
│  │     │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │     ├─ gzip.cpython-39.pyc
│  │     │  │     ├─ httpsredirect.cpython-39.pyc
│  │     │  │     ├─ sessions.cpython-39.pyc
│  │     │  │     ├─ trustedhost.cpython-39.pyc
│  │     │  │     ├─ wsgi.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ requests.py
│  │     │  ├─ responses.py
│  │     │  ├─ routing.py
│  │     │  ├─ schemas.py
│  │     │  ├─ staticfiles.py
│  │     │  ├─ status.py
│  │     │  ├─ templating.py
│  │     │  ├─ testclient.py
│  │     │  ├─ types.py
│  │     │  ├─ websockets.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _utils.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ applications.cpython-39.pyc
│  │     │     ├─ authentication.cpython-39.pyc
│  │     │     ├─ background.cpython-39.pyc
│  │     │     ├─ concurrency.cpython-39.pyc
│  │     │     ├─ config.cpython-39.pyc
│  │     │     ├─ convertors.cpython-39.pyc
│  │     │     ├─ datastructures.cpython-39.pyc
│  │     │     ├─ endpoints.cpython-39.pyc
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ formparsers.cpython-39.pyc
│  │     │     ├─ requests.cpython-39.pyc
│  │     │     ├─ responses.cpython-39.pyc
│  │     │     ├─ routing.cpython-39.pyc
│  │     │     ├─ schemas.cpython-39.pyc
│  │     │     ├─ staticfiles.cpython-39.pyc
│  │     │     ├─ status.cpython-39.pyc
│  │     │     ├─ templating.cpython-39.pyc
│  │     │     ├─ testclient.cpython-39.pyc
│  │     │     ├─ types.cpython-39.pyc
│  │     │     ├─ websockets.cpython-39.pyc
│  │     │     ├─ _compat.cpython-39.pyc
│  │     │     ├─ _utils.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ starlette-0.26.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ threadpoolctl-3.1.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ threadpoolctl.py
│  │     ├─ toml
│  │     │  ├─ decoder.py
│  │     │  ├─ encoder.py
│  │     │  ├─ ordered.py
│  │     │  ├─ tz.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ decoder.cpython-39.pyc
│  │     │     ├─ encoder.cpython-39.pyc
│  │     │     ├─ ordered.cpython-39.pyc
│  │     │     ├─ tz.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ toml-0.10.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ tomli
│  │     │  ├─ py.typed
│  │     │  ├─ _parser.py
│  │     │  ├─ _re.py
│  │     │  ├─ _types.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ _parser.cpython-39.pyc
│  │     │     ├─ _re.cpython-39.pyc
│  │     │     ├─ _types.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ tomli-2.0.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ tornado
│  │     │  ├─ auth.py
│  │     │  ├─ autoreload.py
│  │     │  ├─ concurrent.py
│  │     │  ├─ curl_httpclient.py
│  │     │  ├─ escape.py
│  │     │  ├─ gen.py
│  │     │  ├─ http1connection.py
│  │     │  ├─ httpclient.py
│  │     │  ├─ httpserver.py
│  │     │  ├─ httputil.py
│  │     │  ├─ ioloop.py
│  │     │  ├─ iostream.py
│  │     │  ├─ locale.py
│  │     │  ├─ locks.py
│  │     │  ├─ log.py
│  │     │  ├─ netutil.py
│  │     │  ├─ options.py
│  │     │  ├─ platform
│  │     │  │  ├─ asyncio.py
│  │     │  │  ├─ caresresolver.py
│  │     │  │  ├─ twisted.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ asyncio.cpython-39.pyc
│  │     │  │     ├─ caresresolver.cpython-39.pyc
│  │     │  │     ├─ twisted.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ process.py
│  │     │  ├─ py.typed
│  │     │  ├─ queues.py
│  │     │  ├─ routing.py
│  │     │  ├─ simple_httpclient.py
│  │     │  ├─ speedups.pyd
│  │     │  ├─ tcpclient.py
│  │     │  ├─ tcpserver.py
│  │     │  ├─ template.py
│  │     │  ├─ test
│  │     │  │  ├─ asyncio_test.py
│  │     │  │  ├─ auth_test.py
│  │     │  │  ├─ autoreload_test.py
│  │     │  │  ├─ concurrent_test.py
│  │     │  │  ├─ csv_translations
│  │     │  │  │  └─ fr_FR.csv
│  │     │  │  ├─ curl_httpclient_test.py
│  │     │  │  ├─ escape_test.py
│  │     │  │  ├─ gen_test.py
│  │     │  │  ├─ gettext_translations
│  │     │  │  │  └─ fr_FR
│  │     │  │  │     └─ LC_MESSAGES
│  │     │  │  │        ├─ tornado_test.mo
│  │     │  │  │        └─ tornado_test.po
│  │     │  │  ├─ http1connection_test.py
│  │     │  │  ├─ httpclient_test.py
│  │     │  │  ├─ httpserver_test.py
│  │     │  │  ├─ httputil_test.py
│  │     │  │  ├─ import_test.py
│  │     │  │  ├─ ioloop_test.py
│  │     │  │  ├─ iostream_test.py
│  │     │  │  ├─ locale_test.py
│  │     │  │  ├─ locks_test.py
│  │     │  │  ├─ log_test.py
│  │     │  │  ├─ netutil_test.py
│  │     │  │  ├─ options_test.cfg
│  │     │  │  ├─ options_test.py
│  │     │  │  ├─ options_test_types.cfg
│  │     │  │  ├─ options_test_types_str.cfg
│  │     │  │  ├─ process_test.py
│  │     │  │  ├─ queues_test.py
│  │     │  │  ├─ resolve_test_helper.py
│  │     │  │  ├─ routing_test.py
│  │     │  │  ├─ runtests.py
│  │     │  │  ├─ simple_httpclient_test.py
│  │     │  │  ├─ static
│  │     │  │  │  ├─ dir
│  │     │  │  │  │  └─ index.html
│  │     │  │  │  ├─ robots.txt
│  │     │  │  │  ├─ sample.xml
│  │     │  │  │  ├─ sample.xml.bz2
│  │     │  │  │  └─ sample.xml.gz
│  │     │  │  ├─ static_foo.txt
│  │     │  │  ├─ tcpclient_test.py
│  │     │  │  ├─ tcpserver_test.py
│  │     │  │  ├─ templates
│  │     │  │  │  └─ utf8.html
│  │     │  │  ├─ template_test.py
│  │     │  │  ├─ test.crt
│  │     │  │  ├─ test.key
│  │     │  │  ├─ testing_test.py
│  │     │  │  ├─ twisted_test.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ util_test.py
│  │     │  │  ├─ websocket_test.py
│  │     │  │  ├─ web_test.py
│  │     │  │  ├─ wsgi_test.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ asyncio_test.cpython-39.pyc
│  │     │  │     ├─ auth_test.cpython-39.pyc
│  │     │  │     ├─ autoreload_test.cpython-39.pyc
│  │     │  │     ├─ concurrent_test.cpython-39.pyc
│  │     │  │     ├─ curl_httpclient_test.cpython-39.pyc
│  │     │  │     ├─ escape_test.cpython-39.pyc
│  │     │  │     ├─ gen_test.cpython-39.pyc
│  │     │  │     ├─ http1connection_test.cpython-39.pyc
│  │     │  │     ├─ httpclient_test.cpython-39.pyc
│  │     │  │     ├─ httpserver_test.cpython-39.pyc
│  │     │  │     ├─ httputil_test.cpython-39.pyc
│  │     │  │     ├─ import_test.cpython-39.pyc
│  │     │  │     ├─ ioloop_test.cpython-39.pyc
│  │     │  │     ├─ iostream_test.cpython-39.pyc
│  │     │  │     ├─ locale_test.cpython-39.pyc
│  │     │  │     ├─ locks_test.cpython-39.pyc
│  │     │  │     ├─ log_test.cpython-39.pyc
│  │     │  │     ├─ netutil_test.cpython-39.pyc
│  │     │  │     ├─ options_test.cpython-39.pyc
│  │     │  │     ├─ process_test.cpython-39.pyc
│  │     │  │     ├─ queues_test.cpython-39.pyc
│  │     │  │     ├─ resolve_test_helper.cpython-39.pyc
│  │     │  │     ├─ routing_test.cpython-39.pyc
│  │     │  │     ├─ runtests.cpython-39.pyc
│  │     │  │     ├─ simple_httpclient_test.cpython-39.pyc
│  │     │  │     ├─ tcpclient_test.cpython-39.pyc
│  │     │  │     ├─ tcpserver_test.cpython-39.pyc
│  │     │  │     ├─ template_test.cpython-39.pyc
│  │     │  │     ├─ testing_test.cpython-39.pyc
│  │     │  │     ├─ twisted_test.cpython-39.pyc
│  │     │  │     ├─ util.cpython-39.pyc
│  │     │  │     ├─ util_test.cpython-39.pyc
│  │     │  │     ├─ websocket_test.cpython-39.pyc
│  │     │  │     ├─ web_test.cpython-39.pyc
│  │     │  │     ├─ wsgi_test.cpython-39.pyc
│  │     │  │     ├─ __init__.cpython-39.pyc
│  │     │  │     └─ __main__.cpython-39.pyc
│  │     │  ├─ testing.py
│  │     │  ├─ util.py
│  │     │  ├─ web.py
│  │     │  ├─ websocket.py
│  │     │  ├─ wsgi.py
│  │     │  ├─ _locale_data.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ auth.cpython-39.pyc
│  │     │     ├─ autoreload.cpython-39.pyc
│  │     │     ├─ concurrent.cpython-39.pyc
│  │     │     ├─ curl_httpclient.cpython-39.pyc
│  │     │     ├─ escape.cpython-39.pyc
│  │     │     ├─ gen.cpython-39.pyc
│  │     │     ├─ http1connection.cpython-39.pyc
│  │     │     ├─ httpclient.cpython-39.pyc
│  │     │     ├─ httpserver.cpython-39.pyc
│  │     │     ├─ httputil.cpython-39.pyc
│  │     │     ├─ ioloop.cpython-39.pyc
│  │     │     ├─ iostream.cpython-39.pyc
│  │     │     ├─ locale.cpython-39.pyc
│  │     │     ├─ locks.cpython-39.pyc
│  │     │     ├─ log.cpython-39.pyc
│  │     │     ├─ netutil.cpython-39.pyc
│  │     │     ├─ options.cpython-39.pyc
│  │     │     ├─ process.cpython-39.pyc
│  │     │     ├─ queues.cpython-39.pyc
│  │     │     ├─ routing.cpython-39.pyc
│  │     │     ├─ simple_httpclient.cpython-39.pyc
│  │     │     ├─ tcpclient.cpython-39.pyc
│  │     │     ├─ tcpserver.cpython-39.pyc
│  │     │     ├─ template.cpython-39.pyc
│  │     │     ├─ testing.cpython-39.pyc
│  │     │     ├─ util.cpython-39.pyc
│  │     │     ├─ web.cpython-39.pyc
│  │     │     ├─ websocket.cpython-39.pyc
│  │     │     ├─ wsgi.cpython-39.pyc
│  │     │     ├─ _locale_data.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ tornado-6.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ traitlets
│  │     │  ├─ config
│  │     │  │  ├─ application.py
│  │     │  │  ├─ argcomplete_config.py
│  │     │  │  ├─ configurable.py
│  │     │  │  ├─ loader.py
│  │     │  │  ├─ manager.py
│  │     │  │  ├─ sphinxdoc.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_application.py
│  │     │  │  │  ├─ test_argcomplete.py
│  │     │  │  │  ├─ test_configurable.py
│  │     │  │  │  ├─ test_loader.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_application.cpython-39.pyc
│  │     │  │  │     ├─ test_argcomplete.cpython-39.pyc
│  │     │  │  │     ├─ test_configurable.cpython-39.pyc
│  │     │  │  │     ├─ test_loader.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ application.cpython-39.pyc
│  │     │  │     ├─ argcomplete_config.cpython-39.pyc
│  │     │  │     ├─ configurable.cpython-39.pyc
│  │     │  │     ├─ loader.cpython-39.pyc
│  │     │  │     ├─ manager.cpython-39.pyc
│  │     │  │     ├─ sphinxdoc.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ log.py
│  │     │  ├─ py.typed
│  │     │  ├─ tests
│  │     │  │  ├─ test_traitlets.py
│  │     │  │  ├─ test_traitlets_enum.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ _warnings.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ test_traitlets.cpython-39.pyc
│  │     │  │     ├─ test_traitlets_enum.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     ├─ _warnings.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ traitlets.py
│  │     │  ├─ utils
│  │     │  │  ├─ bunch.py
│  │     │  │  ├─ decorators.py
│  │     │  │  ├─ descriptions.py
│  │     │  │  ├─ getargspec.py
│  │     │  │  ├─ importstring.py
│  │     │  │  ├─ nested_update.py
│  │     │  │  ├─ sentinel.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_bunch.py
│  │     │  │  │  ├─ test_decorators.py
│  │     │  │  │  ├─ test_importstring.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_bunch.cpython-39.pyc
│  │     │  │  │     ├─ test_decorators.cpython-39.pyc
│  │     │  │  │     ├─ test_importstring.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ text.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ bunch.cpython-39.pyc
│  │     │  │     ├─ decorators.cpython-39.pyc
│  │     │  │     ├─ descriptions.cpython-39.pyc
│  │     │  │     ├─ getargspec.cpython-39.pyc
│  │     │  │     ├─ importstring.cpython-39.pyc
│  │     │  │     ├─ nested_update.cpython-39.pyc
│  │     │  │     ├─ sentinel.cpython-39.pyc
│  │     │  │     ├─ text.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ log.cpython-39.pyc
│  │     │     ├─ traitlets.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ traitlets-5.9.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ COPYING.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ typing_extensions-4.5.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ typing_extensions.py
│  │     ├─ tzdata
│  │     │  ├─ zoneinfo
│  │     │  │  ├─ Africa
│  │     │  │  │  ├─ Abidjan
│  │     │  │  │  ├─ Accra
│  │     │  │  │  ├─ Addis_Ababa
│  │     │  │  │  ├─ Algiers
│  │     │  │  │  ├─ Asmara
│  │     │  │  │  ├─ Asmera
│  │     │  │  │  ├─ Bamako
│  │     │  │  │  ├─ Bangui
│  │     │  │  │  ├─ Banjul
│  │     │  │  │  ├─ Bissau
│  │     │  │  │  ├─ Blantyre
│  │     │  │  │  ├─ Brazzaville
│  │     │  │  │  ├─ Bujumbura
│  │     │  │  │  ├─ Cairo
│  │     │  │  │  ├─ Casablanca
│  │     │  │  │  ├─ Ceuta
│  │     │  │  │  ├─ Conakry
│  │     │  │  │  ├─ Dakar
│  │     │  │  │  ├─ Dar_es_Salaam
│  │     │  │  │  ├─ Djibouti
│  │     │  │  │  ├─ Douala
│  │     │  │  │  ├─ El_Aaiun
│  │     │  │  │  ├─ Freetown
│  │     │  │  │  ├─ Gaborone
│  │     │  │  │  ├─ Harare
│  │     │  │  │  ├─ Johannesburg
│  │     │  │  │  ├─ Juba
│  │     │  │  │  ├─ Kampala
│  │     │  │  │  ├─ Khartoum
│  │     │  │  │  ├─ Kigali
│  │     │  │  │  ├─ Kinshasa
│  │     │  │  │  ├─ Lagos
│  │     │  │  │  ├─ Libreville
│  │     │  │  │  ├─ Lome
│  │     │  │  │  ├─ Luanda
│  │     │  │  │  ├─ Lubumbashi
│  │     │  │  │  ├─ Lusaka
│  │     │  │  │  ├─ Malabo
│  │     │  │  │  ├─ Maputo
│  │     │  │  │  ├─ Maseru
│  │     │  │  │  ├─ Mbabane
│  │     │  │  │  ├─ Mogadishu
│  │     │  │  │  ├─ Monrovia
│  │     │  │  │  ├─ Nairobi
│  │     │  │  │  ├─ Ndjamena
│  │     │  │  │  ├─ Niamey
│  │     │  │  │  ├─ Nouakchott
│  │     │  │  │  ├─ Ouagadougou
│  │     │  │  │  ├─ Porto-Novo
│  │     │  │  │  ├─ Sao_Tome
│  │     │  │  │  ├─ Timbuktu
│  │     │  │  │  ├─ Tripoli
│  │     │  │  │  ├─ Tunis
│  │     │  │  │  ├─ Windhoek
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ America
│  │     │  │  │  ├─ Adak
│  │     │  │  │  ├─ Anchorage
│  │     │  │  │  ├─ Anguilla
│  │     │  │  │  ├─ Antigua
│  │     │  │  │  ├─ Araguaina
│  │     │  │  │  ├─ Argentina
│  │     │  │  │  │  ├─ Buenos_Aires
│  │     │  │  │  │  ├─ Catamarca
│  │     │  │  │  │  ├─ ComodRivadavia
│  │     │  │  │  │  ├─ Cordoba
│  │     │  │  │  │  ├─ Jujuy
│  │     │  │  │  │  ├─ La_Rioja
│  │     │  │  │  │  ├─ Mendoza
│  │     │  │  │  │  ├─ Rio_Gallegos
│  │     │  │  │  │  ├─ Salta
│  │     │  │  │  │  ├─ San_Juan
│  │     │  │  │  │  ├─ San_Luis
│  │     │  │  │  │  ├─ Tucuman
│  │     │  │  │  │  ├─ Ushuaia
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ Aruba
│  │     │  │  │  ├─ Asuncion
│  │     │  │  │  ├─ Atikokan
│  │     │  │  │  ├─ Atka
│  │     │  │  │  ├─ Bahia
│  │     │  │  │  ├─ Bahia_Banderas
│  │     │  │  │  ├─ Barbados
│  │     │  │  │  ├─ Belem
│  │     │  │  │  ├─ Belize
│  │     │  │  │  ├─ Blanc-Sablon
│  │     │  │  │  ├─ Boa_Vista
│  │     │  │  │  ├─ Bogota
│  │     │  │  │  ├─ Boise
│  │     │  │  │  ├─ Buenos_Aires
│  │     │  │  │  ├─ Cambridge_Bay
│  │     │  │  │  ├─ Campo_Grande
│  │     │  │  │  ├─ Cancun
│  │     │  │  │  ├─ Caracas
│  │     │  │  │  ├─ Catamarca
│  │     │  │  │  ├─ Cayenne
│  │     │  │  │  ├─ Cayman
│  │     │  │  │  ├─ Chicago
│  │     │  │  │  ├─ Chihuahua
│  │     │  │  │  ├─ Ciudad_Juarez
│  │     │  │  │  ├─ Coral_Harbour
│  │     │  │  │  ├─ Cordoba
│  │     │  │  │  ├─ Costa_Rica
│  │     │  │  │  ├─ Creston
│  │     │  │  │  ├─ Cuiaba
│  │     │  │  │  ├─ Curacao
│  │     │  │  │  ├─ Danmarkshavn
│  │     │  │  │  ├─ Dawson
│  │     │  │  │  ├─ Dawson_Creek
│  │     │  │  │  ├─ Denver
│  │     │  │  │  ├─ Detroit
│  │     │  │  │  ├─ Dominica
│  │     │  │  │  ├─ Edmonton
│  │     │  │  │  ├─ Eirunepe
│  │     │  │  │  ├─ El_Salvador
│  │     │  │  │  ├─ Ensenada
│  │     │  │  │  ├─ Fortaleza
│  │     │  │  │  ├─ Fort_Nelson
│  │     │  │  │  ├─ Fort_Wayne
│  │     │  │  │  ├─ Glace_Bay
│  │     │  │  │  ├─ Godthab
│  │     │  │  │  ├─ Goose_Bay
│  │     │  │  │  ├─ Grand_Turk
│  │     │  │  │  ├─ Grenada
│  │     │  │  │  ├─ Guadeloupe
│  │     │  │  │  ├─ Guatemala
│  │     │  │  │  ├─ Guayaquil
│  │     │  │  │  ├─ Guyana
│  │     │  │  │  ├─ Halifax
│  │     │  │  │  ├─ Havana
│  │     │  │  │  ├─ Hermosillo
│  │     │  │  │  ├─ Indiana
│  │     │  │  │  │  ├─ Indianapolis
│  │     │  │  │  │  ├─ Knox
│  │     │  │  │  │  ├─ Marengo
│  │     │  │  │  │  ├─ Petersburg
│  │     │  │  │  │  ├─ Tell_City
│  │     │  │  │  │  ├─ Vevay
│  │     │  │  │  │  ├─ Vincennes
│  │     │  │  │  │  ├─ Winamac
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ Indianapolis
│  │     │  │  │  ├─ Inuvik
│  │     │  │  │  ├─ Iqaluit
│  │     │  │  │  ├─ Jamaica
│  │     │  │  │  ├─ Jujuy
│  │     │  │  │  ├─ Juneau
│  │     │  │  │  ├─ Kentucky
│  │     │  │  │  │  ├─ Louisville
│  │     │  │  │  │  ├─ Monticello
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ Knox_IN
│  │     │  │  │  ├─ Kralendijk
│  │     │  │  │  ├─ La_Paz
│  │     │  │  │  ├─ Lima
│  │     │  │  │  ├─ Los_Angeles
│  │     │  │  │  ├─ Louisville
│  │     │  │  │  ├─ Lower_Princes
│  │     │  │  │  ├─ Maceio
│  │     │  │  │  ├─ Managua
│  │     │  │  │  ├─ Manaus
│  │     │  │  │  ├─ Marigot
│  │     │  │  │  ├─ Martinique
│  │     │  │  │  ├─ Matamoros
│  │     │  │  │  ├─ Mazatlan
│  │     │  │  │  ├─ Mendoza
│  │     │  │  │  ├─ Menominee
│  │     │  │  │  ├─ Merida
│  │     │  │  │  ├─ Metlakatla
│  │     │  │  │  ├─ Mexico_City
│  │     │  │  │  ├─ Miquelon
│  │     │  │  │  ├─ Moncton
│  │     │  │  │  ├─ Monterrey
│  │     │  │  │  ├─ Montevideo
│  │     │  │  │  ├─ Montreal
│  │     │  │  │  ├─ Montserrat
│  │     │  │  │  ├─ Nassau
│  │     │  │  │  ├─ New_York
│  │     │  │  │  ├─ Nipigon
│  │     │  │  │  ├─ Nome
│  │     │  │  │  ├─ Noronha
│  │     │  │  │  ├─ North_Dakota
│  │     │  │  │  │  ├─ Beulah
│  │     │  │  │  │  ├─ Center
│  │     │  │  │  │  ├─ New_Salem
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ Nuuk
│  │     │  │  │  ├─ Ojinaga
│  │     │  │  │  ├─ Panama
│  │     │  │  │  ├─ Pangnirtung
│  │     │  │  │  ├─ Paramaribo
│  │     │  │  │  ├─ Phoenix
│  │     │  │  │  ├─ Port-au-Prince
│  │     │  │  │  ├─ Porto_Acre
│  │     │  │  │  ├─ Porto_Velho
│  │     │  │  │  ├─ Port_of_Spain
│  │     │  │  │  ├─ Puerto_Rico
│  │     │  │  │  ├─ Punta_Arenas
│  │     │  │  │  ├─ Rainy_River
│  │     │  │  │  ├─ Rankin_Inlet
│  │     │  │  │  ├─ Recife
│  │     │  │  │  ├─ Regina
│  │     │  │  │  ├─ Resolute
│  │     │  │  │  ├─ Rio_Branco
│  │     │  │  │  ├─ Rosario
│  │     │  │  │  ├─ Santarem
│  │     │  │  │  ├─ Santa_Isabel
│  │     │  │  │  ├─ Santiago
│  │     │  │  │  ├─ Santo_Domingo
│  │     │  │  │  ├─ Sao_Paulo
│  │     │  │  │  ├─ Scoresbysund
│  │     │  │  │  ├─ Shiprock
│  │     │  │  │  ├─ Sitka
│  │     │  │  │  ├─ St_Barthelemy
│  │     │  │  │  ├─ St_Johns
│  │     │  │  │  ├─ St_Kitts
│  │     │  │  │  ├─ St_Lucia
│  │     │  │  │  ├─ St_Thomas
│  │     │  │  │  ├─ St_Vincent
│  │     │  │  │  ├─ Swift_Current
│  │     │  │  │  ├─ Tegucigalpa
│  │     │  │  │  ├─ Thule
│  │     │  │  │  ├─ Thunder_Bay
│  │     │  │  │  ├─ Tijuana
│  │     │  │  │  ├─ Toronto
│  │     │  │  │  ├─ Tortola
│  │     │  │  │  ├─ Vancouver
│  │     │  │  │  ├─ Virgin
│  │     │  │  │  ├─ Whitehorse
│  │     │  │  │  ├─ Winnipeg
│  │     │  │  │  ├─ Yakutat
│  │     │  │  │  ├─ Yellowknife
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ Antarctica
│  │     │  │  │  ├─ Casey
│  │     │  │  │  ├─ Davis
│  │     │  │  │  ├─ DumontDUrville
│  │     │  │  │  ├─ Macquarie
│  │     │  │  │  ├─ Mawson
│  │     │  │  │  ├─ McMurdo
│  │     │  │  │  ├─ Palmer
│  │     │  │  │  ├─ Rothera
│  │     │  │  │  ├─ South_Pole
│  │     │  │  │  ├─ Syowa
│  │     │  │  │  ├─ Troll
│  │     │  │  │  ├─ Vostok
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ Arctic
│  │     │  │  │  ├─ Longyearbyen
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ Asia
│  │     │  │  │  ├─ Aden
│  │     │  │  │  ├─ Almaty
│  │     │  │  │  ├─ Amman
│  │     │  │  │  ├─ Anadyr
│  │     │  │  │  ├─ Aqtau
│  │     │  │  │  ├─ Aqtobe
│  │     │  │  │  ├─ Ashgabat
│  │     │  │  │  ├─ Ashkhabad
│  │     │  │  │  ├─ Atyrau
│  │     │  │  │  ├─ Baghdad
│  │     │  │  │  ├─ Bahrain
│  │     │  │  │  ├─ Baku
│  │     │  │  │  ├─ Bangkok
│  │     │  │  │  ├─ Barnaul
│  │     │  │  │  ├─ Beirut
│  │     │  │  │  ├─ Bishkek
│  │     │  │  │  ├─ Brunei
│  │     │  │  │  ├─ Calcutta
│  │     │  │  │  ├─ Chita
│  │     │  │  │  ├─ Choibalsan
│  │     │  │  │  ├─ Chongqing
│  │     │  │  │  ├─ Chungking
│  │     │  │  │  ├─ Colombo
│  │     │  │  │  ├─ Dacca
│  │     │  │  │  ├─ Damascus
│  │     │  │  │  ├─ Dhaka
│  │     │  │  │  ├─ Dili
│  │     │  │  │  ├─ Dubai
│  │     │  │  │  ├─ Dushanbe
│  │     │  │  │  ├─ Famagusta
│  │     │  │  │  ├─ Gaza
│  │     │  │  │  ├─ Harbin
│  │     │  │  │  ├─ Hebron
│  │     │  │  │  ├─ Hong_Kong
│  │     │  │  │  ├─ Hovd
│  │     │  │  │  ├─ Ho_Chi_Minh
│  │     │  │  │  ├─ Irkutsk
│  │     │  │  │  ├─ Istanbul
│  │     │  │  │  ├─ Jakarta
│  │     │  │  │  ├─ Jayapura
│  │     │  │  │  ├─ Jerusalem
│  │     │  │  │  ├─ Kabul
│  │     │  │  │  ├─ Kamchatka
│  │     │  │  │  ├─ Karachi
│  │     │  │  │  ├─ Kashgar
│  │     │  │  │  ├─ Kathmandu
│  │     │  │  │  ├─ Katmandu
│  │     │  │  │  ├─ Khandyga
│  │     │  │  │  ├─ Kolkata
│  │     │  │  │  ├─ Krasnoyarsk
│  │     │  │  │  ├─ Kuala_Lumpur
│  │     │  │  │  ├─ Kuching
│  │     │  │  │  ├─ Kuwait
│  │     │  │  │  ├─ Macao
│  │     │  │  │  ├─ Macau
│  │     │  │  │  ├─ Magadan
│  │     │  │  │  ├─ Makassar
│  │     │  │  │  ├─ Manila
│  │     │  │  │  ├─ Muscat
│  │     │  │  │  ├─ Nicosia
│  │     │  │  │  ├─ Novokuznetsk
│  │     │  │  │  ├─ Novosibirsk
│  │     │  │  │  ├─ Omsk
│  │     │  │  │  ├─ Oral
│  │     │  │  │  ├─ Phnom_Penh
│  │     │  │  │  ├─ Pontianak
│  │     │  │  │  ├─ Pyongyang
│  │     │  │  │  ├─ Qatar
│  │     │  │  │  ├─ Qostanay
│  │     │  │  │  ├─ Qyzylorda
│  │     │  │  │  ├─ Rangoon
│  │     │  │  │  ├─ Riyadh
│  │     │  │  │  ├─ Saigon
│  │     │  │  │  ├─ Sakhalin
│  │     │  │  │  ├─ Samarkand
│  │     │  │  │  ├─ Seoul
│  │     │  │  │  ├─ Shanghai
│  │     │  │  │  ├─ Singapore
│  │     │  │  │  ├─ Srednekolymsk
│  │     │  │  │  ├─ Taipei
│  │     │  │  │  ├─ Tashkent
│  │     │  │  │  ├─ Tbilisi
│  │     │  │  │  ├─ Tehran
│  │     │  │  │  ├─ Tel_Aviv
│  │     │  │  │  ├─ Thimbu
│  │     │  │  │  ├─ Thimphu
│  │     │  │  │  ├─ Tokyo
│  │     │  │  │  ├─ Tomsk
│  │     │  │  │  ├─ Ujung_Pandang
│  │     │  │  │  ├─ Ulaanbaatar
│  │     │  │  │  ├─ Ulan_Bator
│  │     │  │  │  ├─ Urumqi
│  │     │  │  │  ├─ Ust-Nera
│  │     │  │  │  ├─ Vientiane
│  │     │  │  │  ├─ Vladivostok
│  │     │  │  │  ├─ Yakutsk
│  │     │  │  │  ├─ Yangon
│  │     │  │  │  ├─ Yekaterinburg
│  │     │  │  │  ├─ Yerevan
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ Atlantic
│  │     │  │  │  ├─ Azores
│  │     │  │  │  ├─ Bermuda
│  │     │  │  │  ├─ Canary
│  │     │  │  │  ├─ Cape_Verde
│  │     │  │  │  ├─ Faeroe
│  │     │  │  │  ├─ Faroe
│  │     │  │  │  ├─ Jan_Mayen
│  │     │  │  │  ├─ Madeira
│  │     │  │  │  ├─ Reykjavik
│  │     │  │  │  ├─ South_Georgia
│  │     │  │  │  ├─ Stanley
│  │     │  │  │  ├─ St_Helena
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ Australia
│  │     │  │  │  ├─ ACT
│  │     │  │  │  ├─ Adelaide
│  │     │  │  │  ├─ Brisbane
│  │     │  │  │  ├─ Broken_Hill
│  │     │  │  │  ├─ Canberra
│  │     │  │  │  ├─ Currie
│  │     │  │  │  ├─ Darwin
│  │     │  │  │  ├─ Eucla
│  │     │  │  │  ├─ Hobart
│  │     │  │  │  ├─ LHI
│  │     │  │  │  ├─ Lindeman
│  │     │  │  │  ├─ Lord_Howe
│  │     │  │  │  ├─ Melbourne
│  │     │  │  │  ├─ North
│  │     │  │  │  ├─ NSW
│  │     │  │  │  ├─ Perth
│  │     │  │  │  ├─ Queensland
│  │     │  │  │  ├─ South
│  │     │  │  │  ├─ Sydney
│  │     │  │  │  ├─ Tasmania
│  │     │  │  │  ├─ Victoria
│  │     │  │  │  ├─ West
│  │     │  │  │  ├─ Yancowinna
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ Brazil
│  │     │  │  │  ├─ Acre
│  │     │  │  │  ├─ DeNoronha
│  │     │  │  │  ├─ East
│  │     │  │  │  ├─ West
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ Canada
│  │     │  │  │  ├─ Atlantic
│  │     │  │  │  ├─ Central
│  │     │  │  │  ├─ Eastern
│  │     │  │  │  ├─ Mountain
│  │     │  │  │  ├─ Newfoundland
│  │     │  │  │  ├─ Pacific
│  │     │  │  │  ├─ Saskatchewan
│  │     │  │  │  ├─ Yukon
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ CET
│  │     │  │  ├─ Chile
│  │     │  │  │  ├─ Continental
│  │     │  │  │  ├─ EasterIsland
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ CST6CDT
│  │     │  │  ├─ Cuba
│  │     │  │  ├─ EET
│  │     │  │  ├─ Egypt
│  │     │  │  ├─ Eire
│  │     │  │  ├─ EST
│  │     │  │  ├─ EST5EDT
│  │     │  │  ├─ Etc
│  │     │  │  │  ├─ GMT
│  │     │  │  │  ├─ GMT+0
│  │     │  │  │  ├─ GMT+1
│  │     │  │  │  ├─ GMT+10
│  │     │  │  │  ├─ GMT+11
│  │     │  │  │  ├─ GMT+12
│  │     │  │  │  ├─ GMT+2
│  │     │  │  │  ├─ GMT+3
│  │     │  │  │  ├─ GMT+4
│  │     │  │  │  ├─ GMT+5
│  │     │  │  │  ├─ GMT+6
│  │     │  │  │  ├─ GMT+7
│  │     │  │  │  ├─ GMT+8
│  │     │  │  │  ├─ GMT+9
│  │     │  │  │  ├─ GMT-0
│  │     │  │  │  ├─ GMT-1
│  │     │  │  │  ├─ GMT-10
│  │     │  │  │  ├─ GMT-11
│  │     │  │  │  ├─ GMT-12
│  │     │  │  │  ├─ GMT-13
│  │     │  │  │  ├─ GMT-14
│  │     │  │  │  ├─ GMT-2
│  │     │  │  │  ├─ GMT-3
│  │     │  │  │  ├─ GMT-4
│  │     │  │  │  ├─ GMT-5
│  │     │  │  │  ├─ GMT-6
│  │     │  │  │  ├─ GMT-7
│  │     │  │  │  ├─ GMT-8
│  │     │  │  │  ├─ GMT-9
│  │     │  │  │  ├─ GMT0
│  │     │  │  │  ├─ Greenwich
│  │     │  │  │  ├─ UCT
│  │     │  │  │  ├─ Universal
│  │     │  │  │  ├─ UTC
│  │     │  │  │  ├─ Zulu
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ Europe
│  │     │  │  │  ├─ Amsterdam
│  │     │  │  │  ├─ Andorra
│  │     │  │  │  ├─ Astrakhan
│  │     │  │  │  ├─ Athens
│  │     │  │  │  ├─ Belfast
│  │     │  │  │  ├─ Belgrade
│  │     │  │  │  ├─ Berlin
│  │     │  │  │  ├─ Bratislava
│  │     │  │  │  ├─ Brussels
│  │     │  │  │  ├─ Bucharest
│  │     │  │  │  ├─ Budapest
│  │     │  │  │  ├─ Busingen
│  │     │  │  │  ├─ Chisinau
│  │     │  │  │  ├─ Copenhagen
│  │     │  │  │  ├─ Dublin
│  │     │  │  │  ├─ Gibraltar
│  │     │  │  │  ├─ Guernsey
│  │     │  │  │  ├─ Helsinki
│  │     │  │  │  ├─ Isle_of_Man
│  │     │  │  │  ├─ Istanbul
│  │     │  │  │  ├─ Jersey
│  │     │  │  │  ├─ Kaliningrad
│  │     │  │  │  ├─ Kiev
│  │     │  │  │  ├─ Kirov
│  │     │  │  │  ├─ Kyiv
│  │     │  │  │  ├─ Lisbon
│  │     │  │  │  ├─ Ljubljana
│  │     │  │  │  ├─ London
│  │     │  │  │  ├─ Luxembourg
│  │     │  │  │  ├─ Madrid
│  │     │  │  │  ├─ Malta
│  │     │  │  │  ├─ Mariehamn
│  │     │  │  │  ├─ Minsk
│  │     │  │  │  ├─ Monaco
│  │     │  │  │  ├─ Moscow
│  │     │  │  │  ├─ Nicosia
│  │     │  │  │  ├─ Oslo
│  │     │  │  │  ├─ Paris
│  │     │  │  │  ├─ Podgorica
│  │     │  │  │  ├─ Prague
│  │     │  │  │  ├─ Riga
│  │     │  │  │  ├─ Rome
│  │     │  │  │  ├─ Samara
│  │     │  │  │  ├─ San_Marino
│  │     │  │  │  ├─ Sarajevo
│  │     │  │  │  ├─ Saratov
│  │     │  │  │  ├─ Simferopol
│  │     │  │  │  ├─ Skopje
│  │     │  │  │  ├─ Sofia
│  │     │  │  │  ├─ Stockholm
│  │     │  │  │  ├─ Tallinn
│  │     │  │  │  ├─ Tirane
│  │     │  │  │  ├─ Tiraspol
│  │     │  │  │  ├─ Ulyanovsk
│  │     │  │  │  ├─ Uzhgorod
│  │     │  │  │  ├─ Vaduz
│  │     │  │  │  ├─ Vatican
│  │     │  │  │  ├─ Vienna
│  │     │  │  │  ├─ Vilnius
│  │     │  │  │  ├─ Volgograd
│  │     │  │  │  ├─ Warsaw
│  │     │  │  │  ├─ Zagreb
│  │     │  │  │  ├─ Zaporozhye
│  │     │  │  │  ├─ Zurich
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ Factory
│  │     │  │  ├─ GB
│  │     │  │  ├─ GB-Eire
│  │     │  │  ├─ GMT
│  │     │  │  ├─ GMT+0
│  │     │  │  ├─ GMT-0
│  │     │  │  ├─ GMT0
│  │     │  │  ├─ Greenwich
│  │     │  │  ├─ Hongkong
│  │     │  │  ├─ HST
│  │     │  │  ├─ Iceland
│  │     │  │  ├─ Indian
│  │     │  │  │  ├─ Antananarivo
│  │     │  │  │  ├─ Chagos
│  │     │  │  │  ├─ Christmas
│  │     │  │  │  ├─ Cocos
│  │     │  │  │  ├─ Comoro
│  │     │  │  │  ├─ Kerguelen
│  │     │  │  │  ├─ Mahe
│  │     │  │  │  ├─ Maldives
│  │     │  │  │  ├─ Mauritius
│  │     │  │  │  ├─ Mayotte
│  │     │  │  │  ├─ Reunion
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ Iran
│  │     │  │  ├─ iso3166.tab
│  │     │  │  ├─ Israel
│  │     │  │  ├─ Jamaica
│  │     │  │  ├─ Japan
│  │     │  │  ├─ Kwajalein
│  │     │  │  ├─ leapseconds
│  │     │  │  ├─ Libya
│  │     │  │  ├─ MET
│  │     │  │  ├─ Mexico
│  │     │  │  │  ├─ BajaNorte
│  │     │  │  │  ├─ BajaSur
│  │     │  │  │  ├─ General
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ MST
│  │     │  │  ├─ MST7MDT
│  │     │  │  ├─ Navajo
│  │     │  │  ├─ NZ
│  │     │  │  ├─ NZ-CHAT
│  │     │  │  ├─ Pacific
│  │     │  │  │  ├─ Apia
│  │     │  │  │  ├─ Auckland
│  │     │  │  │  ├─ Bougainville
│  │     │  │  │  ├─ Chatham
│  │     │  │  │  ├─ Chuuk
│  │     │  │  │  ├─ Easter
│  │     │  │  │  ├─ Efate
│  │     │  │  │  ├─ Enderbury
│  │     │  │  │  ├─ Fakaofo
│  │     │  │  │  ├─ Fiji
│  │     │  │  │  ├─ Funafuti
│  │     │  │  │  ├─ Galapagos
│  │     │  │  │  ├─ Gambier
│  │     │  │  │  ├─ Guadalcanal
│  │     │  │  │  ├─ Guam
│  │     │  │  │  ├─ Honolulu
│  │     │  │  │  ├─ Johnston
│  │     │  │  │  ├─ Kanton
│  │     │  │  │  ├─ Kiritimati
│  │     │  │  │  ├─ Kosrae
│  │     │  │  │  ├─ Kwajalein
│  │     │  │  │  ├─ Majuro
│  │     │  │  │  ├─ Marquesas
│  │     │  │  │  ├─ Midway
│  │     │  │  │  ├─ Nauru
│  │     │  │  │  ├─ Niue
│  │     │  │  │  ├─ Norfolk
│  │     │  │  │  ├─ Noumea
│  │     │  │  │  ├─ Pago_Pago
│  │     │  │  │  ├─ Palau
│  │     │  │  │  ├─ Pitcairn
│  │     │  │  │  ├─ Pohnpei
│  │     │  │  │  ├─ Ponape
│  │     │  │  │  ├─ Port_Moresby
│  │     │  │  │  ├─ Rarotonga
│  │     │  │  │  ├─ Saipan
│  │     │  │  │  ├─ Samoa
│  │     │  │  │  ├─ Tahiti
│  │     │  │  │  ├─ Tarawa
│  │     │  │  │  ├─ Tongatapu
│  │     │  │  │  ├─ Truk
│  │     │  │  │  ├─ Wake
│  │     │  │  │  ├─ Wallis
│  │     │  │  │  ├─ Yap
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ Poland
│  │     │  │  ├─ Portugal
│  │     │  │  ├─ PRC
│  │     │  │  ├─ PST8PDT
│  │     │  │  ├─ ROC
│  │     │  │  ├─ ROK
│  │     │  │  ├─ Singapore
│  │     │  │  ├─ Turkey
│  │     │  │  ├─ tzdata.zi
│  │     │  │  ├─ UCT
│  │     │  │  ├─ Universal
│  │     │  │  ├─ US
│  │     │  │  │  ├─ Alaska
│  │     │  │  │  ├─ Aleutian
│  │     │  │  │  ├─ Arizona
│  │     │  │  │  ├─ Central
│  │     │  │  │  ├─ East-Indiana
│  │     │  │  │  ├─ Eastern
│  │     │  │  │  ├─ Hawaii
│  │     │  │  │  ├─ Indiana-Starke
│  │     │  │  │  ├─ Michigan
│  │     │  │  │  ├─ Mountain
│  │     │  │  │  ├─ Pacific
│  │     │  │  │  ├─ Samoa
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ UTC
│  │     │  │  ├─ W-SU
│  │     │  │  ├─ WET
│  │     │  │  ├─ zone.tab
│  │     │  │  ├─ zone1970.tab
│  │     │  │  ├─ Zulu
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ zones
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ tzdata-2023.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ LICENSE_APACHE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ urllib3
│  │     │  ├─ connection.py
│  │     │  ├─ connectionpool.py
│  │     │  ├─ contrib
│  │     │  │  ├─ appengine.py
│  │     │  │  ├─ ntlmpool.py
│  │     │  │  ├─ pyopenssl.py
│  │     │  │  ├─ securetransport.py
│  │     │  │  ├─ socks.py
│  │     │  │  ├─ _appengine_environ.py
│  │     │  │  ├─ _securetransport
│  │     │  │  │  ├─ bindings.py
│  │     │  │  │  ├─ low_level.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bindings.cpython-39.pyc
│  │     │  │  │     ├─ low_level.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ appengine.cpython-39.pyc
│  │     │  │     ├─ ntlmpool.cpython-39.pyc
│  │     │  │     ├─ pyopenssl.cpython-39.pyc
│  │     │  │     ├─ securetransport.cpython-39.pyc
│  │     │  │     ├─ socks.cpython-39.pyc
│  │     │  │     ├─ _appengine_environ.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ exceptions.py
│  │     │  ├─ fields.py
│  │     │  ├─ filepost.py
│  │     │  ├─ packages
│  │     │  │  ├─ backports
│  │     │  │  │  ├─ makefile.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ makefile.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ six.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ six.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ poolmanager.py
│  │     │  ├─ request.py
│  │     │  ├─ response.py
│  │     │  ├─ util
│  │     │  │  ├─ connection.py
│  │     │  │  ├─ proxy.py
│  │     │  │  ├─ queue.py
│  │     │  │  ├─ request.py
│  │     │  │  ├─ response.py
│  │     │  │  ├─ retry.py
│  │     │  │  ├─ ssltransport.py
│  │     │  │  ├─ ssl_.py
│  │     │  │  ├─ ssl_match_hostname.py
│  │     │  │  ├─ timeout.py
│  │     │  │  ├─ url.py
│  │     │  │  ├─ wait.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ connection.cpython-39.pyc
│  │     │  │     ├─ proxy.cpython-39.pyc
│  │     │  │     ├─ queue.cpython-39.pyc
│  │     │  │     ├─ request.cpython-39.pyc
│  │     │  │     ├─ response.cpython-39.pyc
│  │     │  │     ├─ retry.cpython-39.pyc
│  │     │  │     ├─ ssltransport.cpython-39.pyc
│  │     │  │     ├─ ssl_.cpython-39.pyc
│  │     │  │     ├─ ssl_match_hostname.cpython-39.pyc
│  │     │  │     ├─ timeout.cpython-39.pyc
│  │     │  │     ├─ url.cpython-39.pyc
│  │     │  │     ├─ wait.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _collections.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ connection.cpython-39.pyc
│  │     │     ├─ connectionpool.cpython-39.pyc
│  │     │     ├─ exceptions.cpython-39.pyc
│  │     │     ├─ fields.cpython-39.pyc
│  │     │     ├─ filepost.cpython-39.pyc
│  │     │     ├─ poolmanager.cpython-39.pyc
│  │     │     ├─ request.cpython-39.pyc
│  │     │     ├─ response.cpython-39.pyc
│  │     │     ├─ _collections.cpython-39.pyc
│  │     │     ├─ _version.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ urllib3-1.26.15.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ uvicorn
│  │     │  ├─ config.py
│  │     │  ├─ importer.py
│  │     │  ├─ lifespan
│  │     │  │  ├─ off.py
│  │     │  │  ├─ on.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ off.cpython-39.pyc
│  │     │  │     ├─ on.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ logging.py
│  │     │  ├─ loops
│  │     │  │  ├─ asyncio.py
│  │     │  │  ├─ auto.py
│  │     │  │  ├─ uvloop.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ asyncio.cpython-39.pyc
│  │     │  │     ├─ auto.cpython-39.pyc
│  │     │  │     ├─ uvloop.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ main.py
│  │     │  ├─ middleware
│  │     │  │  ├─ asgi2.py
│  │     │  │  ├─ message_logger.py
│  │     │  │  ├─ proxy_headers.py
│  │     │  │  ├─ wsgi.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ asgi2.cpython-39.pyc
│  │     │  │     ├─ message_logger.cpython-39.pyc
│  │     │  │     ├─ proxy_headers.cpython-39.pyc
│  │     │  │     ├─ wsgi.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ protocols
│  │     │  │  ├─ http
│  │     │  │  │  ├─ auto.py
│  │     │  │  │  ├─ flow_control.py
│  │     │  │  │  ├─ h11_impl.py
│  │     │  │  │  ├─ httptools_impl.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ auto.cpython-39.pyc
│  │     │  │  │     ├─ flow_control.cpython-39.pyc
│  │     │  │  │     ├─ h11_impl.cpython-39.pyc
│  │     │  │  │     ├─ httptools_impl.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ websockets
│  │     │  │  │  ├─ auto.py
│  │     │  │  │  ├─ websockets_impl.py
│  │     │  │  │  ├─ wsproto_impl.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ auto.cpython-39.pyc
│  │     │  │  │     ├─ websockets_impl.cpython-39.pyc
│  │     │  │  │     ├─ wsproto_impl.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ server.py
│  │     │  ├─ supervisors
│  │     │  │  ├─ basereload.py
│  │     │  │  ├─ multiprocess.py
│  │     │  │  ├─ statreload.py
│  │     │  │  ├─ watchfilesreload.py
│  │     │  │  ├─ watchgodreload.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ basereload.cpython-39.pyc
│  │     │  │     ├─ multiprocess.cpython-39.pyc
│  │     │  │     ├─ statreload.cpython-39.pyc
│  │     │  │     ├─ watchfilesreload.cpython-39.pyc
│  │     │  │     ├─ watchgodreload.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ workers.py
│  │     │  ├─ _subprocess.py
│  │     │  ├─ _types.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ config.cpython-39.pyc
│  │     │     ├─ importer.cpython-39.pyc
│  │     │     ├─ logging.cpython-39.pyc
│  │     │     ├─ main.cpython-39.pyc
│  │     │     ├─ server.cpython-39.pyc
│  │     │     ├─ workers.cpython-39.pyc
│  │     │     ├─ _subprocess.cpython-39.pyc
│  │     │     ├─ _types.cpython-39.pyc
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ uvicorn-0.21.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ wcwidth
│  │     │  ├─ table_wide.py
│  │     │  ├─ table_zero.py
│  │     │  ├─ unicode_versions.py
│  │     │  ├─ wcwidth.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ table_wide.cpython-39.pyc
│  │     │     ├─ table_zero.cpython-39.pyc
│  │     │     ├─ unicode_versions.cpython-39.pyc
│  │     │     ├─ wcwidth.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ wcwidth-0.2.6.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ win32
│  │     │  ├─ Demos
│  │     │  │  ├─ BackupRead_BackupWrite.py
│  │     │  │  ├─ BackupSeek_streamheaders.py
│  │     │  │  ├─ cerapi.py
│  │     │  │  ├─ CopyFileEx.py
│  │     │  │  ├─ CreateFileTransacted_MiniVersion.py
│  │     │  │  ├─ c_extension
│  │     │  │  │  ├─ setup.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ setup.cpython-39.pyc
│  │     │  │  ├─ dde
│  │     │  │  │  ├─ ddeclient.py
│  │     │  │  │  ├─ ddeserver.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ ddeclient.cpython-39.pyc
│  │     │  │  │     └─ ddeserver.cpython-39.pyc
│  │     │  │  ├─ desktopmanager.py
│  │     │  │  ├─ eventLogDemo.py
│  │     │  │  ├─ EvtFormatMessage.py
│  │     │  │  ├─ EvtSubscribe_pull.py
│  │     │  │  ├─ EvtSubscribe_push.py
│  │     │  │  ├─ FileSecurityTest.py
│  │     │  │  ├─ getfilever.py
│  │     │  │  ├─ GetSaveFileName.py
│  │     │  │  ├─ images
│  │     │  │  │  ├─ frowny.bmp
│  │     │  │  │  └─ smiley.bmp
│  │     │  │  ├─ mmapfile_demo.py
│  │     │  │  ├─ NetValidatePasswordPolicy.py
│  │     │  │  ├─ OpenEncryptedFileRaw.py
│  │     │  │  ├─ pipes
│  │     │  │  │  ├─ cat.py
│  │     │  │  │  ├─ runproc.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cat.cpython-39.pyc
│  │     │  │  │     └─ runproc.cpython-39.pyc
│  │     │  │  ├─ print_desktop.py
│  │     │  │  ├─ rastest.py
│  │     │  │  ├─ RegCreateKeyTransacted.py
│  │     │  │  ├─ RegRestoreKey.py
│  │     │  │  ├─ security
│  │     │  │  │  ├─ account_rights.py
│  │     │  │  │  ├─ explicit_entries.py
│  │     │  │  │  ├─ GetTokenInformation.py
│  │     │  │  │  ├─ get_policy_info.py
│  │     │  │  │  ├─ list_rights.py
│  │     │  │  │  ├─ localized_names.py
│  │     │  │  │  ├─ lsaregevent.py
│  │     │  │  │  ├─ lsastore.py
│  │     │  │  │  ├─ query_information.py
│  │     │  │  │  ├─ regsave_sa.py
│  │     │  │  │  ├─ regsecurity.py
│  │     │  │  │  ├─ sa_inherit.py
│  │     │  │  │  ├─ security_enums.py
│  │     │  │  │  ├─ setkernelobjectsecurity.py
│  │     │  │  │  ├─ setnamedsecurityinfo.py
│  │     │  │  │  ├─ setsecurityinfo.py
│  │     │  │  │  ├─ setuserobjectsecurity.py
│  │     │  │  │  ├─ set_file_audit.py
│  │     │  │  │  ├─ set_file_owner.py
│  │     │  │  │  ├─ set_policy_info.py
│  │     │  │  │  ├─ sspi
│  │     │  │  │  │  ├─ fetch_url.py
│  │     │  │  │  │  ├─ simple_auth.py
│  │     │  │  │  │  ├─ socket_server.py
│  │     │  │  │  │  ├─ validate_password.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fetch_url.cpython-39.pyc
│  │     │  │  │  │     ├─ simple_auth.cpython-39.pyc
│  │     │  │  │  │     ├─ socket_server.cpython-39.pyc
│  │     │  │  │  │     └─ validate_password.cpython-39.pyc
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ account_rights.cpython-39.pyc
│  │     │  │  │     ├─ explicit_entries.cpython-39.pyc
│  │     │  │  │     ├─ GetTokenInformation.cpython-39.pyc
│  │     │  │  │     ├─ get_policy_info.cpython-39.pyc
│  │     │  │  │     ├─ list_rights.cpython-39.pyc
│  │     │  │  │     ├─ localized_names.cpython-39.pyc
│  │     │  │  │     ├─ lsaregevent.cpython-39.pyc
│  │     │  │  │     ├─ lsastore.cpython-39.pyc
│  │     │  │  │     ├─ query_information.cpython-39.pyc
│  │     │  │  │     ├─ regsave_sa.cpython-39.pyc
│  │     │  │  │     ├─ regsecurity.cpython-39.pyc
│  │     │  │  │     ├─ sa_inherit.cpython-39.pyc
│  │     │  │  │     ├─ security_enums.cpython-39.pyc
│  │     │  │  │     ├─ setkernelobjectsecurity.cpython-39.pyc
│  │     │  │  │     ├─ setnamedsecurityinfo.cpython-39.pyc
│  │     │  │  │     ├─ setsecurityinfo.cpython-39.pyc
│  │     │  │  │     ├─ setuserobjectsecurity.cpython-39.pyc
│  │     │  │  │     ├─ set_file_audit.cpython-39.pyc
│  │     │  │  │     ├─ set_file_owner.cpython-39.pyc
│  │     │  │  │     └─ set_policy_info.cpython-39.pyc
│  │     │  │  ├─ service
│  │     │  │  │  ├─ nativePipeTestService.py
│  │     │  │  │  ├─ pipeTestService.py
│  │     │  │  │  ├─ pipeTestServiceClient.py
│  │     │  │  │  ├─ serviceEvents.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ nativePipeTestService.cpython-39.pyc
│  │     │  │  │     ├─ pipeTestService.cpython-39.pyc
│  │     │  │  │     ├─ pipeTestServiceClient.cpython-39.pyc
│  │     │  │  │     └─ serviceEvents.cpython-39.pyc
│  │     │  │  ├─ SystemParametersInfo.py
│  │     │  │  ├─ timer_demo.py
│  │     │  │  ├─ win32clipboardDemo.py
│  │     │  │  ├─ win32clipboard_bitmapdemo.py
│  │     │  │  ├─ win32comport_demo.py
│  │     │  │  ├─ win32console_demo.py
│  │     │  │  ├─ win32cred_demo.py
│  │     │  │  ├─ win32fileDemo.py
│  │     │  │  ├─ win32gui_demo.py
│  │     │  │  ├─ win32gui_devicenotify.py
│  │     │  │  ├─ win32gui_dialog.py
│  │     │  │  ├─ win32gui_menu.py
│  │     │  │  ├─ win32gui_taskbar.py
│  │     │  │  ├─ win32netdemo.py
│  │     │  │  ├─ win32rcparser_demo.py
│  │     │  │  ├─ win32servicedemo.py
│  │     │  │  ├─ win32ts_logoff_disconnected.py
│  │     │  │  ├─ win32wnet
│  │     │  │  │  ├─ testwnet.py
│  │     │  │  │  ├─ winnetwk.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ testwnet.cpython-39.pyc
│  │     │  │  │     └─ winnetwk.cpython-39.pyc
│  │     │  │  ├─ winprocess.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ BackupRead_BackupWrite.cpython-39.pyc
│  │     │  │     ├─ BackupSeek_streamheaders.cpython-39.pyc
│  │     │  │     ├─ cerapi.cpython-39.pyc
│  │     │  │     ├─ CopyFileEx.cpython-39.pyc
│  │     │  │     ├─ CreateFileTransacted_MiniVersion.cpython-39.pyc
│  │     │  │     ├─ desktopmanager.cpython-39.pyc
│  │     │  │     ├─ eventLogDemo.cpython-39.pyc
│  │     │  │     ├─ EvtFormatMessage.cpython-39.pyc
│  │     │  │     ├─ EvtSubscribe_pull.cpython-39.pyc
│  │     │  │     ├─ EvtSubscribe_push.cpython-39.pyc
│  │     │  │     ├─ FileSecurityTest.cpython-39.pyc
│  │     │  │     ├─ getfilever.cpython-39.pyc
│  │     │  │     ├─ GetSaveFileName.cpython-39.pyc
│  │     │  │     ├─ mmapfile_demo.cpython-39.pyc
│  │     │  │     ├─ NetValidatePasswordPolicy.cpython-39.pyc
│  │     │  │     ├─ OpenEncryptedFileRaw.cpython-39.pyc
│  │     │  │     ├─ print_desktop.cpython-39.pyc
│  │     │  │     ├─ rastest.cpython-39.pyc
│  │     │  │     ├─ RegCreateKeyTransacted.cpython-39.pyc
│  │     │  │     ├─ RegRestoreKey.cpython-39.pyc
│  │     │  │     ├─ SystemParametersInfo.cpython-39.pyc
│  │     │  │     ├─ timer_demo.cpython-39.pyc
│  │     │  │     ├─ win32clipboardDemo.cpython-39.pyc
│  │     │  │     ├─ win32clipboard_bitmapdemo.cpython-39.pyc
│  │     │  │     ├─ win32comport_demo.cpython-39.pyc
│  │     │  │     ├─ win32console_demo.cpython-39.pyc
│  │     │  │     ├─ win32cred_demo.cpython-39.pyc
│  │     │  │     ├─ win32fileDemo.cpython-39.pyc
│  │     │  │     ├─ win32gui_demo.cpython-39.pyc
│  │     │  │     ├─ win32gui_devicenotify.cpython-39.pyc
│  │     │  │     ├─ win32gui_dialog.cpython-39.pyc
│  │     │  │     ├─ win32gui_menu.cpython-39.pyc
│  │     │  │     ├─ win32gui_taskbar.cpython-39.pyc
│  │     │  │     ├─ win32netdemo.cpython-39.pyc
│  │     │  │     ├─ win32rcparser_demo.cpython-39.pyc
│  │     │  │     ├─ win32servicedemo.cpython-39.pyc
│  │     │  │     ├─ win32ts_logoff_disconnected.cpython-39.pyc
│  │     │  │     └─ winprocess.cpython-39.pyc
│  │     │  ├─ include
│  │     │  │  └─ PyWinTypes.h
│  │     │  ├─ lib
│  │     │  │  ├─ afxres.py
│  │     │  │  ├─ commctrl.py
│  │     │  │  ├─ dbi.py
│  │     │  │  ├─ mmsystem.py
│  │     │  │  ├─ netbios.py
│  │     │  │  ├─ ntsecuritycon.py
│  │     │  │  ├─ pywin32_bootstrap.py
│  │     │  │  ├─ pywin32_testutil.py
│  │     │  │  ├─ pywintypes.py
│  │     │  │  ├─ rasutil.py
│  │     │  │  ├─ regcheck.py
│  │     │  │  ├─ regutil.py
│  │     │  │  ├─ sspi.py
│  │     │  │  ├─ sspicon.py
│  │     │  │  ├─ win2kras.py
│  │     │  │  ├─ win32con.py
│  │     │  │  ├─ win32cryptcon.py
│  │     │  │  ├─ win32evtlogutil.py
│  │     │  │  ├─ win32gui_struct.py
│  │     │  │  ├─ win32inetcon.py
│  │     │  │  ├─ win32netcon.py
│  │     │  │  ├─ win32pdhquery.py
│  │     │  │  ├─ win32pdhutil.py
│  │     │  │  ├─ win32rcparser.py
│  │     │  │  ├─ win32serviceutil.py
│  │     │  │  ├─ win32timezone.py
│  │     │  │  ├─ win32traceutil.py
│  │     │  │  ├─ win32verstamp.py
│  │     │  │  ├─ winerror.py
│  │     │  │  ├─ winioctlcon.py
│  │     │  │  ├─ winnt.py
│  │     │  │  ├─ winperf.py
│  │     │  │  ├─ winxptheme.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ afxres.cpython-39.pyc
│  │     │  │     ├─ commctrl.cpython-39.pyc
│  │     │  │     ├─ dbi.cpython-39.pyc
│  │     │  │     ├─ mmsystem.cpython-39.pyc
│  │     │  │     ├─ netbios.cpython-39.pyc
│  │     │  │     ├─ ntsecuritycon.cpython-39.pyc
│  │     │  │     ├─ pywin32_bootstrap.cpython-39.pyc
│  │     │  │     ├─ pywin32_testutil.cpython-39.pyc
│  │     │  │     ├─ pywintypes.cpython-39.pyc
│  │     │  │     ├─ rasutil.cpython-39.pyc
│  │     │  │     ├─ regcheck.cpython-39.pyc
│  │     │  │     ├─ regutil.cpython-39.pyc
│  │     │  │     ├─ sspi.cpython-39.pyc
│  │     │  │     ├─ sspicon.cpython-39.pyc
│  │     │  │     ├─ win2kras.cpython-39.pyc
│  │     │  │     ├─ win32con.cpython-39.pyc
│  │     │  │     ├─ win32cryptcon.cpython-39.pyc
│  │     │  │     ├─ win32evtlogutil.cpython-39.pyc
│  │     │  │     ├─ win32gui_struct.cpython-39.pyc
│  │     │  │     ├─ win32inetcon.cpython-39.pyc
│  │     │  │     ├─ win32netcon.cpython-39.pyc
│  │     │  │     ├─ win32pdhquery.cpython-39.pyc
│  │     │  │     ├─ win32pdhutil.cpython-39.pyc
│  │     │  │     ├─ win32rcparser.cpython-39.pyc
│  │     │  │     ├─ win32serviceutil.cpython-39.pyc
│  │     │  │     ├─ win32timezone.cpython-39.pyc
│  │     │  │     ├─ win32traceutil.cpython-39.pyc
│  │     │  │     ├─ win32verstamp.cpython-39.pyc
│  │     │  │     ├─ winerror.cpython-39.pyc
│  │     │  │     ├─ winioctlcon.cpython-39.pyc
│  │     │  │     ├─ winnt.cpython-39.pyc
│  │     │  │     ├─ winperf.cpython-39.pyc
│  │     │  │     └─ winxptheme.cpython-39.pyc
│  │     │  ├─ libs
│  │     │  │  └─ pywintypes.lib
│  │     │  ├─ license.txt
│  │     │  ├─ mmapfile.pyd
│  │     │  ├─ odbc.pyd
│  │     │  ├─ perfmon.pyd
│  │     │  ├─ perfmondata.dll
│  │     │  ├─ pythonservice.exe
│  │     │  ├─ scripts
│  │     │  │  ├─ backupEventLog.py
│  │     │  │  ├─ ce
│  │     │  │  │  ├─ pysynch.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ pysynch.cpython-39.pyc
│  │     │  │  ├─ ControlService.py
│  │     │  │  ├─ killProcName.py
│  │     │  │  ├─ rasutil.py
│  │     │  │  ├─ regsetup.py
│  │     │  │  ├─ setup_d.py
│  │     │  │  ├─ VersionStamp
│  │     │  │  │  ├─ BrandProject.py
│  │     │  │  │  ├─ bulkstamp.py
│  │     │  │  │  ├─ vssutil.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ BrandProject.cpython-39.pyc
│  │     │  │  │     ├─ bulkstamp.cpython-39.pyc
│  │     │  │  │     └─ vssutil.cpython-39.pyc
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ backupEventLog.cpython-39.pyc
│  │     │  │     ├─ ControlService.cpython-39.pyc
│  │     │  │     ├─ killProcName.cpython-39.pyc
│  │     │  │     ├─ rasutil.cpython-39.pyc
│  │     │  │     ├─ regsetup.cpython-39.pyc
│  │     │  │     └─ setup_d.cpython-39.pyc
│  │     │  ├─ servicemanager.pyd
│  │     │  ├─ test
│  │     │  │  ├─ handles.py
│  │     │  │  ├─ testall.py
│  │     │  │  ├─ test_clipboard.py
│  │     │  │  ├─ test_exceptions.py
│  │     │  │  ├─ test_odbc.py
│  │     │  │  ├─ test_pywintypes.py
│  │     │  │  ├─ test_security.py
│  │     │  │  ├─ test_sspi.py
│  │     │  │  ├─ test_win32api.py
│  │     │  │  ├─ test_win32crypt.py
│  │     │  │  ├─ test_win32event.py
│  │     │  │  ├─ test_win32file.py
│  │     │  │  ├─ test_win32gui.py
│  │     │  │  ├─ test_win32guistruct.py
│  │     │  │  ├─ test_win32inet.py
│  │     │  │  ├─ test_win32net.py
│  │     │  │  ├─ test_win32pipe.py
│  │     │  │  ├─ test_win32print.py
│  │     │  │  ├─ test_win32profile.py
│  │     │  │  ├─ test_win32rcparser.py
│  │     │  │  ├─ test_win32timezone.py
│  │     │  │  ├─ test_win32trace.py
│  │     │  │  ├─ test_win32wnet.py
│  │     │  │  ├─ win32rcparser
│  │     │  │  │  ├─ python.bmp
│  │     │  │  │  ├─ python.ico
│  │     │  │  │  ├─ test.h
│  │     │  │  │  └─ test.rc
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ handles.cpython-39.pyc
│  │     │  │     ├─ testall.cpython-39.pyc
│  │     │  │     ├─ test_clipboard.cpython-39.pyc
│  │     │  │     ├─ test_exceptions.cpython-39.pyc
│  │     │  │     ├─ test_odbc.cpython-39.pyc
│  │     │  │     ├─ test_pywintypes.cpython-39.pyc
│  │     │  │     ├─ test_security.cpython-39.pyc
│  │     │  │     ├─ test_sspi.cpython-39.pyc
│  │     │  │     ├─ test_win32api.cpython-39.pyc
│  │     │  │     ├─ test_win32crypt.cpython-39.pyc
│  │     │  │     ├─ test_win32event.cpython-39.pyc
│  │     │  │     ├─ test_win32file.cpython-39.pyc
│  │     │  │     ├─ test_win32gui.cpython-39.pyc
│  │     │  │     ├─ test_win32guistruct.cpython-39.pyc
│  │     │  │     ├─ test_win32inet.cpython-39.pyc
│  │     │  │     ├─ test_win32net.cpython-39.pyc
│  │     │  │     ├─ test_win32pipe.cpython-39.pyc
│  │     │  │     ├─ test_win32print.cpython-39.pyc
│  │     │  │     ├─ test_win32profile.cpython-39.pyc
│  │     │  │     ├─ test_win32rcparser.cpython-39.pyc
│  │     │  │     ├─ test_win32timezone.cpython-39.pyc
│  │     │  │     ├─ test_win32trace.cpython-39.pyc
│  │     │  │     └─ test_win32wnet.cpython-39.pyc
│  │     │  ├─ timer.pyd
│  │     │  ├─ win32api.pyd
│  │     │  ├─ win32clipboard.pyd
│  │     │  ├─ win32console.pyd
│  │     │  ├─ win32cred.pyd
│  │     │  ├─ win32crypt.pyd
│  │     │  ├─ win32event.pyd
│  │     │  ├─ win32evtlog.pyd
│  │     │  ├─ win32file.pyd
│  │     │  ├─ win32gui.pyd
│  │     │  ├─ win32help.pyd
│  │     │  ├─ win32inet.pyd
│  │     │  ├─ win32job.pyd
│  │     │  ├─ win32lz.pyd
│  │     │  ├─ win32net.pyd
│  │     │  ├─ win32pdh.pyd
│  │     │  ├─ win32pipe.pyd
│  │     │  ├─ win32print.pyd
│  │     │  ├─ win32process.pyd
│  │     │  ├─ win32profile.pyd
│  │     │  ├─ win32ras.pyd
│  │     │  ├─ win32security.pyd
│  │     │  ├─ win32service.pyd
│  │     │  ├─ win32trace.pyd
│  │     │  ├─ win32transaction.pyd
│  │     │  ├─ win32ts.pyd
│  │     │  ├─ win32wnet.pyd
│  │     │  ├─ winxpgui.pyd
│  │     │  ├─ _win32sysloader.pyd
│  │     │  └─ _winxptheme.pyd
│  │     ├─ win32com
│  │     │  ├─ client
│  │     │  │  ├─ build.py
│  │     │  │  ├─ CLSIDToClass.py
│  │     │  │  ├─ combrowse.py
│  │     │  │  ├─ connect.py
│  │     │  │  ├─ dynamic.py
│  │     │  │  ├─ gencache.py
│  │     │  │  ├─ genpy.py
│  │     │  │  ├─ makepy.py
│  │     │  │  ├─ selecttlb.py
│  │     │  │  ├─ tlbrowse.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ build.cpython-39.pyc
│  │     │  │     ├─ CLSIDToClass.cpython-39.pyc
│  │     │  │     ├─ combrowse.cpython-39.pyc
│  │     │  │     ├─ connect.cpython-39.pyc
│  │     │  │     ├─ dynamic.cpython-39.pyc
│  │     │  │     ├─ gencache.cpython-39.pyc
│  │     │  │     ├─ genpy.cpython-39.pyc
│  │     │  │     ├─ makepy.cpython-39.pyc
│  │     │  │     ├─ selecttlb.cpython-39.pyc
│  │     │  │     ├─ tlbrowse.cpython-39.pyc
│  │     │  │     ├─ util.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ demos
│  │     │  │  ├─ connect.py
│  │     │  │  ├─ dump_clipboard.py
│  │     │  │  ├─ eventsApartmentThreaded.py
│  │     │  │  ├─ eventsFreeThreaded.py
│  │     │  │  ├─ excelAddin.py
│  │     │  │  ├─ excelRTDServer.py
│  │     │  │  ├─ iebutton.py
│  │     │  │  ├─ ietoolbar.py
│  │     │  │  ├─ outlookAddin.py
│  │     │  │  ├─ trybag.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ connect.cpython-39.pyc
│  │     │  │     ├─ dump_clipboard.cpython-39.pyc
│  │     │  │     ├─ eventsApartmentThreaded.cpython-39.pyc
│  │     │  │     ├─ eventsFreeThreaded.cpython-39.pyc
│  │     │  │     ├─ excelAddin.cpython-39.pyc
│  │     │  │     ├─ excelRTDServer.cpython-39.pyc
│  │     │  │     ├─ iebutton.cpython-39.pyc
│  │     │  │     ├─ ietoolbar.cpython-39.pyc
│  │     │  │     ├─ outlookAddin.cpython-39.pyc
│  │     │  │     ├─ trybag.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ HTML
│  │     │  │  ├─ docindex.html
│  │     │  │  ├─ GeneratedSupport.html
│  │     │  │  ├─ image
│  │     │  │  │  ├─ blank.gif
│  │     │  │  │  ├─ BTN_HomePage.gif
│  │     │  │  │  ├─ BTN_ManualTop.gif
│  │     │  │  │  ├─ BTN_NextPage.gif
│  │     │  │  │  ├─ BTN_PrevPage.gif
│  │     │  │  │  ├─ pycom_blowing.gif
│  │     │  │  │  ├─ pythoncom.gif
│  │     │  │  │  └─ www_icon.gif
│  │     │  │  ├─ index.html
│  │     │  │  ├─ misc.html
│  │     │  │  ├─ package.html
│  │     │  │  ├─ PythonCOM.html
│  │     │  │  ├─ QuickStartClientCom.html
│  │     │  │  ├─ QuickStartServerCom.html
│  │     │  │  └─ variant.html
│  │     │  ├─ include
│  │     │  │  ├─ PythonCOM.h
│  │     │  │  ├─ PythonCOMRegister.h
│  │     │  │  └─ PythonCOMServer.h
│  │     │  ├─ libs
│  │     │  │  ├─ axscript.lib
│  │     │  │  └─ pythoncom.lib
│  │     │  ├─ License.txt
│  │     │  ├─ makegw
│  │     │  │  ├─ makegw.py
│  │     │  │  ├─ makegwenum.py
│  │     │  │  ├─ makegwparse.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ makegw.cpython-39.pyc
│  │     │  │     ├─ makegwenum.cpython-39.pyc
│  │     │  │     ├─ makegwparse.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ olectl.py
│  │     │  ├─ readme.html
│  │     │  ├─ server
│  │     │  │  ├─ connect.py
│  │     │  │  ├─ dispatcher.py
│  │     │  │  ├─ exception.py
│  │     │  │  ├─ factory.py
│  │     │  │  ├─ localserver.py
│  │     │  │  ├─ policy.py
│  │     │  │  ├─ register.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ connect.cpython-39.pyc
│  │     │  │     ├─ dispatcher.cpython-39.pyc
│  │     │  │     ├─ exception.cpython-39.pyc
│  │     │  │     ├─ factory.cpython-39.pyc
│  │     │  │     ├─ localserver.cpython-39.pyc
│  │     │  │     ├─ policy.cpython-39.pyc
│  │     │  │     ├─ register.cpython-39.pyc
│  │     │  │     ├─ util.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ servers
│  │     │  │  ├─ dictionary.py
│  │     │  │  ├─ interp.py
│  │     │  │  ├─ perfmon.py
│  │     │  │  ├─ PythonTools.py
│  │     │  │  ├─ test_pycomtest.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ dictionary.cpython-39.pyc
│  │     │  │     ├─ interp.cpython-39.pyc
│  │     │  │     ├─ perfmon.cpython-39.pyc
│  │     │  │     ├─ PythonTools.cpython-39.pyc
│  │     │  │     ├─ test_pycomtest.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ storagecon.py
│  │     │  ├─ test
│  │     │  │  ├─ daodump.py
│  │     │  │  ├─ errorSemantics.py
│  │     │  │  ├─ GenTestScripts.py
│  │     │  │  ├─ pippo.idl
│  │     │  │  ├─ pippo_server.py
│  │     │  │  ├─ policySemantics.py
│  │     │  │  ├─ readme.txt
│  │     │  │  ├─ testAccess.py
│  │     │  │  ├─ testADOEvents.py
│  │     │  │  ├─ testall.py
│  │     │  │  ├─ testArrays.py
│  │     │  │  ├─ testAXScript.py
│  │     │  │  ├─ testClipboard.py
│  │     │  │  ├─ testCollections.py
│  │     │  │  ├─ testConversionErrors.py
│  │     │  │  ├─ testDates.py
│  │     │  │  ├─ testDCOM.py
│  │     │  │  ├─ testDictionary.py
│  │     │  │  ├─ testDictionary.vbs
│  │     │  │  ├─ testDynamic.py
│  │     │  │  ├─ testExchange.py
│  │     │  │  ├─ testExplorer.py
│  │     │  │  ├─ testGatewayAddresses.py
│  │     │  │  ├─ testGIT.py
│  │     │  │  ├─ testInterp.vbs
│  │     │  │  ├─ testIterators.py
│  │     │  │  ├─ testmakepy.py
│  │     │  │  ├─ testMarshal.py
│  │     │  │  ├─ testMSOffice.py
│  │     │  │  ├─ testMSOfficeEvents.py
│  │     │  │  ├─ testNetscape.py
│  │     │  │  ├─ testPersist.py
│  │     │  │  ├─ testPippo.py
│  │     │  │  ├─ testPyComTest.py
│  │     │  │  ├─ Testpys.sct
│  │     │  │  ├─ testPyScriptlet.js
│  │     │  │  ├─ testROT.py
│  │     │  │  ├─ testServers.py
│  │     │  │  ├─ testShell.py
│  │     │  │  ├─ testStorage.py
│  │     │  │  ├─ testStreams.py
│  │     │  │  ├─ testvb.py
│  │     │  │  ├─ testvbscript_regexp.py
│  │     │  │  ├─ testWMI.py
│  │     │  │  ├─ testxslt.js
│  │     │  │  ├─ testxslt.py
│  │     │  │  ├─ testxslt.xsl
│  │     │  │  ├─ util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ daodump.cpython-39.pyc
│  │     │  │     ├─ errorSemantics.cpython-39.pyc
│  │     │  │     ├─ GenTestScripts.cpython-39.pyc
│  │     │  │     ├─ pippo_server.cpython-39.pyc
│  │     │  │     ├─ policySemantics.cpython-39.pyc
│  │     │  │     ├─ testAccess.cpython-39.pyc
│  │     │  │     ├─ testADOEvents.cpython-39.pyc
│  │     │  │     ├─ testall.cpython-39.pyc
│  │     │  │     ├─ testArrays.cpython-39.pyc
│  │     │  │     ├─ testAXScript.cpython-39.pyc
│  │     │  │     ├─ testClipboard.cpython-39.pyc
│  │     │  │     ├─ testCollections.cpython-39.pyc
│  │     │  │     ├─ testConversionErrors.cpython-39.pyc
│  │     │  │     ├─ testDates.cpython-39.pyc
│  │     │  │     ├─ testDCOM.cpython-39.pyc
│  │     │  │     ├─ testDictionary.cpython-39.pyc
│  │     │  │     ├─ testDynamic.cpython-39.pyc
│  │     │  │     ├─ testExchange.cpython-39.pyc
│  │     │  │     ├─ testExplorer.cpython-39.pyc
│  │     │  │     ├─ testGatewayAddresses.cpython-39.pyc
│  │     │  │     ├─ testGIT.cpython-39.pyc
│  │     │  │     ├─ testIterators.cpython-39.pyc
│  │     │  │     ├─ testmakepy.cpython-39.pyc
│  │     │  │     ├─ testMarshal.cpython-39.pyc
│  │     │  │     ├─ testMSOffice.cpython-39.pyc
│  │     │  │     ├─ testMSOfficeEvents.cpython-39.pyc
│  │     │  │     ├─ testNetscape.cpython-39.pyc
│  │     │  │     ├─ testPersist.cpython-39.pyc
│  │     │  │     ├─ testPippo.cpython-39.pyc
│  │     │  │     ├─ testPyComTest.cpython-39.pyc
│  │     │  │     ├─ testROT.cpython-39.pyc
│  │     │  │     ├─ testServers.cpython-39.pyc
│  │     │  │     ├─ testShell.cpython-39.pyc
│  │     │  │     ├─ testStorage.cpython-39.pyc
│  │     │  │     ├─ testStreams.cpython-39.pyc
│  │     │  │     ├─ testvb.cpython-39.pyc
│  │     │  │     ├─ testvbscript_regexp.cpython-39.pyc
│  │     │  │     ├─ testWMI.cpython-39.pyc
│  │     │  │     ├─ testxslt.cpython-39.pyc
│  │     │  │     ├─ util.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ universal.py
│  │     │  ├─ util.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ olectl.cpython-39.pyc
│  │     │     ├─ storagecon.cpython-39.pyc
│  │     │     ├─ universal.cpython-39.pyc
│  │     │     ├─ util.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ win32comext
│  │     │  ├─ adsi
│  │     │  │  ├─ adsi.pyd
│  │     │  │  ├─ adsicon.py
│  │     │  │  ├─ demos
│  │     │  │  │  ├─ objectPicker.py
│  │     │  │  │  ├─ scp.py
│  │     │  │  │  ├─ search.py
│  │     │  │  │  ├─ test.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ objectPicker.cpython-39.pyc
│  │     │  │  │     ├─ scp.cpython-39.pyc
│  │     │  │  │     ├─ search.cpython-39.pyc
│  │     │  │  │     └─ test.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ adsicon.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ authorization
│  │     │  │  ├─ authorization.pyd
│  │     │  │  ├─ demos
│  │     │  │  │  ├─ EditSecurity.py
│  │     │  │  │  ├─ EditServiceSecurity.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ EditSecurity.cpython-39.pyc
│  │     │  │  │     └─ EditServiceSecurity.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ axcontrol
│  │     │  │  ├─ axcontrol.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ axdebug
│  │     │  │  ├─ adb.py
│  │     │  │  ├─ axdebug.pyd
│  │     │  │  ├─ codecontainer.py
│  │     │  │  ├─ contexts.py
│  │     │  │  ├─ debugger.py
│  │     │  │  ├─ documents.py
│  │     │  │  ├─ dump.py
│  │     │  │  ├─ expressions.py
│  │     │  │  ├─ gateways.py
│  │     │  │  ├─ stackframe.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ adb.cpython-39.pyc
│  │     │  │     ├─ codecontainer.cpython-39.pyc
│  │     │  │     ├─ contexts.cpython-39.pyc
│  │     │  │     ├─ debugger.cpython-39.pyc
│  │     │  │     ├─ documents.cpython-39.pyc
│  │     │  │     ├─ dump.cpython-39.pyc
│  │     │  │     ├─ expressions.cpython-39.pyc
│  │     │  │     ├─ gateways.cpython-39.pyc
│  │     │  │     ├─ stackframe.cpython-39.pyc
│  │     │  │     ├─ util.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ axscript
│  │     │  │  ├─ asputil.py
│  │     │  │  ├─ axscript.pyd
│  │     │  │  ├─ client
│  │     │  │  │  ├─ debug.py
│  │     │  │  │  ├─ error.py
│  │     │  │  │  ├─ framework.py
│  │     │  │  │  ├─ pydumper.py
│  │     │  │  │  ├─ pyscript.py
│  │     │  │  │  ├─ pyscript_rexec.py
│  │     │  │  │  ├─ scriptdispatch.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ debug.cpython-39.pyc
│  │     │  │  │     ├─ error.cpython-39.pyc
│  │     │  │  │     ├─ framework.cpython-39.pyc
│  │     │  │  │     ├─ pydumper.cpython-39.pyc
│  │     │  │  │     ├─ pyscript.cpython-39.pyc
│  │     │  │  │     ├─ pyscript_rexec.cpython-39.pyc
│  │     │  │  │     ├─ scriptdispatch.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ Demos
│  │     │  │  │  └─ client
│  │     │  │  │     ├─ asp
│  │     │  │  │     │  ├─ caps.asp
│  │     │  │  │     │  ├─ CreateObject.asp
│  │     │  │  │     │  ├─ interrupt
│  │     │  │  │     │  │  ├─ test.asp
│  │     │  │  │     │  │  ├─ test.html
│  │     │  │  │     │  │  ├─ test1.asp
│  │     │  │  │     │  │  └─ test1.html
│  │     │  │  │     │  └─ tut1.asp
│  │     │  │  │     ├─ ie
│  │     │  │  │     │  ├─ calc.htm
│  │     │  │  │     │  ├─ dbgtest.htm
│  │     │  │  │     │  ├─ demo.htm
│  │     │  │  │     │  ├─ demo_check.htm
│  │     │  │  │     │  ├─ demo_intro.htm
│  │     │  │  │     │  ├─ demo_menu.htm
│  │     │  │  │     │  ├─ docwrite.htm
│  │     │  │  │     │  ├─ foo2.htm
│  │     │  │  │     │  ├─ form.htm
│  │     │  │  │     │  ├─ marqueeDemo.htm
│  │     │  │  │     │  ├─ MarqueeText1.htm
│  │     │  │  │     │  ├─ mousetrack.htm
│  │     │  │  │     │  └─ pycom_blowing.gif
│  │     │  │  │     └─ wsh
│  │     │  │  │        ├─ blank.pys
│  │     │  │  │        ├─ excel.pys
│  │     │  │  │        ├─ registry.pys
│  │     │  │  │        └─ test.pys
│  │     │  │  ├─ server
│  │     │  │  │  ├─ axsite.py
│  │     │  │  │  ├─ error.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ axsite.cpython-39.pyc
│  │     │  │  │     ├─ error.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ test
│  │     │  │  │  ├─ debugTest.pys
│  │     │  │  │  ├─ debugTest.vbs
│  │     │  │  │  ├─ leakTest.py
│  │     │  │  │  ├─ testHost.py
│  │     │  │  │  ├─ testHost4Dbg.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ leakTest.cpython-39.pyc
│  │     │  │  │     ├─ testHost.cpython-39.pyc
│  │     │  │  │     └─ testHost4Dbg.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ asputil.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ bits
│  │     │  │  ├─ bits.pyd
│  │     │  │  ├─ test
│  │     │  │  │  ├─ show_all_jobs.py
│  │     │  │  │  ├─ test_bits.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ show_all_jobs.cpython-39.pyc
│  │     │  │  │     └─ test_bits.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ directsound
│  │     │  │  ├─ directsound.pyd
│  │     │  │  ├─ test
│  │     │  │  │  ├─ ds_record.py
│  │     │  │  │  ├─ ds_test.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ ds_record.cpython-39.pyc
│  │     │  │  │     ├─ ds_test.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ ifilter
│  │     │  │  ├─ demo
│  │     │  │  │  ├─ filterDemo.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ filterDemo.cpython-39.pyc
│  │     │  │  ├─ ifilter.pyd
│  │     │  │  ├─ ifiltercon.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ifiltercon.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ internet
│  │     │  │  ├─ inetcon.py
│  │     │  │  ├─ internet.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ inetcon.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ mapi
│  │     │  │  ├─ demos
│  │     │  │  │  ├─ mapisend.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ mapisend.cpython-39.pyc
│  │     │  │  ├─ emsabtags.py
│  │     │  │  ├─ exchange.pyd
│  │     │  │  ├─ mapi.pyd
│  │     │  │  ├─ mapitags.py
│  │     │  │  ├─ mapiutil.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ emsabtags.cpython-39.pyc
│  │     │  │     ├─ mapitags.cpython-39.pyc
│  │     │  │     ├─ mapiutil.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ propsys
│  │     │  │  ├─ propsys.pyd
│  │     │  │  ├─ pscon.py
│  │     │  │  ├─ test
│  │     │  │  │  ├─ testpropsys.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ testpropsys.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ pscon.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ shell
│  │     │  │  ├─ demos
│  │     │  │  │  ├─ browse_for_folder.py
│  │     │  │  │  ├─ create_link.py
│  │     │  │  │  ├─ dump_link.py
│  │     │  │  │  ├─ explorer_browser.py
│  │     │  │  │  ├─ IActiveDesktop.py
│  │     │  │  │  ├─ IFileOperationProgressSink.py
│  │     │  │  │  ├─ IShellLinkDataList.py
│  │     │  │  │  ├─ ITransferAdviseSink.py
│  │     │  │  │  ├─ IUniformResourceLocator.py
│  │     │  │  │  ├─ servers
│  │     │  │  │  │  ├─ column_provider.py
│  │     │  │  │  │  ├─ context_menu.py
│  │     │  │  │  │  ├─ copy_hook.py
│  │     │  │  │  │  ├─ empty_volume_cache.py
│  │     │  │  │  │  ├─ folder_view.py
│  │     │  │  │  │  ├─ icon_handler.py
│  │     │  │  │  │  ├─ shell_view.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ column_provider.cpython-39.pyc
│  │     │  │  │  │     ├─ context_menu.cpython-39.pyc
│  │     │  │  │  │     ├─ copy_hook.cpython-39.pyc
│  │     │  │  │  │     ├─ empty_volume_cache.cpython-39.pyc
│  │     │  │  │  │     ├─ folder_view.cpython-39.pyc
│  │     │  │  │  │     ├─ icon_handler.cpython-39.pyc
│  │     │  │  │  │     └─ shell_view.cpython-39.pyc
│  │     │  │  │  ├─ shellexecuteex.py
│  │     │  │  │  ├─ viewstate.py
│  │     │  │  │  ├─ walk_shell_folders.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ browse_for_folder.cpython-39.pyc
│  │     │  │  │     ├─ create_link.cpython-39.pyc
│  │     │  │  │     ├─ dump_link.cpython-39.pyc
│  │     │  │  │     ├─ explorer_browser.cpython-39.pyc
│  │     │  │  │     ├─ IActiveDesktop.cpython-39.pyc
│  │     │  │  │     ├─ IFileOperationProgressSink.cpython-39.pyc
│  │     │  │  │     ├─ IShellLinkDataList.cpython-39.pyc
│  │     │  │  │     ├─ ITransferAdviseSink.cpython-39.pyc
│  │     │  │  │     ├─ IUniformResourceLocator.cpython-39.pyc
│  │     │  │  │     ├─ shellexecuteex.cpython-39.pyc
│  │     │  │  │     ├─ viewstate.cpython-39.pyc
│  │     │  │  │     └─ walk_shell_folders.cpython-39.pyc
│  │     │  │  ├─ shell.pyd
│  │     │  │  ├─ shellcon.py
│  │     │  │  ├─ test
│  │     │  │  │  ├─ testShellFolder.py
│  │     │  │  │  ├─ testShellItem.py
│  │     │  │  │  ├─ testSHFileOperation.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ testShellFolder.cpython-39.pyc
│  │     │  │  │     ├─ testShellItem.cpython-39.pyc
│  │     │  │  │     └─ testSHFileOperation.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ shellcon.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  └─ taskscheduler
│  │     │     ├─ taskscheduler.pyd
│  │     │     ├─ test
│  │     │     │  ├─ test_addtask.py
│  │     │     │  ├─ test_addtask_1.py
│  │     │     │  ├─ test_addtask_2.py
│  │     │     │  ├─ test_localsystem.py
│  │     │     │  └─ __pycache__
│  │     │     │     ├─ test_addtask.cpython-39.pyc
│  │     │     │     ├─ test_addtask_1.cpython-39.pyc
│  │     │     │     ├─ test_addtask_2.cpython-39.pyc
│  │     │     │     └─ test_localsystem.cpython-39.pyc
│  │     │     ├─ __init__.py
│  │     │     └─ __pycache__
│  │     │        └─ __init__.cpython-39.pyc
│  │     ├─ xgboost
│  │     │  ├─ callback.py
│  │     │  ├─ collective.py
│  │     │  ├─ compat.py
│  │     │  ├─ config.py
│  │     │  ├─ core.py
│  │     │  ├─ dask.py
│  │     │  ├─ data.py
│  │     │  ├─ federated.py
│  │     │  ├─ lib
│  │     │  │  └─ xgboost.dll
│  │     │  ├─ libpath.py
│  │     │  ├─ plotting.py
│  │     │  ├─ py.typed
│  │     │  ├─ rabit.py
│  │     │  ├─ sklearn.py
│  │     │  ├─ spark
│  │     │  │  ├─ core.py
│  │     │  │  ├─ data.py
│  │     │  │  ├─ estimator.py
│  │     │  │  ├─ model.py
│  │     │  │  ├─ params.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ core.cpython-39.pyc
│  │     │  │     ├─ data.cpython-39.pyc
│  │     │  │     ├─ estimator.cpython-39.pyc
│  │     │  │     ├─ model.cpython-39.pyc
│  │     │  │     ├─ params.cpython-39.pyc
│  │     │  │     ├─ utils.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ testing.py
│  │     │  ├─ tracker.py
│  │     │  ├─ training.py
│  │     │  ├─ VERSION
│  │     │  ├─ _typing.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ callback.cpython-39.pyc
│  │     │     ├─ collective.cpython-39.pyc
│  │     │     ├─ compat.cpython-39.pyc
│  │     │     ├─ config.cpython-39.pyc
│  │     │     ├─ core.cpython-39.pyc
│  │     │     ├─ dask.cpython-39.pyc
│  │     │     ├─ data.cpython-39.pyc
│  │     │     ├─ federated.cpython-39.pyc
│  │     │     ├─ libpath.cpython-39.pyc
│  │     │     ├─ plotting.cpython-39.pyc
│  │     │     ├─ rabit.cpython-39.pyc
│  │     │     ├─ sklearn.cpython-39.pyc
│  │     │     ├─ testing.cpython-39.pyc
│  │     │     ├─ tracker.cpython-39.pyc
│  │     │     ├─ training.cpython-39.pyc
│  │     │     ├─ _typing.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ xgboost-1.7.5.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ yaml
│  │     │  ├─ composer.py
│  │     │  ├─ constructor.py
│  │     │  ├─ cyaml.py
│  │     │  ├─ dumper.py
│  │     │  ├─ emitter.py
│  │     │  ├─ error.py
│  │     │  ├─ events.py
│  │     │  ├─ loader.py
│  │     │  ├─ nodes.py
│  │     │  ├─ parser.py
│  │     │  ├─ reader.py
│  │     │  ├─ representer.py
│  │     │  ├─ resolver.py
│  │     │  ├─ scanner.py
│  │     │  ├─ serializer.py
│  │     │  ├─ tokens.py
│  │     │  ├─ _yaml.cp39-win_amd64.pyd
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ composer.cpython-39.pyc
│  │     │     ├─ constructor.cpython-39.pyc
│  │     │     ├─ cyaml.cpython-39.pyc
│  │     │     ├─ dumper.cpython-39.pyc
│  │     │     ├─ emitter.cpython-39.pyc
│  │     │     ├─ error.cpython-39.pyc
│  │     │     ├─ events.cpython-39.pyc
│  │     │     ├─ loader.cpython-39.pyc
│  │     │     ├─ nodes.cpython-39.pyc
│  │     │     ├─ parser.cpython-39.pyc
│  │     │     ├─ reader.cpython-39.pyc
│  │     │     ├─ representer.cpython-39.pyc
│  │     │     ├─ resolver.cpython-39.pyc
│  │     │     ├─ scanner.cpython-39.pyc
│  │     │     ├─ serializer.cpython-39.pyc
│  │     │     ├─ tokens.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ zipp
│  │     │  ├─ py310compat.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ py310compat.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ zipp-3.15.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ zmq
│  │     │  ├─ asyncio.py
│  │     │  ├─ auth
│  │     │  │  ├─ asyncio.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ certs.py
│  │     │  │  ├─ ioloop.py
│  │     │  │  ├─ thread.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ asyncio.cpython-39.pyc
│  │     │  │     ├─ base.cpython-39.pyc
│  │     │  │     ├─ certs.cpython-39.pyc
│  │     │  │     ├─ ioloop.cpython-39.pyc
│  │     │  │     ├─ thread.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ backend
│  │     │  │  ├─ cffi
│  │     │  │  │  ├─ context.py
│  │     │  │  │  ├─ devices.py
│  │     │  │  │  ├─ error.py
│  │     │  │  │  ├─ message.py
│  │     │  │  │  ├─ socket.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ _cdefs.h
│  │     │  │  │  ├─ _poll.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ context.cpython-39.pyc
│  │     │  │  │     ├─ devices.cpython-39.pyc
│  │     │  │  │     ├─ error.cpython-39.pyc
│  │     │  │  │     ├─ message.cpython-39.pyc
│  │     │  │  │     ├─ socket.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     ├─ _poll.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ cython
│  │     │  │  │  ├─ checkrc.pxd
│  │     │  │  │  ├─ constant_enums.pxi
│  │     │  │  │  ├─ context.cp39-win_amd64.pyd
│  │     │  │  │  ├─ context.pxd
│  │     │  │  │  ├─ error.cp39-win_amd64.pyd
│  │     │  │  │  ├─ libzmq.pxd
│  │     │  │  │  ├─ message.cp39-win_amd64.pyd
│  │     │  │  │  ├─ message.pxd
│  │     │  │  │  ├─ socket.cp39-win_amd64.pyd
│  │     │  │  │  ├─ socket.pxd
│  │     │  │  │  ├─ utils.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _device.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _poll.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _proxy_steerable.cp39-win_amd64.pyd
│  │     │  │  │  ├─ _version.cp39-win_amd64.pyd
│  │     │  │  │  ├─ __init__.pxd
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ select.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ select.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ constants.py
│  │     │  ├─ decorators.py
│  │     │  ├─ devices
│  │     │  │  ├─ basedevice.py
│  │     │  │  ├─ monitoredqueue.cp39-win_amd64.pyd
│  │     │  │  ├─ monitoredqueue.pxd
│  │     │  │  ├─ monitoredqueue.py
│  │     │  │  ├─ monitoredqueuedevice.py
│  │     │  │  ├─ proxydevice.py
│  │     │  │  ├─ proxysteerabledevice.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ basedevice.cpython-39.pyc
│  │     │  │     ├─ monitoredqueue.cpython-39.pyc
│  │     │  │     ├─ monitoredqueuedevice.cpython-39.pyc
│  │     │  │     ├─ proxydevice.cpython-39.pyc
│  │     │  │     ├─ proxysteerabledevice.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ error.py
│  │     │  ├─ eventloop
│  │     │  │  ├─ future.py
│  │     │  │  ├─ ioloop.py
│  │     │  │  ├─ zmqstream.py
│  │     │  │  ├─ _deprecated.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ future.cpython-39.pyc
│  │     │  │     ├─ ioloop.cpython-39.pyc
│  │     │  │     ├─ zmqstream.cpython-39.pyc
│  │     │  │     ├─ _deprecated.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ green
│  │     │  │  ├─ core.py
│  │     │  │  ├─ device.py
│  │     │  │  ├─ eventloop
│  │     │  │  │  ├─ ioloop.py
│  │     │  │  │  ├─ zmqstream.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ ioloop.cpython-39.pyc
│  │     │  │  │     ├─ zmqstream.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ poll.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ core.cpython-39.pyc
│  │     │  │     ├─ device.cpython-39.pyc
│  │     │  │     ├─ poll.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ log
│  │     │  │  ├─ handlers.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ handlers.cpython-39.pyc
│  │     │  │     ├─ __init__.cpython-39.pyc
│  │     │  │     └─ __main__.cpython-39.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ ssh
│  │     │  │  ├─ forward.py
│  │     │  │  ├─ tunnel.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ forward.cpython-39.pyc
│  │     │  │     ├─ tunnel.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ sugar
│  │     │  │  ├─ attrsettr.py
│  │     │  │  ├─ context.py
│  │     │  │  ├─ frame.py
│  │     │  │  ├─ poll.py
│  │     │  │  ├─ socket.py
│  │     │  │  ├─ stopwatch.py
│  │     │  │  ├─ tracker.py
│  │     │  │  ├─ version.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ attrsettr.cpython-39.pyc
│  │     │  │     ├─ context.cpython-39.pyc
│  │     │  │     ├─ frame.cpython-39.pyc
│  │     │  │     ├─ poll.cpython-39.pyc
│  │     │  │     ├─ socket.cpython-39.pyc
│  │     │  │     ├─ stopwatch.cpython-39.pyc
│  │     │  │     ├─ tracker.cpython-39.pyc
│  │     │  │     ├─ version.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ tests
│  │     │  │  ├─ conftest.py
│  │     │  │  ├─ cython_ext.pyx
│  │     │  │  ├─ test_asyncio.py
│  │     │  │  ├─ test_auth.py
│  │     │  │  ├─ test_cffi_backend.py
│  │     │  │  ├─ test_constants.py
│  │     │  │  ├─ test_context.py
│  │     │  │  ├─ test_cython.py
│  │     │  │  ├─ test_decorators.py
│  │     │  │  ├─ test_device.py
│  │     │  │  ├─ test_draft.py
│  │     │  │  ├─ test_error.py
│  │     │  │  ├─ test_etc.py
│  │     │  │  ├─ test_ext.py
│  │     │  │  ├─ test_future.py
│  │     │  │  ├─ test_imports.py
│  │     │  │  ├─ test_includes.py
│  │     │  │  ├─ test_ioloop.py
│  │     │  │  ├─ test_log.py
│  │     │  │  ├─ test_message.py
│  │     │  │  ├─ test_monitor.py
│  │     │  │  ├─ test_monqueue.py
│  │     │  │  ├─ test_multipart.py
│  │     │  │  ├─ test_mypy.py
│  │     │  │  ├─ test_pair.py
│  │     │  │  ├─ test_poll.py
│  │     │  │  ├─ test_proxy_steerable.py
│  │     │  │  ├─ test_pubsub.py
│  │     │  │  ├─ test_reqrep.py
│  │     │  │  ├─ test_retry_eintr.py
│  │     │  │  ├─ test_security.py
│  │     │  │  ├─ test_socket.py
│  │     │  │  ├─ test_ssh.py
│  │     │  │  ├─ test_version.py
│  │     │  │  ├─ test_win32_shim.py
│  │     │  │  ├─ test_z85.py
│  │     │  │  ├─ test_zmqstream.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ conftest.cpython-39.pyc
│  │     │  │     ├─ test_asyncio.cpython-39.pyc
│  │     │  │     ├─ test_auth.cpython-39.pyc
│  │     │  │     ├─ test_cffi_backend.cpython-39.pyc
│  │     │  │     ├─ test_constants.cpython-39.pyc
│  │     │  │     ├─ test_context.cpython-39.pyc
│  │     │  │     ├─ test_cython.cpython-39.pyc
│  │     │  │     ├─ test_decorators.cpython-39.pyc
│  │     │  │     ├─ test_device.cpython-39.pyc
│  │     │  │     ├─ test_draft.cpython-39.pyc
│  │     │  │     ├─ test_error.cpython-39.pyc
│  │     │  │     ├─ test_etc.cpython-39.pyc
│  │     │  │     ├─ test_ext.cpython-39.pyc
│  │     │  │     ├─ test_future.cpython-39.pyc
│  │     │  │     ├─ test_imports.cpython-39.pyc
│  │     │  │     ├─ test_includes.cpython-39.pyc
│  │     │  │     ├─ test_ioloop.cpython-39.pyc
│  │     │  │     ├─ test_log.cpython-39.pyc
│  │     │  │     ├─ test_message.cpython-39.pyc
│  │     │  │     ├─ test_monitor.cpython-39.pyc
│  │     │  │     ├─ test_monqueue.cpython-39.pyc
│  │     │  │     ├─ test_multipart.cpython-39.pyc
│  │     │  │     ├─ test_mypy.cpython-39.pyc
│  │     │  │     ├─ test_pair.cpython-39.pyc
│  │     │  │     ├─ test_poll.cpython-39.pyc
│  │     │  │     ├─ test_proxy_steerable.cpython-39.pyc
│  │     │  │     ├─ test_pubsub.cpython-39.pyc
│  │     │  │     ├─ test_reqrep.cpython-39.pyc
│  │     │  │     ├─ test_retry_eintr.cpython-39.pyc
│  │     │  │     ├─ test_security.cpython-39.pyc
│  │     │  │     ├─ test_socket.cpython-39.pyc
│  │     │  │     ├─ test_ssh.cpython-39.pyc
│  │     │  │     ├─ test_version.cpython-39.pyc
│  │     │  │     ├─ test_win32_shim.cpython-39.pyc
│  │     │  │     ├─ test_z85.cpython-39.pyc
│  │     │  │     ├─ test_zmqstream.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ utils
│  │     │  │  ├─ buffers.pxd
│  │     │  │  ├─ compiler.json
│  │     │  │  ├─ config.json
│  │     │  │  ├─ garbage.py
│  │     │  │  ├─ getpid_compat.h
│  │     │  │  ├─ interop.py
│  │     │  │  ├─ ipcmaxlen.h
│  │     │  │  ├─ jsonapi.py
│  │     │  │  ├─ monitor.py
│  │     │  │  ├─ mutex.h
│  │     │  │  ├─ pyversion_compat.h
│  │     │  │  ├─ strtypes.py
│  │     │  │  ├─ win32.py
│  │     │  │  ├─ z85.py
│  │     │  │  ├─ zmq_compat.h
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ garbage.cpython-39.pyc
│  │     │  │     ├─ interop.cpython-39.pyc
│  │     │  │     ├─ jsonapi.cpython-39.pyc
│  │     │  │     ├─ monitor.cpython-39.pyc
│  │     │  │     ├─ strtypes.cpython-39.pyc
│  │     │  │     ├─ win32.cpython-39.pyc
│  │     │  │     ├─ z85.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _future.py
│  │     │  ├─ _typing.py
│  │     │  ├─ __init__.pxd
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  └─ __pycache__
│  │     │     ├─ asyncio.cpython-39.pyc
│  │     │     ├─ constants.cpython-39.pyc
│  │     │     ├─ decorators.cpython-39.pyc
│  │     │     ├─ error.cpython-39.pyc
│  │     │     ├─ _future.cpython-39.pyc
│  │     │     ├─ _typing.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ _black_version.py
│  │     ├─ _distutils_hack
│  │     │  ├─ override.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ override.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ _pyrsistent_version.py
│  │     ├─ _ruamel_yaml.cp39-win_amd64.pyd
│  │     ├─ _yaml
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ __pycache__
│  │     │  ├─ cycler.cpython-39.pyc
│  │     │  ├─ decorator.cpython-39.pyc
│  │     │  ├─ ipykernel_launcher.cpython-39.pyc
│  │     │  ├─ jupyter.cpython-39.pyc
│  │     │  ├─ mypy_extensions.cpython-39.pyc
│  │     │  ├─ nest_asyncio.cpython-39.pyc
│  │     │  ├─ pathlib.cpython-39.pyc
│  │     │  ├─ pickleshare.cpython-39.pyc
│  │     │  ├─ pylab.cpython-39.pyc
│  │     │  ├─ pythoncom.cpython-39.pyc
│  │     │  ├─ six.cpython-39.pyc
│  │     │  ├─ threadpoolctl.cpython-39.pyc
│  │     │  ├─ typing_extensions.cpython-39.pyc
│  │     │  ├─ _black_version.cpython-39.pyc
│  │     │  └─ _pyrsistent_version.cpython-39.pyc
│  │     └─ ~andas
│  │        ├─ _libs
│  │        │  ├─ algos.cp39-win_amd64.pyd
│  │        │  ├─ algos.pxd
│  │        │  ├─ algos.pyi
│  │        │  ├─ algos.pyx
│  │        │  ├─ algos_common_helper.pxi.in
│  │        │  ├─ algos_take_helper.pxi.in
│  │        │  ├─ arrays.cp39-win_amd64.pyd
│  │        │  ├─ arrays.pxd
│  │        │  ├─ arrays.pyi
│  │        │  ├─ arrays.pyx
│  │        │  ├─ dtypes.pxd
│  │        │  ├─ groupby.cp39-win_amd64.pyd
│  │        │  ├─ groupby.pyi
│  │        │  ├─ groupby.pyx
│  │        │  ├─ hashing.cp39-win_amd64.pyd
│  │        │  ├─ hashing.pyi
│  │        │  ├─ hashing.pyx
│  │        │  ├─ hashtable.cp39-win_amd64.pyd
│  │        │  ├─ hashtable.pxd
│  │        │  ├─ hashtable.pyi
│  │        │  ├─ hashtable.pyx
│  │        │  ├─ hashtable_class_helper.pxi.in
│  │        │  ├─ hashtable_func_helper.pxi.in
│  │        │  ├─ index.cp39-win_amd64.pyd
│  │        │  ├─ index.pyi
│  │        │  ├─ index.pyx
│  │        │  ├─ indexing.cp39-win_amd64.pyd
│  │        │  ├─ indexing.pyi
│  │        │  ├─ indexing.pyx
│  │        │  ├─ index_class_helper.pxi.in
│  │        │  ├─ internals.cp39-win_amd64.pyd
│  │        │  ├─ internals.pyi
│  │        │  ├─ internals.pyx
│  │        │  ├─ interval.cp39-win_amd64.pyd
│  │        │  ├─ interval.pyi
│  │        │  ├─ interval.pyx
│  │        │  ├─ intervaltree.pxi.in
│  │        │  ├─ join.cp39-win_amd64.pyd
│  │        │  ├─ join.pyi
│  │        │  ├─ join.pyx
│  │        │  ├─ json.cp39-win_amd64.pyd
│  │        │  ├─ json.pyi
│  │        │  ├─ khash.pxd
│  │        │  ├─ khash_for_primitive_helper.pxi.in
│  │        │  ├─ lib.cp39-win_amd64.pyd
│  │        │  ├─ lib.pxd
│  │        │  ├─ lib.pyi
│  │        │  ├─ lib.pyx
│  │        │  ├─ missing.cp39-win_amd64.pyd
│  │        │  ├─ missing.pxd
│  │        │  ├─ missing.pyi
│  │        │  ├─ missing.pyx
│  │        │  ├─ ops.cp39-win_amd64.pyd
│  │        │  ├─ ops.pyi
│  │        │  ├─ ops.pyx
│  │        │  ├─ ops_dispatch.cp39-win_amd64.pyd
│  │        │  ├─ ops_dispatch.pyi
│  │        │  ├─ ops_dispatch.pyx
│  │        │  ├─ parsers.cp39-win_amd64.pyd
│  │        │  ├─ parsers.pyi
│  │        │  ├─ parsers.pyx
│  │        │  ├─ properties.cp39-win_amd64.pyd
│  │        │  ├─ properties.pyi
│  │        │  ├─ properties.pyx
│  │        │  ├─ reduction.cp39-win_amd64.pyd
│  │        │  ├─ reduction.pyi
│  │        │  ├─ reduction.pyx
│  │        │  ├─ reshape.cp39-win_amd64.pyd
│  │        │  ├─ reshape.pyi
│  │        │  ├─ reshape.pyx
│  │        │  ├─ sparse.cp39-win_amd64.pyd
│  │        │  ├─ sparse.pyi
│  │        │  ├─ sparse.pyx
│  │        │  ├─ sparse_op_helper.pxi.in
│  │        │  ├─ testing.cp39-win_amd64.pyd
│  │        │  ├─ testing.pyi
│  │        │  ├─ testing.pyx
│  │        │  ├─ tslib.cp39-win_amd64.pyd
│  │        │  ├─ tslib.pyi
│  │        │  ├─ tslib.pyx
│  │        │  ├─ tslibs
│  │        │  │  ├─ base.cp39-win_amd64.pyd
│  │        │  │  ├─ base.pxd
│  │        │  │  ├─ base.pyx
│  │        │  │  ├─ ccalendar.cp39-win_amd64.pyd
│  │        │  │  ├─ ccalendar.pxd
│  │        │  │  ├─ ccalendar.pyi
│  │        │  │  ├─ ccalendar.pyx
│  │        │  │  ├─ conversion.cp39-win_amd64.pyd
│  │        │  │  ├─ conversion.pxd
│  │        │  │  ├─ conversion.pyi
│  │        │  │  ├─ conversion.pyx
│  │        │  │  ├─ dtypes.cp39-win_amd64.pyd
│  │        │  │  ├─ dtypes.pxd
│  │        │  │  ├─ dtypes.pyi
│  │        │  │  ├─ dtypes.pyx
│  │        │  │  ├─ fields.cp39-win_amd64.pyd
│  │        │  │  ├─ fields.pyi
│  │        │  │  ├─ fields.pyx
│  │        │  │  ├─ nattype.cp39-win_amd64.pyd
│  │        │  │  ├─ nattype.pxd
│  │        │  │  ├─ nattype.pyi
│  │        │  │  ├─ nattype.pyx
│  │        │  │  ├─ np_datetime.cp39-win_amd64.pyd
│  │        │  │  ├─ np_datetime.pxd
│  │        │  │  ├─ np_datetime.pyi
│  │        │  │  ├─ np_datetime.pyx
│  │        │  │  ├─ offsets.cp39-win_amd64.pyd
│  │        │  │  ├─ offsets.pxd
│  │        │  │  ├─ offsets.pyi
│  │        │  │  ├─ offsets.pyx
│  │        │  │  ├─ parsing.cp39-win_amd64.pyd
│  │        │  │  ├─ parsing.pxd
│  │        │  │  ├─ parsing.pyi
│  │        │  │  ├─ parsing.pyx
│  │        │  │  ├─ period.cp39-win_amd64.pyd
│  │        │  │  ├─ period.pxd
│  │        │  │  ├─ period.pyi
│  │        │  │  ├─ period.pyx
│  │        │  │  ├─ strptime.cp39-win_amd64.pyd
│  │        │  │  ├─ strptime.pxd
│  │        │  │  ├─ strptime.pyi
│  │        │  │  ├─ strptime.pyx
│  │        │  │  ├─ timedeltas.cp39-win_amd64.pyd
│  │        │  │  ├─ timedeltas.pxd
│  │        │  │  ├─ timedeltas.pyi
│  │        │  │  ├─ timedeltas.pyx
│  │        │  │  ├─ timestamps.cp39-win_amd64.pyd
│  │        │  │  ├─ timestamps.pxd
│  │        │  │  ├─ timestamps.pyi
│  │        │  │  ├─ timestamps.pyx
│  │        │  │  ├─ timezones.cp39-win_amd64.pyd
│  │        │  │  ├─ timezones.pxd
│  │        │  │  ├─ timezones.pyi
│  │        │  │  ├─ timezones.pyx
│  │        │  │  ├─ tzconversion.cp39-win_amd64.pyd
│  │        │  │  ├─ tzconversion.pxd
│  │        │  │  ├─ tzconversion.pyi
│  │        │  │  ├─ tzconversion.pyx
│  │        │  │  ├─ util.pxd
│  │        │  │  ├─ vectorized.cp39-win_amd64.pyd
│  │        │  │  ├─ vectorized.pyi
│  │        │  │  ├─ vectorized.pyx
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-39.pyc
│  │        │  ├─ util.pxd
│  │        │  ├─ window
│  │        │  │  ├─ aggregations.cp39-win_amd64.pyd
│  │        │  │  ├─ aggregations.pyi
│  │        │  │  ├─ aggregations.pyx
│  │        │  │  ├─ concrt140.dll
│  │        │  │  ├─ indexers.cp39-win_amd64.pyd
│  │        │  │  ├─ indexers.pyi
│  │        │  │  ├─ indexers.pyx
│  │        │  │  ├─ msvcp140.dll
│  │        │  │  ├─ vcruntime140_1.dll
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __pycache__
│  │        │  │     └─ __init__.cpython-39.pyc
│  │        │  ├─ writers.cp39-win_amd64.pyd
│  │        │  ├─ writers.pyi
│  │        │  ├─ writers.pyx
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     └─ __init__.cpython-39.pyc
│  │        ├─ _testing
│  │        │  ├─ asserters.py
│  │        │  ├─ compat.py
│  │        │  ├─ contexts.py
│  │        │  ├─ _hypothesis.py
│  │        │  ├─ _io.py
│  │        │  ├─ _random.py
│  │        │  ├─ _warnings.py
│  │        │  ├─ __init__.py
│  │        │  └─ __pycache__
│  │        │     ├─ asserters.cpython-39.pyc
│  │        │     ├─ compat.cpython-39.pyc
│  │        │     ├─ contexts.cpython-39.pyc
│  │        │     ├─ _hypothesis.cpython-39.pyc
│  │        │     ├─ _io.cpython-39.pyc
│  │        │     ├─ _random.cpython-39.pyc
│  │        │     ├─ _warnings.cpython-39.pyc
│  │        │     └─ __init__.cpython-39.pyc
│  │        ├─ _typing.py
│  │        ├─ _version.py
│  │        ├─ __init__.py
│  │        └─ __pycache__
│  │           ├─ conftest.cpython-39.pyc
│  │           ├─ testing.cpython-39.pyc
│  │           ├─ _typing.cpython-39.pyc
│  │           ├─ _version.cpython-39.pyc
│  │           └─ __init__.cpython-39.pyc
│  ├─ pyvenv.cfg
│  ├─ Scripts
│  │  ├─ activate
│  │  ├─ activate-global-python-argcomplete
│  │  ├─ activate.bat
│  │  ├─ Activate.ps1
│  │  ├─ black.exe
│  │  ├─ blackd.exe
│  │  ├─ chardetect.exe
│  │  ├─ datamodel-codegen.exe
│  │  ├─ deactivate.bat
│  │  ├─ email_validator.exe
│  │  ├─ f2py.exe
│  │  ├─ fonttools.exe
│  │  ├─ genson-script.py
│  │  ├─ genson.exe
│  │  ├─ ipython.exe
│  │  ├─ ipython3.exe
│  │  ├─ isort-identify-imports.exe
│  │  ├─ isort.exe
│  │  ├─ jsonschema.exe
│  │  ├─ jupyter-kernel.exe
│  │  ├─ jupyter-kernelspec.exe
│  │  ├─ jupyter-migrate.exe
│  │  ├─ jupyter-run.exe
│  │  ├─ jupyter-troubleshoot.exe
│  │  ├─ jupyter.exe
│  │  ├─ normalizer.exe
│  │  ├─ openapi-spec-validator.exe
│  │  ├─ pip.exe
│  │  ├─ pip3.9.exe
│  │  ├─ pip3.exe
│  │  ├─ prance.exe
│  │  ├─ pyftmerge.exe
│  │  ├─ pyftsubset.exe
│  │  ├─ pygmentize.exe
│  │  ├─ python-argcomplete-check-easy-install-script
│  │  ├─ python.exe
│  │  ├─ pythonw.exe
│  │  ├─ pywin32_postinstall.py
│  │  ├─ pywin32_testall.py
│  │  ├─ register-python-argcomplete
│  │  ├─ ttx.exe
│  │  ├─ uvicorn.exe
│  │  └─ __pycache__
│  │     ├─ pywin32_postinstall.cpython-39.pyc
│  │     └─ pywin32_testall.cpython-39.pyc
│  ├─ share
│  │  ├─ jupyter
│  │  │  └─ kernels
│  │  │     └─ python3
│  │  │        ├─ kernel.json

├─ README.md
├─ requirements.txt
├─ synthetic_features.csv
└─ to-expose.ipynb

```