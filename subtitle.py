import argparse
import os

from handle_subtitle import Subtitle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A subtitle translate tools")
    parser.add_argument("file", type=str, help="custom the file")
    parser.add_argument("--to", "-t", type=str,
                        help="special point to the language that you want to translate to")
    parser.add_argument("--double", "-d",
                        help="double language subtitles (default = single language)",
                        action="store_true")
    args = parser.parse_args()

    file = args.file
    if args.to:
        TO = args.to
    else:
        TO = 'zh'
    if args.double:
        by_words = False
    else:
        by_words = True
    if not os.path.splitext(file)[1] in ['.srt']:
        print(os.path.splitext(file)[1] + ' is not a srt file !')
    elif Subtitle.handle_subtitle(os.path.abspath(file), to=TO, by_words=by_words):
        print('Success!')
    else:
        print('error')
else:
    print("error: ", "Please specify a file .")
