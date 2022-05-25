"""Examples of how to NOT use the decorator."""
import click


def main(name, prefix):
    """Print a message."""
    if prefix is not None:
        name = prefix + " " + name
    print("Hello, {}!".format(name))


def my_decorator(func):
    """Print a message before and after calling the function."""
    def wrapper(*args, **kwargs):
        print("About to call a different function.")
        func(*args, **kwargs)
        print("Finished calling a different function.")
    return wrapper


# Use main as an argument to my_decorator. It returns a new function.
main = my_decorator(main)

# The click functions return decorators.
# The decorator is applied to the function.
click_decorator = click.option("--prefix", default=None, help="Prefix for the name.")

# main is a function, and functions are objects.
# Inside click_decorator, the options above are stored in main.__click_params__
# for later use. main() would still act as expected at this point.
main = click_decorator(main)

# There is no reason to make click_decorator, you could use it directly.
# This is what's happening when you use complex decorators like this.
#
# @click.option("--prefix", default=None, help="Prefix for the name.")
# main():
#     pass
#
# The above is equivalent to:
#
# click_decorator = click.option("--prefix", default=None, help="Prefix for the name.")
# @click_decorator
# main():
#     pass

# Or to do it without the decorator:
main = click.argument("name")(main)

# At this point, main no longer takes the same arguments as before.
# It will be a click.Command object which is called without arguments.
main = click.command()(main)

if __name__ == "__main__":
    main()
