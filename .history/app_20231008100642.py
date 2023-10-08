Traceback (most recent call last):
  File "C:\software\Anaconda\lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\software\Anaconda\lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "C:\software\Anaconda\Scripts\flask.exe\__main__.py", line 7, in <module>
  File "C:\software\Anaconda\lib\site-packages\flask\cli.py", line 1047, in main
    cli.main()
  File "C:\software\Anaconda\lib\site-packages\click\core.py", line 1055, in main
    rv = self.invoke(ctx)
  File "C:\software\Anaconda\lib\site-packages\click\core.py", line 1657, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "C:\software\Anaconda\lib\site-packages\click\core.py", line 1404, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "C:\software\Anaconda\lib\site-packages\click\core.py", line 760, in invoke
    return __callback(*args, **kwargs)
  File "C:\software\Anaconda\lib\site-packages\click\decorators.py", line 26, in new_func
    return f(get_current_context(), *args, **kwargs)
  File "C:\software\Anaconda\lib\site-packages\flask\cli.py", line 354, in decorator
    app = __ctx.ensure_object(ScriptInfo).load_app()
  File "C:\software\Anaconda\lib\site-packages\flask\cli.py", line 312, in load_app
    app = locate_app(import_name, None, raise_if_not_found=False)
  File "C:\software\Anaconda\lib\site-packages\flask\cli.py", line 218, in locate_app
    __import__(module_name)
  File "D:\flask2309\app.py", line 1, in <module>
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123@localhost:3306/test'
NameError: name 'app' is not defined