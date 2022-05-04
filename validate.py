import argparse
import json
import jsonschema

def object_pairs_hook(pairs):
    d = {}
    for k, v in pairs:
        if k in d:
            raise KeyError('duplicate key found')
        d[k] = v
    return d

def dump_pretty(data, f, sort_keys=False):
    f.seek(0)
    json.dump(data, f, indent=4, sort_keys=sort_keys)
    f.truncate()
    f.write('\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='pattern json file')
    parser.add_argument('schema', type=str, help='pattern schema json file')
    parser.add_argument('--prettify', action='store_true', help='overwrite the files with prettified versions')
    args = parser.parse_args()

    with open(args.schema, 'r+') as f:
        schema = json.load(f)
        if args.prettify:
            dump_pretty(schema, f, sort_keys=False)

    with open(args.file, 'r+') as f:
        data = json.load(f, object_pairs_hook=object_pairs_hook)
        if args.prettify:
            dump_pretty(data, f, sort_keys=True)

    jsonschema.validate(data, schema)


if __name__ == '__main__':
    main()
