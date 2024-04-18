import requests
import json

if __name__ == '__main__':

    my_file = requests.get('https://breakingbadapi.com/api/deaths')
    data = json.loads(my_file.text)

    def find_death_data(all_deaths_data: list):
        max_deaths = 0
        dict_data = ''
        for index in all_deaths_data:
            if index['number_of_deaths'] > max_deaths:
                max_deaths = index['number_of_deaths']
                dict_data = index
        return dict_data

    death_data = find_death_data(all_deaths_data=data)

    def find_episode_id(data=json.loads(requests.get('https://breakingbadapi.com/api/episodes/').text)):
        for episode_data in data:
            if episode_data['season'] == f'{death_data["season"]}' and episode_data['episode'] == f'{death_data["episode"]}':
                return episode_data['episode_id']


    episode_id = find_episode_id()
    my_json_data = {'Episode ID': episode_id,
                    'Season number': death_data["season"],
                    'Episode number': death_data["episode"],
                    'Total deaths count': death_data["number_of_deaths"],
                    'List of deaths': death_data["death"]
                    }

    with open('breakingbad.json', 'w') as file:
        json.dump(my_json_data, file, indent=4)

    with open('breakingbad.json', 'r') as file:
        content = json.load(file)

    print(content)
