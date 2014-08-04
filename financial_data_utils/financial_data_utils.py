from options.yahoo_options import YahooOptions
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('symbol')

def main ():

    class C :
        pass
    params = C()
    parser.parse_args(namespace=params)
    YahooOptions( params.symbol )

if __name__ == "__main__":
    main()
