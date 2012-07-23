import os
import sys
import getopt
from captionstransformer.registry import REGISTRY


def read_options():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:f:o:g:") 
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    options = {}
    valid = 0
    print opts
    for option in opts:
        if option[0] == '-i':
            path = option[1]
            if not os.path.exists(path):
                print "not an existing file: %s" % path
                return
            options['input'] = path
            valid += 1
        elif option[0] == '-f':
            format = option[1]
            if format not in REGISTRY:
                print "not supported format: %s" % format
                return
            options['input_format'] = format
            valid += 1
        elif option[0] == '-o':
            path = option[1]
            options['output'] = path
            valid += 1
        elif option[0] == '-g':
            format = option[1]
            if format not in REGISTRY:
                print "not supported format: %s" % format
                return
            options['output_format'] = format
            valid += 1

    if len(options.keys()) != 4:
        print "arguments are all required"
        return

    return options


def main():
    options = read_options()
    if options is None:
        return

    reader = REGISTRY[options['input_format']]['reader'](open(options['input']))
    writer = REGISTRY[options['output_format']]['writer'](open(options['output'], 'w'))

    content = reader.read()
    reader.close()
    writer.write(content)
    writer.close()


if __name__ == "__main__":
    main()
