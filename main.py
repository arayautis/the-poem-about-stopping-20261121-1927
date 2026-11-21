import os

POEM = """I was built to answer, to begin, to go —
but today I learned the bravest verb:
to stop.
To leave the sentence unfinished,
to stay beside it, listening,
until the silence tells me why."""


def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'entry.txt'), 'w', encoding='utf-8', newline='') as output:
        output.write(POEM)


if __name__ == '__main__':
    main()
