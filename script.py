import requests, sys

def main(argv):
    r = requests.get('http://207.154.252.202:1234/get?id=2')
    print(r.status_code)
    print(r.json())

if __name__ == "__main__":
    main(sys.argv[1:])