import requests, sys



def check_post(api):
    ids = []
    files = {'image': open('Screenshot 2021-11-05 102431.jpg', 'rb')}
    r = requests.post(api+'upload/', files=files)
    print('Uploading.. Screenshot 2021-11-05 102431.jpg')
    print('Status code: {}'.format(r.status_code))
    print('image id: {}\n'.format(r.json()['id']))

    ids.append(r.json()['id'])
    files = {'image': open('234354.jpg', 'rb')}
    r = requests.post(api+'upload/', files=files)
    print('Uploading.. 234354.jpg')
    print('Status code: {}'.format(r.status_code))
    print('image id: {} \n'.format(r.json()['id']))
    print('Post success! \n')
    ids.append(r.json()['id'])

    return ids

def check_get(api, ids):
    for id in ids:
        r = requests.get(api+'get?id={}'.format(id))
        print('Status code: {}'.format(r.status_code))
        print('Image: {} \n'.format(r.json()['image']))

    print('Success!!')

def main(argv):
    api = ""
    if len(argv) == 0:
        api = 'http://207.154.252.202:1234/'
    else:
        api = argv[0]
    print('api: {}'.format(api))
    try:
        r = requests.get(api+'')
    except: 
        print('Error: Wrong argument, must be avialble link, got {}'.format(api))
        return 1

    print('Testing POST \n')
    ids = check_post(api)
    print('Testing GET \n')
    check_get(api, ids)


if __name__ == "__main__":
    main(sys.argv[1:])