"""Classed and methods for comparing expected and published items in DBs"""


class DBAssert:

    @classmethod
    def count_of_types(cls, dbcon, queried_type, expected, **kwargs):
        """Queries 'dbcon' and counts documents of type 'queried_type'

            Args:
                dbcon (AvalonMongoDB)
                queried_type (str): type of document ("asset", "version"...)
                expected (int): number of documents found
                any number of additional keyword arguments

                special handling of argument additional_args (dict)
                    with additional args like
                    {"context.subset": "XXX"}
        """
        args = {"type": queried_type}
        for key, val in kwargs.items():
            if key == "additional_args":
                args.update(val)
            else:
                args[key] = val

        msg = None
        no_of_docs = dbcon.count_documents(args)
        if expected != no_of_docs:
            msg = "Not expected no of versions. "\
                  "Expected {}, found {}".format(expected, no_of_docs)

        args.pop("type")
        detail_str = " "
        if args:
            detail_str = " with {}".format(args)

        status = "successful"
        if msg:
            status = "failed"

        print("Comparing count of {}{} {}".format(queried_type,
                                                  detail_str,
                                                  status))
        if msg:
            print(msg)

        return msg
