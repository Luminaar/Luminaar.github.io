Title: Python decorators
Date: 2019-04-23 18:00:00
Category: Python
Tags: python
Summary: What I wish I knew when I first tried to understand decorators.

It took me quite a while to understand how decorators work in Python
and when are they useful. And even after I understood them, I still
had to look up how to do them properly (for example how to make a
decorator with parameters).

Then a I saw this paragraph in the [official documentation](https://docs.python.org/3/reference/compound_stmts.html#function):

> A function definition may be wrapped by one or more **decorator
> expressions**. Decorator **expressions are evaluated when the
> function is defined**, in the scope that contains the function
> definition. **The result must be a callable**, which is invoked **with
> the function object as the only argument**. The **returned value is
> bound to the function name instead of the function object**.
> Multiple decorators are applied in nested fashion.

I have not found any other explanation of decorators anywhere else in
the docs. Because there is nothing more to explain!

All you need to know is that your `@expression` has to return a
callable which will be called with the wrapped function as an
argument, and result will be bound to the function name. And
that's it.

A simple decorator might look something like this:

```python
def logs(func):
	def wrapper(*args, **kwargs):
		logger.info("Start")
		funs(*args, **kwargs)
		logger.info("Stop")
	return wrapper

@logs  # Return the wrapper directly
def greeter(name):
	print(f"Hello {name}")

```

Need to pass arguments to the wrapper?

```python
    def repeated(times):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for i in range(times):
                    func(*args, **kwargs)

            return wrapper

        return decorator

    @repeated(3)  # Call `repeated` to get the wrapper
    def printer(message):
        print(message)
```

The lesson is: read the documentation, it's all there. I know I
didn't...
