"""Examples of how to use the decorator."""
import click


def my_decorator(func):
    """Print a message before and after calling the function."""
    def wrapper(*args, **kwargs):
        print("About to call a different function.")
        func(*args, **kwargs)
        print("Finished calling a different function.")
    return wrapper


# I usually like to put main() at the top of the file,
# but the decorator needed to be defined to be used.
@click.command()
@click.argument("name")
@click.option("--prefix", default=None, help="Prefix for the name.")
@my_decorator
def main(name, prefix):
    """Print a message."""
    if prefix is not None:
        name = prefix + " " + name
    print("Hello, {}!".format(name))


if __name__ == "__main__":
    main()
