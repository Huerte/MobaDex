import requests

API_BASE_URL = 'https://mlbb-stats.ridwaanhall.com/api'

def fetch_api(to_fetch):
    try:
        response = requests.get(f'{API_BASE_URL}/{to_fetch}')
        return response.json()
    except requests.exceptions.RequestException:
        return None
    

def all_heroes():
    data = fetch_api('hero-list')
    heroes = []
    if data:
        for id, name in data.items():
            heroes.append(
                (int(id), name)
            )
    return heroes

def hero_rank(days=1, rank='all', size=127, index=127, sort_field='win_rate', sort_order='desc'):
    res = fetch_api(f'hero-rank/?days={days}&rank={rank}&size={size}&index={index}&sort_field={sort_field}&sort_order={sort_order}')
    records = res.get('data', {}).get('records', [])
    total_count = res.get('data', {}).get('total_count', 0)  # Make sure API returns this
    
    data = []
    for hero_entry in records:
        hero = {
            'main_hero_id': hero_entry['data']['main_heroid'],
            'main_hero_name': hero_entry['data']['main_hero']['data']['name'],
            'main_hero_img': hero_entry['data']['main_hero']['data']['head'],
            'win_rate': hero_entry['data']['main_hero_win_rate'] * 100,
            'ban_rate': hero_entry['data']['main_hero_ban_rate'] * 100,
            'appearance_rate': hero_entry['data']['main_hero_appearance_rate'] * 100,
            'channel_id': hero_entry['data']['main_hero_channel']['id'],
            'sub_heroes': []
        }
        for sub in hero_entry['data']['sub_hero']:
            hero['sub_heroes'].append({
                'heroid': sub['heroid'],
                'img': sub['hero']['data']['head'],
                'channel_id': sub['hero_channel']['id'],
                'increase_win_rate': sub['increase_win_rate'] * 100,
            })


        data.append(hero)

    data.sort(key=lambda x: x.get(sort_field, 0), reverse=(sort_order=='desc'))

    return data, total_count

def hero_counters(main_hero_id=1):
    res = fetch_api(f'hero-counter/{main_hero_id}/')

    records = res.get('data', {}).get('records', [])
    if not records:
        return None

    record = records[0]['data']
    main = {
        'id': record['main_heroid'],
        'name': record['main_hero']['data'].get('name', 'Unknown'),
        'img': record['main_hero']['data'].get('head', ''),
        'win_rate': record.get('main_hero_win_rate', 0) * 100,
        'ban_rate': record.get('main_hero_ban_rate', 0) * 100,
        'appearance_rate': record.get('main_hero_appearance_rate', 0) * 100,
    }

    counters = []
    for sub in record.get('sub_hero', []):
        hero_data = sub.get('hero', {}).get('data', {})
        counters.append({
            'heroid': sub.get('heroid', 0),
            'img': hero_data.get('head', ''),
            'win_rate': sub.get('hero_win_rate', 0) * 100,
            'appearance_rate': sub.get('hero_appearance_rate', 0) * 100,
            'increase_win_rate': sub.get('increase_win_rate', 0) * 100,
            'channel_id': sub.get('hero_channel', {}).get('id', 0),
        })

    return {
        'main_hero': main,
        'counters': sorted(counters, key=lambda x: x['increase_win_rate'], reverse=True)
    }

# if __name__ == '__main__':
#     print(hero_counters())