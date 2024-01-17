# BEGIN (write your solution here)
def transform(input_file, output_file, rules):
    input_value = open(input_file)
    output = open(output_file, 'w')
    output.writelines(
        map(
            lambda x: f"{' '.join(x)}\n",
            filter(
                lambda x: len(x) > 0,
                map(
                    lambda list_str:
                    list(
                        map(
                            lambda z:
                            z.capitalize()
                            if z.startswith(tuple(rules['capital_letters']))
                            else z,
                            filter(
                                lambda y:
                                y.lower() not in rules['censored_words'],
                                filter(
                                    lambda x:
                                    len(x) >= rules['word_min_len'],
                                    list_str
                                )
                            )
                        )
                    ),
                    map(lambda line: line.split(), input_value)
                )
            )
        )
    )
    input_value.close()
    output.close()
# END
