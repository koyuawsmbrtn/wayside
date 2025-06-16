import sys

def convert_newlines():
    try:
        # Read from stdin if no file is specified
        if len(sys.argv) == 1:
            while True:
                line = sys.stdin.buffer.read1(1024)
                if not line:
                    break
                sys.stdout.buffer.write(line.replace(b'\n', b'\r'))
        else:
            # Process each file provided as argument
            for filename in sys.argv[1:]:
                with open(filename, 'rb') as f:
                    while True:
                        chunk = f.read(1024)
                        if not chunk:
                            break
                        sys.stdout.buffer.write(chunk.replace(b'\n', b'\r'))
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    convert_newlines()